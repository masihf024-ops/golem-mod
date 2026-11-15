# Ganton Mosque — blockout v2 notes

Version 2 adds a more recognizable Iranian mosque silhouette: a stepped turquoise dome, paired minarets with balconies, arched entrance and window surrounds, cobalt/turquoise façade bands, a courtyard pool and low perimeter walls.

## Run

1. Open Blender 3.6+.
2. Go to the Scripting workspace.
3. Open `assets/blender/ganton_mosque_blockout_v2.py`.
4. Run Script.
5. Save the scene as `ganton_mosque_blockout_v2.blend`.
6. Export the mesh as OBJ if the automatic export operator is unavailable.

## Coordinate / scale notes

- Model footprint is approximately 25 x 22 Blender units.
- Front entrance faces negative Y.
- The scene origin is centered on the courtyard.
- These are blockout dimensions only. Final placement coordinates and scale must be checked against Ganton in-game.

## Not yet complete

This is still an untextured blockout with simple material colors. It has not been converted to DFF/TXD/COL, has no IDE/IPL, and has not been tested in GTA San Andreas. Before game integration, split render and collision meshes, reduce unnecessary objects, create proper UVs/textures, and verify the location in-game.
