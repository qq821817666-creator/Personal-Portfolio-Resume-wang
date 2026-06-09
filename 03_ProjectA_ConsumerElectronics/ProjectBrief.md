# Project A: AURA — 高端无线耳机 CMF
# Premium Wireless Headphones | 个人音频设备

> **Template Version:** v2.0 | 完整闭环版
> **Built from:** ProjectA_Brief.md (legacy) + A3 Lumina pilot structure
> **Upgraded:** 2026-06-03

---

## PHASE 0: BUSINESS CONTEXT / 商业背景

### 0.1 Brand & Market Positioning / 品牌与市场定位

AURA is a premium personal audio brand positioned at the intersection of acoustic engineering and wearable design. It competes in the fiercely contested premium headphone market against B&O (material luxury), Apple AirPods Max (ecosystem lock-in + aluminum precision), Sony WH-1000XM (noise-cancelling dominance), and Dyson Zone (disruption-through-weirdness). AURA differentiates by being the first brand to synthesize **Warm Tech tactility with Neo-Sensorial color intelligence** — headphones that feel like a natural extension of the body while expressing a forward-looking, digitally-native color language.

- **Brand Tone / 品牌调性:** Warm intelligence. Body-extension. Sensory-rich minimalism. Technology that feels human.
- **Market Tier / 市场层级:** Premium (accessible luxury)
- **Retail Price / 零售价区间:** ¥1,800 – ¥3,200 | $250 – $450 *(设计假设, based on competitive benchmarking: B&O Beoplay H95 ¥5,998, Apple AirPods Max ¥4,399, Sony WH-1000XM5 ¥2,499, Nothing Ear (buds) ¥899)*
- **Annual Volume / 年产量:** 80,000 – 150,000 units/year *(设计假设)*
- **Target Margin / 目标利润率:** 45-50% (audio industry standard)
- **BOM Cost Target / 物料成本目标:** ≤ ¥200 / unit (excl. drivers, electronics & packaging)
- **Key Markets / 主要市场:** China (Tier 1 cities, 40%), North America (25%), EU (20%), Japan/Korea (15%)

### 0.2 Target User Persona / 目标用户画像

**The Sonic Curator / 声音策展人**

Gender-balanced, 25-40, urban professional, household income ¥300K+. They curate their life across analog and digital — vinyl records AND lossless streaming, film photography AND Instagram, mechanical watches AND Apple Watch. Audio quality matters (they notice compression artifacts), but so does how the headphones look around their neck in a coffee shop. They own 2+ pairs of headphones for different contexts. The headphones must: (1) deliver reference-grade audio wrapped in materials that feel worth touching, (2) express personal aesthetic — not anonymous black plastic, (3) look intentional when worn as a neck-piece between listening sessions, (4) age with dignity — leather that patinas, metal that records use.

### 0.3 Business Constraints → CMF Framework / 商业约束 → CMF推导

| Constraint / 约束 | Value / 数值 | CMF Implication / CMF推导 |
|---|---|---|
| Retail Price / 零售价 | ¥1,800-3,200 | Allows genuine aluminum, anodized finishes, vegan leather, and textile integration. Not: titanium, carbon fiber, hand-stitched leather, precious metal PVD. |
| BOM Budget (CMF only) / 物料预算 | ≤ ¥200/unit | ~30% to earcup shells (largest visible surfaces), 20% to headband, 20% to ear cushions, 15% to metal arm/hinge, 15% to controls/accents |
| Annual Volume / 年产量 | 80-150K units | Injection molding for earcups and headband shell. Aluminum arm via CNC or die-casting — both viable. Ear cushion production: automated cutting + sewing. Finish: in-mold or UV hardcoat for body; PVD/anodize for metal. |
| Key Markets / 主要市场 | China + NA + EU + JP/KR | Must meet: GB 4943.1 (China IT safety), UL 62368 (NA), CE/REACH (EU), Japan Radio Law. Color palette: warm neutrals (global), holographic accents (younger demographic, Asia-strong), eco-visible aesthetics (EU-strong). |
| Brand Position / 品牌定位 | Premium | Defect tolerance: zero visible knit lines on earcup A-surface. Acceptable: minor flow marks on headband inner surface (against head). CMF complexity: 5-6 material zones, rich but coherent — premium headphone expectations demand visible material quality. |
| User Touchpoints / 用户触点 | Earcup shells (primary visual, handled during put-on/take-off), ear cushions (continuous skin contact 2-6 hrs/day), headband (skin contact, visible when worn), metal arm (visible, structural — perceived quality anchor), controls (fingertip interaction) | Premium investment in earcup shells (user sees and touches constantly) and ear cushions (comfort = retention). Metal arm is the quality anchor — users judge headphone build by how the hinge feels. Controls must be findable by touch without looking. |

---

## PHASE 1: MARKET & TREND RESEARCH / 市场与趋势研究

### 1.1 Market Demand Analysis / 市场需求分析

The global premium headphone market exceeded $25B in 2024, driven by three converging forces: lossless streaming adoption (Apple Music/QQ Music Hi-Res tiers), remote work normalization (all-day wear comfort), and headphones-as-fashion-accessory (social media visibility). Three demand signals drive CMF:

1. **Headphones are jewelry now:** Over-ear headphones are worn visibly — on Zoom calls, in coffee shops, on public transit. They signal taste the way a watch or bag does. CMF must deliver "worth showing" not "worth hiding." The neck-worn-between-listening moment is the most visible product state.

2. **All-day wear demands material intelligence:** Users wear premium headphones 4-8 hours daily. Ear cushion materials must breathe, headband padding must distribute pressure, surfaces must resist skin oils and hair products. CMF that looks premium but feels hot/heavy after 30 minutes is a return waiting to happen.

3. **The "black plastic problem":** The headphone market's default CMF is black/dark gray matte plastic — indistinguishable from ¥200 generics at a distance. Premium brands must signal quality through visible material differentiation: real metal, genuine texture, intentional color.

**User Pain Points with Existing CMF:**
- B&O Beoplay H95: Beautiful material mixing (aluminum + fabric + lambskin) but ¥5,998 pricing limits market. The luxury palette reads as "gentleman's study," not "creative professional."
- Apple AirPods Max: Anodized aluminum precision is unmatched, but 385g weight (heaviest in class) makes all-day wear fatiguing. The mesh canopy headband is innovative but the color palette is primary-school — red, green, blue, pink — reads as "toy" not "premium audio."
- Sony WH-1000XM5: Class-leading noise cancellation but the soft-touch matte body shows fingerprints instantly. Single-color strategy (black or silver) limits self-expression. "Looks like every other Sony headphone."
- Dyson Zone: Unconventional material approach with the air-purifying visor, but the product reads as "Dyson appliance" not "audio instrument." Polarizing aesthetics.

### 1.2 Industry CMF Trend Research / 行业CMF趋势调研

*Framework: STEEP Analysis — adapted from the 3 trend directions in the original ProjectA_Brief*

**Trend 1: Warm Tech / 温暖科技**
- **Driver / 驱动力:** Social — post-pandemic desire for technology that feels nurturing, not clinical. Biophilic design principles entering consumer electronics.
- **Keywords / 关键词:** Soft textures, warm neutrals, tactile warmth, fabric integration, matte-over-gloss, human-centered
- **CMF Manifestation / CMF表现:** Warm beige, taupe, and terracotta replace stark white and silver. Soft-touch matte finishes (3-5 GU). Textile integration at touch points. Vegan leather in cognac and warm gray tones. Sandblasted aluminum in champagne and copper PVD tones.

**Trend 2: Neo-Sensorial / 超感体验**
- **Driver / 驱动力:** Technological — advanced coatings, chameleon pigments, and holographic films democratizing from automotive to consumer electronics
- **Keywords / 关键词:** Iridescence, holographic, dynamic color, color-shift, translucent, phygital, sensory-rich
- **CMF Manifestation / CMF表现:** Gradient anodized aluminum (color-shift dye process). Holographic foil inlays under transparent PMMA. Iridescent thread in textile weaves. Edge-lit laser-etched controls. Surfaces that shift with viewing angle — the product is never one color.

