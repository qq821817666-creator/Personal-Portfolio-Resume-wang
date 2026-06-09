"""
Blender CMF Material Presets
Blender CMF材质预设库

Run this script inside Blender's Scripting workspace.
在Blender的Scripting工作区中运行此脚本。

Creates a library of CMF-essential materials:
- Anodized Aluminum (various colors)
- Soft-touch Paint
- PVD Coating (various metallic finishes)
- Brushed Metal
- Vegan Leather / Microfiber
- Carbon Fiber
- Wood Veneer
- Translucent Plastic with Holographic Effect
- Recycled Plastic with Speckle
- Textile Mesh

Usage:
    Open Blender → Scripting workspace → Paste and run this script.
    Materials will be created in the current .blend file.
"""

import bpy
import math


def ensure_node_tree(material):
    """Set up the material with nodes if needed."""
    mat = bpy.data.materials.get(material)
    if mat is None:
        return None
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()
    return mat, nodes, links


def create_pbr_node_group(name):
    """Create a reusable PBR material with standard inputs."""
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()

    # Output
    output = nodes.new('ShaderNodeOutputMaterial')
    output.location = (400, 0)

    # Principled BSDF
    bsdf = nodes.new('ShaderNodeBsdfPrincipled')
    bsdf.location = (100, 0)
    bsdf.label = "CMF_Principled"
    links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])

    return mat, nodes, links, bsdf


# ═══════════════════════════════════════════════════════════════════════════
# MATERIAL PRESETS
# ═══════════════════════════════════════════════════════════════════════════

def create_anodized_aluminum(name="CMF_Anodized_Aluminum", color=(0.8, 0.82, 0.85, 1.0), roughness=0.15):
    """
    Sandblasted + anodized aluminum.
    Used for: Consumer electronics body, automotive trim accents.
    """
    mat, nodes, links, bsdf = create_pbr_node_group(name)
    bsdf.inputs['Base Color'].default_value = color
    bsdf.inputs['Metallic'].default_value = 0.0  # Anodized layer is non-metallic in PBR
    bsdf.inputs['Roughness'].default_value = roughness
    bsdf.inputs['Specular IOR Level'].default_value = 0.5  # Subtle specular
    # Slight anisotropy for brushed look
    bsdf.inputs['Anisotropic'].default_value = 0.3
    bsdf.inputs['Anisotropic Rotation'].default_value = 0.0
    print(f"✅ Created: {name}")
    return mat


def create_pvd_coating(name="CMF_PVD_Champagne", color=(0.854, 0.698, 0.459, 1.0), roughness=0.08):
    """
    PVD (Physical Vapor Deposition) coating on metal substrate.
    Used for: Premium trim accents, decorative rings, logos.
    Note: PVD colors — Champagne Gold, Rose Gold, Dark Chrome, Black Titanium
    """
    mat, nodes, links, bsdf = create_pbr_node_group(name)
    bsdf.inputs['Base Color'].default_value = color
    bsdf.inputs['Metallic'].default_value = 1.0  # PVD is highly metallic
    bsdf.inputs['Roughness'].default_value = roughness
    bsdf.inputs['Specular IOR Level'].default_value = 0.7
    # Subtle anisotropic for brushed texture under coating
    bsdf.inputs['Anisotropic'].default_value = 0.15
    print(f"✅ Created: {name}")
    return mat


def create_soft_touch_paint(name="CMF_SoftTouch_Matte", color=(0.18, 0.19, 0.22, 1.0), roughness=0.55):
    """
    Soft-touch matte paint (rubber-like feel coating).
    Used for: Consumer electronics housing, grip surfaces, automotive interior panels.
    Critical parameters: High roughness (0.5-0.65), zero metallic, low specular.
    """
    mat, nodes, links, bsdf = create_pbr_node_group(name)
    bsdf.inputs['Base Color'].default_value = color
    bsdf.inputs['Metallic'].default_value = 0.0
    bsdf.inputs['Roughness'].default_value = roughness
    bsdf.inputs['Specular IOR Level'].default_value = 0.1  # Very low specular
    bsdf.inputs['Clearcoat Roughness'].default_value = 0.3
    print(f"✅ Created: {name}")
    return mat


