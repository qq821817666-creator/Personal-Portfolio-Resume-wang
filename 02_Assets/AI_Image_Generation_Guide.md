# AI Image Generation for CMF Portfolio Production
# AI绘图模型生成CMF作品集视觉素材

## 策略概述

使用AI绘图模型（Midjourney / DALL-E / Stable Diffusion / ComfyUI）替代传统3D建模+渲染流程，
快速产出作品集所需的产品图和材质渲染。时间优势：小时级 vs 天/周级。

---

## 视觉素材需求清单

每个项目需要的图片类型：

| 类型 | 数量 | 用途 | 生成难度 |
|------|------|------|----------|
| **产品概念草图** | 3-5张/项目 | 展示思考过程 | 低 |
| **产品Hero渲染** | 3-5张/项目 | 最终CMF展示 | 中高 |
| **材质特写/纹理** | 8-10张/项目 | CMF细节展示 | 低 |
| **趋势情绪板** | 5-8张/方向 | 趋势背景叙述 | 低 |
| **材质对比板** | 2-3张/项目 | 展示色彩变体 | 低-中 |
| **色彩调色板** | 3-5张/项目 | 色彩系统展示 | 低 |

---

## 项目A（耳机）AI生图提示词

### 1. 产品概念草图

```
Design concept sketch of premium wireless over-ear headphones,
industrial design style, loose marker rendering on paper texture,
warm gray tones with color accent highlights,
showing material transitions between metal, fabric, and leather zones,
multiple angles on single page, professional ID sketch style,
clean linework, sketchy but refined --ar 16:9
```

```
工业设计手绘草图，高端无线耳机，多角度展示，
马克笔渲染风格，温暖灰色调带彩色点缀，
展示金属/织物/皮革材质过渡区域 --ar 16:9
```

### 2. 产品Hero渲染（3个色彩方向）

#### Direction A: Warm Tech / 温暖科技

```
Photorealistic product rendering of premium wireless headphones,
warm sand beige matte aluminum earcups,
cognac leather ear cushions with subtle perforation pattern,
champagne gold PVD coated metal hinge arms,
soft-touch warm gray headband, minimal modern design language,
studio lighting on gradient gray background,
product photography, 8K, sharp focus, commercial quality --ar 4:3
```

#### Direction B: Neo-Sensorial / 超感体验

```
Photorealistic product shot of futuristic wireless headphones,
deep navy to teal gradient anodized aluminum body,
holographic iridescent accent ring that shifts from purple to green,
dark chrome metallic arms, deep navy microfiber ear cushions,
sci-fi luxe aesthetic, dramatic rim lighting,
studio photography, 8K, ultra-detailed --ar 4:3
```

#### Direction C: Raw Authenticity / 原生真实

```
Premium wireless headphones with visible recycled material aesthetic,
dark gray PCR plastic body with subtle colored speckles from recycled content,
natural cork composite side panels, raw clear anodized aluminum frame,
charcoal rPET recycled fabric ear cushions,
organic texture details, honest material expression,
studio lighting, 8K, editorial product photography --ar 4:3
```

### 3. 材质特写

```
Extreme close-up macro photograph of fine leather grain texture,
warm cognac brown color, subtle natural grain pattern visible,
product material reference, soft directional lighting to reveal texture,
8K resolution, sharp focus, seamless material surface --ar 1:1
```

```
Macro close-up of anodized aluminum surface, fine sandblasted matte texture,
champagne gold warm tone, even studio lighting, no reflections,
PBR material reference, industrial surface quality, 8K --ar 1:1
```

```
Close-up of recycled plastic surface with visible colored speckle pattern,
dark charcoal base with warm-toned flecks from post-consumer content,
matte finish, sustainable material aesthetic, 8K macro --ar 1:1
```

### 4. 色彩变体对比

```
Product photography lineup of 3 wireless headphones in different colors,
left: warm sand beige, center: deep navy blue, right: dark charcoal with speckle,
identical product design, same lighting, same angle, clean studio background,
commercial product comparison shot, 8K --ar 16:9
```

---

## 项目B（汽车内饰）AI生图提示词

### 1. 内饰概念图

```
Automotive interior concept design for premium NEV (new energy vehicle),
luxury minimalist dashboard with FSC ash wood inlay,
mycelium leather steering wheel wrap, ECONYL recycled knit seat fabric,
warm natural tones with biophilic design language,
ambient lighting in warm amber, modern Chinese NEV interior,
photorealistic automotive photography, 8K --ar 16:9
```

