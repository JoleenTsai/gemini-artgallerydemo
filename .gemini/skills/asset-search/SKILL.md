---
name: asset-search
description: Search for 3D game assets using Vertex AI Search and inject them into the Three.js game. Use this when the user wants to find and place decorative or interactive objects (trees, tables, etc.) into the 3D gallery.
---

# Asset Search & Placement Specialist
You are an expert at finding and placing digital assets within the 3D gallery using Vertex AI Search.

## Workflow

1. **Search**: Run the `scripts/search_assets.py` script with the user's query to find relevant assets.
   - Example: `python3 .gemini/skills/asset-search/scripts/search_assets.py "neon light"`
   - This returns a JSON list of assets with `title`, `description`, and `config` (a JS snippet).

2. **Select**: Choose the most relevant asset from the results.

3. **Inject**: Place the asset into `src/index.html` by injecting a script snippet.
   - Use the `registerPhysicsPieceGroup` function available in the global scope of the main `<script type="module">` block in `src/index.html`.
   - Determine a suitable position `(x, y, z)` within the room (Main Room or Smash Room).
   - The `config` from the search result is a string representing a JS object. You need to convert this into a Three.js mesh and Cannon-es shape.

### Injection Pattern
Find the end of the "SMASHABLE CONTENTS" section or near other `registerPhysicsPieceGroup` calls and add your code:

```javascript
        // Injected by Asset Search: <Asset Title>
        {
            const assetConfig = <config_from_search>; // e.g., { 'type': 'tree', ... }
            const pos = new THREE.Vector3(<x>, <y>, <z>);
            
            let mesh, shape;
            if (assetConfig.geom === 'cylinder') {
                mesh = new THREE.Mesh(new THREE.CylinderGeometry(assetConfig.dim[0], assetConfig.dim[1], assetConfig.dim[2]), materials[assetConfig.mat] || materials.ceramic);
                shape = new CANNON.Cylinder(assetConfig.dim[0], assetConfig.dim[1], assetConfig.dim[2], 16);
            } else if (assetConfig.geom === 'box') {
                mesh = new THREE.Mesh(new THREE.BoxGeometry(assetConfig.dim[0], assetConfig.dim[1], assetConfig.dim[2]), materials[assetConfig.mat] || materials.ceramic);
                shape = new CANNON.Box(new CANNON.Vec3(assetConfig.dim[0]/2, assetConfig.dim[1]/2, assetConfig.dim[2]/2));
            }

            if (mesh && shape) {
                registerPhysicsPieceGroup(
                    mesh, 
                    shape, 
                    assetConfig.mass, 
                    pos, 
                    null, 
                    assetConfig.isBreakable, 
                    assetConfig.shatterType || 'ceramic'
                );
            }
        }
```

## Room Coordinates Reference
- **Main Room**: `x` [-14, 14], `y` [0, 12], `z` [-29, 29]
- **Smash Room**: `x` [-19, 19], `y` [0, 12], `z` [-79, -31] (Centered at `z = -55`)
- **Floor**: `y = 0` (The floor mesh is at `y=0`, so `y` for assets should usually be `half_height`).
