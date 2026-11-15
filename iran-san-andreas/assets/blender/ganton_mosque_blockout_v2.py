# Iran San Andreas — Ganton Mosque blockout v2
# Blender 3.6+ / 4.x. Run from Blender's Scripting workspace.
# Creates editable low-poly source geometry and exports an OBJ.
# OBJ is an intermediate mesh, NOT a GTA San Andreas DFF.

import bpy
import math
import os
from mathutils import Vector

# ---------- scene ----------
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

def mat(name, color):
    m = bpy.data.materials.new(name)
    m.diffuse_color = (*color, 1.0)
    return m

LIMESTONE = mat("01 Limestone", (0.68, 0.56, 0.39))
PLASTER = mat("02 Warm white plaster", (0.88, 0.82, 0.69))
TURQUOISE = mat("03 Turquoise glazed tile", (0.035, 0.43, 0.48))
DARKBLUE = mat("04 Cobalt tile", (0.035, 0.14, 0.34))
PALEBLUE = mat("05 Pale blue tile", (0.28, 0.58, 0.68))
WOOD = mat("06 Dark entrance wood", (0.19, 0.095, 0.045))
WATER = mat("07 Courtyard water", (0.035, 0.25, 0.34))
GOLD = mat("08 Brass details", (0.62, 0.39, 0.12))

def cube(name, loc, dims, material, bevel=0.0):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    o = bpy.context.object
    o.name = name
    o.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    o.data.materials.append(material)
    if bevel:
        b = o.modifiers.new("Tiny edge chamfer", 'BEVEL')
        b.width = bevel
        b.segments = 1
        o.modifiers.new("Weighted normals", 'WEIGHTED_NORMAL')
    return o

def cyl(name, loc, radius, depth, material, vertices=12, radius2=None):
    if radius2 is None:
        bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=loc)
    else:
        bpy.ops.mesh.primitive_cone_add(vertices=vertices, radius1=radius, radius2=radius2, depth=depth, location=loc)
    o = bpy.context.object
    o.name = name
    o.data.materials.append(material)
    return o

def sphere(name, loc, scale, material, segments=16, rings=8):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=rings, radius=1, location=loc)
    o = bpy.context.object
    o.name = name
    o.scale = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    o.data.materials.append(material)
    return o