def create_textured_paint(name="CMF_TexturedPaint", color=(0.9, 0.88, 0.84, 1.0), roughness=0.4):
    """
    Paint with visible texture (fine orange peel or leather-grain texture).
    Requires a bump/normal map for the texture pattern.
    """
    mat, nodes, links, bsdf = create_pbr_node_group(name)
    bsdf.inputs['Base Color'].default_value = color
    bsdf.inputs['Metallic'].default_value = 0.0
    bsdf.inputs['Roughness'].default_value = roughness

    # Add noise-based bump for subtle texture
    tex = nodes.new('ShaderNodeTexNoise')
    tex.location = (-300, -200)
    tex.inputs['Scale'].default_value = 80.0
    tex.inputs['Detail'].default_value = 4.0
    tex.inputs['Roughness'].default_value = 0.6

    bump = nodes.new('ShaderNodeBump')
    bump.location = (-100, -200)
    bump.inputs['Strength'].default_value = 0.02  # Very subtle
    links.new(tex.outputs['Fac'], bump.inputs['Height'])
    links.new(bump.outputs['Normal'], bsdf.inputs['Normal'])

    print(f"✅ Created: {name}")
    return mat


def create_leather_vegan(name="CMF_Vegan_Leather", color=(0.22, 0.17, 0.13, 1.0), roughness=0.6):
    """
    Vegan leather / bio-based PU.
    Used for: Ear cushions, headbands, automotive seat surfaces.
    """
    mat, nodes, links, bsdf = create_pbr_node_group(name)
    bsdf.inputs['Base Color'].default_value = color
    bsdf.inputs['Metallic'].default_value = 0.0
    bsdf.inputs['Roughness'].default_value = roughness
    bsdf.inputs['Sheen Weight'].default_value = 0.3  # Leather sheen
    bsdf.inputs['Sheen Tint'].default_value = 0.2

    # Subtle surface grain via noise
    tex = nodes.new('ShaderNodeTexNoise')
    tex.location = (-300, -200)
    tex.inputs['Scale'].default_value = 150.0
    tex.inputs['Detail'].default_value = 6.0

    bump = nodes.new('ShaderNodeBump')
    bump.location = (-100, -200)
    bump.inputs['Strength'].default_value = 0.03
    links.new(tex.outputs['Fac'], bump.inputs['Height'])
    links.new(bump.outputs['Normal'], bsdf.inputs['Normal'])

    print(f"✅ Created: {name}")
    return mat


def create_textile_knit(name="CMF_Textile_Knit", color=(0.5, 0.48, 0.45, 1.0), roughness=0.75):
    """
    Woven/knit textile.
    Used for: Speaker grille fabric, automotive seat fabric, headphone mesh.
    """
    mat, nodes, links, bsdf = create_pbr_node_group(name)
    bsdf.inputs['Base Color'].default_value = color
    bsdf.inputs['Metallic'].default_value = 0.0
    bsdf.inputs['Roughness'].default_value = roughness
    bsdf.inputs['Sheen Weight'].default_value = 0.15
    bsdf.inputs['Sheen Tint'].default_value = 0.0

    # Fabric texture
    tex = nodes.new('ShaderNodeTexNoise')
    tex.location = (-300, -200)
    tex.inputs['Scale'].default_value = 200.0
    tex.inputs['Detail'].default_value = 8.0

    # Mix with wave for woven look
    wave = nodes.new('ShaderNodeTexWave')
    wave.location = (-300, -400)
    wave.inputs['Scale'].default_value = 10.0
    wave.inputs['Distortion'].default_value = 2.0

    mix = nodes.new('ShaderNodeMixRGB')
    mix.location = (-100, -300)
    mix.inputs['Fac'].default_value = 0.5
    links.new(tex.outputs['Fac'], mix.inputs['Color1'])
    links.new(wave.outputs['Fac'], mix.inputs['Color2'])

    bump = nodes.new('ShaderNodeBump')
    bump.location = (100, -300)
    bump.inputs['Strength'].default_value = 0.06
    links.new(mix.outputs['Color'], bump.inputs['Height'])
    links.new(bump.outputs['Normal'], bsdf.inputs['Normal'])

    print(f"✅ Created: {name}")
    return mat


