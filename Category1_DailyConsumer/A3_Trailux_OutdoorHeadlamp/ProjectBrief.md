# A3: Trailux — 户外高端头灯 CMF
# Premium Outdoor Headlamp | 专业户外装备

> **Template Version:** v2.0 | 完整闭环版
> **Upgraded:** 2026-06-03 | Based on A1 Lumina pilot structure

---

## PHASE 0: BUSINESS CONTEXT / 商业背景

### 0.1 Brand & Market Positioning / 品牌与市场定位

Trailux is a premium outdoor lighting brand positioned at the intersection of alpine performance and refined design. It competes in the growing premium headlamp category against Petzl (mountaineering authority), Black Diamond (all-mountain heritage), and Biolite (tech-sustainability). Trailux differentiates through **geological material language** — not a plastic gadget strapped to your head, but an instrument carved from the mountain's own palette.

- **Brand Tone / 品牌调性:** Rugged precision. Technical but not tactical. Nature-inspired, not military. Alpine geology as the design source.
- **Market Tier / 市场层级:** Premium Outdoor (accessible pro-sumer)
- **Retail Price / 零售价区间:** ¥400 – ¥800 | $55 – $110 *(设计假设, based on competitive benchmarking: Petzl Actik Core ¥450, Black Diamond Storm 500-R $75, Biolite Headlamp 800 Pro $99)*
- **Annual Volume / 年产量:** 80,000 – 150,000 units/year *(设计假设)*
- **Target Margin / 目标利润率:** 45-50% (outdoor gear industry standard)
- **BOM Cost Target / 物料成本目标:** ≤ ¥45 / unit (excl. electronics, battery & packaging)
- **Key Markets / 主要市场:** China (outdoor sports boom, 35%), EU (Alpine region, 30%), North America (trail running + climbing, 35%)

### 0.2 Target User Persona / 目标用户画像

**The Alpine Purist / 高山纯粹主义者**

Male-skewed but growing female segment, 25-40, urban professional with serious outdoor hobbies. They run ultra-trails, climb alpine routes, and camp above the treeline. They research gear obsessively — comparing lumens, grams, and IP ratings on specialist forums. They own 3+ headlamps for different activities. Their gear is identity: they choose equipment that signals "I know what I'm doing" without the tactical-cosplay vibe of military-style gear. The headlamp must: (1) perform flawlessly in extreme conditions (IP67, -20°C to +50°C), (2) weigh under 80g, (3) look like it was designed by people who actually climb mountains, (4) age with character — scratches should reveal material depth, not cheap plastic.

### 0.3 Business Constraints → CMF Framework / 商业约束 → CMF推导

| Constraint / 约束 | Value / 数值 | CMF Implication / CMF推导 |
|---|---|---|
| Retail Price / 零售价 | ¥400-800 | Allows aluminum lens ring (machined or MIM), bio-based or recycled polymers, premium textile headband. Not: carbon fiber, titanium, full-metal housing. |
| BOM Budget (CMF only) / 物料预算 | ≤ ¥45/unit | ~30% to housing body, 25% to lens ring, 15% to headband, 15% to button + clip, 15% to packaging |
| Annual Volume / 年产量 | 80-150K units | Injection molding for housing (multi-cavity). Aluminum ring via CNC turning or MIM — both viable at this volume. Silicone button molding: compression mold, low cost per cavity. |
| Key Markets / 主要市场 | China + EU + NA | Must meet: IP67 waterproofing (affects seal design), CE/UKCA (EU), ANSI/PLATO FL1 (NA), GB 7000 (China lighting). Color palette: alpine neutrals + high-vis safety accents. EU preference for muted earth tones, NA slightly more open to bold accent colors. |
| Brand Position / 品牌定位 | Premium Outdoor | Defect tolerance: zero visible knit lines on body A-surface. Acceptable: minor flow marks on internal battery compartment. CMF complexity: 4-5 material zones — functional and deliberate, not decorative. Every finish serves a purpose (grip, visibility, durability). |
| User Touchpoints / 用户触点 | Housing body (handheld during battery change), lens ring (adjustable focus — rotated frequently), button (single press per mode change — primary interaction), headband clip (adjustment), headband (continuous skin contact — sweat, rain, dirt) | Premium investment in lens ring (rotational tactile quality) and headband (skin comfort + moisture wicking). Button must be findable by touch in the dark with cold/wet fingers — high-vis color + tactile dome are functional requirements, not decoration. |

---

## PHASE 1: MARKET & TREND RESEARCH / 市场与趋势研究

### 1.1 Market Demand Analysis / 市场需求分析

The global outdoor headlamp market exceeded $2.5B in 2024, driven by explosive growth in trail running (38% CAGR in China), alpine touring, and ultramarathon participation. Three demand signals drive CMF:

1. **Weight-to-performance ratio is the ultimate currency:** Users weigh their gear in grams. Every material choice must justify its mass. Aluminum lens rings stay because they provide functional heat dissipation for high-lumen LEDs — a performance material, not decoration. The housing must be as light as polymer allows.

2. **Gear as identity signal:** Outdoor enthusiasts wear their equipment choices as tribal markers. A Petzl user is different from a Black Diamond user. CMF must create a distinct visual signature that says "alpine purist" — refined, knowledgeable, not entry-level — without the aggressive cosplay of tactical/military aesthetics.

3. **Patina, not damage:** Premium outdoor gear should age with dignity. Scratches on an anodized aluminum ring reveal raw metal beneath — a record of use, not a flaw. Stone-textured polymer bodies hide micro-scratches that would ruin a glossy finish. "Worn-in" should look better than "brand new."

**User Pain Points with Existing CMF:**
- Petzl: Functional and trusted but looks like medical equipment crossed with caving gear. Red/black/yellow palette unchanged for a decade. Zero lifestyle appeal.
- Black Diamond: Rugged and capable but the dark gray/black monochrome reads as generic "outdoor stuff." No material warmth or geological reference.
- Biolite: Interesting sustainability story but the bright color-blocking and glossy finishes read as "tech startup," not "mountain tool." Feels fragile, not field-ready.
- Fenix/Nitecore: High-performance specs but pure industrial design — looks like a flashlight on a strap. No emotional connection to the landscape.

### 1.2 Industry CMF Trend Research / 行业CMF趋势调研

*Framework: STEEP Analysis*

**Trend 1: Alpine Biomimicry / 高山仿生**
- **Driver / 驱动力:** Environmental — growing awareness of fragile alpine ecosystems. Consumers seek gear that visually references the environment it's used in. Lichen colors, mineral textures, geological strata as design language.
- **Keywords / 关键词:** Lichen, granite, moss, mineral veins, glacial ice, weathered patina, geological time
- **CMF Manifestation / CMF表现:** Stone-textured polymer housings (Mold-Tech MT-11030, VDI 24-27), anodized aluminum rings in raw titanium and champagne tones, colors extracted from alpine photography: granite gray, moss green, glacial blue. High-vis safety accents in lichen orange and safety yellow.

**Trend 2: Technical Transparency / 技术透明**
- **Driver / 驱动力:** Social + Technological — the "prosumer" demands to see how things work. Materials should communicate their function honestly. No fake carbon fiber, no chrome-plated plastic pretending to be metal.
- **Keywords / 关键词:** Honest materials, functional finishes, visible engineering, material provenance, GRS/FSC certification
- **CMF Manifestation / CMF表现:** Real anodized aluminum (not painted plastic). Laser-etched grip lines that are both decorative AND functional (rotational grip). Recycled content percentages called out on the product. Every finish has a performance justification: matte = glare reduction, texture = grip, high-vis accent = safety.

**Trend 3: Ultralight Culture / 超轻文化**
- **Driver / 驱动力:** Economic + Social — the "fast and light" movement in trail running, thru-hiking, and alpine climbing. Equipment is pared down to essentials. Every gram is interrogated.
- **Keywords / 关键词:** Ultralight, gram-counting, fast-and-light, minimal-but-functional, material efficiency
- **CMF Manifestation / CMF表现:** Thin-wall injection molding pushed to structural minimum. Aluminum used only where heat dissipation justifies the weight penalty. Recycled elastic headband — lighter than neoprene, better moisture management. No superfluous trim, no overmolding for decoration. If it doesn't have a function, it doesn't exist.

### 1.3 Competitor CMF Audit / 竞品CMF审计

