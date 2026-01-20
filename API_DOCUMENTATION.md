# FranceTerme API Documentation

## Overview

FranceTerme is an official database of French terminology published by the French Ministry of Culture. The data contains scientific and technical terms recommended in the Journal officiel de la République française.

## Legal Information

**License:** The FranceTerme data is available under the French Open License (Licence Ouverte)
- License URL: https://www.etalab.gouv.fr/wp-content/uploads/2014/05/Licence_Ouverte.pdf
- Data Type: Public administrative information under Article 10 of Law n° 78-753 of July 17, 1978

## Data Access Methods

### 1. Official Dataset Page

The primary dataset is hosted on the French Ministry of Culture's open data portal:

**Main URL:** https://data.culture.gouv.fr/explore/dataset/base-franceterme-termes-scientifiques-et-techniques/

This page provides:
- Dataset description and metadata
- Export buttons for multiple formats
- API endpoint information
- Update history

### 2. OpenDataSoft API (Huwise Platform)

The data.culture.gouv.fr portal uses the OpenDataSoft (now branded as Huwise) platform, which provides REST API access.

#### API Base URL
```
https://data.culture.gouv.fr/api/explore/v2.0/catalog/datasets/base-franceterme-termes-scientifiques-et-techniques/
```

#### API Version
The platform supports two API versions:
- **v2.0**: Standard production version
- **v2.1**: Latest version (paths start with `/api/explore/v2.1`)

#### Key Endpoints

##### 1. Get Records
```
GET /api/explore/v2.0/catalog/datasets/base-franceterme-termes-scientifiques-et-techniques/records
```

**Parameters:**
- `limit`: Number of records to return (default: 10, max varies by endpoint)
- `offset`: Number of records to skip for pagination
- `where`: Filter using ODSQL (Opendatasoft Query Language)
- `select`: Specify fields to return
- `order_by`: Sort results by field(s)

**Example:**
```bash
curl "https://data.culture.gouv.fr/api/explore/v2.0/catalog/datasets/base-franceterme-termes-scientifiques-et-techniques/records?limit=10"
```

##### 2. Get Single Record
```
GET /api/explore/v2.0/catalog/datasets/base-franceterme-termes-scientifiques-et-techniques/records/{record_id}
```

##### 3. Export Data
```
GET /api/explore/v2.0/catalog/datasets/base-franceterme-termes-scientifiques-et-techniques/exports/{format}
```

**Supported formats:**
- `json`
- `csv`
- `xls`
- `geojson` (if geographic data exists)

**Note:** The exports endpoint has no record limit, unlike the records endpoint.

### 3. Direct File Downloads

The dataset page provides direct download links for complete datasets in various formats:
- XML (full database export)
- JSON
- CSV
- Excel

These can be downloaded directly from the dataset page at:
https://data.culture.gouv.fr/explore/dataset/base-franceterme-termes-scientifiques-et-techniques/

### 4. Alternative Access via data.gouv.fr

The dataset is also referenced on the national open data portal:

**URL:** https://www.data.gouv.fr/datasets/base-franceterme-termes-scientifiques-et-techniques-1

This provides:
- Additional metadata
- Community discussions
- Reuse examples
- Alternative download links

## API Features

### Query Language (ODSQL)

The API uses Opendatasoft Query Language (ODSQL) for filtering and querying:

**Examples:**
```
# Filter by domain
where=domaine:"Informatique"

# Filter by year
where=date_publication >= "2025-01-01"

# Multiple conditions
where=domaine:"Informatique" AND date_publication >= "2025-01-01"

# Select specific fields
select=terme_francais,terme_anglais,domaine,definition
```

### Response Format

The API returns JSON responses with the following structure:
```json
{
  "total_count": 8309,
  "results": [
    {
      "terme_francais": "interface de programmation d'application",
      "terme_anglais": "application programming interface",
      "domaine": "Informatique",
      "definition": "Interface logicielle qui permet...",
      "date_publication": "2022-04-30",
      ...
    }
  ]
}
```