def arch_solid(name, x, y, z, width, straight_height, arch_radius, depth, material):
    """Extruded arched panel. Front face points toward negative Y."""
    r = min(arch_radius, width / 2.0)
    pts = [(-width/2, 0), (width/2, 0),
           (width/2, straight_height)]
    # semicircular crown from right spring point to left spring point
    for i in range(1, 9):
        a = math.pi * i / 8.0
        pts.append((r * math.cos(a), straight_height + r * math.sin(a)))
    pts.append((-width/2, 0))
    # Remove duplicate consecutive/closing point
    clean = []
    for p in pts:
        if not clean or (Vector(p) - Vector(clean[-1])).length > 1e-5:
            clean.append(p)
    n = len(clean)
    verts = []
    for yy in (y - depth/2, y + depth/2):
        verts.extend([(x + px, yy, z + pz) for px, pz in clean])
    faces = [tuple(range(n)), tuple(range(n, 2*n))]
    for i in range(n):
        j = (i + 1) % n
        faces.append((i, j, n+j, n+i))
    mesh = bpy.data.meshes.new(name + "Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.materials.append(material)
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    return obj

# ---------- courtyard and prayer hall ----------
cube("Courtyard plinth", (0, 0, 0.15), (25, 22, 0.3), LIMESTONE, 0.08)
cube("Prayer hall mass", (0, 2.3, 2.15), (13.5, 10.5, 3.7), PLASTER, 0.05)
cube("Front cobalt dado", (0, -3.02, 1.25), (13.55, 0.16, 0.72), DARKBLUE)
cube("Front tile frieze", (0, -3.04, 3.45), (13.55, 0.18, 0.32), TURQUOISE)
cube("Roof parapet", (0, 2.3, 4.12), (14.0, 11.0, 0.42), LIMESTONE, 0.04)

# Main entrance: deep blue surround, recessed arched opening, wood door.
arch_solid("Entrance blue arch surround", 0, -3.22, 0.55, 3.5, 1.65, 1.75, 0.34, DARKBLUE)
arch_solid("Entrance recessed opening", 0, -3.42, 0.58, 2.65, 1.45, 1.32, 0.14, LIMESTONE)
arch_solid("Arched wooden door", 0, -3.53, 0.60, 2.05, 1.25, 1.02, 0.10, WOOD)
# Door leaves and brass studs
cube("Door central seam", (0, -3.60, 1.45), (0.035, 0.035, 1.65), GOLD)
for x in (-0.72, 0.72):
    for z in (1.1, 1.55, 2.0):
        sphere("Door brass stud", (x, -3.62, z), (0.045, 0.025, 0.045), GOLD, 8, 4)

# Façade arched windows, two on each side of entrance.
for x in (-4.7, -2.8, 2.8, 4.7):
    arch_solid("Window cobalt surround", x, -3.18, 1.55, 0.95, 0.78, 0.47, 0.22, DARKBLUE)
    arch_solid("Window pale blue inset", x, -3.32, 1.62, 0.65, 0.65, 0.32, 0.10, PALEBLUE)
    cube("Window sill", (x, -3.36, 1.52), (1.15, 0.28, 0.12), LIMESTONE)

# Main dome drum, stepped turquoise dome and finial.
cyl("Main dome drum", (0, 2.3, 4.55), 2.55, 0.75, DARKBLUE, 16)
cyl("Dome turquoise lower ring", (0, 2.3, 5.02), 2.42, 0.22, TURQUOISE, 16)
sphere("Main turquoise dome", (0, 2.3, 5.85), (2.38, 2.38, 1.55), TURQUOISE, 16, 8)
cyl("Dome neck", (0, 2.3, 7.22), 0.18, 0.38, GOLD, 8)
sphere("Dome finial orb", (0, 2.3, 7.48), (0.16, 0.16, 0.22), GOLD, 8, 4)
cyl("Dome finial spike", (0, 2.3, 7.77), 0.035, 0.42, GOLD, 8, 0.0)

# Minarets, set slightly forward of the dome.
for x in (-5.35, 5.35):
    y = -2.45
    cyl("Minaret stone base", (x, y, 1.15), 0.82, 1.55, LIMESTONE, 12)
    cyl("Minaret blue base band", (x, y, 1.92), 0.68, 0.18, DARKBLUE, 12)
    cyl("Minaret shaft", (x, y, 3.75), 0.43, 3.55, PLASTER, 12)
    cyl("Minaret turquoise band", (x, y, 5.15), 0.47, 0.18, TURQUOISE, 12)
    cyl("Minaret balcony lower", (x, y, 5.62), 0.72, 0.18, DARKBLUE, 12)
    cyl("Minaret balcony upper", (x, y, 5.78), 0.64, 0.12, LIMESTONE, 12)
    cyl("Minaret lantern shaft", (x, y, 6.55), 0.28, 1.45, PLASTER, 12)
    cyl("Minaret lantern band", (x, y, 7.28), 0.36, 0.12, TURQUOISE, 12)
    cyl("Minaret pointed cap", (x, y, 7.68), 0.38, 0.72, TURQUOISE, 12, 0.025)
    cyl("Minaret finial", (x, y, 8.18), 0.035, 0.35, GOLD, 8, 0.0)

# Side tile panels and shallow buttresses.
for side in (-1, 1):
    for y in (-1.6, 1.0, 3.6, 5.7):
        cube("Side wall buttress", (side * 6.82, y, 2.0), (0.28, 0.65, 3.0), LIMESTONE)
        cube("Side cobalt tile inset", (side * 6.98, y, 2.35), (0.08, 0.42, 1.25), DARKBLUE)

# Courtyard pool, stone rim and shallow steps.
cube("Pool outer stone rim", (0, -7.2, 0.48), (5.8, 3.15, 0.42), LIMESTONE, 0.06)
cube("Pool blue water", (0, -7.2, 0.70), (5.25, 2.58, 0.06), WATER)
for i in range(3):
    cube("Entrance approach step", (0, -4.05 - i*0.62, 0.45 - i*0.07),
         (4.3, 0.68, 0.18), LIMESTONE, 0.025)

# Low courtyard boundary walls with a clear central opening.
for x in (-10.4, 10.4):
    cube("Courtyard side wall", (x, -0.2, 0.82), (0.35, 15.0, 1.25), PLASTER)
    for y in (-6.5, -2.5, 1.5, 5.5):
        cube("Courtyard wall pier", (x, y, 1.05), (0.55, 0.55, 1.7), LIMESTONE)
# Rear wall
cube("Courtyard rear wall", (0, 9.9, 0.82), (21.0, 0.35, 1.25), PLASTER)

# Scene organization
root = bpy.data.collections.new("IRAN SA - Ganton Mosque")
bpy.context.scene.collection.children.link(root)
for obj in list(bpy.context.scene.objects):
    for c in list(obj.users_collection):
        c.objects.unlink(obj)
    root.objects.link(obj)

# Export selected objects to OBJ beside this script (or current working directory).
bpy.ops.object.select_all(action='SELECT')
out_dir = os.path.dirname(bpy.data.filepath) if bpy.data.filepath else os.getcwd()
out_path = os.path.join(out_dir, "ganton_mosque_blockout_v2.obj")
try:
    bpy.ops.wm.obj_export(filepath=out_path, export_selected_objects=True)
except Exception:
    try:
        bpy.ops.export_scene.obj(filepath=out_path, use_selection=True)
    except Exception as exc:
        print("OBJ export unavailable; save the Blender file and export OBJ manually:", exc)

print("Iran San Andreas mosque blockout v2 created:", out_path)