| Competitor / 竞品 | Model / 型号 | Key CMF Features / 关键CMF特征 | Strengths / 优势 | Weaknesses → Our Opportunity / 劣势→我们的机会 |
|---|---|---|---|---|
| Petzl | Actik Core | Red/black ABS body, silver plastic lens ring, elastic headband with reflective threads, utilitarian design, 10+ year aesthetic | Industry standard. Trusted by professionals. Functional everything. | Looks like caving equipment — zero emotional design. Red accent reads as dated/safety-equipment. Plastic lens ring feels cheap at ¥450. |
| Black Diamond | Storm 500-R | Dark gray/black monochrome, rubberized body, orange button, functional but generic | Rugged feel. Good grip texture. Trusted brand in climbing. | Generic "outdoor black" blends into every other headlamp. No material distinction. No color variants. Misses the premium lifestyle segment. |
| Biolite | Headlamp 800 Pro | White/silver housing, bright color-blocking (teal/orange accents), glossy finish, sustainable brand story | Distinctive. Tech-forward. Sustainability resonates with younger consumers. | Glossy finish shows scratches. Color-blocking reads as "gadget" not "gear." Feels fragile. No alpine material language. |
| Fenix | HM65R-T | Industrial anodized aluminum housing, olive green/dark gray, pure performance aesthetic | Genuine metal quality. Excellent build. Performance-focused. | Industrial, not emotional. Reads as flashlight factory, not mountain tool. No lifestyle appeal. No textile story. |

**Competitive Insight / 竞争洞察:** The market is split between "professional but soulless" (Petzl, Fenix) and "stylish but unserious" (Biolite). Black Diamond owns the middle ground but does nothing with CMF beyond "make it black." **The opportunity: a headlamp that uses alpine geological material language — actual stone textures, mineral anodizing tones, lichen-inspired accent colors — to create a product that looks carved from the mountain, not assembled in a factory.**

### 1.4 Inspiration Board / 灵感板

**Primary Inspiration Sources / 主要灵感来源:**
- **Alpine Geology:** Weathered granite surfaces (crystalline texture, feldspar/quartz/mica flecks), lichen-covered rock (orange-on-gray, organic pattern on mineral base), glacial ice (compressed blue, internal fractures, translucent depth)
- **Mountaineering Equipment Heritage:** Vintage ice axes (aged ash wood, forged steel with patina), 1970s expedition gear (canvas, leather, brass — natural materials before plastics took over), modern ultralight shelters (silnylon translucency, carbon fiber weave)
- **Mineral & Rock Textures:** Slate cleavage planes, iron-oxide staining on sandstone, serpentine green stone, raw bauxite/aluminum ore (connection to the aluminum lens ring material origin)
- **Alpine Flora:** Crustose lichen (orange, gray-green, white — slow-growing, geological-timescale beauty), alpine moss, saxifrage flowers in rock crevices

**Visual References / 视觉参考 (to be generated/curated):**

| Ref # | Source / 来源 | Description / 描述 | CMF Extraction / CMF提取 |
|---|---|---|---|
| 1 | Alpine Granite Face | Weathered granite rock face, Chamonix. Crystalline texture, gray with quartz/feldspar flecks | Dark warm gray base with subtle mineral fleck texture (MT-11030 reference) |
| 2 | Lichen on Rock | Crustose lichen in bright orange, growing on dark gray stone, Alpine region | High-vis orange accent on stone-gray body — safety color from nature, not a safety catalog |
| 3 | Glacial Ice Cave | Compressed glacial ice with internal blue refraction, Iceland | Pale ice blue-gray with depth, translucent quality — soft-touch matte with subtle cool undertone |
| 4 | Anodized Aluminum | Raw bauxite ore → refined aluminum → anodized finish | Material provenance story: the mountain IS the material. Aluminum sourced from the rock it climbs on. |

**Color Extraction Direction / 色彩提取方向:** Use Python `cmf_color_extractor.py` to run k-means (k=5) on curated reference image set of alpine rock faces + lichen macro + glacial ice formations. Expected extraction: warm granite gray base (L=30-40), mineral mid-tone (L=50-60), lichen orange accent (high chroma), moss green support (L=35-45, a=-5 to -10, b=8-15), glacial blue accent (L=55-65, a=-3 to -8, b=-5 to -15).

---

## PHASE 2: CONCEPT EXPLORATION / 方案探索

### 2.1 Design Strategy Formulation / 设计策略制定

*From Phase 1 research + Phase 0 constraints, three design pillars emerge:*

**Pillar 1: Geological Provenance / 地质起源**
- **Principle / 原则:** The headlamp should look like it was carved from the mountain — its materials, colors, and textures reference alpine geology directly. The aluminum lens ring traces back to bauxite ore; the stone-textured body mirrors weathered granite.
- **CMF Translation / CMF转化:** Stone-textured polymer housings (Mold-Tech MT-11030). Anodized aluminum in raw mineral tones — titanium gray, champagne, bright silver. Colors extracted from alpine photography, not Pantone trend books. Every material has a geological story.

**Pillar 2: Functional Finishes / 功能性表面处理**
- **Principle / 原则:** No decoration without function. Matte finishes reduce glare (critical for night vision preservation). Textured surfaces improve grip (wet/cold hands at altitude). High-vis accents are safety requirements, not style choices. Laser-etched grip rings on the lens barrel enable one-handed focus adjustment.
- **CMF Translation / CMF转化:** VDI/MT-textured housing = grip + scratch resistance. Laser-etched concentric grooves on aluminum ring = rotational grip. Glow-in-dark button pigment = findability in bivouac. Recycled elastic jacquard headband = moisture-wicking + reflective thread = visibility.

**Pillar 3: Lightweight Honesty / 轻量诚实**
- **Principle / 原则:** Under 80 grams. Every material choice is interrogated for its mass. Aluminum stays only where heat dissipation justifies the weight (lens ring — LED thermal path). Elsewhere, polymer optimized to minimum wall thickness. Nothing superfluous.
- **CMF Translation / CMF转化:** Thin-wall injection molding with structural ribs hidden internally. Aluminum ring is hollow — CNC'd for weight reduction. Headband uses recycled PET elastic — 40% lighter than neoprene, better dry time. No overmolding, no decorative inserts, no metal badges.

### 2.2 Multi-Scheme Generation / 多方案生成

#### Scheme A: Pure Technical / 纯技术派

| Dimension / 维度 | Description / 描述 |
|---|---|
| **Tagline / 一句话** | "Every gram accounted for. Nothing else." |
| **Emotional Response / 情感目标** | Utilitarian trust, serious performance, zero-distraction |
| **Primary Material / 主材质** | Glass-filled nylon (all-black, all-matte) |
| **Core Palette / 核心配色** | Matte black body + Silver aluminum ring + Dark gray button + Black headband |
| **Key Texture/Process / 核心工艺** | Fine matte glass-filled nylon (VDI 24), clear anodized aluminum, no color accents, no visible branding |
| **Estimated BOM / 估算BOM** | ¥32/unit (lowest — single color, fewer materials) |
| **Strengths / 优势** | Lightest weight (no pigment complexity). Strongest "serious gear" signal. Lowest cost. Easiest manufacturing — single material, single color. Appeals to hardcore gram-counters. Indistinguishable from Petzl/Black Diamond at a glance — but that's also its weakness. |
| **Risks / 风险** | Zero differentiation from Petzl/Black Diamond. The "all black" segment is saturated. No lifestyle appeal — won't attract the growing female trail-running market. No geological material language. Reads as generic "outdoor gear." Cannot justify premium pricing if it looks identical to ¥200 generic headlamps. |

#### Scheme B: Bio-Rugged / 生物机能

| Dimension / 维度 | Description / 描述 |
|---|---|
| **Tagline / 一句话** | "Carved by the mountain." |
| **Emotional Response / 情感目标** | Alpine authenticity, refined capability, geological connection |
| **Primary Material / 主材质** | Stone-textured PC/ABS or Bio-PA + anodized aluminum lens ring + recycled elastic headband |
| **Core Palette / 核心配色** | V1: Granite gray + Titanium aluminum + Lichen orange. V2: Moss green + Champagne aluminum + Safety yellow. V3: Glacial blue + Silver aluminum + Electric cyan |
| **Key Texture/Process / 核心工艺** | MT-11030 stone-textured body, laser-etched concentric grip on anodized aluminum ring, matte silicone button with glow-in-dark pigment, recycled jacquard elastic headband with reflective tracer |
| **Estimated BOM / 估算BOM** | ¥42/unit (mid — three color SKUs, aluminum ring, textured mold) |
| **Strengths / 优势** | Directly delivers "geological provenance" positioning. Three-variant strategy maps to different alpine environments: granite face, moss forest, glacial ice. Stone texture hides scratches functionally AND tells a geological story. Laser-etched aluminum ring = functional (grip) + beautiful (precision detailing). High-vis accents are nature-referenced (lichen orange, not safety-catalog orange). Recycled headband with reflective thread addresses sustainability + visibility together. |
| **Risks / 风险** | Three SKUs increase inventory complexity. Stone texture mold requires higher tooling investment (¥80-120K/cavity for MT-11030). Glow-in-dark pigment consistency across batches needs QC. Bio-PA (V2) has narrower processing window than PC/ABS. |