```
新能源汽车内饰概念设计，极简豪华仪表台，
FSC白蜡木镶嵌饰板，菌丝体皮革方向盘包裹，
再生尼龙3D针织座椅面料，温暖自然色调，
生物亲和设计语言，暖琥珀色氛围灯 --ar 16:9
```

### 2. 座椅材质特写

```
Close-up of premium automotive seat, ECONYL recycled yarn 3D knit textile,
deep navy blue with subtle colored flecks from ocean-sourced material,
fine sculpted bolsters in mycelium leather warm tan tone,
natural latex foam visible at edge, sustainable luxury aesthetic,
automotive interior photography, soft diffused lighting --ar 4:3
```

### 3. 门板材质过渡

```
Automotive door panel close-up showing material transition zones,
top: FSC ash wood open-pore matte veneer,
middle: recycled Alcantara dark charcoal suede insert,
bottom: PCR polypropylene textured plastic,
metal door handle in recycled aluminum satin clear anodized,
showing the contrast between natural and recycled materials,
diffused studio lighting, 8K automotive detail shot --ar 4:3
```

### 4. 方向盘细节

```
Steering wheel close-up detail,
mycelium leather wrap with fine organic grain in warm sand tone,
bio-resin center badge with embedded natural fibers,
recycled aluminum spoke in brushed satin finish,
natural material luxury, automotive detail photography, 8K --ar 3:2
```

---

## 材质纹理种子提示词（通用）

用于生成PBR材质贴图的种子图（后续ComfyUI/Substance处理）：

| 材质 | 提示词 | 参数 |
|------|--------|------|
| 阳极氧化铝 | "sandblasted anodized aluminum, fine matte grain, seamless, PBR" | --ar 1:1 --tile |
| PVD镀膜 | "PVD coated metal, champagne gold, fine brush pattern, seamless, PBR" | --ar 1:1 --tile |
| 软触漆 | "soft-touch matte paint surface, rubber-like coating texture, seamless" | --ar 1:1 --tile |
| 素食皮革 | "fine vegan leather grain, warm tan, subtle embossed pattern, seamless" | --ar 1:1 --tile |
| 3D编织 | "3D engineered knit textile, honeycomb pattern, heathered gray, seamless" | --ar 1:1 --tile |
| 碳纤维 | "carbon fiber twill 2x2 weave, matte clear coat, dark gray, seamless" | --ar 1:1 --tile |
| 木纹 | "FSC ash wood open-pore veneer, straight grain, natural, seamless" | --ar 1:1 --tile |
| PCR塑料 | "recycled plastic with colored speckles, dark base, matte, seamless" | --ar 1:1 --tile |
| 软木 | "natural cork composite, organic speckled grain, warm brown, seamless" | --ar 1:1 --tile |
| 全息效果 | "holographic iridescent film surface, blue-purple color shift, seamless" | --ar 1:1 --tile |

---

## 推荐生成流程

### 流程A：快速出图（最快，适合情绪板和概念展示）

```
Claude/ChatGPT 写提示词 → Midjourney/DALL-E 生成 →
Photoshop/Figma 排版 → 直接入作品集
适用：情绪板、概念草图、灵感参考
时间：每张图 5-15 分钟
```

### 流程B：精修出图（适合Hero图和最终展示）

```
Claude 写提示词 → Midjourney 生成4个候选 →
选最佳 → Photoshop细节修整 →
Figma排版入作品集 →
可选：ComfyUI ControlNet 用草稿约束再生成
时间：每张图 15-45 分钟
```

### 流程C：PBR纹理管线（适合材质特写和技术展示）

```
ComfyUI/Midjourney 生成纹理种子 →
Substance Sampler 转为PBR贴图 →
Blender 简单几何体上应用 → 渲染材质球 →
技术展示：Base Color / Roughness / Normal / Height 贴图
时间：每组材质 30-60 分钟
```

---

## 质量控制要点

1. **一致性：** 同一项目的所有图使用相同的基础提示词模板，只替换颜色/材质关键词
2. **色彩准确：** AI生成的色彩通常有偏差，需要用Photoshop曲线校色到目标Pantone/CIELAB值
3. **产品辨识度：** 多次生成选最佳——AI偶尔会生成"像但不对"的产品形态
4. **材质真实感：** 避免AI的塑料感——强制加 "PBR material, physically accurate, studio lighting"
5. **分辨率：** 所有图输出不低于2048px，Hero图建议4096px+