**Trend 3: Raw Authenticity / 原生真实**
- **Driver / 驱动力:** Environmental — sustainability evolving from invisible compliance to celebrated aesthetic. Consumers want to SEE the recycled content.
- **Keywords / 关键词:** Visible recycled content, material honesty, PCR, natural materials, sustainability-as-aesthetic, terrazzo-effect
- **CMF Manifestation / CMF表现:** PCR plastics with visible speckle (colored flecks in dark base = terrazzo-like). Natural cork, bamboo veneer, wood composite panels. Raw unpolished aluminum — celebrating sand-cast texture rather than hiding it. rPET woven textiles for mesh and cushions.

### 1.3 Competitor CMF Audit / 竞品CMF审计

| Competitor / 竞品 | Model / 型号 | Key CMF Features / 关键CMF特征 | Strengths / 优势 | Weaknesses → Our Opportunity / 劣势→我们的机会 |
|---|---|---|---|---|
| B&O | Beoplay H95/H100 | Aluminum arms + lambskin leather + fabric headband + circular earcup design, warm gold/cream palette | Luxury material mixing. Danish design credibility. Beautiful color palettes. | ¥5,998 — inaccessible. Color palette is conservative/luxury — no experimental direction. Heavy at 323g. |
| Apple | AirPods Max | Anodized aluminum earcups + mesh canopy headband + silicone headband frame + Digital Crown, 5 solid colors | Industry-best aluminum precision. Mesh headband innovation. Strong color identity (if polarizing). | 385g — heaviest in class. Colors read as "toy" (red/green/blue). No textile/leather story. No color variants beyond solid hues. |
| Sony | WH-1000XM5 | Soft-touch matte PC/ABS body + synthetic leather cushions + minimal metal (slider only), black/silver only | Best-in-class NC. Comfortable for long wear. Recognizable silhouette. | Fingerprint magnet. Two colors only. Looks generic — indistinguishable from XM4/XM3 at distance. Zero material luxury. |
| Nothing | Ear (2) / Ear (stick) | Transparent PC housing revealing internal components, white/red/black accents | Unique transparent design language. Genuinely differentiated. Strong Gen-Z appeal. | Translucent plastic reads as "tech demo" not "premium audio." Limited to buds — over-ear product would be more complex. Transparent PC scratches visibly. |

**Competitive Insight / 竞争洞察:** The market is split between "luxury conservative" (B&O), "ecosystem premium" (Apple), "performance-generic" (Sony), and "tech-disruptive" (Nothing). **The opportunity: headphones that bridge Warm Tech material tactility with Neo-Sensorial color intelligence — genuine material quality (aluminum, vegan leather, textile) expressed through a forward-looking color palette that spans warm naturals, holographic gradients, and eco-visible textures.**

### 1.4 Inspiration Board / 灵感板

**Primary Inspiration Sources / 主要灵感来源:**
- **Fashion Accessories:** High-end eyewear (acetate frames with layered color depth, titanium temples), mechanical watch dials (sunburst brushing, applied indices catching light), designer bag hardware (brushed gold, dark chrome, copper PVD)
- **Automotive Interiors:** Perforated leather seats (acoustic-transparent pattern), gradient anodized aluminum trim, ambient light guides in PMMA
- **Architecture & Interior:** Warm minimalism (oak, linen, clay plaster — the tactile palette), iridescent glass facades (angle-dependent color shift), terrazzo flooring (visible aggregate in neutral base)
- **Digital Art & Gaming:** Holographic UI elements, gradient color spaces, vaporwave/synthwave color palettes, cyberpunk material mashups

**Visual References / 视觉参考:**

| Ref # | Source / 来源 | Description / 描述 | CMF Extraction / CMF提取 |
|---|---|---|---|
| 1 | B&O H95 | Lambskin leather earcup in cognac tone, aluminum arm with hairline brush, fabric headband | Material mixing formula: warm leather + brushed metal + textile. Rich but not heavy. |
| 2 | Holographic Film | Light-refracting iridescent film, color shift blue → teal → violet with viewing angle | Gradient anodize or foil-inlay technique. Dynamic color that changes as the wearer moves. |
| 3 | Terrazzo Surface | Dark charcoal base with visible cream/amber/copper aggregate, matte polished | PCR speckle effect — every product is slightly unique. Sustainability as visible aesthetic. |
| 4 | Eyewear Acetate | Layered acetate in tortoiseshell pattern, depth from color lamination, polished to high gloss | Color depth through layering. Not flat paint — material has internal light play. |

---

## PHASE 2: CONCEPT EXPLORATION / 方案探索

### 2.1 Design Strategy Formulation / 设计策略制定

*From Phase 1 research + Phase 0 constraints, three design pillars emerge:*

**Pillar 1: Tactile Intelligence / 触感智能**
- **Principle / 原则:** Headphones are worn on the body for hours. Every surface the user touches — earcup shell, cushion, headband, controls — must feel intentional. Warm materials where the body contacts, cool precision where the eye judges.
- **CMF Translation / CMF转化:** Soft-touch matte body warm to the touch, vegan leather cushions that breathe, brushed metal arms that feel cool and solid under the finger, textile headband that distributes weight without pressure points. No sharp edges. No cold plastic shock.

**Pillar 2: Dynamic Color / 动态色彩**
- **Principle / 原则:** Headphones move with the wearer through changing light conditions — indoor/outdoor, morning/evening, natural/artificial. Color should be alive, not static. Gradient shifts, holographic catches, and texture reveals reward the observer from different angles.
- **CMF Translation / CMF转化:** Gradient anodized aluminum. Holographic foil inlays. Iridescent thread in ear cushion mesh. Color sampled from digital-native palettes — aurora gradients, synthwave violets, cyber-teal — but executed with material sophistication, not screen-glow garishness.

**Pillar 3: Visible Integrity / 可见诚实**
- **Principle / 原则:** If it's recycled, show it. If it's metal, let it be metal. Avoid fake wood, fake metal, fake leather, fake carbon fiber. Material honesty is the ultimate premium signal in a world of imitations.
- **CMF Translation / CMF转化:** PCR plastics with visible speckle — the recycled content IS the aesthetic. Uncoated aluminum in raw anodized finish — not painted to look like metal. Vegan leather that's proud to be vegan — not fake-animal. Cork and bamboo composite panels — natural, not plastic pretending.

### 2.2 Multi-Scheme Generation / 多方案生成

*Three schemes distilled from the original 9 variants in the legacy ProjectA_Brief*

#### Scheme A: Desert Dawn / 沙漠黎明 (Warm Tech Dominant)

| Dimension / 维度 | Description / 描述 |
|---|---|
| **Tagline / 一句话** | "Technology that feels like skin, not silicon." |
| **Emotional Response / 情感目标** | Warm, approachable, sophisticated — headphones as a natural body extension |
| **Primary Material / 主材质** | Soft-touch matte PC/ABS body + genuine vegan leather cushions + sandblasted aluminum arms |
| **Core Palette / 核心配色** | Warm sand beige body + Burnished copper PVD metal + Cognac vegan leather + Cream knit mesh |
| **Key Texture/Process / 核心工艺** | Soft-touch matte body (3-5 GU), brushed copper PVD on aluminum arm, fine grain vegan leather (breathable perforation), knit textile mesh on ear cushion face |
| **Estimated BOM / 估算BOM** | ¥185/unit (mid — copper PVD costs more, vegan leather mid-tier) |
| **Strengths / 优势** | Warmest emotional appeal. Broadest market acceptance (warm neutrals are gender-neutral, age-neutral, culture-neutral). Vegan leather + copper reads as "accessible B&O." Strong gift-market potential. |
| **Risks / 风险** | Warm beige body shows dirt/oils from skin faster than dark colors. Copper PVD color consistency across batches is tighter than silver/chrome. May read as "too safe" — doesn't express the Neo-Sensorial innovation half of the brand. |