#### Scheme C: Urban Crossover / 城市跨界

| Dimension / 维度 | Description / 描述 |
|---|---|
| **Tagline / 一句话** | "From trailhead to coffee shop." |
| **Emotional Response / 情感目标** | Fashion-forward, versatile, urban-outdoor lifestyle |
| **Primary Material / 主材质** | Soft-touch matte polymer + polished PVD aluminum ring + premium woven headband |
| **Core Palette / 核心配色** | V1: Warm sand beige + Rose gold PVD ring + Cream headband. V2: Slate navy + Dark chrome ring + Navy heather band. V3: Terracotta clay + Copper PVD ring + Sand band |
| **Key Texture/Process / 核心工艺** | Soft-touch matte body (suede-like, 2-3 GU), polished PVD ring with diamond-cut chamfer, flat-knit headband in premium cotton-blend look, embossed logo |
| **Estimated BOM / 估算BOM** | ¥52/unit (exceeds target — PVD costs, premium textiles, soft-touch coating) |
| **Strengths / 优势** | Strong urban lifestyle appeal. Crosses over to everyday carry (EDC) market. Pastel/earth tone palette attracts female consumers. Looks like a premium tech accessory, not outdoor gear. High Instagram potential. |
| **Risks / 风险** | BOM exceeds ¥45 target by 15%. Soft-touch coating degrades with sunscreen/sweat exposure — fails the "alpine patina" requirement. PVD ring shows scratches on polished surface. Pastel palette reads as "fashion" not "mountain" — alienates the core alpine audience. Cotton-blend headband absorbs moisture (dangerous in cold conditions). The product looks like it would fail an IP67 test. |

### 2.3 Scheme Comparison Matrix / 方案对比矩阵

| Criterion / 评价标准 | Weight / 权重 | A: Pure Technical | B: Bio-Rugged | C: Urban Crossover |
|---|---|---|---|---|
| Brand Alignment / 品牌匹配度 | 25% | ★★★☆☆ | ★★★★★ | ★★☆☆☆ |
| Market Differentiation / 市场差异化 | 20% | ★☆☆☆☆ | ★★★★★ | ★★★★☆ |
| User Desirability / 用户吸引力 | 20% | ★★★☆☆ | ★★★★★ | ★★★★☆ |
| Production Feasibility / 量产可行性 | 20% | ★★★★★ | ★★★★☆ | ★★★☆☆ |
| Cost Control / 成本可控性 | 15% | ★★★★★ | ★★★★☆ | ★★☆☆☆ |
| **Weighted Score / 加权得分** | **100%** | **3.10** | **4.70** | **3.05** |

### 2.4 Elimination & Optimization / 淘汰与优化

**Eliminated / 淘汰:** Scheme C (Urban Crossover) — BOM exceeds target by 15% and the soft-touch coating fails the core durability requirement (sunscreen/sweat degradation). More critically, the urban-fashion aesthetic contradicts the "alpine purist" brand identity — this product would look out of place above the treeline. The cotton-blend headband is a safety liability in cold/wet conditions. Not the right direction for an outdoor performance brand.

**Eliminated / 淘汰:** Scheme A (Pure Technical) — While cost-efficient and functionally sound, it offers zero differentiation from market leaders Petzl and Black Diamond. The all-black monochrome cannot justify premium pricing (¥400-800) against functionally identical ¥200 generics. Critically, it misses the emotional connection to alpine landscape that is Trailux's core differentiation.

**Winner / 胜出:** Scheme B (Bio-Rugged) — Scores highest across all weighted criteria. The geological material language (stone-textured body + mineral-tone anodizing + lichen-inspired accents) is unique in the category. The three-variant strategy maps to real alpine environments that resonate with the target user's actual experience. Every finish serves a function: stone texture = scratch resistance + grip, laser-etched ring = rotational control, glow-in-dark button = findability, reflective headband thread = visibility.

**Post-Selection Refinements / 定案后优化:**
- V1 (Alpine Granite) body material stays PC/ABS for cost and processing reliability; the warm dark gray matches weathered granite of the Mont Blanc massif
- V2 (Alpine Moss) body upgraded to bio-based PA (castor oil feedstock) — 40% lower carbon footprint and the matte sandblasted finish reads as organic, not industrial
- V3 (Glacial Ice) body uses PC/ABS with soft-touch matte — the pale blue-gray evokes compressed glacial ice. Glow-in-dark button pigment increased to 8% loading for stronger ambient glow
- Aluminum lens ring finish differentiated per variant: raw titanium (V1), warm champagne (V2), bright silver (V3) — each a different "mineral" tone
- Headband material unified to 65% recycled PET / 35% elastane across all variants (replaces V3 ocean-plastic yarn — supply chain not ready for 150K unit volume)
- Reflective tracer thread added to all headbands — functional visibility, not decoration
- Absorbed Scheme A's weight-obsession — target weight confirmed at <78g (competitive with Petzl Actik Core at 82g)

---

## PHASE 3: FINAL CMF STRATEGY / 最终CMF策略

### 3.1 Core Direction / 核心方向

**Bio-Rugged / 生物机能**

"Carved by the mountain." Trailux uses alpine geology as its material source code. The stone-textured housing body feels like weathered granite under your fingers — a texture that hides scratches and improves grip simultaneously. The anodized aluminum lens ring, laser-etched with concentric grip lines, recalls precision optical instruments carried on expeditions. The high-vis button is colored like crustose lichen on rock — safety orange that nature invented first. The recycled elastic headband carries a reflective tracer thread like a mineral vein. Three color variants map to three alpine environments: the granite face, the moss forest, and the glacial ice cave. Every material choice has two justifications — one functional, one geological. The result is a headlamp that looks like it belongs above the treeline.

### 3.2 Color Variants / 色彩方案

#### V1: Alpine Granite / 高山花岗岩

| Zone / 区域 | Material / 材料 | Material Grade & Supplier Ref / 材料等级 | Color / 颜色 | Pantone / NCS | CIELAB D65/10° (±ΔE Tol.) | Finish & Process / 表面处理 | Texture Spec / 纹理参数 | Gloss / 光泽度 | Haptics / 触感 | Touch Freq. / 接触频率 | Cost Tier / 成本 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Housing body / 外壳主体 | PC/ABS (70/30 blend) | UV-stabilized, impact-modified for -20°C | Warm dark gray / 暖深灰 | Pantone 18-4005 TCX | L*=35, a*=1, b*=-2 (±ΔE≤1.5) | Injection molded, MT-11030 fine stone texture | MT-11030 (fine stone, 20-25μm depth) | 2-3 GU @ 60° | Matte stone-like, grip-enhancing micro-texture | High (handheld during battery change) | ¥¥ |
| Lens ring / 镜头环 | Aluminum 6061-T6 | ASTM B221, 75% post-industrial recycled content | Raw titanium gray / 原钛灰 | Pantone 16-3850 TCX | L*=55, a*=2, b*=-1 (±ΔE≤1.5) | CNC turned, clear anodized (Type II, Class 1), laser-etched concentric grip | Laser-etched grooves, 0.3mm pitch, 0.08mm depth | 8-12 GU @ 60° (satin metallic) | Cool metal, fine grip ridges, precision | High (rotated frequently for focus adjustment) | ¥¥¥ |
| Button / 按钮 | Silicone rubber (LSR) | Shore A 60, glow-in-dark pigment 5% strontium aluminate | Glow orange / 荧光橙 | Pantone 16-1362 TCX | L*=48, a*=35, b*=55 (±ΔE≤2.0) | Compression molded matte dome, glow-in-dark pigment loaded | Smooth matte dome, Ø12mm, 3mm dome height | 2-3 GU @ 60° | Soft tactile dome, findable by touch in dark | Highest (primary interaction — every mode change) | ¥ |
| Headband clip / 头带扣 | Glass-filled nylon (PA66-GF30) | Recycled content ≥30%, glass fiber 30% | Charcoal black with metallic flake / 炭黑金属闪 | Pantone 19-4006 TCX | L*=25, a*=1, b*=-1 (±ΔE≤1.5) | Injection molded, subtle metallic flake in resin | Mold polish SPI B-2 with metallic additive | 4-6 GU @ 60° | Rigid, slight metallic glint | Low (adjusted once per use) | ¥ |
| Headband / 头带 | Recycled PET elastic jacquard | 65% recycled PET, 35% elastane, GRS certified | Granite gray with orange fleck + reflective tracer / 花岗灰橙点反光 | Pantone 17-1502 TCX (base) | L*=42, a*=3, b*=1 (±ΔE≤2.0, textile) | Jacquard woven with orange fleck yarn + reflective tracer thread | Woven — elastic, 25mm width, moisture-wicking | Matte (textile — gloss N/A) | Soft elastic, moisture-wicking, subtle texture | High (continuous skin contact) | ¥¥ |