def create_carbon_fiber(name="CMF_CarbonFiber"):
    """Carbon fiber weave pattern."""
    mat, nodes, links, bsdf = create_pbr_node_group(name)
    bsdf.inputs['Base Color'].default_value = (0.02, 0.02, 0.03, 1.0)
    bsdf.inputs['Metallic'].default_value = 0.0
    bsdf.inputs['Roughness'].default_value = 0.25
    bsdf.inputs['Specular IOR Level'].default_value = 0.4

    # Carbon fiber weave pattern
    wave_x = nodes.new('ShaderNodeTexWave')
    wave_x.location = (-400, -200)
    wave_x.inputs['Scale'].default_value = 15.0
    wave_x.inputs['Distortion'].default_value = 0.5
    wave_x.wave_type = 'BANDS'
    wave_x.bands_direction = 'X'

    wave_y = nodes.new('ShaderNodeTexWave')
    wave_y.location = (-400, -400)
    wave_y.inputs['Scale'].default_value = 15.0
    wave_y.inputs['Distortion'].default_value = 0.5
    wave_y.wave_type = 'BANDS'
    wave_y.bands_direction = 'Y'

    mix = nodes.new('ShaderNodeMixRGB')
    mix.location = (-100, -300)
    links.new(wave_x.outputs['Fac'], mix.inputs['Color1'])
    links.new(wave_y.outputs['Fac'], mix.inputs['Color2'])

    bump = nodes.new('ShaderNodeBump')
    bump.location = (100, -300)
    bump.inputs['Strength'].default_value = 0.02
    links.new(mix.outputs['Color'], bump.inputs['Height'])
    links.new(bump.outputs['Normal'], bsdf.inputs['Normal'])

    print(f"✅ Created: {name}")
    return mat


def create_recycled_plastic_speckle(name="CMF_PCR_Plastic", base_color=(0.15, 0.15, 0.17, 1.0), roughness=0.3):
    """
    Post-consumer recycled plastic with visible speckle pattern.
    Used for: Sustainable product housing.
    """
    mat, nodes, links, bsdf = create_pbr_node_group(name)
    bsdf.inputs['Base Color'].default_value = base_color
    bsdf.inputs['Metallic'].default_value = 0.0
    bsdf.inputs['Roughness'].default_value = roughness

    # Speckle pattern: high-scale noise mapped through color ramp for dots
    noise = nodes.new('ShaderNodeTexNoise')
    noise.location = (-400, -200)
    noise.inputs['Scale'].default_value = 200.0
    noise.inputs['Detail'].default_value = 10.0

    # Color ramp to create speckle dots from noise
    ramp = nodes.new('ShaderNodeValToRGB')
    ramp.location = (-200, -200)
    ramp.color_ramp.elements[0].position = 0.55
    ramp.color_ramp.elements[0].color = base_color
    ramp.color_ramp.elements[1].position = 0.65
    ramp.color_ramp.elements[1].color = (0.85, 0.82, 0.55, 1.0)  # Warm speckle
    links.new(noise.outputs['Fac'], ramp.inputs['Fac'])

    mix = nodes.new('ShaderNodeMixRGB')
    mix.location = (0, -200)
    mix.inputs['Fac'].default_value = 0.7
    links.new(ramp.outputs['Color'], mix.inputs['Color1'])
    mix.inputs['Color2'].default_value = base_color

    # Bump for speckle texture
    bump = nodes.new('ShaderNodeBump')
    bump.location = (200, -200)
    bump.inputs['Strength'].default_value = 0.01
    links.new(noise.outputs['Fac'], bump.inputs['Height'])
    links.new(bump.outputs['Normal'], bsdf.inputs['Normal'])

    # Route the mixed color through a subtle addition to Base Color
    # (Simplified — in practice use an image texture from AI generation)
    print(f"✅ Created: {name}")

    return mat