#### Scheme B: Midnight Prism / 午夜棱镜 (Neo-Sensorial Dominant)

| Dimension / 维度 | Description / 描述 |
|---|---|
| **Tagline / 一句话** | "Color that moves with you." |
| **Emotional Response / 情感目标** | Forward-looking, creative, expressive — headphones as digital-era jewelry |
| **Primary Material / 主材质** | Gradient anodized aluminum earcups + holographic PMMA accent ring + dark chrome PVD arms + microfiber cushions |
| **Core Palette / 核心配色** | Midnight blue → Teal gradient body + Aurora green holographic ring + Dark chrome PVD arms + Deep navy microfiber cushions with iridescent thread |
| **Key Texture/Process / 核心工艺** | Gradient anodized aluminum (color-shift dye process), holographic foil inlay under transparent PMMA ring, dark chrome PVD on stainless steel arm, edge-lit laser-etched PMMA control ring |
| **Estimated BOM / 估算BOM** | ¥215/unit (highest — gradient anodizing + holographic foil + PVD all add cost) |
| **Strengths / 优势** | Maximum visual differentiation. The gradient-anodized earcup is genuinely new in the headphone category. Holographic accent creates Instagram-worthy light play. Appeals to creative professionals, gamers, fashion-forward consumers. Strong Asia market potential. |
| **Risks / 风险** | BOM exceeds ¥200 target by 7.5%. Gradient anodizing yield rate is lower than solid-color anodizing (~85% vs. 95%). Holographic aesthetic may polarize — some users will find it too "loud." Color-shift effect is hard to photograph accurately for e-commerce — may create expectation/reality gap. |

#### Scheme C: Raw Carbon / 原生碳素 (Raw Authenticity Dominant)

| Dimension / 维度 | Description / 描述 |
|---|---|
| **Tagline / 一句话** | "Sustainability you can see." |
| **Emotional Response / 情感目標** | Grounded, honest, environmentally conscious — headphones as material statement |
| **Primary Material / 主材质** | 85% PCR PC/ABS body with visible speckle + natural cork panel + raw clear-anodized aluminum arms + rPET woven cushions |
| **Core Palette / 核心配色** | PCR Carbon (dark gray base with visible cream/amber flecks) + Natural cork + Raw aluminum (clear anodized) + Charcoal rPET weave |
| **Key Texture/Process / 核心工艺** | PCR speckled injection molding (speckle from unmelted PCR particles — terrazzo-like), natural cork composite panel (compressed, sealed matte), raw sand-cast aluminum texture left visible under clear anodize, GRS-certified rPET woven mesh |
| **Estimated BOM / 估算BOM** | ¥175/unit (lowest — PCR is cheaper than virgin, cork is inexpensive, raw aluminum saves on PVD) |
| **Strengths / 优势** | Strongest sustainability story. PCR speckle is inherently unique per unit — every headphone is one-of-a-kind. Cork panel is warm, lightweight, and naturally anti-microbial. Lowest BOM. Strong EU market appeal (EU consumers willing to pay premium for visible sustainability). |
| **Risks / 风险** | PCR speckle consistency is hard to control — some units will have more/less visible flecks (is this a feature or a defect?). Cork panel durability over 3+ years of use is unproven at scale. Raw aluminum may oxidize unevenly if anodize is too thin. "Visible sustainability" aesthetic may read as "unfinished" or "budget" to non-EU markets. |

### 2.3 Scheme Comparison Matrix / 方案对比矩阵

| Criterion / 评价标准 | Weight / 权重 | A: Desert Dawn | B: Midnight Prism | C: Raw Carbon |
|---|---|---|---|---|
| Brand Alignment / 品牌匹配度 | 25% | ★★★★☆ | ★★★★★ | ★★★☆☆ |
| Market Differentiation / 市场差异化 | 20% | ★★★☆☆ | ★★★★★ | ★★★★☆ |
| User Desirability / 用户吸引力 | 20% | ★★★★☆ | ★★★★★ | ★★★☆☆ |
| Production Feasibility / 量产可行性 | 20% | ★★★★☆ | ★★★☆☆ | ★★★★☆ |
| Cost Control / 成本可控性 | 15% | ★★★★☆ | ★★★☆☆ | ★★★★★ |
| **Weighted Score / 加权得分** | **100%** | **3.95** | **4.40** | **3.55** |

### 2.4 Elimination & Optimization / 淘汰与优化

**Eliminated / 淘汰:** Scheme C (Raw Carbon) — While the strongest sustainability story and lowest cost, the "visible PCR speckle" aesthetic divides audiences too sharply. EU consumers love it, but NA and China consumers perceive it as "dirty plastic" rather than "premium recycled." The raw aluminum arm is too close to the industrial/DIY aesthetic — at ¥2,500+, consumers expect refinement. The cork panel's long-term durability (3+ years of skin oil, sweat, and handling) is unvalidated at 150K unit scale.

**Winner / 胜出:** Scheme B (Midnight Prism) — Scores highest on differentiation and user desirability. The gradient-anodized earcup is a genuine category first. The holographic accent ring creates dynamic visual interest as the wearer moves — solving the "headphones look the same from every angle" problem. Strong alignment with the AURA brand promise of "warm intelligence meets sensory-rich color."

**However — the gap between Scheme A and B is manageable, and Scheme A addresses a different consumer segment.**

**Post-Selection Refinements / 定案后优化:**
- **Decision: Dual-strategy — Scheme B selected as the HERO direction (Midnight Prism), but Scheme A's warm-neutral palette is absorbed as V1 to capture the broader market.** The three final variants span Warm Tech → Neo-Sensorial, creating a gradient of adventurousness:
  - V1 (Desert Dawn): Absorbed from Scheme A — warm sand + copper + cognac leather. The "accessible luxury" entry point. Broadest market appeal.
  - V2 (Midnight Prism): Scheme B elevated — navy-teal gradient + holographic + dark chrome. The HERO variant. Maximum differentiation. Creative professional target.
  - V3 (Arctic Haze): New synthesized variant — pale silver-white gradient + violet shimmer + brushed silver. Absorbs the lighter end of Neo-Sensorial. Gender-neutral cool tone. Bridges V1 warmth and V2 boldness.
- Gradient anodizing concentrated on V2 only (limits yield risk to one SKU). V1 and V3 use solid anodizing with PVD accents — simpler, more predictable.
- Holographic foil ring retained on V2 and V3 (subtle on V3: violet shimmer instead of full holographic). V1 uses copper PVD ring instead.
- Ear cushion material unified: all variants use premium vegan leather (bio-based PU, 30% castor oil). V1 in cognac, V2 in deep navy, V3 in pale gray. Microfiber face fabric with subtle color-matched thread — no iridescent thread (too fragile for high-wear zone).
- Headband: V1 = warm gray knit textile, V2 = dark woven jacquard, V3 = white/gray silicone mesh. Material differentiation per variant while maintaining comfort consistency.
- BOM re-optimized: V2 at ¥205 (slightly over target, offset by V1/V3 at ¥185-190). Blended BOM across SKUs = ¥195 — within target.

---

## PHASE 3: FINAL CMF STRATEGY / 最终CMF策略

### 3.1 Core Direction / 核心方向

**Warm Prism / 暖棱镜**

A hybrid CMF strategy synthesizing Warm Tech tactility with Neo-Sensorial color intelligence. The headphones feel warm and natural against the body — soft-touch surfaces, vegan leather that breathes, brushed metal that matches body temperature within seconds. But the color language is forward-looking: gradient anodizing on the hero variant, holographic light-catch accents, colors drawn from digital-native palettes rendered with material sophistication. Three variants span a gradient of adventurousness — from warm-sand accessibility to midnight-gradient boldness to arctic-violet cool. Every surface the user touches is intentional. Every angle reveals a slightly different color. These are headphones that reward attention.

### 3.2 Color Variants / 色彩方案

#### V1: Desert Dawn / 沙漠黎明