**Color Palette / 色彩面板:**

| Swatch / 色板 | Pantone | CIELAB (L*, a*, b*) | Hex (ref only) | Role / 角色 |
|---|---|---|---|---|
| Warm Dark Gray | Pantone 18-4005 TCX | L*=35, a*=1, b*=-2 | #57585A | Dominant / 主色 |
| Raw Titanium Gray | Pantone 16-3850 TCX | L*=55, a*=2, b*=-1 | #8A8C8B | Secondary metallic / 次要金属 |
| Glow Orange | Pantone 16-1362 TCX | L*=48, a*=35, b*=55 | #E06030 | High-Vis accent / 高视点缀 |
| Charcoal Flake | Pantone 19-4006 TCX | L*=25, a*=1, b*=-1 | #3D3E40 | Clip / 扣具色 |

#### V2: Alpine Moss / 高山苔藓

| Zone / 区域 | Material / 材料 | Material Grade & Supplier Ref / 材料等级 | Color / 颜色 | Pantone / NCS | CIELAB D65/10° (±ΔE Tol.) | Finish & Process / 表面处理 | Texture Spec / 纹理参数 | Gloss / 光泽度 | Haptics / 触感 | Touch Freq. / 接触频率 | Cost Tier / 成本 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Housing body / 外壳主体 | Bio-based PA (PA610, 60% castor oil) | ISCC PLUS certified, 40% bio-content | Dark moss green / 深苔绿 | Pantone 18-0322 TCX | L*=32, a*=-8, b*=12 (±ΔE≤1.5) | Injection molded, fine sandblasted matte (VDI 24) | VDI 24 (fine matte sandblast texture) | 2-3 GU @ 60° | Warm matte, slightly organic, bio-material feel | High | ¥¥ |
| Lens ring / 镜头环 | Recycled Aluminum 6061-T6 | 90% post-consumer recycled, ASTM B221 | Warm champagne / 暖香槟 | Pantone 14-1110 TCX | L*=68, a*=4, b*=15 (±ΔE≤1.5) | CNC turned, clear anodized (Type II), laser-etched grip | Laser-etched 0.3mm pitch concentric | 10-15 GU @ 60° | Warm metallic, champagne luster | High | ¥¥¥ |
| Button / 按钮 | Silicone rubber (LSR) | Shore A 60, standard pigment (no glow) | Safety yellow / 安全黄 | Pantone 13-0858 TCX | L*=72, a*=8, b*=85 (±ΔE≤2.0) | Compression molded matte dome | Smooth matte dome, Ø12mm | 2-3 GU @ 60° | Soft tactile, high-vis yellow | Highest | ¥ |
| Headband clip / 头带扣 | Glass-filled nylon (PA66-GF30) | Recycled content ≥30% | Dark moss matching / 深苔匹配 | Pantone 19-0415 TCX | L*=28, a*=-4, b*=6 (±ΔE≤1.5) | Injection molded, matte finish | Mold polish SPI B-2 | 4-6 GU @ 60° | Rigid matte, color-matched | Low | ¥ |
| Headband / 头带 | Recycled PET elastic jacquard | 65% recycled PET, 35% elastane, GRS certified | Dark green with yellow tracer + reflective thread / 墨绿黄线反光 | Pantone 19-0415 TCX (base) | L*=28, a*=-4, b*=6 (±ΔE≤2.0) | Jacquard woven, yellow tracer stripe + reflective thread | Woven — elastic, 25mm width | Matte | Soft elastic, subtle yellow tracer line | High | ¥¥ |

**Color Palette / 色彩面板:**

| Swatch / 色板 | Pantone | CIELAB (L*, a*, b*) | Hex (ref only) | Role / 角色 |
|---|---|---|---|---|
| Dark Moss Green | Pantone 18-0322 TCX | L*=32, a*=-8, b*=12 | #3D4F3A | Dominant / 主色 |
| Warm Champagne | Pantone 14-1110 TCX | L*=68, a*=4, b*=15 | #B8A888 | Secondary metallic / 次要金属 |
| Safety Yellow | Pantone 13-0858 TCX | L*=72, a*=8, b*=85 | #F5C800 | High-Vis accent / 高视点缀 |
| Dark Moss Match | Pantone 19-0415 TCX | L*=28, a*=-4, b*=6 | #3A3F34 | Clip / 扣具色 |

#### V3: Glacial Ice / 冰川冰蓝

| Zone / 区域 | Material / 材料 | Material Grade & Supplier Ref / 材料等级 | Color / 颜色 | Pantone / NCS | CIELAB D65/10° (±ΔE Tol.) | Finish & Process / 表面处理 | Texture Spec / 纹理参数 | Gloss / 光泽度 | Haptics / 触感 | Touch Freq. / 接触频率 | Cost Tier / 成本 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Housing body / 外壳主体 | PC/ABS (70/30 blend) | UV-stabilized, soft-touch additive (non-coating — molded-in) | Pale ice blue-gray / 浅冰蓝灰 | Pantone 14-4203 TCX | L*=68, a*=-4, b*=-8 (±ΔE≤1.5) | Injection molded, soft-touch matte — molded-in texture (no post-coat) | Mold-Tech MT-11010 (velvet matte) | 1.5-2.5 GU @ 60° | Soft-touch matte, velvety, cool | High | ¥¥ |
| Lens ring / 镜头环 | Aluminum 6061-T6 | ASTM B221, 75% post-industrial recycled | Bright silver / 亮银 | Pantone 14-4002 TCX | L*=78, a*=0, b*=-2 (±ΔE≤1.5) | CNC turned, brushed concentric #220 then clear anodized (Type II) | Brushed concentric, 0.15mm line pitch | 15-20 GU @ 60° | Cool bright metal, brushed grain | High | ¥¥¥ |
| Button / 按钮 | Silicone rubber (LSR) | Shore A 60, glow-in-dark pigment 8% strontium aluminate | Electric cyan / 电光青 | Pantone 15-4722 TCX | L*=58, a*=-18, b*=-22 (±ΔE≤2.0) | Compression molded matte dome, enhanced glow pigment | Smooth matte dome, Ø12mm, brighter glow than V1 | 2-3 GU @ 60° | Soft tactile, cool cyan with strong ambient glow | Highest | ¥ |
| Headband clip / 头带扣 | Glass-filled nylon (PA66-GF30) | Recycled content ≥30% | Ice gray matching / 冰灰匹配 | Pantone 15-4101 TCX | L*=62, a*=-2, b*=-5 (±ΔE≤1.5) | Injection molded, matte finish | Mold polish SPI B-2 | 4-6 GU @ 60° | Rigid, cool gray | Low | ¥ |
| Headband / 头带 | Recycled PET elastic jacquard | 65% recycled PET, 35% elastane, GRS certified | Ice blue with white geometric weave + reflective thread / 冰蓝白织纹反光 | Pantone 14-4203 TCX (base) | L*=68, a*=-4, b*=-8 (±ΔE≤2.0) | Jacquard woven, white geometric pattern + reflective thread | Woven — elastic, 25mm width, geometric pattern | Matte | Soft elastic, subtle geometric weave texture | High | ¥¥ |

**Color Palette / 色彩面板:**

