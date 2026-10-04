# Opération La Défense

A playful arcade game built on the FranceTerme database (termes recommandés au Journal officiel).

- Play: `/game`
- Data: `tools/game/gamedata.json` (226 curated terms in three difficulty tiers, plus 18 bosses)
- Refresh after a new FranceTerme release:
  1. Download the latest XML: http://www.franceterme.culture.gouv.fr/public/FranceTerme.xml (also listed on data.gouv.fr)
  2. Save it as `FranceTerme.xml` in the repo root
  3. Run `python3 tools/game/build_game.py`
  4. Commit and push; Vercel redeploys automatically.

## Embedding in Ghost
Add an HTML card:

    <iframe src="https://YOUR-VERCEL-URL/game"
      style="width:100%;height:820px;border:0;border-radius:12px"
      allow="microphone; autoplay" loading="lazy"
      title="Opération La Défense"></iframe>

Voice mode works best in Chrome. Data: Licence Ouverte, ministère de la Culture.