| Zone / 区域 | Material / 材料 | Material Grade & Supplier Ref / 材料等级 | Color / 颜色 | Pantone / NCS | CIELAB D65/10° (±ΔE Tol.) | Finish & Process / 表面处理 | Texture Spec / 纹理参数 | Gloss / 光泽度 | Haptics / 触感 | Touch Freq. / 接触频率 | Cost Tier / 成本 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Earcup shell / 耳罩外壳 | PC/ABS (UV-stabilized) | Soft-touch additive, molded-in (no coating) | Warm sand beige / 暖沙米 | Pantone 13-1014 TCX | L*=70, a*=5, b*=15 (±ΔE≤1.5) | Injection molded, soft-touch matte — molded-in texture | Mold-Tech MT-11010 (velvet matte) | 3-5 GU @ 60° | Warm soft-touch, slight velvety drag | High (primary visual + frequent touch) | ¥¥ |
| Metal arm / 金属臂 | Aluminum 6061-T6 | ASTM B221, CNC formed | Burnished copper PVD / 锻铜 | — | L*=55, a*=18, b*=28 (±ΔE≤2.0, PVD process) | Sandblasted #180 pre-treatment → copper PVD coating (0.5μm) | Sandblasted + PVD — fine matte metallic | 12-18 GU @ 60° | Cool metal initially, warms within seconds, slight grain | High (quality perception anchor) | ¥¥¥ |
| Ear cushion / 耳垫 | Bio-based PU (30% castor oil) vegan leather | OEKO-TEX certified, anti-microbial treatment | Cognac / 干邑棕 | Pantone 17-1340 TCX | L*=45, a*=18, b*=25 (±ΔE≤2.0) | Fine leather-like grain, micro-perforated (Ø0.5mm holes, 2mm pitch) | Vegan leather grain — fine, uniform | 2-4 GU @ 60° | Soft, breathable, subtle grain texture | Highest (continuous skin contact) | ¥¥ |
| Ear cushion mesh / 耳垫网面 | Knit textile (polyester + elastane) | Acoustically transparent, moisture-wicking | Warm cream / 暖奶油 | Pantone 12-1006 TCX | L*=82, a*=3, b*=8 (±ΔE≤2.0, textile) | Fine knit, acoustically transparent weave | Textile knit — 0.8mm hole pitch | Matte (textile) | Soft knit, breathable | High (against ear) | ¥ |
| Headband / 头梁 | Knit textile wrap over silicone cushion | Recycled polyester blend, GRS certified | Warm gray heather / 暖灰杂 | Pantone 15-1305 TCX | L*=65, a*=3, b*=8 (±ΔE≤2.0) | Knit textile wrap, seamless | Textile knit — heather yarn mix | Matte | Soft knit, cushioned, even pressure | High (continuous head contact) | ¥¥ |
| Control ring / 控制环 | Anodized aluminum ring + laser-etched PMMA insert | Al 6061 + optical PMMA | Copper PVD ring + warm white LED edge-lit | Ring matches arm finish | — | Brushed + PVD ring, laser-etched PMMA insert with edge-lit 2700K LED | Brushed concentric #220 + PVD | 12-18 GU ring, translucent PMMA | Cool metal ring, click detent feedback | Medium (playback controls) | ¥¥ |

**Color Palette / 色彩面板:**

| Swatch | Pantone | CIELAB | Hex (ref) | Role |
|---|---|---|---|---|
| Warm Sand Beige | Pantone 13-1014 TCX | L*=70, a*=5, b*=15 | #B8A898 | Dominant / 主色 |
| Burnished Copper | — | L*=55, a*=18, b*=28 | #C48058 | Metallic accent / 金属点缀 |
| Cognac Leather | Pantone 17-1340 TCX | L*=45, a*=18, b*=25 | #A06040 | Cushion / 耳垫色 |
| Warm Cream | Pantone 12-1006 TCX | L*=82, a*=3, b*=8 | #D5CEC4 | Mesh / 网面色 |

#### V2: Midnight Prism / 午夜棱镜

| Zone / 区域 | Material / 材料 | Material Grade & Supplier Ref / 材料等级 | Color / 颜色 | Pantone / NCS | CIELAB D65/10° (±ΔE Tol.) | Finish & Process / 表面处理 | Texture Spec / 纹理参数 | Gloss / 光泽度 | Haptics / 触感 | Touch Freq. / 接触频率 | Cost Tier / 成本 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Earcup shell / 耳罩外壳 | Aluminum 6061 (deep-drawn + CNC trim) | Gradient anodizing: dark navy at top → teal at bottom edge | Midnight → Teal gradient / 午夜→青蓝渐变 | Pantone 19-4027 TCX → 17-5024 TCX | L*=22→35, a*=2→-10, b*=-12→-5 (±ΔE≤2.5, gradient process wider tolerance) | Deep-drawn aluminum, gradient anodized (color-shift dye process), UV hardcoat | Brushed #320 concentric — visible under anodize | 15-25 GU @ 60° (gradient shifts reflectivity slightly) | Cool smooth aluminum, solid weight, precision | High | ¥¥¥¥ |
| Metal arm / 金属臂 | Stainless steel 316L | ASTM A240, investment cast + CNC finish | Dark chrome PVD / 暗铬 | — | L*=42, a*=1, b*=-2 (±ΔE≤2.0) | Micro-blasted → dark chrome PVD (0.6μm) | Micro-blasted matte + dark PVD | 10-15 GU @ 60° | Cool, solid heft, dark luster | High | ¥¥¥ |
| Ear cushion / 耳垫 | Bio-based PU vegan leather | OEKO-TEX certified | Deep navy / 深海军蓝 | Pantone 19-4027 TCX | L*=22, a*=2, b*=-12 (±ΔE≤2.0) | Fine leather grain, micro-perforated | Vegan leather grain — fine, uniform | 2-4 GU @ 60° | Soft, deep color, breathable | Highest | ¥¥ |
| Ear cushion mesh / 耳垫网面 | Microfiber with subtle iridescent thread | Acoustically transparent | Dark navy + subtle teal shimmer / 深蓝+青闪 | Pantone 19-4027 TCX (base) | L*=22 (base), shimmer shifts with angle (±ΔE≤3.0) | Woven microfiber, 0.02% iridescent polyester thread woven in — barely visible, catches light at certain angles | Microfiber weave — fine, smooth | Matte (microfiber) | Ultra-soft microfiber, subtle shimmer on close inspection | High | ¥¥ |
| Headband / 头梁 | Jacquard woven textile over silicone | Recycled polyester, GRS | Dark jacquard with teal tracer / 深色提花青线 | Pantone 19-4027 TCX (base) | L*=22, a*=2, b*=-12 (±ΔE≤2.0) | Jacquard woven — geometric subtle pattern | Textile jacquard — tonal pattern | Matte | Dense woven texture, cushioned | High | ¥¥ |
| Control ring / 控制环 | Holographic foil inlay under transparent PMMA ring | PMMA (optical grade) + holographic film | Aurora green holographic / 极光绿全息 | — | L*=varies with angle — green→blue→violet shift | Holographic PET film insert, overmolded with clear PMMA, edge-lit LED 4000K | Holographic foil under 1mm PMMA | 60-80 GU PMMA surface (glossy) | Smooth PMMA, holographic depth beneath surface | Medium | ¥¥¥ |

**Color Palette / 色彩面板:**

| Swatch | Pantone | CIELAB | Hex (ref) | Role |
|---|---|---|---|---|
| Midnight Navy | Pantone 19-4027 TCX | L*=22, a*=2, b*=-12 | #1C2D3D | Gradient start / 渐变起点 |
| Deep Teal | Pantone 17-5024 TCX | L*=35, a*=-10, b*=-5 | #2D6058 | Gradient end / 渐变终点 |
| Dark Chrome | — | L*=42, a*=1, b*=-2 | #6A6B6C | Metal / 金属色 |
| Aurora Holographic | — | Dynamic / 动态 | N/A | Accent ring / 光环 |

