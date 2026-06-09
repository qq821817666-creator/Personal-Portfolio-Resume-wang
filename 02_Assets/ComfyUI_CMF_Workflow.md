# ComfyUI CMF Texture Generation Workflow
# ComfyUI CMF纹理生成工作流

## Overview / 概述

This document provides CMF-specific ComfyUI workflows for generating production-ready material textures.
ComfyUI's node-based approach allows precise control over texture output — essential for CMF design where
material accuracy matters more than artistic expression.

本文档提供面向CMF的ComfyUI工作流，用于生成可投入生产的材质纹理。

---

## Workflow 1: Seamless PBR Texture Generation
## 工作流1：无缝PBR纹理生成

### Node Setup

```
[Load Checkpoint: SDXL Base 1.0]
    │
    ├──▶ [CLIP Text Encode (Positive)]
    │       │
    │       └──▶ [KSampler (Efficient)]
    │                │
    ├──▶ [CLIP Text Encode (Negative)]
    │       │
    │       └──▶ [KSampler (Efficient)]
    │
    └──▶ [VAE Decode]
             │
             └──▶ [Save Image]

Optional ControlNet Additions:
[Load ControlNet: depth / canny / tile]
    │
    └──▶ [Apply ControlNet] ──▶ [KSampler]
```

### Recommended Checkpoints for CMF

| Checkpoint | Best For |
|------------|----------|
| SDXL Base 1.0 | General purpose, good for material textures |
| Juggernaut XL | Photorealistic product materials |
| Realistic Vision | Close-up macro textures |

---

## Workflow 2: CMF-Specific Prompt Templates
## 工作流2：CMF专用提示词模板

### Metal Finishes / 金属表面

```
POSITIVE: "close-up macro photograph of [FINISH] aluminum surface,
[DETAIL] texture visible, seamless tileable material texture,
PBR material reference, even studio lighting, neutral white balance,
industrial design reference, 8K, sharp focus, product quality"

NEGATIVE: "blurry, depth of field, vignette, shadows, reflections,
context, product visible, brand logo, text, watermark, 3D render"

Replace [FINISH] / [DETAIL] with:
- "sandblasted anodized" / "fine matte grain"
- "brushed hairline" / "horizontal fine lines, #220 grit"
- "polished mirror" / "high reflection, chrome-like"
- "PVD coated gunmetal" / "dark metallic with blue undertone"
- "bead blasted matte" / "uniform fine texture, low reflectivity"
```

### Leather & Textiles / 皮革与纺织

```
POSITIVE: "[MATERIAL] surface, close-up macro, [TEXTURE] visible,
seamless tileable, PBR material texture, studio lighting,
neutral gray background, 8K resolution, high detail fabric scan"

MATERIAL options:
- "fine Nappa leather grain, warm cognac brown"
- "Alcantara microfiber suede, dark charcoal, directional nap"
- "3D spacer knit textile, geometric honeycomb pattern, gray"
- "vegan bio-PU leather, fine embossed grain, cream"
- "recycled PET felt, compressed fiber texture, heathered gray"
```

### Plastics & Coatings / 塑料与涂层

```
POSITIVE: "[PLASTIC TYPE] surface, [FINISH] texture visible,
seamless tileable material scan, PBR reference,
industrial product quality, 8K macro, flat even lighting"

PLASTIC TYPE options:
- "soft-touch matte painted plastic, warm sand beige"
- "PCR recycled plastic with visible colored speckles, dark gray base"
- "fine Mold-Tech MT-11020 texture on black ABS plastic"
- "translucent frosted PMMA acrylic, edge-lit glow effect"
```

### Wood & Natural / 木材与天然

```
POSITIVE: "[WOOD TYPE] veneer, [GRAIN] grain visible,
open-pore matte finish, seamless tileable, PBR material scan,
natural wood texture, 8K, top-down flat scan, even exposure"

WOOD options:
- "FSC ash wood, straight grain, pale Scandinavian finish"
- "walnut burl, swirling dramatic grain, satin oil finish"
- "bamboo strand-woven, uniform linear pattern, carbonized amber"
- "cork composite, natural speckled texture, warm brown"
```