| Swatch / 色板 | Pantone | CIELAB (L*, a*, b*) | Hex (ref only) | Role / 角色 |
|---|---|---|---|---|
| Pale Ice Blue-Gray | Pantone 14-4203 TCX | L*=68, a*=-4, b*=-8 | #A5ABB4 | Dominant / 主色 |
| Bright Silver | Pantone 14-4002 TCX | L*=78, a*=0, b*=-2 | #C4C7CA | Secondary metallic / 次要金属 |
| Electric Cyan | Pantone 15-4722 TCX | L*=58, a*=-18, b*=-22 | #2DAAB5 | High-Vis accent / 高视点缀 |
| Ice Gray | Pantone 15-4101 TCX | L*=62, a*=-2, b*=-5 | #9B9FA6 | Clip / 扣具色 |

### 3.3 Color Harmony Analysis / 色彩和谐分析

**V1 Alpine Granite — Monochromatic Mineral Harmony:**
| Relationship / 关系 | Zone Pair / 色区对 | ΔE | Perception / 感知效果 |
|---|---|---|
| Body ↔ Lens Ring | Dark gray → Titanium gray | ΔE≈24 | Medium contrast within grayscale — titanium ring reads as "light catching on a granite crystal face." Body is dark and absorbing; ring catches light. |
| Body ↔ Button | Dark gray → Glow orange | ΔE≈65 | Maximum intentional contrast — the button is a safety beacon. ΔE>50 is functionally required: must be findable at night with peripheral vision. |
| Button ↔ Headband | Orange → Gray with orange fleck | ΔE≈55 | The headband's orange fleck threads pick up the button color — color continuity from body to strap. |

**V2 Alpine Moss — Earth-Tone Complementary Harmony:**
| Relationship / 关系 | Zone Pair / 色区对 | ΔE | Perception / 感知效果 |
|---|---|---|
| Body ↔ Lens Ring | Moss green → Champagne | ΔE≈30 | Warm earth contrast — green body (forest floor) against warm gold ring (mineral vein). The champagne ring feels like discovering mica in dark stone. |
| Body ↔ Button | Moss green → Safety yellow | ΔE≈60 | Maximum functional contrast. Yellow-on-green is the highest-visibility color pair in peripheral vision (human retina peak sensitivity at 555nm = yellow-green). |
| Button ↔ Headband | Yellow → Green with yellow tracer | ΔE≈55 | Headband tracer thread extends the yellow accent — continuous visual line from button to strap. |

**V3 Glacial Ice — Cool Analogous Harmony:**
| Relationship / 关系 | Zone Pair / 色区对 | ΔE | Perception / 感知效果 |
|---|---|---|
| Body ↔ Lens Ring | Ice blue → Bright silver | ΔE≈19 | Subtle cool shift — silver ring reads as "compressed ice catching light." Both are cool-toned but the ring is lighter/brighter. |
| Body ↔ Button | Ice blue → Electric cyan | ΔE≈28 | Medium cool contrast — cyan against ice blue is distinct but harmonious. The button reads as a glacial pool — bright but not jarring. |
| Body ↔ Headband | Ice blue → Ice blue with white weave | ΔE≈8 | Lowest contrast pair — headband integrates with body color. The white geometric weave adds texture, not color contrast. |

**Cross-Variant Comparison:**
| Variant Pair | Overall ΔE (dominant colors) | Alpine Environment Match |
|---|---|
| V1 ↔ V2 | ΔE≈22 (granite gray vs. moss green) | Granite face → Alpine meadow |
| V1 ↔ V3 | ΔE≈38 (warm dark gray vs. cool ice blue) | Granite face → Glacier |
| V2 ↔ V3 | ΔE≈42 (moss green vs. ice blue) | Alpine meadow → Glacier |

**Metamerism Note / 同色异谱说明:** The anodized aluminum lens ring shows the most metamerism across lighting conditions — titanium gray anodizing shifts slightly warmer under incandescent (A) vs. daylight (D65), ΔE shift ≈1.0-1.5. Acceptable — headlamps are used in varied lighting and the shift is subtle. The silicone button shows negligible metamerism across D65/A/TL84 (ΔE<0.8). The PC/ABS body shows minimal shift (ΔE<1.0) due to in-mold color — no coating to cause metameric variation.

### 3.4 Material Narrative / 材料叙事

"Carved by the mountain."

The Trailux headlamp begins with geology. The body texture is Mold-Tech MT-11030 — the same fine crystalline roughness you feel running a hand over a weathered granite boulder in Chamonix. It's not smooth plastic pretending to be stone; it's a functional texture that hides scratches, improves wet-weather grip, and feels like rock under your fingertips.

The lens ring is real 6061 aluminum — the same element you'd extract from bauxite ore in the mountain you're climbing. We anodize it in mineral tones: raw titanium gray, warm champagne, bright silver. Laser-etched concentric grip rings let you adjust focus one-handed with cold fingers. They catch light like strata lines in a rock face.

The button is colored like lichen — crustose orange that nature perfected as a signal on gray stone. It glows in the dark because finding your gear in a bivouac at 3am shouldn't require a second headlamp. The recycled elastic headband carries a reflective tracer thread like a quartz vein through granite — invisible in daylight, bright under a headlamp beam when your running partner needs to see you on the trail.

After 1,000 trail kilometers, the anodized ring will show edge wear — raw aluminum gleaming through at high points. That's not damage. That's your record. The stone texture won't show a single scratch. The button will still glow. The headband will have shaped itself to your head. The product at kilometer zero is a promise; the product at kilometer 1,000 is proof.

---

## PHASE 4: PRODUCTION FEASIBILITY / 量产可行性

### 4.1 Process-Material Matrix / 工艺-材料矩阵

| Zone / 区域 | Material / 材料 | Primary Process / 一次工艺 | Secondary Process / 二次工艺 | Est. Cycle Time / 估算周期 | Yield Rate (target) / 良率目标 | Key Quality Risk / 关键质量风险 |
|---|---|---|---|---|---|---|
| Housing body | PC/ABS, Bio-PA | Injection molding (2-cavity, hot runner) | Mold texture from cavity (MT-11030 or VDI 24) — no post-spray | 30-35 sec/part | ≥96% | MT-11030 texture release — insufficient draft causes drag marks. Draft ≥1.5° required. Bio-PA (V2) processing window narrower: barrel temp ±3°C for color consistency. |
| Lens ring | Al 6061-T6 | CNC turning from tube stock (multi-spindle) | Clear anodize Type II Class 1 (10-15μm), laser-etch concentric grooves | CNC: 45-60 sec/part, Anodize: batch 45 min | ≥94% | Laser-etch depth consistency across curved surface. Anodize color lot-to-lot matching (ΔE≤1.5). Recycled Al 6061 may have slightly different etch response — process validation needed. |
| Button | LSR silicone | Compression molding (8-cavity) | Glow pigment pre-dispersed in LSR compound | 25-30 sec/part | ≥97% | Glow pigment dispersion uniformity — streaking if not fully compounded. Shore A 60 ±3 tolerance. Strontium aluminate pigment is abrasive — increased mold wear over 500K cycles. |
| Headband clip | PA66-GF30 | Injection molding (4-cavity) | Mold polish SPI B-2 — no post-finish | 20-25 sec/part | ≥95% | Metallic flake (V1) flow-line visibility at gate — gate location optimization needed. Glass fiber orientation affects surface appearance. |
| Headband | rPET elastic jacquard | Jacquard weaving (continuous roll) | Cut-to-length + heat-seal ends, reflective thread co-woven | Roll production: 5m/min, Cut: 3 sec/band | ≥98% | Elastic tension consistency across roll. Reflective thread breakage during weaving — tension control critical. Color matching between elastic base and non-elastic jacquard yarn. |

### 4.2 Texture & Surface Specification / 纹理与表面规格

*Reference Standards: Mold-Tech (MT-xxxxx), VDI 3400, SPI, Ra/Rz for objective roughness.*

| Zone / 区域 | Texture Standard / 纹理标准 | Reference Code / 参考编号 | Depth / 纹理深度 (μm) | Draft Angle Req. / 拔模要求 | Ra / 粗糙度Ra (μm) | Gloss @ 60° / 光泽度 | Tactile descriptor / 触感描述 |
|---|---|---|---|---|---|---|
| Housing body (V1) | Mold-Tech | MT-11030 | 20-25 | ≥1.5° | 1.5-2.2 | 2-3 GU | Fine stone texture — like weathered granite, crystalline roughness |
| Housing body (V2) | VDI 3400 | VDI 24 | 18-22 | ≥1.5° | 1.2-1.8 | 2-3 GU | Fine sandblast matte — organic, natural feel |
| Housing body (V3) | Mold-Tech | MT-11010 | 10-15 | ≥1.5° | 0.8-1.2 | 1.5-2.5 GU | Velvet matte — soft-touch, cool, like compressed ice |
| Lens ring (all) | Laser-etched concentric (custom pattern) | N/A | 80 (etch depth) | N/A | 0.4-0.8 (between grooves) | 8-20 GU (varies by anodize) | Precision ridged — like a camera focus ring, fine teeth under finger |
| Button (all) | Mold polish | SPI B-2 | N/A | N/A | 0.5-0.8 | 2-3 GU | Smooth matte dome — soft, findable by touch |
| Headband clip | Mold polish | SPI B-2 | N/A | N/A | 0.5-1.0 | 4-6 GU | Rigid smooth, slight texture from glass fiber |

