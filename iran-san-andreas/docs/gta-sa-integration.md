# GTA San Andreas integration plan

## Asset pipeline

1. Review and optimize the Blender source mesh.
2. Separate render geometry from collision geometry.
3. Create or bake textures into a TXD-compatible image set.
4. Convert the render mesh to RenderWare DFF using a compatible GTA SA toolchain.
5. Create a simplified COL collision mesh and verify collision bounds.
6. Add IDE object definition and IPL placement.
7. Test loading through Mod Loader and inspect for crashes, z-fighting, bad normals and blocked paths.

## Placement constraints

- Ganton / Grove Street area, in a genuinely open footprint.
- Do not delete, replace or cover CJ's house.
- Preserve vehicle and pedestrian access on surrounding streets.
- Check the placement in-game before finalizing coordinates.

## Required final Mod Loader structure (planned)

```
modloader/
  Iran San Andreas/
    models/
      gta3.img/
        ganton_mosque.dff
        ganton_mosque.txd
        ganton_mosque.col
    data/
      maps/
        ganton_mosque.ide
        ganton_mosque.ipl
```

The exact folder and map-loading conventions must be verified against the chosen GTA SA installation and the final converted assets. The structure above is a target, not a tested package.