def create_wood_veneer(name="CMF_Wood_Walnut"):
    """Dark walnut wood veneer with visible grain."""
    mat, nodes, links, bsdf = create_pbr_node_group(name)
    bsdf.inputs['Base Color'].default_value = (0.25, 0.15, 0.08, 1.0)
    bsdf.inputs['Metallic'].default_value = 0.0
    bsdf.inputs['Roughness'].default_value = 0.4
    bsdf.inputs['Sheen Weight'].default_value = 0.2

    # Wood grain: stretched wave texture
    mapping = nodes.new('ShaderNodeMapping')
    mapping.location = (-500, -200)
    mapping.inputs['Scale'].default_value = (1.0, 0.1, 1.0)  # Stretched in Y

    coord = nodes.new('ShaderNodeTexCoord')
    coord.location = (-700, -200)
    links.new(coord.outputs['Object'], mapping.inputs['Vector'])

    wave = nodes.new('ShaderNodeTexWave')
    wave.location = (-300, -200)
    wave.inputs['Scale'].default_value = 3.0
    wave.inputs['Distortion'].default_value = 8.0
    wave.wave_type = 'BANDS'
    wave.bands_direction = 'Y'
    links.new(mapping.outputs['Vector'], wave.inputs['Vector'])

    # Color ramp for wood tones
    ramp = nodes.new('ShaderNodeValToRGB')
    ramp.location = (-100, -200)
    ramp.color_ramp.elements[0].position = 0.0
    ramp.color_ramp.elements[0].color = (0.15, 0.08, 0.02, 1.0)
    ramp.color_ramp.elements[1].position = 0.5
    ramp.color_ramp.elements[1].color = (0.35, 0.20, 0.10, 1.0)
    links.new(wave.outputs['Fac'], ramp.inputs['Fac'])

    bump = nodes.new('ShaderNodeBump')
    bump.location = (100, -200)
    bump.inputs['Strength'].default_value = 0.02
    links.new(wave.outputs['Fac'], bump.inputs['Height'])
    links.new(bump.outputs['Normal'], bsdf.inputs['Normal'])

    print(f"✅ Created: {name}")
    return mat


def create_holographic_iridescent(name="CMF_Holographic"):
    """Holographic/iridescent color-shifting effect."""
    mat, nodes, links, bsdf = create_pbr_node_group(name)

    # Use a thin-film like effect via layer weight node
    layer_weight = nodes.new('ShaderNodeLayerWeight')
    layer_weight.location = (-400, 0)
    layer_weight.inputs['Blend'].default_value = 0.3

    # Color ramp to create angle-dependent color shift
    ramp = nodes.new('ShaderNodeValToRGB')
    ramp.location = (-200, 0)
    ramp.color_ramp.elements[0].position = 0.0
    ramp.color_ramp.elements[0].color = (0.2, 0.0, 0.6, 1.0)  # Deep purple
    ramp.color_ramp.elements[1].position = 0.3
    ramp.color_ramp.elements[1].color = (0.0, 0.4, 0.8, 1.0)  # Blue
    ramp.color_ramp.interpolation = 'B_SPLINE'
    links.new(layer_weight.outputs['Facing'], ramp.inputs['Fac'])

    bsdf.inputs['Base Color'].default_value = (0.5, 0.3, 0.9, 1.0)
    bsdf.inputs['Metallic'].default_value = 0.1
    bsdf.inputs['Roughness'].default_value = 0.05
    bsdf.inputs['Clearcoat'].default_value = 1.0
    bsdf.inputs['Clearcoat Roughness'].default_value = 0.02

    # Drive clearcoat tint with iridescent color
    # links.new(ramp.outputs['Color'], bsdf.inputs['???'])

    # Simplified: Use a gradient texture for base color
    grad = nodes.new('ShaderNodeTexGradient')
    grad.location = (-400, -200)
    grad.gradient_type = 'SPHERICAL'

    color_ramp = nodes.new('ShaderNodeValToRGB')
    color_ramp.location = (-200, -200)
    color_ramp.color_ramp.elements[0].position = 0.0
    color_ramp.color_ramp.elements[0].color = (0.8, 0.2, 0.7, 1.0)
    color_ramp.color_ramp.elements[1].position = 0.5
    color_ramp.color_ramp.elements[1].color = (0.2, 0.6, 0.9, 1.0)
    color_ramp.color_ramp.interpolation = 'B_SPLINE'
    links.new(grad.outputs['Fac'], color_ramp.inputs['Fac'])
    links.new(color_ramp.outputs['Color'], bsdf.inputs['Base Color'])

    print(f"✅ Created: {name}")
    return mat


