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

    <iframe src="https://franceterme-data.vercel.app/game"
      style="width:100%;height:min(820px,85vh);min-height:520px;border:0;border-radius:12px"
      allow="microphone; autoplay; fullscreen" allowfullscreen loading="lazy"
      title="Opération La Défense"></iframe>

The height adapts to the reader's screen (85% of the window, never taller than 820px),
so the whole game fits without zooming out. `fullscreen` lets the "⛶ Plein écran" button
enlarge the game; if an embed doesn't allow it, the button opens the game in a new tab instead.

Voice mode works best in Chrome. Data: Licence Ouverte, ministère de la Culture.
