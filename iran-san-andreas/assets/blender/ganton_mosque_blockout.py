# Iran San Andreas — Ganton Mosque blockout
# Blender 3.x+
# Creates a low-poly, untextured blockout and exports an OBJ.
# This is source geometry only; it is NOT a GTA DFF.

import bpy
import math
import os
from mathutils import Vector

# Clear scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

def material(name, color):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = (*color, 1.0)
    return mat

sand = material("Warm limestone", (0.72, 0.62, 0.45))
tile = material("Turquoise dome", (0.05, 0.55, 0.58))
blue = material("Blue tile accents", (0.08, 0.25, 0.48))
white = material("White plaster", (0.88, 0.84, 0.72))
water = material("Pool water", (0.08, 0.35, 0.48))

def cube(name, loc, scale, mat, bevel=0.0):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    if bevel:
        mod = obj.modifiers.new("Soft stone edges", 'BEVEL')
        mod.width = bevel
        mod.segments = 1
        obj.modifiers.new("Weighted corner normals", 'WEIGHTED_NORMAL')
    return obj

def cylinder(name, loc, radius, depth, mat, vertices=12):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(mat)
    return obj

def uv_sphere(name, loc, scale, mat, segments=16, rings=8):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=rings, radius=1, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    return obj

# Courtyard platform and prayer hall
cube("Courtyard foundation", (0, 0, 0.25), (24, 20, 0.5), sand)
cube("Prayer hall", (0, 2.0, 2.2), (13, 10, 4.0), white)
cube("Front facade band", (0, -3.08, 2.0), (13.2, 0.28, 1.0), blue)
cube("Roof parapet", (0, 2.0, 4.35), (13.5, 10.5, 0.5), sand)

# Main turquoise dome and drum
cylinder("Dome drum", (0, 2.0, 4.9), 2.55, 1.0, white, 16)
uv_sphere("Main turquoise dome", (0, 2.0, 5.75), (2.55, 2.55, 1.75), tile, 16, 8)
cylinder("Dome finial stem", (0, 2.0, 7.55), 0.09, 0.65, sand, 8)
uv_sphere("Dome finial", (0, 2.0, 7.95), (0.18, 0.18, 0.28), sand, 8, 4)

# Two minarets, symmetrically placed at the front corners
for x in (-5.2, 5.2):
    cylinder("Minaret base", (x, -3.0, 1.15), 0.85, 1.8, sand, 12)
    cylinder("Minaret shaft", (x, -3.0, 4.0), 0.48, 4.0, white, 12)
    cylinder("Minaret balcony", (x, -3.0, 5.75), 0.78, 0.22, blue, 12)
    cylinder("Minaret upper shaft", (x, -3.0, 6.75), 0.32, 1.8, white, 12)
    uv_sphere("Minaret cap", (x, -3.0, 7.8), (0.48, 0.48, 0.7), tile, 12, 6)
    cylinder("Minaret finial", (x, -3.0, 8.45), 0.06, 0.5, sand, 8)

# Stylized arched entrance: rectangular surround with a dark inset and lintel.
cube("Entrance surround", (0, -3.25, 1.85), (3.4, 0.32, 3.5), blue)
cube("Entrance recess", (0, -3.45, 1.65), (2.35, 0.12, 2.75), sand)
cube("Entrance door", (0, -3.54, 1.45), (1.8, 0.1, 2.35), white)
# Decorative tile strips on the facade
for x in (-4.5, -3.2, 3.2, 4.5):
    cube("Blue facade tile panel", (x, -3.24, 2.2), (0.55, 0.12, 1.9), blue)

# Small courtyard pool
cube("Pool stone rim", (0, -7.0, 0.72), (5.2, 2.8, 0.45), white)
cube("Pool water", (0, -7.0, 0.96), (4.65, 2.25, 0.06), water)

# Simple entrance steps
for i in range(3):
    cube("Entrance step", (0, -4.2 - i*0.55, 0.55 + i*0.12), (4.0, 0.65, 0.22), sand)

# Set origin and export selected scene objects
bpy.ops.object.select_all(action='SELECT')
bpy.context.view_layer.objects.active = bpy.context.selected_objects[0]
for obj in bpy.context.selected_objects:
    obj.select_set(True)

out_dir = os.path.dirname(bpy.data.filepath) if bpy.data.filepath else os.getcwd()
out_path = os.path.join(out_dir, "ganton_mosque_blockout.obj")

try:
    bpy.ops.wm.obj_export(filepath=out_path, export_selected_objects=True)
except Exception:
    try:
        bpy.ops.export_scene.obj(filepath=out_path, use_selection=True)
    except Exception as exc:
        print("OBJ export operator unavailable. Save the .blend and export OBJ manually:", exc)

print("Ganton Mosque blockout scene created.")