### Pagination

For large datasets:
1. Use `limit` parameter to set page size
2. Use `offset` parameter to skip records
3. Check `total_count` in response for total available records

**Example:**
```bash
# Get second page of 100 records
curl "https://data.culture.gouv.fr/api/explore/v2.0/catalog/datasets/base-franceterme-termes-scientifiques-et-techniques/records?limit=100&offset=100"
```

## Data Structure

### Fields

The FranceTerme dataset typically includes:

| Field | Description |
|-------|-------------|
| `terme` | French term |
| `definition` | French definition |
| `english` / `equi_prop` | English equivalent |
| `domain` / `domaine` | Subject domain (e.g., "Informatique", "Chimie") |
| `subdomain` / `s_dom` | Subdomain if applicable |
| `date_pub` | Publication date in Journal officiel |
| `commission` | Commission that recommended the term |

**Note:** Field names may vary between XML export and API responses. Check the dataset schema for exact field names.

## Update Frequency

The dataset is updated after each new publication of recommended terms in the Journal officiel. This typically occurs:
- Multiple times per year
- Following official commission meetings
- When new domains are addressed

## Implementation Examples

### Python Example
```python
import requests

# Fetch 2025 terms
url = "https://data.culture.gouv.fr/api/explore/v2.0/catalog/datasets/base-franceterme-termes-scientifiques-et-techniques/records"
params = {
    "where": "date_pub >= '2025-01-01'",
    "limit": 100
}
response = requests.get(url, params=params)
data = response.json()

for record in data['results']:
    print(f"{record['terme']} - {record['domaine']}")
```

### JavaScript Example
```javascript
// Fetch terms from a specific domain
const url = 'https://data.culture.gouv.fr/api/explore/v2.0/catalog/datasets/base-franceterme-termes-scientifiques-et-techniques/records';
const params = new URLSearchParams({
    where: 'domaine:"Informatique"',
    limit: 50
});

fetch(`${url}?${params}`)
    .then(response => response.json())
    .then(data => {
        data.results.forEach(term => {
            console.log(`${term.terme} (${term.english})`);
        });
    });
```

## Current Implementation in This Project

This project currently uses:
- **Data Source:** XML file (`FranceTerme.xml`) downloaded from the official source
- **Processing:** Python script (`analyze_terms.py`) to parse XML and extract specific years
- **Output:** Static JSON files (`terms_2025.json`) for web application
- **Deployment:** Static file hosting (GitHub Pages compatible)

### Advantages of Current Approach
- Works offline without API calls
- No rate limiting concerns
- Fast page loads (static JSON)
- GitHub Pages compatible

### Potential API Integration Benefits
- Always up-to-date data
- No need to regenerate JSON files
- Can fetch data by year/domain dynamically
- Smaller initial page load (fetch on demand)

### Recommended Hybrid Approach
1. Use static JSON for initial page load (fast)
2. Optional: Add "Refresh Data" button that fetches from API
3. Cache API responses locally
4. Fall back to static JSON if API unavailable

## API Documentation Resources

- **OpenDataSoft API Docs:** https://help.opendatasoft.com/apis/ods-explore-v2/
- **Ministry of Culture API Console:** https://data.culture.gouv.fr/api/v1/console
- **Dataset API Page:** https://data.culture.gouv.fr/explore/dataset/base-franceterme-termes-scientifiques-et-techniques/api/

## Attribution

When using FranceTerme data, please provide attribution:

> Data source: FranceTerme - Délégation générale à la langue française et aux langues de France (DGLFLF), Ministère de la Culture
>
> License: Licence Ouverte / Open License
>
> https://www.culture.fr/franceterme

## Contact & Support

For questions about the data or API:
- **Official Website:** https://www.culture.fr/franceterme
- **Data Portal:** https://data.culture.gouv.fr
- **GitHub Issues:** (for this project) https://github.com/chobrien99-svg/franceterme-data/issues

---

*Last Updated: January 2026*
