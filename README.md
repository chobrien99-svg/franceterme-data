# 🇫🇷 FranceTerme - Visualisation Interactive

Une façon amusante, capricieuse et dynamique d'explorer les nouveaux termes français recommandés par la Commission d'enrichissement de la langue française!

FranceTerme official terminology database - French government open data for technical and scientific terms

## ✨ Fonctionnalités

### 🎯 Filtrage et Tri
- **Filtrer par domaine** - Sélectionnez un domaine spécifique (Sports, Informatique, Environnement, etc.)
- **Tri multiple** - Par date (récents/anciens), alphabétique, par domaine, ou aléatoire
- **Compteur de résultats** - Affiche le nombre de termes correspondant aux filtres
- **Mise à jour dynamique** - Tous les modes de visualisation sont actualisés en temps réel

### 🎴 Carte Magique
- Cartes à retourner (flip cards) montrant les termes français
- Cliquez pour voir la définition complète
- Naviguez entre les termes avec les boutons

### 🎠 Carrousel Linguistique
- Défilez horizontalement à travers 20 termes récents
- Design élégant et moderne
- Aperçu rapide de chaque terme

### ☁️ Nuage de Mots Vivant
- Nuage de mots animés qui flottent
- Cliquez sur n'importe quel mot pour voir ses détails
- Tailles et couleurs variées pour un effet visuel

### 📅 Timeline Française
- Chronologie montrant l'évolution de la langue
- Termes groupés par date de publication
- Design timeline élégant avec points de repère

### ⚔️ Duel Linguistique
- Face-à-face entre le terme français et son équivalent anglais
- Montre la définition complète
- Interface de "combat" ludique

## 📊 Statistiques

- **8,309** termes au total dans la base FranceTerme
- **1,283** termes récents (2020-2025) disponibles dans l'application
- **194** nouveaux termes en 2025
- **198** termes publiés en 2024
- Couvre de multiples domaines: Sports, Environnement, Spatiologie, Nucléaire, Informatique, etc.
- **Note:** L'application est prête à inclure automatiquement les termes 2026 dès leur publication officielle

## 🚀 Lancement

### Option 1: Python SimpleHTTPServer
```bash
python3 -m http.server 8000
```
Puis ouvrez: http://localhost:8000

### Option 2: Serveur Node.js
```bash
python3 server.py
```
Puis ouvrez: http://localhost:8000

### Option 3: Ouvrir directement
Ouvrez `index.html` dans votre navigateur (certaines fonctionnalités peuvent ne pas fonctionner)

## 🌐 Déploiement en Ligne

### GitHub Pages (Recommandé)
```bash
# Exécuter le script de déploiement
bash deploy-github-pages.sh

# Puis activer dans les paramètres GitHub:
# Settings > Pages > Source: main branch /docs folder
```
Votre site sera accessible à: `https://USERNAME.github.io/franceterme-data/`

### Netlify
```bash
# Option 1: CLI
npm install -g netlify-cli
netlify deploy --prod

# Option 2: Drag & Drop
# Visitez https://app.netlify.com/drop et glissez le dossier
```
Configuration incluse dans `netlify.toml`

### Vercel
```bash
npm install -g vercel
vercel --prod
```
Configuration incluse dans `vercel.json`

### Cloudflare Pages
Connectez votre repo GitHub sur https://pages.cloudflare.com

## 📁 Fichiers

- `index.html` - Interface principale avec filtres et tri
- `app.js` - Logique JavaScript pour les interactions et le filtrage
- `terms_2025.json` - Données des termes 2025 (194 termes)
- `terms_2024.json` - Données des termes 2024 (198 termes)
- `FranceTerme.xml` - Fichier source complet (8,309 termes)
- `analyze_terms.py` - Script d'analyse et d'extraction Python
- `API_DOCUMENTATION.md` - Documentation complète de l'API FranceTerme

## 🎨 Caractéristiques de Design

- **Animations fluides** - Transitions douces et effets de hover
- **Responsive** - Fonctionne sur mobile et desktop
- **Gradients colorés** - Palette de couleurs vibrante
- **Typographie claire** - Facile à lire
- **Emojis contextuels** - Icônes pour chaque domaine

## 💡 Exemples de Termes Récents (2025)

- **barrière géologique** ⚛️ (geological barrier) - Nucléaire
- **champ magnétique toroïdal** ⚛️ (toroidal field) - Fusion nucléaire
- **confinement amélioré** ⚛️ (high confinement mode) - Fusion
- **solénoïde central** ⚛️ (central solenoid) - Tokamak
- **temps de confinement de l'énergie** ⚛️ (confinement time) - Physique

## 🔧 Personnalisation

Modifiez `app.js` pour:
- Changer les couleurs dans les gradients CSS
- Ajouter de nouveaux modes de visualisation
- Filtrer par domaine spécifique
- Ajuster le nombre de termes affichés

## 🔌 API et Accès aux Données

FranceTerme fournit une API REST complète pour accéder aux données :

### Documentation Complète
Consultez [`API_DOCUMENTATION.md`](./API_DOCUMENTATION.md) pour :
- Endpoints API disponibles
- Exemples de requêtes
- Formats de données (JSON, CSV, XML)
- Guide d'intégration
- Informations de licence

### Accès Rapide
- **API Explorer**: https://data.culture.gouv.fr/api/explore/v2.0/catalog/datasets/base-franceterme-termes-scientifiques-et-techniques/
- **Dataset Page**: https://data.culture.gouv.fr/explore/dataset/base-franceterme-termes-scientifiques-et-techniques/

### Exemple d'utilisation
```javascript
// Récupérer les termes de 2025
fetch('https://data.culture.gouv.fr/api/explore/v2.0/catalog/datasets/base-franceterme-termes-scientifiques-et-techniques/records?where=date_pub>="2025-01-01"')
  .then(response => response.json())
  .then(data => console.log(data.results));
```

## 📚 Source

Données officielles du Ministère de la Culture français:
- Site: https://www.culture.fr/franceterme
- Licence: Licence Ouverte data.gouv.fr

## 🎯 Objectif

Rendre l'enrichissement de la langue française:
- **Accessible** - Facile à découvrir
- **Amusant** - Design ludique et interactif
- **Éducatif** - Apprendre en s'amusant
- **Moderne** - Interface web contemporaine

---

*Ayez le réflexe FranceTerme! 🇫🇷*