---

## Workflow 3: ControlNet for Product-Specific Textures
## 工作流3：使用ControlNet控制产品专用纹理

When you need the AI-generated texture to align with a specific product surface:

```
1. Render a grayscale depth/normal map of your 3D product surface
2. Use ControlNet (Canny or Depth) to constrain AI generation
3. The AI respects the surface contours while generating the texture
```

### Node Setup

```
[Load Image: product_depth_map.png]
    │
    └──▶ [ControlNet: Depth Preprocessor]
             │
             └──▶ [ControlNet Apply: Depth]
                      │
                      └──▶ [KSampler] ◀── [Prompt]

Result: AI texture that follows the product's 3D surface
```

---

## Workflow 4: Batch Texture Variation Generation
## 工作流4：批量纹理变体生成

Use ComfyUI's built-in batch capabilities to generate texture variations:

### Method: Prompt Queue with CSV

1. Create a CSV file with prompt variations:
```csv
seed,material,color,finish
42,anodized aluminum,space gray,matte bead blast
42,anodized aluminum,gold champagne,fine brush
42,anodized aluminum,midnight blue,matte fine grain
```

2. Use **Efficiency Nodes** or **WAS Node Suite** to read CSV and batch process

### Method: XY Plot for Color Variations

```
[CLIP Text Encode: base prompt]
    │
    └──▶ [XY Plot: replace "[COLOR]" with list]
             │
             └──▶ [KSampler] ──▶ [Grid Output]

Color list for XY:
"warm sand beige, charcoal black, sage green, terracotta clay,
 deep navy blue, champagne gold, mist gray, burnt orange,
 midnight violet, cream white"
```

---

## Post-Processing Pipeline
## 后处理流程

After ComfyUI generation, process textures for CMF use:

```
AI Generated Texture (PNG)
    │
    ├──▶ [Photoshop/GIMP: Make Seamless]
    │       - Offset filter (50%, 50%)
    │       - Clone stamp / content-aware fill seams
    │
    ├──▶ [Substance Sampler: Image-to-Material]
    │       - De-light the image
    │       - Generate: Base Color, Roughness, Normal, Height, Metallic
    │
    └──▶ [Blender/KeyShot: Apply as PBR Material]
            - Load PBR maps into Principled BSDF
            - Adjust scale and rotation
            - Test render under studio lighting
```

---

## Seed Library: Proven CMF Prompts
## 种子库：已验证的CMF提示词

### Category 1: Premium Metals
```
1. "sandblasted anodized aluminum surface, fine matte micro-texture,
   space gray color with subtle blue undertone, PBR material scan,
   seamless tileable, 8K, even studio lighting, sharp focus,
   product design reference, neutral white balance"

2. "brushed stainless steel, uniform horizontal hairline scratches,
   #320 grit finish, cool silver tone, PBR metal texture,
   seamless tileable, macro photo, flat lighting, 8K"
```

### Category 2: Automotive Interior
```
3. "automotive Alcantara microfiber, fine suede nap texture,
   dark charcoal gray, directional surface, premium car interior grade,
   PBR material, seamless, 8K macro, even diffused lighting"

4. "carbon fiber twill weave, 2x2 pattern, matte clear coat finish,
   dark gray with visible fiber direction, automotive grade,
   seamless tileable, PBR, 8K, flat top-down scan"
```

### Category 3: Sustainable Materials
```
5. "recycled ocean plastic speckle texture, dark base with
   multicolor visible flecks, matte satin finish, sustainable material,
   PBR scan, seamless tileable, 8K, even lighting, product quality"

6. "natural cork composite surface, organic speckled grain pattern,
   warm brown tone, sealed satin finish, sustainable material,
   PBR texture, seamless, 8K macro, flat scan"
```

### Category 4: Textiles
```
7. "3D engineered knit textile, geometric wave pattern,
   heathered gray melange yarn, sportswear-grade fabric,
   seamless tileable, PBR material, 8K macro scan"

8. "fine wool felt, compressed fiber texture, subtle heathered
   variation, warm gray tone, acoustic panel grade,
   seamless, PBR, 8K, flat even lighting"
```
