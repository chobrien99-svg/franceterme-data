#!/bin/bash
# Deploy FranceTerme to GitHub Pages

echo "🚀 Deploying to GitHub Pages..."
echo ""

# Create docs directory for GitHub Pages
mkdir -p docs

# Copy necessary files
echo "📦 Copying files..."
cp index.html docs/
cp app.js docs/
cp terms_2024.json docs/
cp -r . docs/ 2>/dev/null || true

# Create a simple CNAME file if you want a custom domain (optional)
# echo "franceterme.yourdomain.com" > docs/CNAME

echo ""
echo "✅ Files copied to docs/ folder"
echo ""
echo "📝 Next steps:"
echo "1. git add docs/"
echo "2. git commit -m 'Add GitHub Pages deployment'"
echo "3. git push"
echo "4. Go to: https://github.com/chobrien99-svg/franceterme-data/settings/pages"
echo "5. Set Source to: 'Deploy from a branch'"
echo "6. Set Branch to: 'main' and folder to '/docs'"
echo "7. Click Save"
echo ""
echo "🌐 Your site will be live at:"
echo "   https://chobrien99-svg.github.io/franceterme-data/"
echo ""
echo "⏱️  Allow 1-2 minutes for initial deployment"
