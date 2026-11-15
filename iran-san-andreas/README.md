# Iran San Andreas — Ganton Mosque 1.0

A community mod project for **GTA San Andreas Classic PC**. The first milestone is a standalone Iranian-style mosque placed in an open area of Ganton without removing CJ's house or blocking Grove Street.

## Project status

- [x] Project branch created: `iran-san-andreas`
- [x] Initial asset specification
- [x] Procedural Blender source for a low-poly mosque blockout
- [ ] Review the model in Blender and tune scale/orientation
- [ ] Export and convert to GTA SA DFF/TXD/COL
- [ ] Create IDE/IPL placement files
- [ ] Test in-game with Mod Loader
- [ ] Package a verified ZIP

**Important:** DFF/TXD/COL conversion and in-game testing have not yet been completed. This repository does not claim that a ready-to-install mod exists yet.

## First asset: Ganton Mosque

Target look:
- Medium-sized Iranian mosque, GTA SA-era low-poly style
- Turquoise central dome and two slim minarets
- Blue/white tile accents, arched entrance, small courtyard and pool
- Three-color Iranian flag motif may be added as a separate texture/decal in a later pass
- Keep collision simple and walkable; do not block nearby roads or CJ's home

## Build the blockout

1. Open Blender 3.x or newer.
2. Switch to the Scripting workspace.
3. Open `assets/blender/ganton_mosque_blockout.py` and run it.
4. The script creates the blockout and attempts to export `ganton_mosque_blockout.obj` next to the script.

The OBJ is an intermediate source mesh, **not** a GTA DFF. The next conversion stage requires a GTA SA-compatible pipeline/toolchain and an in-game test.

## Folder map

- `assets/blender/` — procedural source meshes
- `docs/` — asset and integration notes

## Target game integration

Final Mod Loader layout will be documented after the model has been converted and tested. Planned game assets include DFF, TXD and COL, plus IDE/IPL placement data. Do not copy the current source OBJ directly into the GTA game folders.