### 4.3 Durability & Testing Requirements / 耐久与测试要求

| Test Item / 测试项目 | Standard / 测试标准 | Requirement / 要求 | Affected Zones / 涉及区域 | Notes / 备注 |
|---|---|---|---|---|
| Impact / 跌落 | IEC 60068-2-31 | 2m drop onto concrete, no structural failure, lens ring must retain alignment | Housing body, lens ring | Headlamp used in climbing — higher drop risk than consumer electronics. Aluminum ring provides structural reinforcement. |
| Abrasion / 耐磨 | Taber CS-10, 500g, 300 cycles | Weight loss ≤25mg, texture still legible (MT-11030 should survive with minimal visible change) | Housing body, lens ring | Stone texture is inherently abrasion-resistant — this is a functional choice, not just aesthetic. |
| UV Stability / 紫外老化 | QUV (ASTM G154), 300 hrs | ΔE ≤ 3.0 (body), ΔE ≤ 4.0 (headband), no chalking | All exterior zones | Extended UV exposure at altitude — UV degradation is accelerated at 3000m+. UV-stabilized grades required. |
| Chemical Resistance / 耐化学 | ISO 2812 | No change after 24hr contact: DEET (insect repellent), sunscreen SPF50, sweat simulant (ISO 105-E04) | Housing body, button, headband | DEET is aggressive on polymers — PC/ABS blend must be validated. Soft-touch V3 must not degrade with sunscreen. |
| Water Immersion / 浸水 | IP67 (IEC 60529) | 1m depth, 30 min, no water ingress | All zones (seal at lens ring/body interface) | Silicone O-ring seal behind lens ring — not a CMF zone but affects material selection at the interface. |
| Cold Impact / 低温冲击 | ISO 179-1 (Charpy, -20°C) | No brittle fracture at -20°C | Housing body, clip | PC/ABS maintains toughness at -20°C. Bio-PA (V2) must be validated — some bio-PA grades lose impact strength at low temp. |
| Glow Performance / 蓄光性能 | ISO 17514 (phosphorescent) | After 10 min charge (headlamp LED), visible glow ≥8 hours | Button (V1, V3) | Strontium aluminate pigment, 5% V1 / 8% V3 loading. Higher loading in V3 compensates for lighter body color (less contrast). |
| Headband Tension / 头带张力 | Internal standard | Elastic recovery ≥90% after 500 stretch cycles to 150% length | Headband | rPET elastic must match virgin PET elastic performance. 35% elastane content maintains recovery. |

### 4.4 Mass Production Cost Breakdown / 量产成本分解

*Estimated at 100K annual volume, single-shift production, Shenzhen/Dongguan supply base.*

| Zone / 区域 | Material Cost / 材料成本 (¥/unit) | Process Cost / 加工成本 (¥/unit) | Finishing Cost / 表面处理 (¥/unit) | Assembly / 装配 (¥/unit) | Subtotal / 小计 (¥/unit) | % of BOM |
|---|---|---|---|---|---|---|
| Housing body | ¥5.50 (PC/ABS compound, avg.) | ¥4.00 (injection molding, 2-cavity) | ¥0 (mold texture) | ¥1.50 | ¥11.00 | 26% |
| Lens ring | ¥6.00 (Al 6061 tube stock) | ¥8.00 (CNC turning + laser etch) | ¥3.00 (clear anodize Type II) | ¥1.50 | ¥18.50 | 44% |
| Button | ¥1.00 (LSR + glow pigment) | ¥2.00 (compression molding, 8-cavity) | ¥0 | ¥0.50 | ¥3.50 | 8% |
| Headband clip | ¥1.50 (PA66-GF30) | ¥2.00 (injection molding, 4-cavity) | ¥0 | ¥0.50 | ¥4.00 | 10% |
| Headband | ¥2.50 (rPET elastic jacquard, per 45cm) | ¥2.00 (cut + heat-seal) | ¥0 | ¥1.00 | ¥5.50 | 13% |
| **TOTAL / 合计** | | | | | **¥42.50** | **100%** |

**BOM vs. Target / 物料成本 vs. 目标:** ¥42.50 vs. ≤ ¥45.00 — **On target, ¥2.50 under.** The aluminum lens ring is the costliest single zone (44% of BOM) but is the primary quality signal and functional requirement (LED heat dissipation). Savings from in-mold texture (no paint line, no coating booth) offset the CNC aluminum investment.

**Cost Down Roadmap (for 200K+ volume):**
- Lens ring: MIM (Metal Injection Molding) replaces CNC at 200K+ → save ¥3.50/unit
- Housing: 4-cavity mold instead of 2 → save ¥1.50/unit
- Headband: automated cut-to-length from roll → save ¥0.80/unit
- **Target BOM at scale: ¥36.70** (14% reduction)

### 4.5 Sustainability Assessment / 可持续性评估

| Dimension / 维度 | Status / 状态 | Details / 详情 |
|---|---|---|
| Recycled Content / 回收含量 | V1: 75% post-industrial Al in lens ring, 65% rPET headband. V2: 90% post-consumer Al ring, 65% rPET headband, bio-PA body. V3: 75% post-industrial Al ring, 65% rPET headband. | GRS certification for headband and Al ring (V2). rPET elastic performance validated to match virgin PET in 500-cycle stretch test. |
| Bio-Based Materials / 生物基材料 | V2: Bio-PA (PA610, 60% castor oil) body — 40% lower carbon footprint than PC/ABS. | ISCC PLUS certified. Bio-PA processing: 15°C lower melt temp than PC/ABS = energy savings in molding. |
| Recyclability / 可回收性 | Designed for disassembly: lens ring unscrews (threaded, not bonded), button pops out, clip unclips, headband detaches. Housing = mono-material polymer per variant — no mixed-material bonding. | Electronics (LED, battery, PCB) removed as e-waste. Remaining materials: aluminum ring 100% recyclable, PC/ABS technically recyclable (single-polymer stream), silicone button recyclable through specialized program. |
| Packaging / 包装 | FSC recycled cardboard hang-tag, no plastic window, soy-based ink. Headband doubles as package retention — no plastic clips needed. | Minimal packaging by design — hang-tag format reduces material by 60% vs. boxed format. |
| Carbon Footprint / 碳足迹 | Estimated ~3.2kg CO₂e/unit (cradle-to-gate, excl. electronics). Industry average for this category: ~4.8kg CO₂e. Reduction driver: recycled Al (70% energy reduction vs. virgin), bio-PA V2 body, no paint line, minimal packaging. | 33% below category average. V2 variant leads at ~2.8kg CO₂e/unit (bio-PA + 90% recycled Al). |

---

## PHASE 5: DELIVERABLES / 产出清单

### 5.1 AI Image Generation Prompts / AI生图提示词

#### Phase 1 — Research & Inspiration (研究阶段)

**Trend Mood Board — Alpine Geology:**
```
Editorial mood board composition, combining outdoor product design references and natural material samples,
weathered granite rock face texture macro photography, lichen-covered stone in orange and gray-green,
glacial ice formations with compressed blue depth, raw bauxite ore sample,
anodized aluminum material swatches in titanium gray champagne and silver tones,
recycled elastic jacquard textile samples in dark tones with reflective thread,
clean dark gray background with curated sample arrangement,
alpine geology meets product design, 8K --ar 16:9
```

**Competitor Headlamp Grid:**
```
Product comparison shot, five outdoor headlamps in a row, front view on dark technical background,
left to right: Petzl Actik Core (red/black plastic, utilitarian),
Black Diamond Storm 500-R (dark gray monochrome, rubberized),
Biolite Headlamp 800 Pro (white/silver, color-blocked teal accents),
Fenix HM65R-T (olive green industrial aluminum),
Trailux placeholder (empty space with question mark on slate),
same angle, same lighting, competitive analysis for outdoor gear,
8K product photography --ar 16:9
```