#### V3: Arctic Haze / 北极雾霭

| Zone / 区域 | Material / 材料 | Material Grade & Supplier Ref / 材料等级 | Color / 颜色 | Pantone / NCS | CIELAB D65/10° (±ΔE Tol.) | Finish & Process / 表面处理 | Texture Spec / 纹理参数 | Gloss / 光泽度 | Haptics / 触感 | Touch Freq. / 接触频率 | Cost Tier / 成本 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Earcup shell / 耳罩外壳 | PC/ABS (UV-stabilized) with pearl additive | Pearl pigment 2% in resin, molded-in | Pearl silver-white / 珍珠银白 | Pantone 11-0601 TCX (base) + pearl shift | L*=88, a*=1, b*=2 (±ΔE≤1.5) | Injection molded with pearl pigment, UV hardcoat matte | Mold-Tech MT-11020 (fine matte) with pearl undertone | 5-8 GU @ 60° | Smooth matte, subtle pearl depth shift with angle | High | ¥¥ |
| Metal arm / 金属臂 | Aluminum 6061-T6 | ASTM B221, clear anodized | Brushed silver / 拉丝银 | — | L*=78, a*=0, b*=-2 (±ΔE≤1.5) | Brushed concentric #220 → clear anodize Type II | Brushed aluminum — 0.15mm line pitch | 18-25 GU @ 60° | Cool brushed metal, bright but not chrome | High | ¥¥ |
| Ear cushion / 耳垫 | Bio-based PU vegan leather | OEKO-TEX certified | Pale gray / 浅灰 | Pantone 14-4104 TCX | L*=72, a*=1, b*=-2 (±ΔE≤2.0) | Fine grain, micro-perforated | Vegan leather grain — fine, uniform | 2-4 GU @ 60° | Soft pale leather, clean, minimal | Highest | ¥¥ |
| Ear cushion mesh / 耳垫网面 | Knit textile (polyester + elastane) | Acoustically transparent | Silver-white heather / 银白杂 | Pantone 11-0601 TCX (base) | L*=88, a*=1, b*=2 (±ΔE≤2.0) | Fine knit with subtle silver heather — barely visible fiber mixing | Textile knit — 0.8mm pitch | Matte | Soft knit, bright, airy feel | High | ¥ |
| Headband / 头梁 | Silicone mesh over memory foam | Medical-grade silicone (hypoallergenic) | Translucent white / 半透白 | — | L*=90 (translucent) | Silicone mesh — breathable grid pattern | Silicone grid — 1.5mm hole pitch, 1mm thickness | 5-10 GU (silicone) | Cool silicone, flexible, modern-tech feel | High | ¥¥ |
| Control ring / 控制环 | Anodized aluminum ring + frosted PMMA insert | Al 6061 + optical PMMA | Brushed silver ring + violet shimmer insert / 银环+紫微光 | Ring matches arm finish | — | Brushed + clear anodized ring, violet shimmer film under frosted PMMA, edge-lit 3500K | Subtle violet shimmer — less intense than V2 holographic | 18-25 GU ring, matte-frosted PMMA | Cool metal ring, subtle violet catch | Medium | ¥¥ |

**Color Palette / 色彩面板:**

| Swatch | Pantone | CIELAB | Hex (ref) | Role |
|---|---|---|---|---|
| Pearl White | Pantone 11-0601 TCX (base) | L*=88, a*=1, b*=2 | #E2DDD8 | Dominant / 主色 |
| Brushed Silver | — | L*=78, a*=0, b*=-2 | #C8C8C8 | Metal / 金属色 |
| Pale Gray Leather | Pantone 14-4104 TCX | L*=72, a*=1, b*=-2 | #B5B5B4 | Cushion / 耳垫色 |
| Violet Shimmer | — | Dynamic, subtle | N/A | Accent / 点缀 |

### 3.3 Color Harmony Analysis / 色彩和谐分析

**V1 Desert Dawn — Warm Monochromatic + Metallic Depth:**
| Relationship / 关系 | Zone Pair / 色区对 | ΔE | Perception / 感知效果 |
|---|---|---|
| Earcup ↔ Cushion | Sand beige → Cognac leather | ΔE≈21 | Medium contrast — the darker cognac cushion creates visual depth. Like a sand dune shadow. The ear "reads" as a darker interior within a lighter shell. |
| Earcup ↔ Metal Arm | Sand beige → Copper PVD | ΔE≈27 | Strong warm contrast — copper is warmer and darker than the sand body. The metal arm is the visual anchor — it's where the eye goes first. Like a copper hinge on an oak door. |
| Cushion ↔ Headband | Cognac → Warm gray heather | ΔE≈19 | Moderate bridging contrast — the headband is cooler and lighter than the cushion, creating a deliberate material break between "ear zone" and "head zone." |

**V2 Midnight Prism — Dark Gradient + Holographic Shock:**
| Relationship / 关系 | Zone Pair / 色区对 | ΔE | Perception / 感知效果 |
|---|---|---|
| Earcup top ↔ bottom | Navy → Teal gradient | ΔE≈18 (top→bottom shift) | Intentional color travel — the product is never one color. The gradient is subtle enough to read as "material depth" at a distance, but reveals teal undertones on closer inspection. |
| Earcup ↔ Holographic Ring | Navy → Aurora green (dynamic) | ΔE≈35+ (depending on angle) | Maximum accent contrast — the holographic ring is the "exclamation point." It catches light unpredictably. Like a gemstone setting on a dark watch dial. |
| Earcup ↔ Ear Cushion | Navy → Deep navy leather | ΔE≈3 | Minimal contrast — the cushion blends with the earcup. Creates a monolithic dark impression. The holographic ring becomes even more pronounced against this dark uniformity. |

**V3 Arctic Haze — Cool Minimal + Violet Whisper:**
| Relationship / 关系 | Zone Pair / 色区对 | ΔE | Perception / 感知效果 |
|---|---|---|
| Earcup ↔ Metal Arm | Pearl white → Brushed silver | ΔE≈12 | Subtle cool contrast — the silver arm is slightly darker and cooler than the pearl body. Like morning frost on a white surface. |
| Earcup ↔ Cushion | Pearl white → Pale gray leather | ΔE≈17 | Gentle gray contrast — the cushion is darker and cooler. Creates a visual "shadow" zone around the ear. |
| Metal Arm ↔ Violet Ring | Silver → Violet shimmer | ΔE≈variable | The violet shimmer is the only color accent in an otherwise monochrome palette — subtle, sophisticated, almost hidden. Reveals itself when the wearer turns their head. |

**Cross-Variant Comparison:**
| Variant Pair | Overall ΔE (dominant colors) | Stylistic Range |
|---|---|
| V1 ↔ V2 | ΔE≈52 (warm sand vs. dark navy) | Full spectrum — warm natural → dark digital |
| V1 ↔ V3 | ΔE≈23 (warm sand vs. pearl white) | Warm → Cool within light tones |
| V2 ↔ V3 | ΔE≈60 (dark navy vs. pearl white) | Dark → Light maximum contrast |

### 3.4 Material Narrative / 材料叙事

"Color that moves with you."

AURA headphones begin with the body. Put them on: the ear cushions are bio-based vegan leather, micro-perforated to breathe through a 4-hour work session. The headband distributes weight through a knit textile wrap — no pressure points, no plastic creak. The aluminum arm is cool for the first two seconds against your fingertip, then warms to body temperature — the metal remembers you.

Now look at them. The V1 Desert Dawn is warm sand with copper accents — headphones that coordinate with a cognac leather bag, an oak desk, a cream linen shirt. The V2 Midnight Prism shifts from navy to teal as you turn it in your hand — the gradient anodized earcup is never one color. The holographic control ring catches light like oil on water. The V3 Arctic Haze is pearl-white minimal with a violet shimmer that only reveals itself when the light hits at the right angle — a secret for the attentive observer.

