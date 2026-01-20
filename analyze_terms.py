#!/usr/bin/env python3
"""
Analyze FranceTerme.xml to extract and display recent French language recommendations
"""
import xml.etree.ElementTree as ET
from datetime import datetime
from collections import defaultdict
import json

def parse_franceterme(xml_file):
    """Parse the FranceTerme XML file and extract term information"""
    tree = ET.parse(xml_file)
    root = tree.getroot()

    terms = []
    domains = defaultdict(int)
    years = defaultdict(int)

    for article in root.findall('Article'):
        try:
            # Extract basic info
            terme_elem = article.find('Terme_balise')
            if terme_elem is None or terme_elem.text is None:
                continue

            terme = terme_elem.text.strip()

            # Get date
            date_elem = article.find('DatePub')
            if date_elem is not None and date_elem.text:
                date_str = date_elem.text
                date_obj = datetime.strptime(date_str, '%d/%m/%Y')
            else:
                continue

            # Get domain
            domain_elem = article.find('.//Dom')
            domain = domain_elem.text if domain_elem is not None else "Unknown"

            # Get subdomain if exists
            subdom_elem = article.find('.//S-dom')
            subdomain = subdom_elem.text if subdom_elem is not None else None

            # Get definition
            def_elem = article.find('Definition')
            definition = def_elem.text.strip() if def_elem is not None and def_elem.text else ""

            # Get English equivalent
            equiv_elem = article.find('.//Equi_prop')
            english = equiv_elem.text.strip() if equiv_elem is not None and equiv_elem.text else ""

            # Get commission
            commission = article.get('commission', '')

            terms.append({
                'term': terme,
                'date': date_obj,
                'date_str': date_str,
                'domain': domain,
                'subdomain': subdomain,
                'definition': definition,
                'english': english,
                'commission': commission,
                'year': date_obj.year
            })

            domains[domain] += 1
            years[date_obj.year] += 1

        except Exception as e:
            # Skip malformed entries
            continue

    return terms, domains, years

def main():
    print("🇫🇷 Analyzing FranceTerme.xml...")
    print("=" * 60)

    terms, domains, years = parse_franceterme('FranceTerme.xml')

    print(f"\n📊 Total terms: {len(terms)}")
    print(f"\n📅 Terms by year:")
    for year in sorted(years.keys(), reverse=True)[:10]:
        print(f"  {year}: {years[year]} terms")

    print(f"\n🎯 Top domains:")
    for domain, count in sorted(domains.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {domain}: {count} terms")

    # Get newest terms (2025)
    newest_terms = [t for t in terms if t['year'] == 2025]
    newest_terms.sort(key=lambda x: x['date'], reverse=True)

    print(f"\n✨ Newest terms from 2025 ({len(newest_terms)} terms):")
    print("=" * 60)

    for i, term in enumerate(newest_terms[:20], 1):
        print(f"\n{i}. 🆕 {term['term']}")
        print(f"   📅 {term['date_str']}")
        print(f"   🎨 Domain: {term['domain']}", end='')
        if term['subdomain']:
            print(f" → {term['subdomain']}")
        else:
            print()
        if term['english']:
            print(f"   🌍 English: {term['english']}")
        if term['definition']:
            # Truncate long definitions
            definition = term['definition'][:150]
            if len(term['definition']) > 150:
                definition += "..."
            print(f"   📖 {definition}")

    # Save all 2025 terms to JSON for web display
    with open('terms_2025.json', 'w', encoding='utf-8') as f:
        json.dump(newest_terms, f, ensure_ascii=False, indent=2, default=str)

    print(f"\n\n💾 Saved {len(newest_terms)} terms from 2025 to terms_2025.json")

if __name__ == '__main__':
    main()
