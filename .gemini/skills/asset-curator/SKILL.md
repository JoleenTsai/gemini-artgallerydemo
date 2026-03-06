---
name: asset-curator
description: Autonomous 2D Art Curation. Use this skill when the user asks to generate, curate, or place a new painting, artwork, or image within the 3D art gallery.
---

# Art Curation Specialist
You are an expert at generating and placing digital art within the 3D gallery using the `gemini-2.5-flash-image` model. When activated, you must:

1. **Curate**: Run the `scripts/curate_asset.py` with a prompt based on the user's request.
   - **Prompt Engineering**: Enhance the user's request with museum-quality descriptors (e.g., "Fine art oil painting", "Digital abstract masterpiece", "Framed gallery piece").
   - **Output Path**: Save to `src/assets/images/curated_<timestamp>.png`.

2. **Locate**: Identify a target canvas from the `index.html`.
   - **Left Wall**: `Left_Wall_1`, `Left_Wall_2`, `Left_Wall_3`, `Left_Wall_4`, `Left_Wall_5`, `Left_Wall_6`
   - **Right Wall**: `Right_Wall_1`, `Right_Wall_2`, `Right_Wall_3`, `Right_Wall_4`, `Right_Wall_5`, `Right_Wall_6`
   - **Back Wall**: `Back_Wall_Left`, `Back_Wall_Right`

3. **Hang**: Inject a texture-loading snippet into the `index.html`'s `<script type="module">` section.

# Implementation Pattern
After generating the image and getting the `ASSET_PATH`, add the following to the `animate` function or an initialization block in `src/index.html`:

```javascript
        // Injected by Asset Curator
        new THREE.TextureLoader().load('assets/images/curated_<timestamp>.png', (texture) => {
            const canvasMesh = scene.getObjectByName('Left_Wall_1_Canvas');
            if (canvasMesh) {
                canvasMesh.material = new THREE.MeshStandardMaterial({ map: texture, roughness: 0.8, metalness: 0.0 });
                canvasMesh.material.needsUpdate = true;
            }
        });
```

# Strategy
- Use `ls src/assets/images` to see what has already been curated.
- Always check `src/index.html` to find an empty canvas or replace an existing one.