#### Phase 2 — Concept Exploration (方案探索)

**3-Scheme Comparison Render:**
```
Three identical premium outdoor headlamps in front 3/4 angle, same soft studio lighting,

LEFT — "Pure Technical / 纯技术派":
All-black glass-filled nylon body, matte VDI 24, silver aluminum lens ring,
dark gray button, black headband, utilitarian minimal, industrial aesthetic,

CENTER — "Bio-Rugged / 生物机能" (WINNER):
Warm dark gray PC/ABS body with MT-11030 stone texture,
raw titanium gray anodized aluminum lens ring with laser-etched grip lines,
glow orange silicone button, granite gray headband with orange flecks and reflective tracer,
rugged-but-refined, geological material language,

RIGHT — "Urban Crossover / 城市跨界":
Warm sand beige soft-touch body, rose gold PVD lens ring,
cream headband, lifestyle aesthetic, fashion-forward but less technical,

clean dark background, product comparison format,
photorealistic 8K PBR rendering, identical perspective --ar 16:9
```

#### Phase 3 — Final CMF (最终方案)

**Hero Product Render — V1 Alpine Granite:**
```
Photorealistic product rendering of a premium outdoor headlamp,
front 3/4 angle, dramatic studio lighting on dark gradient background,
housing in warm dark gray PC/ABS (Pantone 18-4005 TCX) with fine stone-like MT-11030 texture,
raw titanium gray anodized aluminum lens ring (Pantone 16-3850 TCX) with laser-etched concentric grip lines,
glow orange matte silicone dome button (Pantone 16-1362 TCX) — 12mm diameter, tactile,
charcoal black headband clip with subtle metallic flake,
recycled elastic jacquard headband in granite gray with orange fleck yarn and reflective tracer thread,
rugged refined aesthetic — carved-from-rock feel,
outdoor gear product photography, 8K, sharp focus, PBR materials, commercial quality --ar 4:3
```

**Hero Product Render — V2 Alpine Moss:**
```
Premium outdoor headlamp, front 3/4 angle,
dark moss green bio-based PA body (Pantone 18-0322 TCX) with VDI 24 sandblasted matte finish,
warm champagne anodized aluminum lens ring (Pantone 14-1110 TCX) with laser-etched grip,
safety yellow matte silicone button — bright high-visibility accent,
dark green recycled PET elastic headband with yellow tracer stripe and reflective thread,
organic natural feel — alpine meadow mood,
outdoor gear product photography, 8K, PBR materials --ar 4:3
```

**Hero Product Render — V3 Glacial Ice:**
```
Premium outdoor headlamp, front 3/4 angle,
pale ice blue-gray PC/ABS body (Pantone 14-4203 TCX) with MT-11010 velvet matte soft-touch finish,
bright silver brushed aluminum lens ring (Pantone 14-4002 TCX) with concentric brush lines + laser-etched grip,
electric cyan silicone dome button with enhanced glow-in-dark pigment — subtle ambient glow,
ice blue recycled PET elastic headband with white geometric jacquard weave and reflective thread,
crisp glacial aesthetic — compressed ice and cold alpine air,
outdoor gear product photography, 8K, PBR materials --ar 4:3
```

**3-Variant Color Comparison:**
```
Three identical premium outdoor headlamps in a line against a dark technical studio background,
left: warm dark gray stone-textured body + titanium gray ring + orange button (V1 Alpine Granite),
center: moss green sandblasted body + champagne ring + yellow button (V2 Alpine Moss),
right: ice blue soft-touch body + bright silver ring + cyan button (V3 Glacial Ice),
same front 3/4 angle, same studio lighting (5500K + rim light),
product lineup photography for catalog, 8K PBR rendering --ar 16:9
```

#### Phase 4 — Technical Documentation (技术文档)

**Material Detail — Stone Texture (MT-11030):**
```
Extreme macro close-up of dark gray PC/ABS surface with MT-11030 fine stone texture,
crystalline roughness similar to fine-grained granite,
matte finish, 2-3 GU, visible micro-pitting and mineral-like surface variation,
sharp directional lighting from 45° left to reveal full texture depth (20-25μm),
outdoor product material reference, geological texture for industrial design,
8K, seamless surface, scientific reference quality --ar 1:1
```

**Material Detail — Anodized Aluminum Ring with Laser-Etch:**
```
Close-up macro of aluminum ring surface,
raw titanium gray clear anodized finish (Type II, 10-15μm),
laser-etched concentric grip lines visible — 0.3mm pitch, 0.08mm depth — catching light,
subtle metallic sheen, satin luster 8-12 GU,
precision-engineered surface transition from smooth anodize to etched groove,
studio macro photography, 8K, sharp focus on texture transition --ar 1:1
```

**Material Detail — Glow-in-Dark Silicone Button:**
```
Macro close-up of matte silicone dome button on dark headlamp body,
glow orange color in daylight (Pantone 16-1362 TCX),
smooth matte dome surface, 12mm diameter, 3mm dome height,
soft directional light showing the tactile dome profile against the stone-textured body,
second image inset: same button glowing faint green-yellow in complete darkness,
material reference photo for product design, 8K --ar 1:1
```

**Material Detail — Recycled Jacquard Headband:**
```
Macro close-up of elastic jacquard-woven headband,
granite gray base with orange fleck yarns woven in — like mineral veins in stone,
reflective tracer thread catching light — silver line running parallel to edge,
elastic textile with visible weave structure, 25mm width,
soft directional light to show texture depth and reflective thread,
textile material reference for outdoor product design, 8K --ar 3:2
```

**CMF Swatch Board — V1 Alpine Granite:**
```
CMF specification presentation board, professional product design format,
left column: physical material samples arranged vertically —
  PC/ABS stone-textured plaque (warm dark gray, Pantone 18-4005 TCX, MT-11030, 2-3 GU),
  anodized aluminum chip (raw titanium gray, Pantone 16-3850 TCX, laser-etched, 8-12 GU),
  silicone button dome (glow orange, Pantone 16-1362 TCX, Shore A 60),
  glass-filled nylon clip sample (charcoal black with metallic flake, Pantone 19-4006 TCX),
  rPET elastic jacquard headband swatch (granite gray + orange fleck + reflective thread),
right column: corresponding color swatches with Pantone labels and CIELAB values,
top title: "TRAILUX V1 — ALPINE GRANITE / 高山花岗岩 — CMF SPECIFICATION",
dark studio background, CMF industry standard presentation,
8K, sharp focus --ar 3:4
```

**Exploded Material View:**
```
Technical exploded isometric view of an outdoor headlamp,
components separated with equal spacing, 30° isometric angle,
from front to back:
1. Lens Ring (anodized aluminum, laser-etched grip pattern) — floating in front
2. Button (silicone dome, glow orange) — above body
3. Housing Body (PC/ABS, stone-textured MT-11030) — central
4. Headband Clip (glass-filled nylon, charcoal) — behind body
5. Headband (recycled PET elastic jacquard, granite gray with orange fleck) — flowing behind
clean dark technical background, material callout leader lines with labels,
technical documentation style, 8K --ar 1:1
```

#### Phase 5 — Lifestyle & Context (生活场景)

**In-Use Context — Trail Runner at Dawn:**
```
Editorial outdoor photography, trail runner on alpine ridge at dawn,
wearing a dark gray stone-textured headlamp (Trailux V1 Alpine Granite),
headlamp beam cutting through morning mist,
orange button visible as a small bright accent against the gray body,
runner in technical gear, mountains in background, golden hour light,
the headlamp looks like it belongs in this landscape,
authentic outdoor feel — not staged studio, real mountain light,
8K editorial adventure photography --ar 3:2
```

**In-Use Context — Climber on Rock Face:**
```
Adventure photography, rock climber on a granite face,
wearing V2 Alpine Moss headlamp — dark moss green body visible against gray rock,
champagne aluminum ring catching sunlight,
the headlamp's geological colors blend with the actual granite and lichen on the rock face,
product-as-part-of-the-landscape — the headlamp matches the mountain,
dramatic alpine light, authentic climbing photography,
8K editorial adventure photography --ar 3:2
```

**Packaging — Sustainable Hang-Tag:**
```
Product photography, Trailux headlamp attached to FSC recycled cardboard hang-tag,
headband wrapped around the card as product retention — no plastic clips,
soy-based ink printing: minimal typography, topographic contour line pattern in background,
"CARVED BY THE MOUNTAIN" tagline, GRS and FSC certification logos visible,
dark slate background, premium minimal packaging design,
sustainability-focused product presentation, 8K --ar 4:3
```