def create_cmf_studio_lighting():
    """
    Set up a CMF-friendly studio lighting rig.
    3-point lighting optimized for material review (not dramatic product shots).
    """
    # Remove existing lights
    for obj in bpy.data.objects:
        if obj.type == 'LIGHT':
            bpy.data.objects.remove(obj)

    # Key light (main illumination)
    key = bpy.data.objects.new("CMF_KeyLight", bpy.data.lights.new("CMF_KeyLight", 'AREA'))
    bpy.context.collection.objects.link(key)
    key.location = (3, -2, 4)
    key.rotation_euler = (math.radians(45), math.radians(15), math.radians(30))
    key.data.energy = 500
    key.data.size = 2.0

    # Fill light (soften shadows)
    fill = bpy.data.objects.new("CMF_FillLight", bpy.data.lights.new("CMF_FillLight", 'AREA'))
    bpy.context.collection.objects.link(fill)
    fill.location = (-2, 1, 2)
    fill.rotation_euler = (math.radians(30), math.radians(-15), math.radians(-20))
    fill.data.energy = 200
    fill.data.size = 3.0

    # Rim/back light (separate product from background)
    rim = bpy.data.objects.new("CMF_RimLight", bpy.data.lights.new("CMF_RimLight", 'AREA'))
    bpy.context.collection.objects.link(rim)
    rim.location = (0, -4, 2.5)
    rim.rotation_euler = (math.radians(60), 0, math.radians(180))
    rim.data.energy = 300
    rim.data.size = 1.5

    # Neutral gradient background
    world = bpy.context.scene.world
    world.use_nodes = True
    world_nodes = world.node_tree.nodes
    world_nodes.clear()

    bg = world_nodes.new('ShaderNodeBackground')
    bg.inputs['Strength'].default_value = 0.3

    # Gradient: light gray top → mid gray bottom
    grad = world_nodes.new('ShaderNodeTexGradient')
    grad.gradient_type = 'LINEAR'

    coord = world_nodes.new('ShaderNodeTexCoord')
    bg_map = world_nodes.new('ShaderNodeMapping')
    bg_map.inputs['Rotation'].default_value = (0, 0, math.radians(90))
    world_nodes.links.new(coord.outputs['Generated'], bg_map.inputs['Vector'])
    world_nodes.links.new(bg_map.outputs['Vector'], grad.inputs['Vector'])

    ramp = world_nodes.new('ShaderNodeValToRGB')
    ramp.color_ramp.elements[0].color = (0.85, 0.85, 0.85, 1.0)  # Bottom
    ramp.color_ramp.elements[1].color = (0.95, 0.95, 0.95, 1.0)  # Top
    world_nodes.links.new(grad.outputs['Fac'], ramp.inputs['Fac'])
    world_nodes.links.new(ramp.outputs['Color'], bg.inputs['Color'])

    output = world_nodes.new('ShaderNodeOutputWorld')
    world_nodes.links.new(bg.outputs['Background'], output.inputs['Surface'])

    # Set render settings for CMF-quality output
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.cycles.samples = 512
    bpy.context.scene.cycles.use_denoising = True
    bpy.context.scene.render.resolution_x = 3000
    bpy.context.scene.render.resolution_y = 3000
    bpy.context.scene.render.film_transparent = True
    bpy.context.scene.view_settings.view_transform = 'Filmic'
    bpy.context.scene.view_settings.look = 'Medium High Contrast'

    print("✅ Studio lighting rig created")
    print("✅ Render settings: Cycles, 512 samples, 3000px, Filmic")