Take them off. Around your neck, the earcups face outward — the most visible product state. This is where the CMF earns its place: the gradient catches room light, the copper PVD gleams against a sweater, the pearl body with subtle shimmer marks these as "objects of intention." Not anonymous black plastic. Not disposable tech. Headphones as an accessory worth wearing.

---

## PHASE 4: PRODUCTION FEASIBILITY / 量产可行性

### 4.1 Process-Material Matrix / 工艺-材料矩阵

| Zone / 区域 | Material / 材料 | Primary Process / 一次工艺 | Secondary Process / 二次工艺 | Est. Cycle Time / 估算周期 | Yield Rate (target) / 良率目标 | Key Quality Risk / 关键质量风险 |
|---|---|---|---|---|---|---|
| Earcup shell (V1, V3) | PC/ABS soft-touch / pearl | Injection molding (2-cavity, hot runner) | Mold texture + UV hardcoat (V3 pearl additive in resin) | 40-50 sec/part | ≥94% | Soft-touch molded-in texture consistency. Pearl pigment dispersion uniformity (V3). No visible knit lines on A-surface. |
| Earcup shell (V2) | Al 6061 deep-drawn + CNC | Deep drawing (2-stage) → CNC trim → brush #320 | Gradient anodize (color-shift dye process) → UV hardcoat | Drawing: 15 sec, CNC: 45 sec, Anodize: batch 60 min | ≥85% (gradient process is the bottleneck) | Gradient dye consistency at the transition zone — the midpoint where navy meets teal must be smooth, not a hard line. Color lot-to-lot matching (ΔE≤2.5 across transition). |
| Metal arm (V1, V3) | Al 6061-T6 | CNC machining from billet | Sandblast + PVD (V1) or Brush + clear anodize (V3) | CNC: 60 sec, PVD: batch 90 min | ≥93% | PVD color consistency across batches. Brushed grain uniformity. |
| Metal arm (V2) | SS 316L | Investment casting → CNC finish | Micro-blast + dark chrome PVD | Cast: 30 sec, CNC: 45 sec, PVD: batch 90 min | ≥90% | SS casting porosity — 316L is more expensive but higher quality. Micro-blast texture uniformity before PVD. |
| Ear cushion | Bio-PU vegan leather + memory foam | PU sheet casting → die-cut → RF weld seams → foam insert | Micro-perforation (laser or mechanical punch) | Per cushion: 45 sec assembly | ≥95% | RF weld seam strength — peel test ≥15N/cm. Perforation hole consistency — blocked holes affect breathability. Bio-PU yellowing under UV — UV stabilizer package required. |
| Control ring (V2) | PMMA + holographic PET film | Injection mold PMMA ring cavity → insert holographic film → overmold | Laser-etch markings, edge-lit LED channel | 35 sec/part | ≥88% | Holographic film placement accuracy during overmolding — misalignment creates visible wrinkles. PMMA-PET bond clarity — no delamination or hazing. |

### 4.2 Texture & Surface Specification / 纹理与表面规格

| Zone / 区域 | Texture Standard / 纹理标准 | Reference Code / 参考编号 | Depth / 纹理深度 (μm) | Ra (μm) | Gloss @ 60° / 光泽度 | Tactile descriptor / 触感描述 |
|---|---|---|---|---|---|---|
| Earcup (V1) | Mold-Tech | MT-11010 | 10-15 | 0.8-1.2 | 3-5 GU | Velvet matte — warm soft-touch, slight drag |
| Earcup (V2) | Brushed aluminum | #320 concentric brush | 2-5 (brush depth) | 0.4-0.8 | 15-25 GU | Smooth brushed metal — cool, directional grain |
| Earcup (V3) | Mold-Tech + pearl | MT-11020 + 2% pearl | 15-20 | 1.2-1.8 | 5-8 GU | Fine matte with subtle pearl depth shift |
| Metal arm (V1) | Sandblast #180 + PVD | — | 8-12 (blast depth) | 0.8-1.5 | 12-18 GU | Fine sandblasted matte with copper luster |
| Metal arm (V2) | Micro-blast + dark PVD | — | 5-8 | 0.5-1.0 | 10-15 GU | Smooth dark chrome matte — premium weight |
| Ear cushion | Vegan leather grain | Fine uniform grain | — | — | 2-4 GU | Soft, breathable leather-like, fine texture |
| Control ring (V2) | Holographic film under PMMA | Optical grade PMMA | — | Ra<0.05 (PMMA surface) | 60-80 GU | Glossy smooth, holographic depth beneath surface |

### 4.3 Durability & Testing Requirements / 耐久与测试要求

| Test Item / 测试项目 | Standard / 测试标准 | Requirement / 要求 | Affected Zones / 涉及区域 | Notes / 备注 |
|---|---|---|---|---|
| Skin Oil Resistance / 耐皮脂 | ISO 105-E04 (sweat) + artificial sebum | No discoloration or surface degradation after 72hr contact | Earcup shell, ear cushion, headband | Headphones worn 4-8hrs/day — skin oil exposure is continuous. Soft-touch V1 must not become sticky. |
| Abrasion / 耐磨 | Taber CS-10, 500g, 500 cycles | Weight loss ≤20mg, no visible wear-through | Earcup shell (all variants) | Earcups contact desk surfaces when placed down. Gradient anodize V2 must not wear through to raw aluminum. |
| Hinge Cycle / 折叠循环 | Internal standard | 10,000 fold/unfold cycles, no change in metal arm finish or detent feel | Metal arm, hinge mechanism | The hinge is the most mechanically stressed zone. PVD/anodize must survive repeated contact without chipping. |
| UV Stability / 紫外老化 | QUV (ASTM G154), 300 hrs | ΔE ≤ 3.0 (all zones), vegan leather no yellowing, holographic film no delamination | All exterior zones | V3 pearl white is most UV-sensitive — yellowing is highly visible on white. Vegan leather requires UV stabilizer. |
| Headband Stretch / 头梁拉伸 | Internal standard | 5,000 stretch cycles at 150% extension, elastic recovery ≥85% | Headband | Knit textile (V1, V2) must not bag or lose tension. Silicone mesh (V3) must not tear at attachment points. |
| Drop / 跌落 | 1.5m onto hardwood floor, 6 faces, 3 drops each | No structural failure, minor cosmetic scuff acceptable, no finish delamination | Earcup, metal arm | At ¥2,500+, users expect drop survival. Anodized aluminum earcup (V2) is most vulnerable to edge denting. |
| Ear Cushion Durability / 耳垫耐久 | Internal standard | 500 hours simulated wear (compression + heat + humidity), no foam collapse, no leather peeling | Ear cushion | The #1 warranty claim for premium headphones is ear cushion degradation. Bio-PU must match or exceed petroleum PU durability. |

### 4.4 Mass Production Cost Breakdown / 量产成本分解

*Estimated at 100K annual volume, blended across V1/V2/V3 at 40/35/25 split.*

| Zone / 区域 | Material Cost / 材料成本 (¥/unit) | Process Cost / 加工成本 (¥/unit) | Finishing Cost / 表面处理 (¥/unit) | Assembly / 装配 (¥/unit) | Subtotal / 小计 (¥/unit) | % of BOM |
|---|---|---|---|---|---|---|
| Earcup shells (pair) | ¥22.00 (V1/V3 PC/ABS avg) / ¥38.00 (V2 Al) | ¥15.00 (injection/CNC) | ¥8.00 (V1,V3) / ¥22.00 (V2 gradient anodize) | ¥5.00 | ¥50.00 (avg) | 26% |
| Metal arms (pair) | ¥18.00 (Al/SS) | ¥20.00 (CNC + cast) | ¥10.00 (PVD/anodize) | ¥6.00 | ¥54.00 | 28% |
| Ear cushions (pair) | ¥12.00 (bio-PU + foam) | ¥15.00 (cast + die-cut + RF weld) | ¥3.00 (perforation) | ¥5.00 | ¥35.00 | 18% |
| Headband | ¥8.00 (textile/silicone + silicone cushion) | ¥10.00 (wrap + bond) | ¥0 | ¥4.00 | ¥22.00 | 11% |
| Control rings (pair) | ¥5.00 (V1,V3) / ¥12.00 (V2 holographic) | ¥8.00 (IM + laser-etch) | ¥3.00 (V1,V3) / ¥8.00 (V2 foil insert) | ¥3.00 | ¥19.00 (avg) | 10% |
| Internal structure + misc | ¥10.00 (ABS internal frame) | ¥5.00 | ¥0 | ¥2.00 | ¥17.00 | 9% |
| **TOTAL / 合计 (blended)** | | | | | **¥197.00** | **100%** |

