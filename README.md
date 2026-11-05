# Autocar ACTT Configurator

Static Three.js configurator prepared for GitHub Pages.

## Required model assets
Copy these existing viewer assets into the repository root before publishing if they are not already included:

- `tinker.obj`
- `obj.mtl`
- `aarfontein_pan_4k.hdr`
- contents of the existing `models/` folder, including `models/manifest.json`

The HTML currently references those paths directly.

## Configuration backend
Edit `configurator.json` to manage the configurator without editing the UI code.

Structure:

`Section -> Subsection -> Option -> rules.show / rules.hide`

Supported rule targets:

- `group:<groupName>` for groups defined in the viewer
- `component:<number>` for indexed components in the main CAD model
- `name:<objectName>` for model/mesh object names

Example:

```json
{
  "id": "square",
  "label": "Square step fuel tank",
  "rules": {
    "show": ["group:squareTank"],
    "hide": ["group:roundTank", "group:lhSteps"]
  }
}
```

## Publish with GitHub Pages
1. Create a GitHub repository.
2. Upload the *contents* of this folder to the repository root.
3. Confirm all model files use matching capitalization. GitHub Pages paths are case-sensitive.
4. In GitHub open **Settings -> Pages**.
5. Under **Build and deployment**, select **Deploy from a branch**.
6. Select your main branch and `/ (root)`, then save.

The site is intentionally static. No build step, npm install, or server-side code is required.

## Important
Do not open `index.html` by double-clicking it for final testing. Some browser fetch behavior differs for local `file://` pages. Test through GitHub Pages or a local HTTP server such as `python -m http.server 8000`.