# ═══════════════════════════════════════════════════════════════════════════
# GENERATE ALL PRESETS
# ═══════════════════════════════════════════════════════════════════════════

def generate_cmf_library():
    """Generate the complete CMF material library."""
    print("\n🎨 Generating CMF Material Library...")
    print("=" * 50)

    # ── Anodized Aluminum Series ──
    create_anodized_aluminum("CMF_Anodized_SpaceGray", color=(0.18, 0.19, 0.21, 1.0), roughness=0.12)
    create_anodized_aluminum("CMF_Anodized_Silver", color=(0.82, 0.83, 0.85, 1.0), roughness=0.10)
    create_anodized_aluminum("CMF_Anodized_Midnight", color=(0.08, 0.09, 0.15, 1.0), roughness=0.12)
    create_anodized_aluminum("CMF_Anodized_Gold", color=(0.82, 0.70, 0.50, 1.0), roughness=0.10)

    # ── PVD Coating Series ──
    create_pvd_coating("CMF_PVD_ChampagneGold", color=(0.854, 0.698, 0.459, 1.0), roughness=0.08)
    create_pvd_coating("CMF_PVD_RoseGold", color=(0.85, 0.60, 0.55, 1.0), roughness=0.08)
    create_pvd_coating("CMF_PVD_DarkChrome", color=(0.25, 0.26, 0.28, 1.0), roughness=0.05)
    create_pvd_coating("CMF_PVD_BlackTitanium", color=(0.12, 0.13, 0.14, 1.0), roughness=0.06)

    # ── Soft-Touch Paint Series ──
    create_soft_touch_paint("CMF_SoftTouch_Charcoal", color=(0.18, 0.19, 0.22, 1.0), roughness=0.55)
    create_soft_touch_paint("CMF_SoftTouch_WarmSand", color=(0.82, 0.78, 0.71, 1.0), roughness=0.55)
    create_soft_touch_paint("CMF_SoftTouch_Clay", color=(0.65, 0.50, 0.42, 1.0), roughness=0.55)
    create_soft_touch_paint("CMF_SoftTouch_SageGreen", color=(0.55, 0.60, 0.52, 1.0), roughness=0.55)

    # ── Vegan Leather Series ──
    create_leather_vegan("CMF_Leather_Cognac", color=(0.35, 0.20, 0.10, 1.0), roughness=0.55)
    create_leather_vegan("CMF_Leather_Black", color=(0.06, 0.06, 0.07, 1.0), roughness=0.55)
    create_leather_vegan("CMF_Leather_WarmGray", color=(0.32, 0.30, 0.28, 1.0), roughness=0.55)

    # ── Specialty Materials ──
    create_textile_knit("CMF_Textile_KnitGray", color=(0.5, 0.48, 0.45, 1.0), roughness=0.75)
    create_carbon_fiber("CMF_CarbonFiber_Twill")
    create_wood_veneer("CMF_Wood_Walnut")
    create_holographic_iridescent("CMF_Holographic_Aurora")
    create_recycled_plastic_speckle("CMF_PCR_SpeckledBlack", base_color=(0.12, 0.13, 0.15, 1.0), roughness=0.35)

    print("\n" + "=" * 50)
    print("✅ CMF Material Library Complete!")
    print(f"   Total materials: {len(bpy.data.materials)}")
    print("\n📋 Next Steps:")
    print("   1. Import your 3D model (File → Import)")
    print("   2. Select objects and assign CMF materials")
    print("   3. Adjust lighting (run create_cmf_studio_lighting())")
    print("   4. Render (F12)")
    print("=" * 50)


# Run on script execution
if __name__ == "__main__":
    generate_cmf_library()
    create_cmf_studio_lighting()