### 5.2 Render Shot List / 渲染镜头清单

| # | Shot / 镜头描述 | Type / 类型 | Phase / 对应阶段 |
|---|---|---|---|
| 1 | Trend mood board — Alpine geology + material samples | Moodboard | Phase 1 |
| 2 | Competitor headlamp comparison (Petzl, BD, Biolite, Fenix) | Research | Phase 1 |
| 3 | 3-scheme comparison — Pure Technical vs. Bio-Rugged vs. Urban Crossover | Exploration | Phase 2 |
| 4 | Hero front 3/4 — V1 Alpine Granite (studio, dark background) | Hero | Phase 3 |
| 5 | Hero front 3/4 — V2 Alpine Moss (studio) | Hero | Phase 3 |
| 6 | Hero front 3/4 — V3 Glacial Ice (studio) | Hero | Phase 3 |
| 7 | 3-variant color comparison lineup (studio, catalog format) | Comparison | Phase 3 |
| 8 | Material transition: stone-textured body → anodized ring → silicone button (V1) | Transition | Phase 3 |
| 9 | Material transition: sandblasted body → champagne ring → yellow button (V2) | Transition | Phase 3 |
| 10 | Material transition: soft-touch body → brushed silver ring → cyan button (V3) | Transition | Phase 3 |
| 11 | Texture macro — MT-11030 stone texture on PC/ABS | Material | Phase 4 |
| 12 | Texture macro — anodized aluminum ring with laser-etched grip lines | Material | Phase 4 |
| 13 | Texture macro — glow-in-dark silicone button (daylight + dark inset) | Material | Phase 4 |
| 14 | Texture macro — recycled jacquard elastic headband with reflective thread | Material | Phase 4 |
| 15 | CMF swatch board — V1 Alpine Granite (all materials + Pantone/CIELAB labels) | Spec | Phase 4 |
| 16 | Texture specification board — all 3 variants with MT/VDI/Ra callouts | Spec | Phase 4 |
| 17 | Exploded material view — isometric, 5 components, material callouts | Info | Phase 4 |
| 18 | In-use context — trail runner at dawn, alpine ridge (V1) | Context | Phase 5 |
| 19 | In-use context — climber on granite face (V2) | Context | Phase 5 |
| 20 | Packaging — FSC hang-tag, sustainable unboxing | Context | Phase 5 |

---

## APPENDIX: CMF SPECIFICATION SHEET / 附录：CMF规格书

*Refer to the full spec template at `02_Assets/CMF_Spec_Template.md` for production-grade documentation.*

### V1 Alpine Granite / 高山花岗岩 — Quick Spec / 快速规格

| | Zone 1: Housing Body | Zone 2: Lens Ring | Zone 3: Button | Zone 4: Headband Clip | Zone 5: Headband |
|---|---|---|---|---|---|
| **Material** | PC/ABS (70/30) | Al 6061-T6 | LSR Silicone | PA66-GF30 | rPET Elastic Jacquard |
| **Grade** | UV-stabilized, -20°C impact | ASTM B221, 75% recycled | Shore A 60, 5% glow pigment | Recycled ≥30%, GF30% | 65% rPET, 35% elastane, GRS |
| **Pantone** | 18-4005 TCX | 16-3850 TCX | 16-1362 TCX | 19-4006 TCX | 17-1502 TCX (base) |
| **CIELAB** | L*=35, a*=1, b*=-2 | L*=55, a*=2, b*=-1 | L*=48, a*=35, b*=55 | L*=25, a*=1, b*=-1 | L*=42, a*=3, b*=1 |
| **ΔE Tolerance** | ±1.5 | ±1.5 | ±2.0 | ±1.5 | ±2.0 (textile) |
| **Finish** | MT-11030 stone texture | Clear anodize + laser-etch | Matte dome, glow pigment | SPI B-2 matte | Jacquard weave + reflective thread |
| **Texture Ref** | MT-11030 | Laser 0.3mm pitch | SPI B-2 | SPI B-2 | Woven 25mm width |
| **Gloss @ 60°** | 2-3 GU | 8-12 GU | 2-3 GU | 4-6 GU | Matte (textile) |
| **Hardness** | Rockwell R 115 | — | Shore A 60 | Rockwell R 120 | — |
| **Supplier** | TBD (Shenzhen/Dongguan) | TBD (Dongguan CNC) | TBD (Shenzhen silicone) | TBD (Shenzhen) | TBD (Jiangsu textile) |

### V2 Alpine Moss / 高山苔藓 — Quick Spec / 快速规格

| | Zone 1: Housing Body | Zone 2: Lens Ring | Zone 3: Button | Zone 4: Headband Clip | Zone 5: Headband |
|---|---|---|---|---|---|
| **Material** | Bio-PA (PA610, 60% castor) | Recycled Al 6061-T6 | LSR Silicone | PA66-GF30 | rPET Elastic Jacquard |
| **Grade** | ISCC PLUS, 40% bio | ASTM B221, 90% post-consumer | Shore A 60, standard pigment | Recycled ≥30% | 65% rPET, 35% elastane, GRS |
| **Pantone** | 18-0322 TCX | 14-1110 TCX | 13-0858 TCX | 19-0415 TCX | 19-0415 TCX (base) |
| **CIELAB** | L*=32, a*=-8, b*=12 | L*=68, a*=4, b*=15 | L*=72, a*=8, b*=85 | L*=28, a*=-4, b*=6 | L*=28, a*=-4, b*=6 |
| **ΔE Tolerance** | ±1.5 | ±1.5 | ±2.0 | ±1.5 | ±2.0 |
| **Finish** | VDI 24 sandblast matte | Clear anodize + laser-etch | Matte dome, standard pigment | SPI B-2 matte | Jacquard + yellow tracer + reflective |
| **Texture Ref** | VDI 24 | Laser 0.3mm pitch | SPI B-2 | SPI B-2 | Woven 25mm |
| **Gloss @ 60°** | 2-3 GU | 10-15 GU | 2-3 GU | 4-6 GU | Matte |
| **Hardness** | Rockwell R 110 | — | Shore A 60 | Rockwell R 120 | — |
| **Supplier** | TBD | TBD | TBD | TBD | TBD |

### V3 Glacial Ice / 冰川冰蓝 — Quick Spec / 快速规格

| | Zone 1: Housing Body | Zone 2: Lens Ring | Zone 3: Button | Zone 4: Headband Clip | Zone 5: Headband |
|---|---|---|---|---|---|
| **Material** | PC/ABS (70/30) | Al 6061-T6 | LSR Silicone | PA66-GF30 | rPET Elastic Jacquard |
| **Grade** | UV-stabilized, soft-touch additive | ASTM B221, 75% recycled | Shore A 60, 8% glow pigment | Recycled ≥30% | 65% rPET, 35% elastane, GRS |
| **Pantone** | 14-4203 TCX | 14-4002 TCX | 15-4722 TCX | 15-4101 TCX | 14-4203 TCX (base) |
| **CIELAB** | L*=68, a*=-4, b*=-8 | L*=78, a*=0, b*=-2 | L*=58, a*=-18, b*=-22 | L*=62, a*=-2, b*=-5 | L*=68, a*=-4, b*=-8 |
| **ΔE Tolerance** | ±1.5 | ±1.5 | ±2.0 | ±1.5 | ±2.0 |
| **Finish** | MT-11010 velvet matte | Brushed #220 + clear anodize | Matte dome, enhanced glow | SPI B-2 matte | Jacquard + white geometric + reflective |
| **Texture Ref** | MT-11010 | Brush #220 + laser 0.3mm | SPI B-2 | SPI B-2 | Woven 25mm |
| **Gloss @ 60°** | 1.5-2.5 GU | 15-20 GU | 2-3 GU | 4-6 GU | Matte |
| **Hardness** | Rockwell R 115 | — | Shore A 60 | Rockwell R 120 | — |
| **Supplier** | TBD | TBD | TBD | TBD | TBD |

---

*Document generated with reference to: CMF_Crash_Course.md (color science, STEEP, material-process knowledge), CMF_Spec_Template.md (production spec structure), AI_Image_Generation_Guide.md (prompt engineering for CMF visualization).*
*本文档参考内置知识库生成：色彩科学、趋势方法论、材料工艺对照、量产规格结构。所有商业数据（定价、BOM、产量）均为设计假设。*
