#!/usr/bin/env python3
"""
🇫🇷 FranceTerme - Mot du Jour (Term of the Day)

Displays a random French term from the FranceTerme database
Perfect for daily language enrichment!
"""
import json
import random
from datetime import datetime

EMOJI_MAP = {
    'Biologie': '🧬',
    'Chimie': '⚗️',
    'Spatiologie': '🚀',
    'Économie et gestion d\'entreprise': '💼',
    'Nucléaire': '⚛️',
    'Sports': '⚽',
    'Informatique': '💻',
    'Finance': '💰',
    'Télécommunications': '📡',
    'Défense': '🛡️',
    'Automobile': '🚗',
    'Énergie': '⚡',
    'Environnement': '🌍',
    'Santé': '⚕️',
    'Agriculture': '🌾',
    'Transports': '🚆'
}

def get_emoji(domain):
    return EMOJI_MAP.get(domain, '📚')

def display_term_of_the_day():
    """Display a beautifully formatted term of the day"""

    # Load terms
    try:
        with open('terms_2024.json', 'r', encoding='utf-8') as f:
            terms = json.load(f)
    except FileNotFoundError:
        print("❌ Error: terms_2024.json not found. Run analyze_terms.py first!")
        return

    # Use date as seed for consistent "daily" term
    today = datetime.now().date()
    random.seed(str(today))
    term = random.choice(terms)

    # Display
    print("\n" + "=" * 70)
    print("🇫🇷  LE MOT DU JOUR  🇫🇷".center(70))
    print("=" * 70)
    print()

    print(f"  📅 {today.strftime('%d %B %Y')}")
    print()

    print("  " + "─" * 66)
    print(f"  🆕 TERME FRANÇAIS")
    print(f"     {term['term']}")
    print("  " + "─" * 66)
    print()

    if term['english']:
        print(f"  🌍 ENGLISH EQUIVALENT")
        print(f"     {term['english']}")
        print()

    print(f"  {get_emoji(term['domain'])} DOMAINE")
    print(f"     {term['domain']}", end='')
    if term['subdomain']:
        print(f" → {term['subdomain']}")
    else:
        print()
    print()

    print(f"  📖 DÉFINITION")
    # Word wrap definition
    definition = term.get('definition', 'Pas de définition disponible.')
    words = definition.split()
    lines = []
    current_line = "     "

    for word in words:
        if len(current_line) + len(word) + 1 > 66:
            lines.append(current_line)
            current_line = "     " + word
        else:
            if current_line == "     ":
                current_line += word
            else:
                current_line += " " + word

    if current_line.strip():
        lines.append(current_line)

    for line in lines:
        print(line)
    print()

    print(f"  📅 PUBLIÉ LE")
    print(f"     {term['date_str']}")
    print()

    print("=" * 70)
    print()
    print("  💡 Astuce: Lancez ce script chaque jour pour un nouveau terme!")
    print("  🔄 Le terme change automatiquement chaque jour")
    print()
    print("  ✨ Ayez le réflexe FranceTerme! ✨")
    print()

def show_random_term():
    """Display a completely random term (not date-based)"""

    try:
        with open('terms_2024.json', 'r', encoding='utf-8') as f:
            terms = json.load(f)
    except FileNotFoundError:
        print("❌ Error: terms_2024.json not found. Run analyze_terms.py first!")
        return

    term = random.choice(terms)

    print("\n" + "🎲 " * 20)
    print()
    print(f"  🆕 {term['term']}")
    if term['english']:
        print(f"  🌍 {term['english']}")
    print(f"  {get_emoji(term['domain'])} {term['domain']}")
    if term['definition']:
        print(f"  📖 {term['definition'][:100]}...")
    print()
    print("🎲 " * 20)

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == '--random':
        show_random_term()
    else:
        display_term_of_the_day()
