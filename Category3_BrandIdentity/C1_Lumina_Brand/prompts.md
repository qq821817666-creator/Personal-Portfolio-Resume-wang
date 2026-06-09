# C1 Lumina Brand Identity — AI Image Prompts

> 使用 GPT Image 2 / Nano Banana Pro 生成。图片放入 `Renders/` 目录。
> 当前页面用纯CSS占位，生成图片后替换对应区域。

---

## 01_hero_logo.png — Hero区Logo主视觉

```
A luxury beauty brand logo hero image. The word "LUMINA" displayed in an elegant refined serif typeface on a pristine white marble surface with soft rose gold ambient lighting. A geometric abstract logomark symbol (a stylized intersecting circle-and-arc representing light and skin) sits above the wordmark. Premium editorial photography style, cream and rose gold warm metallic tones, shallow depth of field, polished marble texture visible. The logo is centered and prominent. 16:9 cinematic composition with generous negative space around the logo.
```
- Aspect ratio: `16:9`
- Size: `2K`

---

## 02_brand_moodboard.png — 品牌情绪板

```
Brand identity moodboard for a luxury skincare-tech brand called LUMINA. Editorial collage style featuring: dermatology precision tools (a sleek metal treatment tool), smooth jade stones, frosted glass serum bottles, soft warm linen textiles, warm candlelight glow, a minimalist spa interior with marble surfaces, and soft green botanical elements. The overall color palette is cream, rose gold, soft sage green, and warm beige. Refined, minimal, high-end beauty and wellness aesthetic. Centered composition.
```
- Aspect ratio: `16:9`
- Size: `2K`

---

## 03_logo_system.png — Logo系统规范图

```
Brand identity logo system guideline sheet for LUMINA brand. Clean white background with four logo variations arranged in a 2x2 grid: (1) full horizontal logo — abstract geometric circular symbol on the left + "LUMINA" wordmark on the right, (2) stacked logo — symbol centered above the wordmark, (3) logomark icon only — the abstract geometric symbol standalone, (4) wordmark only — just the "LUMINA" text. Thin gray dimension lines and arrows indicate clear space rules around each logo. Professional brand guidelines layout, minimal, precise, like a page from a design system manual.
```
- Aspect ratio: `4:3`
- Size: `2K`

---

## 04_packaging.png — 产品包装Mockup

```
Luxury beauty device product packaging box mockup. Pearl white FSC-certified kraft paper box with a rose gold foil-stamped "LUMINA" logo centered on the lid. The box is shown at a 3/4 angle, partially open, revealing a molded sugarcane fiber interior tray in natural beige. A sleek white and rose gold beauty device is nestled inside, wrapped in soft translucent tissue paper. Placed on a marble vanity surface with soft warm natural window light. Clean premium product photography style. Rose gold foil catch-light visible.
```
- Aspect ratio: `4:3`
- Size: `2K`

---

## 05_quickstart_guide.png — 快速入门指南

```
Product quick-start instruction card flat-lay overhead photography for a beauty device brand. A bi-fold card made of recycled uncoated paper, opened flat, with clean minimal typography in indigo navy and rose gold accent colors. Simple line icon illustrations showing numbered usage steps. The card design has generous white space, a small Lumina logo at the top, and a clean grid layout. Placed on a light cream linen surface with soft natural light. Editorial product photography style, overhead angle.
```
- Aspect ratio: `4:3`
- Size: `2K`

---

## 06_poster.png — 营销海报

```
Beauty campaign poster for LUMINA Derma-Luxury brand, portrait orientation. A woman's hand holding a sleek white and rose gold beauty device against a soft-focused background of warm ambient light. Editorial photography style reminiscent of high-end skincare campaigns. Cream, pearl white, and rose gold color palette with subtle warm gradients. The brand logo "LUMINA" and tagline "Derma-Luxury" placed elegantly in the lower third with generous breathing room. Magazine quality, warm emotional tone, cinematic soft lighting.
```
- Aspect ratio: `3:4`
- Size: `2K`

---

## 07_brand_pattern.png — 品牌纹样

```
Abstract luxury brand pattern design for a beauty-tech brand called LUMINA. Inspired by concentric circular treatment-head geometry and skincare serum droplet textures. Soft repeating organic concentric ring patterns in pearl white, cream, and subtle rose gold tones on a warm off-white background. The pattern is subtle and atmospheric — suitable for packaging tissue paper, shopping bag liner, or website background texture. Minimal, elegant, seamless repeat pattern with generous spacing between elements.
```
- Aspect ratio: `1:1`
- Size: `2K`

---

## 使用方式

1. 获取 Gemini API Key: https://aistudio.google.com/apikey
2. 设置环境变量: `export GEMINI_API_KEY=your_key`
3. 运行生成命令，例如：

```bash
python3 ~/.claude/skills/nano-banana-pro/generate_image.py \
  "prompt文本..." \
  -o /Users/wang/Desktop/CMF作品集/Category3_BrandIdentity/C1_Lumina_Brand/Renders/01_hero_logo.png \
  --aspect-ratio 16:9 \
  --size 2K
```

4. 图片生成后，在 `portfolio.html` 中将CSS占位mockup替换为 `<img>` 标签。