**BOM vs. Target / 物料成本 vs. 目标:** ¥197.00 blended vs. ≤ ¥200.00 — **On target, ¥3.00 under blended.** V2 Midnight Prism alone: ¥210 (over by ¥10, acceptable as HERO SKU at lower volume). V1: ¥185. V3: ¥192. The V2 premium is offset by V1's cost efficiency in the blended BOM.

**Cost Down Roadmap (for 200K+ volume):**
- Gradient anodize yield improvement from 85% → 92% at scale → save ¥5.00 (V2)
- Aluminum deep-draw tooling amortization → save ¥3.00 (V2)
- Ear cushion automated assembly line → save ¥4.00 (all)
- **Target blended BOM at scale: ¥185.00** (6% reduction)

### 4.5 Sustainability Assessment / 可持续性评估

| Dimension / 维度 | Status / 状态 | Details / 详情 |
|---|---|---|
| Bio-Based Materials / 生物基材料 | Bio-PU vegan leather (30% castor oil) across all variants. V2 aluminum earcup = infinitely recyclable. | OEKO-TEX certified. Bio-PU carbon footprint ~35% lower than petroleum PU. |
| Recycled Content / 回收含量 | Headband textile: 65% recycled polyester (V1, V2). Aluminum arms: 75% post-industrial recycled (V1, V3). | GRS certification for textile. Recycled Al uses 95% less energy than virgin aluminum smelting. |
| Recyclability / 可回收性 | Designed for disassembly: earcups unscrew from arms, cushions detach via snap-fit (not glued), headband slides off rail. | Modular design enables ear cushion replacement (extending product life is the #1 sustainability win for headphones). Electronics = e-waste stream. Aluminum + PC/ABS = separable for recycling. |
| Packaging / 包装 | FSC molded pulp tray, recycled polyester fabric pouch (doubles as travel case), soy-based ink, zero plastic windows. | Molded pulp replaces EPS foam. Fabric pouch replaces plastic bag + adds user value (travel case). Package weight 28% below category average. |
| Carbon Footprint / 碳足迹 | Estimated ~22kg CO₂e/unit (cradle-to-gate, excl. electronics). Industry average for premium headphones: ~35kg CO₂e. Reduction driver: recycled aluminum, bio-PU cushions, no paint line (in-mold texture), FSC packaging. | 37% below category average. V2 variant offset: aluminum earcup production is more carbon-intensive initially, but recyclability + product longevity offset over 5-year lifecycle. |

---

## PHASE 5: DELIVERABLES / 产出清单

### 5.1 AI Image Generation Prompts / AI生图提示词

#### Phase 1 — Research & Inspiration (研究阶段)

**Trend Mood Board — Warm Tech + Neo-Sensorial:**
```
Editorial mood board composition, split layout — left side: warm beige and terracotta material samples,
soft-touch matte surfaces, cognac vegan leather swatches, brushed copper metal,
right side: holographic iridescent film color-shifting blue→teal→violet,
gradient anodized aluminum samples, edge-lit PMMA with laser etching,
clean dark gray background, curated material palette,
warm tech meets neo-sensorial, 2026-2027 CMF direction,
8K editorial photography --ar 16:9
```

**Competitor Headphone Grid:**
```
Five premium over-ear headphones in a row, front view, studio lighting,
left to right: B&O Beoplay H95 (cream/gold, lambskin + aluminum, luxury),
Apple AirPods Max (space gray, anodized aluminum + mesh canopy),
Sony WH-1000XM5 (black, soft-touch plastic, minimal metal),
Dyson Zone (dark gray/silver, metallic visor, unconventional),
AURA placeholder (empty space with warm gradient silhouette),
same angle, same lighting, competitive analysis,
8K product photography --ar 16:9
```

#### Phase 2 — Concept Exploration (方案探索)

**3-Scheme Comparison Render:**
```
Three identical premium over-ear headphones side by side, front 3/4 view, dark studio background,

LEFT — "Desert Dawn / 沙漠黎明":
Warm sand beige soft-touch matte earcups, copper PVD metal arms,
cognac vegan leather cushions, warm gray knit headband,
accessible luxury — warm, approachable, natural,

CENTER — "Midnight Prism / 午夜棱镜" (HERO):
Dark navy to teal gradient anodized aluminum earcups,
aurora green holographic ring detail on earcup center,
dark chrome PVD stainless steel arms, deep navy leather cushions with subtle iridescent thread,
forward-looking — color-shift, bold, creative professional,

RIGHT — "Raw Carbon / 原生碳素":
Dark charcoal PCR plastic earcups with visible cream/amber speckle (terrazzo-like),
natural cork panel insert, raw clear-anodized aluminum arms,
charcoal rPET woven cushions, sustainability-as-aesthetic,

photorealistic 8K PBR rendering, identical perspective --ar 16:9
```

#### Phase 3 — Final CMF / 最终方案

**Hero Product — V1 Desert Dawn:**
```
Photorealistic product rendering of premium over-ear wireless headphones,
front 3/4 angle, warm studio lighting on cream gradient background,
earcups in warm sand beige soft-touch matte PC/ABS (Pantone 13-1014 TCX, 3-5 GU),
metal arms in burnished copper PVD on sandblasted aluminum — warm metallic luster,
ear cushions in cognac bio-based vegan leather with fine grain and micro-perforation,
ear cushion face mesh in warm cream knit textile,
headband in warm gray heather knit textile over silicone cushion,
control ring in brushed copper PVD with warm white LED edge-lit,
8K, PBR materials, commercial product photography quality --ar 4:3
```

**Hero Product — V2 Midnight Prism:**
```
Premium over-ear headphones, front 3/4 angle, dramatic dark-to-teal gradient studio background,
earcups in gradient anodized aluminum — dark navy at top flowing into deep teal at bottom edge,
brushed #320 concentric pattern visible beneath the anodize,
aurora green holographic control ring — catches blue/green/violet light at different angles — set into earcup center,
metal arms in dark chrome PVD on micro-blasted stainless steel — dark luster,
ear cushions in deep navy bio-based vegan leather with subtle iridescent thread in microfiber face mesh,
headband in dark tonal jacquard woven textile,
the headphones look like digital-era jewelry — color moves with the viewing angle,
8K, PBR, commercial quality --ar 4:3
```

**Hero Product — V3 Arctic Haze:**
```
Premium over-ear headphones, front 3/4 angle, clean cool white studio background,
earcups in pearl silver-white PC/ABS with subtle pearl pigment depth (Pantone 11-0601 base, 5-8 GU),
metal arms in brushed silver aluminum with clear anodize — #220 concentric grain visible,
ear cushions in pale gray bio-based vegan leather,
ear cushion mesh in silver-white heather knit,
headband in translucent white silicone mesh over memory foam — modern technical feel,
control ring in brushed silver with subtle violet shimmer insert — only visible at certain angles,
arctic minimal, cool, sophisticated,
8K, PBR, commercial quality --ar 4:3
```

**3-Variant Comparison:**
```
Three premium over-ear headphones side by side against a dark neutral studio background,
left: warm sand beige + copper + cognac leather (V1 Desert Dawn),
center: navy-to-teal gradient aluminum + dark chrome + deep navy (V2 Midnight Prism),
right: pearl white + brushed silver + pale gray (V3 Arctic Haze),
same front 3/4 angle, same studio lighting,
product lineup catalog photography,
8K PBR rendering --ar 16:9
```

#### Phase 4 — Technical Documentation & Macros

**Material Detail — Gradient Anodized Aluminum:**
```
Extreme macro close-up of gradient anodized aluminum surface,
color transition from dark navy (top half) to deep teal (bottom half),
brushed #320 concentric lines visible through the anodize,
smooth metallic surface, 15-25 GU, clean transition zone — no hard line,
premium metal finish reference, 8K, sharp directional light --ar 1:1
```

**Material Detail — Copper PVD on Sandblasted Aluminum:**
```
Macro close-up of copper PVD coated aluminum surface,
fine sandblasted #180 texture beneath the warm copper metallic coating,
matte-satin luster 12-18 GU, visible micro-texture catching light,
metal finish reference for premium consumer electronics,
8K macro photography --ar 1:1
```

**Material Detail — Vegan Leather Micro-Perforation:**
```
Extreme macro of bio-based vegan leather surface in cognac tone,
fine uniform leather-like grain texture, micro-perforation holes visible — 0.5mm diameter, 2mm pitch,
matte 2-4 GU, soft organic surface,
acoustic-transparent leather reference, 8K --ar 1:1
```

**Material Detail — Holographic Foil Under PMMA:**
```
Macro close-up of control ring surface,
clear PMMA surface (60-80 GU, perfectly smooth),
holographic film visible beneath — color shift green→blue→violet depending on viewing angle,
edge-lit LED channel visible as a hairline at the ring perimeter,
premium detail reference, 8K --ar 1:1
```

**Exploded Material View:**
```
Technical exploded isometric view of premium over-ear headphones,
components separated, 30° angle, dark technical background,

left earcup assembly:
- Outer shell (gradient anodized aluminum)
- Control ring (holographic foil under PMMA)
- Ear cushion (vegan leather with visible micro-perforation)
- Mesh face fabric

headband assembly (above):
- Textile/jacquard wrap layer
- Silicone cushion core
- Internal spring steel band

right earcup (symmetrical):
- Outer shell
- Ear cushion + mesh

metal arms connecting earcups to headband:
- Dark chrome PVD stainless steel
- Hinge mechanism

material callout leader lines, clean technical labeling,
8K illustration --ar 1:1
```

#### Phase 5 — Lifestyle & Packaging

**Lifestyle — Worn in Creative Workspace:**
```
Editorial lifestyle photography, creative professional wearing AURA V1 Desert Dawn headphones,
warm sand beige earcups visible, copper arm catching window light,
worn in a bright modern workspace with oak desk, plants, natural light,
the headphones look like an intentional accessory — not anonymous tech,
person in focus creating/writing, headphones-on but the shot is about the whole scene,
natural warm light, 8K editorial photography --ar 3:2
```

**Lifestyle — Neck-Worn Between Use:**
```
Fashion-lifestyle photography, AURA V2 Midnight Prism headphones worn around the neck,
gradient navy-to-teal earcups facing outward — the most visible product state,
holographic ring catching a glint of window light,
person in dark minimalist outfit, coffee shop background,
the headphones as jewelry — the earcups are the visual anchor of the outfit,
8K editorial photography --ar 3:2
```

**Packaging — Sustainable Unboxing:**
```
Flat-lay product photography, AURA headphones nestled in FSC molded pulp tray (natural kraft),
recycled polyester fabric travel pouch partially visible,
soy-based ink outer box in dark charcoal with warm gradient accent,
USB-C charging cable in braided recycled PET sleeve,
documentation printed on recycled paper,
zero plastic visible, premium sustainable packaging,
8K editorial product photography --ar 4:3
```

### 5.2 Render Shot List / 渲染镜头清单

| # | Shot / 镜头描述 | Type / 类型 | Phase / 对应阶段 |
|---|---|---|---|
| 1 | Trend mood board — Warm Tech + Neo-Sensorial | Moodboard | Phase 1 |
| 2 | Competitor headphone grid (B&O, Apple, Sony, Dyson) | Research | Phase 1 |
| 3 | 3-scheme comparison — Desert Dawn vs. Midnight Prism vs. Raw Carbon | Exploration | Phase 2 |
| 4 | Hero front 3/4 — V1 Desert Dawn (warm studio) | Hero | Phase 3 |
| 5 | Hero front 3/4 — V2 Midnight Prism (gradient background) | Hero | Phase 3 |
| 6 | Hero front 3/4 — V3 Arctic Haze (cool studio) | Hero | Phase 3 |
| 7 | 3-variant color comparison lineup | Comparison | Phase 3 |
| 8 | Material transition V1: soft-touch body → copper arm → cognac leather → knit mesh | Transition | Phase 3 |
| 9 | Material transition V2: gradient Al → dark chrome → navy leather → iridescent mesh | Transition | Phase 3 |
| 10 | Material transition V3: pearl body → brushed silver → pale gray → silicone headband | Transition | Phase 3 |
| 11 | Texture macro — gradient anodized aluminum, navy→teal | Material | Phase 4 |
| 12 | Texture macro — copper PVD on sandblasted aluminum | Material | Phase 4 |
| 13 | Texture macro — vegan leather micro-perforation, cognac | Material | Phase 4 |
| 14 | Texture macro — holographic foil under PMMA, color-shift | Material | Phase 4 |
| 15 | CMF swatch board — V2 Midnight Prism (all materials + Pantone/CIELAB callouts) | Spec | Phase 4 |
| 16 | Texture specification board — all 3 variants with process codes | Spec | Phase 4 |
| 17 | Exploded material view — isometric, components separated | Info | Phase 4 |
| 18 | Lifestyle — worn in creative workspace (V1) | Context | Phase 5 |
| 19 | Lifestyle — neck-worn between use (V2) | Context | Phase 5 |
| 20 | Packaging — FSC tray + fabric pouch + box | Context | Phase 5 |

---

## APPENDIX: CMF SPECIFICATION SHEET / 附录：CMF规格书

### V2 Midnight Prism / 午夜棱镜 — Quick Spec / 快速规格 (HERO Variant)

| | Earcup Shell | Metal Arm | Ear Cushion | Mesh Face | Headband | Control Ring |
|---|---|---|---|---|---|---|
| **Material** | Al 6061 deep-drawn | SS 316L | Bio-PU vegan leather | Microfiber + iridescent thread | Recycled PET jacquard | PMMA + holographic PET film |
| **Grade** | ASTM B221 | ASTM A240 | OEKO-TEX, 30% castor oil | Acoustically transparent | GRS certified | Optical grade PMMA |
| **Pantone** | 19-4027 → 17-5024 (gradient) | — | 19-4027 TCX | 19-4027 (base) | 19-4027 (base) | — (dynamic) |
| **CIELAB** | L*=22→35, a*=2→-10, b*=-12→-5 | L*=42, a*=1, b*=-2 | L*=22, a*=2, b*=-12 | L*=22 (base) | L*=22 | Dynamic |
| **ΔE Tol.** | ±2.5 (gradient) | ±2.0 | ±2.0 | ±3.0 | ±2.0 | N/A |
| **Finish** | Gradient anodize + UV hardcoat | Micro-blast + dark chrome PVD | Fine grain + laser micro-perforation | Microfiber weave | Jacquard woven | Holographic film under PMMA, edge-lit |
| **Texture Ref** | #320 brush + anodize | Micro-blast + PVD | Vegan leather grain | Microfiber | Woven jacquard | Optical polish |
| **Gloss @ 60°** | 15-25 GU | 10-15 GU | 2-4 GU | Matte | Matte | 60-80 GU |
| **Supplier** | TBD | TBD | TBD | TBD | TBD | TBD |

*(V1 Desert Dawn and V3 Arctic Haze spec sheets follow same format — see Phase 3.2 tables for full CIELAB/Pantone/texture data.)*

---

*Document generated from legacy ProjectA_Brief.md using v2.0 template. Reference: CMF_Crash_Course.md, CMF_Spec_Template.md, AI_Image_Generation_Guide.md. All business data are design assumptions / 所有商业数据均为设计假设.*
