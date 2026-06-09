# A2: Aether — 智能空气净化器 CMF
# Smart Air Purifier | 家用电子产品

> **Template Version:** v2.0 | 完整闭环版
> **Upgraded:** 2026-05-28 | Based on A3 Lumina pilot structure

---

## PHASE 0: BUSINESS CONTEXT / 商业背景

### 0.1 Brand & Market Positioning / 品牌与市场定位

Aether is a premium home-environment brand positioned at the intersection of air science and domestic design. It competes in the urban air quality market against Dyson (tech-performance), Molekule (science-forward), and IKEA Starkvind (democratic design). Aether differentiates through **biophilic material language** — not a machine that cleans air, but a domestic object that makes clean air feel natural. Every surface choice communicates "this belongs in a home, not a server room."

- **Brand Tone / 品牌调性:** Biophilic minimalism. Calm technology. Warm restraint. Disappears when not in use.
- **Market Tier / 市场层级:** Mass-Premium (accessible design luxury)
- **Retail Price / 零售价区间:** ¥1,800 – ¥3,200 | $250 – $450 *(设计假设, based on competitive benchmarking: Dyson Pure Cool ¥3,690, Molekule Air Mini+ $349, IKEA Starkvind ¥999)*
- **Annual Volume / 年产量:** 30,000 – 60,000 units/year *(设计假设)*
- **Target Margin / 目标利润率:** 40-45% (home appliance industry standard)
- **BOM Cost Target / 物料成本目标:** ≤ ¥180 / unit (excl. filters, electronics & packaging)
- **Key Markets / 主要市场:** China (Tier 1 cities, 45%), EU (Scandinavia/Germany, 30%), North America (coastal urban, 25%)

### 0.2 Target User Persona / 目标用户画像

**The Conscious Nester / 有意识的筑巢者**

Female-leaning, 28-40, urban apartment dweller, household income ¥300K+. She curates her living space like a gallery — every object earns its place. She follows interior design accounts on Xiaohongshu and Instagram, knows the difference between oak and walnut, and chose her sofa fabric after ordering 12 swatches. Air quality matters to her (she monitors AQI, keeps plants, burns candles selectively), but she refuses to let a plastic air purifier ruin the room she spent years perfecting. The purifier must: (1) be visually quiet enough to live in her living room or bedroom, (2) use materials that coordinate with her furniture palette, (3) feel warm to touch — not cold hard plastic, (4) offer color variants that work across different interior styles (Scandi light, Japandi warm, modern dark).

### 0.3 Business Constraints → CMF Framework / 商业约束 → CMF推导

| Constraint / 约束 | Value / 数值 | CMF Implication / CMF推导 |
|---|---|---|
| Retail Price / 零售价 | ¥1,800-3,200 | Enables natural material composites (wood fiber, stone powder) and ceramic accents, but not solid hardwood or hand-crafted finishes |
| BOM Budget (CMF only) / 物料预算 | ≤ ¥180/unit | ~30% to body shell (largest surface area), 25% to fabric grille (user-facing), 15% to base ring, 15% to control ring, 15% to LED/diffuser |
| Annual Volume / 年产量 | 30-60K units | Injection molding for body shell (not CNC). Fabric cutting + tension-fit assembly. Ceramic (zirconia) ring via powder injection molding viable at this volume. |
| Key Markets / 主要市场 | China + EU + North America | Must meet: GB 4706 (China home appliances), CE/REACH (EU), UL (North America), flammability standards for fabric components. Color palette: warm neutrals for Scandi/Japandi interiors (EU/NA), muted earth tones (China Tier 1 urban preference). |
| Brand Position / 品牌定位 | Mass-Premium | Defect tolerance: zero visible defects on front grille and body A-surface. Acceptable: minor knit-line visibility on rear panel (against wall). CMF complexity: 4-5 material zones with harmonious transitions — rich but restrained. |
| User Touchpoints / 用户触点 | Body shell (visual anchor), fabric grille (primary visual surface, touched during filter changes), base ring (touched when moving), control ring (daily interaction), LED (ambient feedback) | Premium investment in fabric grille (user's primary visual and tactile interface) and control ring (daily touch). Body must photograph well in room context. Base ring visible when unit is moved; must match variant story. |

---

## PHASE 1: MARKET & TREND RESEARCH / 市场与趋势研究

### 1.1 Market Demand Analysis / 市场需求分析

The global air purifier market exceeded $14B in 2024, with China representing 35% of demand. Three key demand signals drive CMF decisions for Aether:

1. **The visible appliance problem:** 70% of air purifier owners place the device in their living room or bedroom — the two most design-curated spaces in the home (Xiaohongshu home-design survey, 2024). Yet the category's dominant CMF language remains "white plastic box" or "futuristic tower." Users express frustration that a ¥3,000+ purchase looks like a ¥300 appliance. The CMF must earn its place in the room.

2. **Material warmth as purchase driver:** Post-pandemic, consumers associate "clean air" with natural materials (wood, stone, wool) rather than clinical/surgical materials (white ABS, chrome). The purifier category has been slow to adopt warm material language, creating a gap between what users want (furniture-like warmth) and what the market offers (appliance-white plastic).

3. **Silent visual presence:** Unlike smartphones (personal, carried) or speakers (accent objects), air purifiers must visually recede. Users want them to "disappear" — which, in CMF terms, means blending with interior materials rather than screaming for attention with LED rings and glossy surfaces. This is the opposite of Dyson's "look at me" aesthetic.

**User Pain Points with Existing CMF:**
- Dyson Pure: Sculptural and recognizable but reads as "gadget." The glossy white plastic and bladeless ring scream technology. No material warmth.
- Molekule: The aluminum body signals premium but leans cold/industrial. Limited color options. Feels like a server rack accessory.
- IKEA Starkvind: Great price-to-design ratio but material quality reads as "fast furniture" — the fabric feels thin, the plastic is clearly entry-level.
- Xiaomi: Utilitarian white cylinders. Affordable but invisible in a bad way — they look like they should be hidden, not displayed.

### 1.2 Industry CMF Trend Research / 行业CMF趋势调研

*Framework: STEEP Analysis*

**Trend 1: Biophilic Interiors / 亲生物室内设计**
- **Driver / 驱动力:** Social + Environmental — post-pandemic indoor living, biophilic design principles entering mainstream home design, 65% of new residential projects in Tier 1 Chinese cities include "natural material" briefs
- **Keywords / 关键词:** Indoor nature, natural light, wood warmth, living materials, organic forms, plant integration
- **CMF Manifestation / CMF表现:** Wood-fiber composites, stone-powder filled polymers, cork, wool felt — materials that signal "natural" even when they are technically engineered. Colors drawn from soil, moss, bark, and stone. Matte and open-pore finishes that absorb light rather than reflect it. The opposite of high-gloss appliance plastic.

**Trend 2: Calm Technology / 平静科技**
- **Driver / 驱动力:** Technological + Social — screen fatigue, notification burnout, the rise of "dumbphone" aesthetics. Consumers seeking technology that doesn't demand attention.
- **Keywords / 关键词:** Hidden-when-off, ambient feedback, soft indicators, receding interfaces, slow technology
- **CMF Manifestation / CMF表现:** Displays that disappear (etched PMMA that reads as a solid surface when off). Warm-dim LEDs (2200-2700K, not clinical 6000K). Touch surfaces that are tactile and intuitive — ceramic rings, fabric-covered controls. No screens. No blinking lights. The device communicates through material presence, not digital displays.

**Trend 3: Warm Minimalism / 温暖极简**
- **Driver / 驱动力:** Social — evolution beyond cold/white Scandinavian minimalism toward Japandi (Japanese + Scandinavian) aesthetics. Consumers want "minimal but not cold."
- **Keywords / 关键词:** Japandi, wabi-sabi, textured neutrals, natural tones, curated emptiness, imperfect perfection
- **CMF Manifestation / CMF表现:** Warm beige replaces stark white. Textured matte replaces smooth gloss. Heathered fabrics replace flat-dyed textiles. The color palette shifts from cool grays (2010s minimalism) to warm taupes, oatmeals, and moss tones. Wood tones are natural — not painted or lacquered. Ceramic reads as handcrafted, not industrial.

### 1.3 Competitor CMF Audit / 竞品CMF审计

| Competitor / 竞品 | Model / 型号 | Key CMF Features / 关键CMF特征 | Strengths / 优势 | Weaknesses → Our Opportunity / 劣势→我们的机会 |
|---|---|---|---|---|
| Dyson | Pure Cool TP09 | White/silver ABS body, bladeless loop, high-gloss finish, single colorway | Iconic silhouette. Strong brand recognition. Premium perceived value from sculptural form. | Reads as "gadget." Glossy white plastic dominates. No material warmth. No color variants for different interiors. "Look at me" aesthetic contradicts calm technology. |
| Molekule | Air Mini+ | Aluminum body (silver), tan vegan leather strap, cylindrical form, single colorway | Aluminum signals quality. Leather strap is a smart domestic touch. Science-credible brand. | Cold metallic aesthetic. Leather strap reads as "tech accessory," not furniture. No fabric/textile language. Premium but not warm. |
| IKEA | Starkvind | Gray/white fabric + white plastic, budget-oriented, flat-pack aesthetic | Fabric front is the right direction. Accessible price. Democratic design ethos. | Fabric feels thin/economical. Plastic base reads as "IKEA budget." No premium material language. No luxury aspiration. |
| Coway | Airmega 150 | White/silver plastic, glossy front panel, LED ring, appliance aesthetic | Solid filtration performance. Good price-performance ratio. | Pure appliance language. Looks like a kitchen appliance. Plastic-dominant. Zero furniture-like material cues. LED ring is distracting. |
| Blueair | DustMagnet 5410 | White/gray fabric + steel, Scandinavian design language, discrete LED | Steel + fabric is closer to "furniture" than most competitors. Swedish design credibility. | Color limited to light gray only. Steel body is still cold. Fabric is utilitarian (speaker grille), not domestic (furniture textile). |

**Competitive Insight / 竞争洞察:** The market is bifurcated between "sculptural gadget" (Dyson) and "boring box" (Coway, Xiaomi). IKEA and Blueair gesture toward fabric/textile integration but stop at "speaker grille" language — not genuine furniture-grade materials. Molekule's leather strap is a clever domestic signal but isolated. **The opportunity: a purifier that genuinely uses furniture material language — wood composite, wool/wool-like felt, ceramic — to blend into designed interiors. Not "a pretty appliance" but "a piece of furniture that filters air."**

### 1.4 Inspiration Board / 灵感板

**Primary Inspiration Sources / 主要灵感来源:**
- **Furniture Craft:** Danish mid-century cabinetry (oiled oak, wool upholstery, tapered legs), Japanese joinery (natural wood-on-wood, no hardware), contemporary Korean furniture design (warm minimalism, stone + wood + fabric combinations)
- **Textile Arts:** Heathered wool felt (color depth through fiber mixing), Japanese sashiko stitching (textural pattern through repetition), linen weaves (visible slubs, natural irregularity)
- **Architecture:** Tadao Ando's concrete (smooth but warm-toned, light-absorbing), Kengo Kuma's wood lattice (material repetition, light filtration), Axel Vervoordt interiors (raw stone + warm linen + aged wood)
- **Natural Forms:** River stones (smooth but textured, warm gray palette), moss-covered bark (green-on-brown, soft-on-rough), coastal driftwood (sun-bleached wood tones, salt-worn texture)

**Visual References / 视觉参考 (to be generated/curated):**

| Ref # | Source / 来源 | Description / 描述 | CMF Extraction / CMF提取 |
|---|---|---|---|
| 1 | Danish Furniture | Hans Wegner oak + wool armchair, oiled finish, wool in oatmeal heathered tone | Oiled oak warmth (L=55-65, a=8-12, b=25-35), heathered wool (fiber-level color mixing), matte wood grain |
| 2 | Japanese Garden | Moss-covered stone lantern, soft green-gray patina, filtered light through maple leaves | Moss green (Pantone 16-0228), stone gray (Pantone 15-1305), contrast of soft moss vs. hard stone |
| 3 | Korean Ceramic | Moon jar (dalbang-a), white porcelain with subtle warm undertone, matte glaze, hand-thrown texture | Milky white ceramic (Pantone 11-0601 → but warmer), matte glaze with subtle throwing lines, cool dense touch |
| 4 | Textile Mill | Heathered wool felt in natural undyed tones, fiber-level color variation, soft drape | Oatmeal heathered (Pantone 14-1107), charcoal heathered (19-3909), moss heathered (16-0613) |

**Color Extraction Direction / 色彩提取方向:** Use Python `cmf_color_extractor.py` to run k-means (k=5) on curated reference image set of Danish furniture interiors + Japanese garden textures + Korean ceramic surfaces. Expected extraction: warm oak mid-tone (L=55-65), oatmeal neutral (L=70-80), moss green accent (L=45-55, a=-5 to -10, b=5-15), warm charcoal anchor (L=25-35), ceramic white base (L=85-92).

---

## PHASE 2: CONCEPT EXPLORATION / 方案探索

### 2.1 Design Strategy Formulation / 设计策略制定

*From Phase 1 research + Phase 0 constraints, three design pillars emerge:*

**Pillar 1: Furniture, Not Appliance / 家具，非电器**
- **Principle / 原则:** The air purifier should use materials and finishes found in furniture showrooms, not electronics stores. Users should touch it and feel wood grain, fabric warmth, and ceramic cool — not plastic seams.
- **CMF Translation / CMF转化:** Wood-fiber composites for the body instead of painted ABS. Textile-grade acoustic felt for the grille instead of perforated plastic. Ceramic or bamboo for touch points. Zero glossy plastic anywhere. Every surface has a domestic material reference.

**Pillar 2: Visual Silence / 视觉静默**
- **Principle / 原则:** The purifier must be "invisible" in the room — it blends with interior materials, not announces itself as technology. The LED should read as ambient light, not a display.
- **CMF Translation / CMF转化:** Hidden-when-off LED (frosted PMMA with etched micro-dot pattern — reads as solid surface when unlit). Matte finishes absorb light instead of reflecting it (gloss <5 GU across body). Color palette drawn from interior neutrals — oak beige, slate gray, moss green — not product colors.

**Pillar 3: Tactile Harmony / 触觉和谐**
- **Principle / 原则:** Interacting with the purifier should be a pleasant tactile experience — changing the filter, pressing the control, moving the unit. Every touchpoint is an opportunity to reinforce quality.
- **CMF Translation / CMF转化:** Control ring in cool ceramic — temperature contrast against warm body. Fabric grille is soft and textile-like, inviting touch. Base ring with natural wood feel — warm, slight grain texture. All edges are soft-radius — no sharp parting lines. Weight distribution makes the unit feel stable and grounded.

### 2.2 Multi-Scheme Generation / 多方案生成

#### Scheme A: Tech Seamless / 科技无缝

| Dimension / 维度 | Description / 描述 |
|---|---|
| **Tagline / 一句话** | "Technology that disappears into architecture." |
| **Emotional Response / 情感目标** | Clean, modern, sophisticated — like a piece of high-end architectural lighting |
| **Primary Material / 主材质** | Mineral-filled ABS (stone-powder composite), all-body |
| **Core Palette / 核心配色** | Warm white body + Sandblasted aluminum base + White ceramic ring |
| **Key Texture/Process / 核心工艺** | Micro-textured mineral composite body (VDI 24 matte), sandblasted + clear anodized aluminum base, matte white ceramic control ring |
| **Estimated BOM / 估算BOM** | ¥145/unit (lowest — single primary material, fewer zones) |
| **Strengths / 优势** | Cleanest visual. Strongest "calm technology" expression. Monolithic presence works in modern interiors. Lowest cost — one dominant material, fewer assembly steps. No fabric = no dust-trapping concern, easier to clean. |
| **Risks / 风险** | Reads potentially as "premium Xiaomi" — still essentially a plastic monolith. Missing the "furniture" material language — no wood, no fabric, no domestic warmth. Single texture strategy may feel under-designed at ¥2,500+ price. No textile means misses "cozy" home aesthetic entirely. |

#### Scheme B: Natural Home / 自然家居

| Dimension / 维度 | Description / 描述 |
|---|---|
| **Tagline / 一句话** | "A piece of home that happens to clean air." |
| **Emotional Response / 情感目标** | Warm, grounded, design-conscious — feels chosen, not purchased out of necessity |
| **Primary Material / 主材质** | Multiple domestic materials — wood-fiber composite body + textile felt grille + ceramic touch + bamboo/cork base |
| **Core Palette / 核心配色** | Warm oak beige + Oatmeal heathered felt + Natural bamboo + Matte ceramic white (V1); Slate gray + Charcoal felt + Walnut + Charcoal ceramic (V2); Sage green + Moss felt + Cork + Cream ceramic (V3) |
| **Key Texture/Process / 核心工艺** | Wood-fiber-filled ABS body with visible particle texture, recycled PET acoustic felt with heathered fiber mixing, open-pore bamboo composite base, ceramic (zirconia) powder injection molded control ring with matte glaze, hidden-when-off etched PMMA LED diffuser |
| **Estimated BOM / 估算BOM** | ¥175/unit (mid — more material zones, fabric assembly, ceramic ring) |
| **Strengths / 优势** | Directly delivers "furniture, not appliance" positioning. Three-variant strategy addresses different interior styles (Scandi, Japandi, Industrial). Multi-material transitions create rich tactile experience. Every material has a domestic reference — wood, fabric, ceramic, bamboo/cork. Strong differentiation from all competitors. |
| **Risks / 风险** | Fabric grille requires dust-management strategy (removable/washable? vacuum-friendly?). Multi-material assembly has more potential QC failure points. Ceramic ring at this volume requires reliable PIM (powder injection molding) supplier. Wood-fiber composite color consistency harder to control than painted ABS. |

#### Scheme C: Sculptural Earth / 大地雕塑

| Dimension / 维度 | Description / 描述 |
|---|---|
| **Tagline / 一句话** | "An art object for clean air." |
| **Emotional Response / 情感目标** | Awe, uniqueness, gallery-worthy presence — a conversation piece |
| **Primary Material / 主材质** | Terrazzo-pattern body (recycled stone aggregate in bio-resin) + brass PVD trim + smoked oak base |
| **Core Palette / 核心配色** | Warm terrazzo (cream + amber + charcoal aggregate) + Satin brass + Smoked oak + Tinted glass PMMA |
| **Key Texture/Process / 核心工艺** | Cast terrazzo body (ground + polished surface), satin PVD brass control ring, smoked FSC oak base ring with Danish oil finish, smoked-tinted PMMA diffuser |
| **Estimated BOM / 估算BOM** | ¥245/unit (highest — cast terrazzo, brass PVD, smoked oak is most expensive wood option) |
| **Strengths / 优势** | Maximum visual impact. Truly unique in the category — no competitor anywhere near terrazzo. Brass + terrazzo + smoked oak is a rich, sophisticated palette that signals "design object." Strong Instagram/Pinterest potential for earned media. |
| **Risks / 风险** | BOM exceeds ¥180 target by 36% — would require ¥3,800+ retail, moving toward premium tier. Terrazzo casting has high scrap rate (~15-20%), affecting yield. Heavy weight increases shipping cost and carbon footprint. Brass PVD on a touch ring will show fingerprints. Terrazzo pattern is divisive — some users will love it, others will find it too bold for a permanent room fixture. |

### 2.3 Scheme Comparison Matrix / 方案对比矩阵

| Criterion / 评价标准 | Weight / 权重 | A: Tech Seamless | B: Natural Home | C: Sculptural Earth |
|---|---|---|---|---|
| Brand Alignment / 品牌匹配度 | 25% | ★★★☆☆ | ★★★★★ | ★★★☆☆ |
| Market Differentiation / 市场差异化 | 20% | ★★☆☆☆ | ★★★★★ | ★★★★★ |
| User Desirability / 用户吸引力 | 20% | ★★★☆☆ | ★★★★★ | ★★★★☆ |
| Production Feasibility / 量产可行性 | 20% | ★★★★★ | ★★★★☆ | ★★☆☆☆ |
| Cost Control / 成本可控性 | 15% | ★★★★★ | ★★★★☆ | ★★☆☆☆ |
| **Weighted Score / 加权得分** | **100%** | **3.20** | **4.65** | **3.25** |

### 2.4 Elimination & Optimization / 淘汰与优化

**Eliminated / 淘汰:** Scheme A (Tech Seamless) — While the most cost-efficient and cleanest expression of "calm technology," it fails to deliver the core brand promise of "furniture, not appliance." The monolithic mineral body reads as "premium Xiaomi" or "architectural Dyson" — still unmistakably a machine. Missing the domestic material language entirely: no wood, no fabric, no warmth. At this price point, the user expects material richness that a single-material strategy cannot provide.

**Eliminated / 淘汰:** Scheme C (Sculptural Earth) — Visually stunning and truly differentiated, but the terrazzo + brass + smoked oak palette pushes BOM 36% over target, forcing a retail price that exits mass-premium. More critically, the bold aesthetic contradicts "visual silence" — an art object in the room draws attention, whereas Aether's brand promise is to recede. Terrazzo's high scrap rate and the fingerprint-prone brass ring are production risks the launch volume cannot absorb.

**Winner / 胜出:** Scheme B (Natural Home) — Scores highest on brand alignment and user desirability. The four-material strategy (wood composite + textile felt + ceramic + bamboo/cork) directly materializes the "furniture, not appliance" positioning. The three-variant palette (warm oak, slate, moss) maps to the three dominant interior styles in our target markets (Scandi, Japandi, Industrial/Warm-Modern). Every touchpoint tells a material story: warm wood-fiber body, soft felt grille, cool ceramic ring, natural base.

**Post-Selection Refinements / 定案后优化:**
- Fabric grille upgraded from standard PET felt to recycled PET acoustic felt — reinforces sustainability story and improves sound absorption (the purifier fan is audible, so acoustic fabric has a functional benefit beyond aesthetics)
- Base ring material split by variant: V1 uses bamboo composite (warm + renewable), V2 uses FSC walnut veneer (dark + rich), V3 uses cork composite (lightweight + textural). This creates stronger variant differentiation than a single base material
- Control ring ceramic upgraded from generic matte glaze to variant-specific tones — warm white (V1), matte charcoal (V2), matte cream (V3) — ensuring the daily touchpoint harmonizes with each palette
- LED color temperature tuned per variant: V1 = 2700K warm, V2 = 2700K warm amber, V3 = 3000K soft white — matching the emotional temperature of each palette
- Absorbed Scheme A's "hidden-when-off" etched PMMA LED approach — the diffuser reads as a solid ceramic-like surface when unlit, only revealing its indicator function on interaction

---

## PHASE 3: FINAL CMF STRATEGY / 最终CMF策略

### 3.1 Core Direction / 核心方向

**Natural Home / 自然家居**

"A piece of home that happens to clean air." The Aether purifier embraces domestic material language — warm wood tones, soft acoustic fabric, cool ceramic, and natural base materials — textures and colors found in furniture showrooms, not electronics aisles. Every zone choice references an interior material: the wood-fiber composite body recalls Scandinavian cabinetry, the heathered felt grille recalls upholstery textiles, the ceramic control ring recalls hand-thrown pottery, and the bamboo/cork/walnut base recalls flooring and furniture legs. The form recedes visually; the LED indicator, etched into frosted PMMA, is invisible when off — only acknowledging the technology when you interact with it. Three color variants map to the three dominant interior palettes in our target market: warm Nordic, dark Japandi, and natural organic.

### 3.2 Color Variants / 色彩方案

#### V1: Warm Oak / 暖橡木

| Zone / 区域 | Material / 材料 | Material Grade & Supplier Ref / 材料等级 | Color / 颜色 | Pantone / NCS | CIELAB D65/10° (±ΔE Tol.) | Finish & Process / 表面处理 | Texture Spec / 纹理参数 | Gloss / 光泽度 | Haptics / 触感 | Touch Freq. / 接触频率 | Cost Tier / 成本 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Body shell / 机身外壳 | ABS + 30% wood-fiber composite | PCR content ≥40%, FSC-certified wood fiber | Warm oak beige / 暖橡米 | Pantone 15-1215 TCX | L*=68, a*=6, b*=18 (±ΔE≤1.5) | Injection molded, fine matte with visible wood particles | MT-11020 (fine matte stone/wood texture) | 3-5 GU @ 60° | Warm matte, subtle organic grain feel | Low (visual surface) | ¥¥ |
| Front grille / 前面网 | Recycled PET acoustic felt | GRS certified, 70% post-consumer PET, 30% virgin PET | Oatmeal heathered gray / 燕麦杂灰 | Pantone 14-1107 TCX | L*=72, a*=3, b*=8 (±ΔE≤2.0, fabric ΔE tolerance wider) | Needle-punched acoustic felt, heathered fiber mixing | Textile — fiber density 400g/m², thickness 4mm | Matte (fabric — gloss not applicable) | Soft felt, slight fiber texture, acoustic dampening | High (primary visual surface, touched during filter change) | ¥¥¥ |
| Base ring / 底部环 | Bamboo composite (bamboo powder + PLA binder) | FSC bamboo, bio-based binder ≥60% | Natural bamboo tone / 自然竹色 | Pantone 16-1333 TCX | L*=63, a*=10, b*=28 (±ΔE≤2.0, natural material) | Compression molded, open-pore matte, no coating | Natural fiber — fine sanded, Ra=2.0-3.0μm | 2-4 GU @ 60° | Warm, slight grain, organic | Medium (touched when moving unit) | ¥ |
| Control ring / 控制环 | Ceramic (zirconia ZrO₂) | Yttria-stabilized zirconia, powder injection molded | Matte warm white / 哑光暖白 | Pantone 11-0601 TCX | L*=91, a*=1, b*=4 (±ΔE≤1.0) | Powder injection molded + sintered, matte glaze | As-fired matte, Ra=0.8-1.2μm | 3-5 GU @ 60° | Cool smooth, dense, premium weight | High (daily touch interaction) | ¥¥¥ |
| LED diffuser / LED散光板 | Frosted PMMA | UV-stabilized, optical grade | Hidden-when-off / 息屏无形 | — | L*=88 (translucent when lit) | Injection molded + laser-etched micro-dot pattern | Etched dot matrix, 0.5mm dot pitch, 0.1mm depth | Translucent matte (diffuse transmittance ≥85%) | Smooth matte, reads as solid when off | Low-Medium (indicator only) | ¥ |

**Color Palette / 色彩面板:**

| Swatch / 色板 | Pantone | NCS (if applicable) | CIELAB (L*, a*, b*) | Hex (ref only) | Role / 角色 |
|---|---|---|---|---|---|
| Warm Oak Beige | Pantone 15-1215 TCX | NCS S 2010-Y30R | L*=68, a*=6, b*=18 | #B8A089 | Dominant / 主色 |
| Oatmeal Heathered | Pantone 14-1107 TCX | NCS S 1505-Y20R | L*=72, a*=3, b*=8 | #C0B7A8 | Secondary / 次要色 |
| Natural Bamboo | Pantone 16-1333 TCX | NCS S 3020-Y30R | L*=63, a*=10, b*=28 | #B8956C | Accent warm / 暖点缀 |
| Matte Ceramic White | Pantone 11-0601 TCX | NCS S 0502-Y | L*=91, a*=1, b*=4 | #EDE8E0 | Touch point / 触点色 |

#### V2: Slate Mist / 薄雾灰

| Zone / 区域 | Material / 材料 | Material Grade & Supplier Ref / 材料等级 | Color / 颜色 | Pantone / NCS | CIELAB D65/10° (±ΔE Tol.) | Finish & Process / 表面处理 | Texture Spec / 纹理参数 | Gloss / 光泽度 | Haptics / 触感 | Touch Freq. / 接触频率 | Cost Tier / 成本 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Body shell / 机身外壳 | ABS + 30% stone-powder composite | Post-industrial recycled stone powder (quartz/limestone), PCR ABS ≥30% | Warm mid-gray / 暖中灰 | Pantone 16-3802 TCX | L*=52, a*=2, b*=3 (±ΔE≤1.5) | Injection molded, micro-textured matte | MT-11030 (medium matte, subtle grain) | 2-4 GU @ 60° | Matte, slight mineral coolness | Low | ¥¥ |
| Front grille / 前面网 | Recycled PET acoustic felt | GRS certified, 80% post-consumer PET | Dark heathered charcoal / 深麻炭灰 | Pantone 19-3909 TCX | L*=28, a*=2, b*=0 (±ΔE≤2.0, fabric) | Needle-punched, heathered with subtle gray fiber flecks | Textile — 400g/m², 4mm | Matte | Soft dense felt, premium acoustic weight | High | ¥¥¥ |
| Base ring / 底部环 | FSC walnut veneer on birch ply core | FSC 100% walnut, water-based matte sealer | Rich dark brown / 丰富深棕 | Pantone 19-1213 TCX | L*=32, a*=8, b*=12 (±ΔE≤2.0, natural material) | Veneer press + CNC edge, open-pore matte | Natural wood grain — fine sanded, Ra=1.5-2.5μm | 2-4 GU @ 60° | Warm wood grain, furniture-grade quality | Medium | ¥¥ |
| Control ring / 控制环 | Ceramic (zirconia ZrO₂) | Yttria-stabilized zirconia, PIM + dark pigment loading | Matte charcoal / 哑光炭黑 | Pantone 19-3911 TCX | L*=30, a*=1, b*=-1 (±ΔE≤1.0) | Powder injection molded + sintered, matte glaze | As-fired matte, Ra=0.8-1.2μm | 2-4 GU @ 60° | Cool dense, dark ceramic, premium weight | High | ¥¥¥ |
| LED diffuser / LED散光板 | Frosted PMMA + warm amber LED (2700K) | UV-stabilized, optical grade | Hidden-when-off / 息屏无形 | — | L*=85 (amber glow when on) | Injection molded + laser-etched micro-dot | Etched dot matrix, 0.5mm pitch | Translucent matte | Smooth, warm amber glow | Low-Medium | ¥ |

**Color Palette / 色彩面板:**

| Swatch / 色板 | Pantone | NCS (if applicable) | CIELAB (L*, a*, b*) | Hex (ref only) | Role / 角色 |
|---|---|---|---|---|---|
| Warm Mid-Gray | Pantone 16-3802 TCX | NCS S 3502-Y | L*=52, a*=2, b*=3 | #8A8682 | Dominant / 主色 |
| Dark Charcoal Felt | Pantone 19-3909 TCX | NCS S 7502-B | L*=28, a*=2, b*=0 | #4A4848 | Secondary / 次要色 |
| Rich Walnut | Pantone 19-1213 TCX | NCS S 7010-Y30R | L*=32, a*=8, b*=12 | #5C4A40 | Accent dark / 深点缀 |
| Matte Charcoal Ceramic | Pantone 19-3911 TCX | NCS S 8000-N | L*=30, a*=1, b*=-1 | #4D4E50 | Touch point / 触点色 |

#### V3: Nordic Moss / 北欧苔绿

| Zone / 区域 | Material / 材料 | Material Grade & Supplier Ref / 材料等级 | Color / 颜色 | Pantone / NCS | CIELAB D65/10° (±ΔE Tol.) | Finish & Process / 表面处理 | Texture Spec / 纹理参数 | Gloss / 光泽度 | Haptics / 触感 | Touch Freq. / 接触频率 | Cost Tier / 成本 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Body shell / 机身外壳 | Bio-PP + 30% wood fiber | ISCC PLUS certified bio-polypropylene, FSC wood fiber | Soft sage green / 柔和鼠尾草绿 | Pantone 15-6315 TCX | L*=65, a*=-8, b*=12 (±ΔE≤1.5) | Injection molded, fine matte | MT-11020 (fine matte with subtle fiber texture) | 3-5 GU @ 60° | Warm matte, subtle organic feel | Low | ¥¥ |
| Front grille / 前面网 | Recycled wool felt blend | 60% recycled wool, 40% recycled PET, GRS certified | Light moss heather / 浅苔藓杂色 | Pantone 16-0613 TCX | L*=60, a*=-4, b*=15 (±ΔE≤2.0, natural fiber) | Needle-punched wool blend felt, heathered green-gray fibers | Textile — 380g/m², 4mm | Matte | Soft natural wool feel, slight fiber irregularity | High | ¥¥¥ |
| Base ring / 底部环 | Cork composite (cork granules + bio-PU binder) | FSC cork, bio-based binder ≥50%, carbon-negative raw material | Warm cork tone / 暖软木色 | Pantone 15-1214 TCX | L*=58, a*=8, b*=22 (±ΔE≤2.0, natural material) | Compression molded, raw cork surface — uncoated | Natural cork — fine ground, Ra=3.0-5.0μm | 1-3 GU @ 60° | Warm soft cork, lightweight, natural texture | Medium | ¥ |
| Control ring / 控制环 | Ceramic (zirconia ZrO₂) | Yttria-stabilized zirconia, PIM + warm cream pigment | Matte cream / 哑光奶油色 | Pantone 12-0601 TCX | L*=89, a*=2, b*=10 (±ΔE≤1.0) | Powder injection molded + sintered, matte glaze | As-fired matte, Ra=0.8-1.2μm | 3-5 GU @ 60° | Cool smooth, warm-toned cream, dense | High | ¥¥¥ |
| LED diffuser / LED散光板 | Frosted PMMA + soft white LED (3000K) | UV-stabilized, optical grade | Hidden-when-off / 息屏无形 | — | L*=90 (soft white when lit) | Injection molded + laser-etched micro-dot | Etched dot matrix, 0.5mm pitch | Translucent matte | Smooth, soft white glow | Low-Medium | ¥ |

**Color Palette / 色彩面板:**

| Swatch / 色板 | Pantone | NCS (if applicable) | CIELAB (L*, a*, b*) | Hex (ref only) | Role / 角色 |
|---|---|---|---|---|---|
| Soft Sage Green | Pantone 15-6315 TCX | NCS S 2010-G30Y | L*=65, a*=-8, b*=12 | #9EAB8C | Dominant / 主色 |
| Light Moss Heather | Pantone 16-0613 TCX | NCS S 3010-G40Y | L*=60, a*=-4, b*=15 | #9A9478 | Secondary / 次要色 |
| Warm Cork | Pantone 15-1214 TCX | NCS S 3010-Y30R | L*=58, a*=8, b*=22 | #A8886B | Accent warm / 暖点缀 |
| Matte Cream Ceramic | Pantone 12-0601 TCX | NCS S 1005-Y20R | L*=89, a*=2, b*=10 | #E4DDCA | Touch point / 触点色 |

### 3.3 Color Harmony Analysis / 色彩和谐分析

**V1 Warm Oak — Analogous Warm Harmony:**
| Relationship / 关系 | Zone Pair / 色区对 | ΔE | Perception / 感知效果 |
|---|---|---|
| Body ↔ Grille | Oak beige → Oatmeal felt | ΔE≈9 | Gentle contrast, body is warmer/darker than felt. Felt reads as lighter "window" against wood body — analogous to furniture upholstery-on-wood. |
| Body ↔ Base | Oak beige → Bamboo | ΔE≈12 | Medium contrast, bamboo is warmer and slightly darker. Creates visual grounding at the base — the unit feels anchored. |
| Body ↔ Control Ring | Oak beige → Ceramic white | ΔE≈27 | High contrast, ceramic reads as bright touch beacon. The cool white ring is the only "technology signal" — clean and intentional. |

**V2 Slate Mist — Monochromatic Depth Harmony:**
| Relationship / 关系 | Zone Pair / 色区对 | ΔE | Perception / 感知效果 |
|---|---|---|
| Body ↔ Grille | Mid-gray → Dark charcoal felt | ΔE≈25 | Strong contrast within grayscale, charcoal felt creates dramatic shadow effect against lighter gray body. Rich depth. |
| Body ↔ Base | Mid-gray → Walnut | ΔE≈27 | Strong contrast, warm walnut against cool gray. Wood warmth prevents the gray-on-gray from feeling cold. |
| Body ↔ Control Ring | Mid-gray → Charcoal ceramic | ΔE≈24 | Matched dark accent, ring blends with grille tone. The interface recedes — you find it by touch, not by looking. |

**V3 Nordic Moss — Natural Analogous Harmony:**
| Relationship / 关系 | Zone Pair / 色区对 | ΔE | Perception / 感知效果 |
|---|---|---|
| Body ↔ Grille | Sage green → Moss heather | ΔE≈7 | Subtle analogous shift, body is greener, felt is warmer/yellower. Together they read as "moss and lichen" — natural companions. |
| Body ↔ Base | Sage green → Cork | ΔE≈14 | Warm contrast, cork's amber warmth complements green body. Grounding effect similar to soil beneath plants. |
| Body ↔ Control Ring | Sage green → Cream ceramic | ΔE≈27 | High contrast, cream ring is the visual anchor. The warmth of cream (b*=10) harmonizes with the green's yellow undertone. |

**Cross-Variant Comparison:**
| Variant Pair | Overall ΔE (dominant colors) | Interior Style Match |
|---|---|
| V1 ↔ V2 | ΔE≈28 (warm vs. cool neutral) | Scandi → Japandi range |
| V1 ↔ V3 | ΔE≈25 (beige vs. green) | Scandi → Organic Natural |
| V2 ↔ V3 | ΔE≈20 (gray vs. green) | Dark Japandi → Organic Natural |

**Metamerism Note / 同色异谱说明:** The wood-fiber composite body (V1, V3) shows mild metamerism between D65 (daylight) and A (incandescent) lighting — the wood particles shift slightly redder under warm light (ΔE shift ≈1.5-2.0). This is actually desirable for a home product predominantly seen under warm interior lighting. The recycled PET felt grille shows negligible metamerism (ΔE shift <1.0 across D65/A/TL84) due to solution-dyed fibers. The ceramic control ring is metamerism-stable across all common light sources (ΔE shift <0.5).

### 3.4 Material Narrative / 材料叙事

"A piece of home that happens to clean air."

The Aether purifier is a study in domestic material memory. Run your fingers across the wood-fiber body — it's warm like an oak sideboard, with tiny visible particles that catch light like wood grain. The felt grille is soft as upholstery fabric, heathered with subtle color flecks that give it depth rather than the flat monotone of speaker mesh. Your daily interaction — a press of the ceramic control ring — delivers the cool, dense satisfaction of hand-thrown pottery: a moment of craft in an engineered object.

Move the unit and you feel the natural base — bamboo grain under your fingertips (V1), rich walnut warmth (V2), or the soft give of cork (V3). These are the materials of flooring and furniture, not electronics.

When the purifier runs, the LED breathes warm amber through etched PMMA — a firelight glow, not a notification. When it's off, the PMMA reads as solid ceramic, hiding its digital nature. The technology doesn't announce itself. The air simply feels cleaner, and the object in the corner looks like it belongs.

---

## PHASE 4: PRODUCTION FEASIBILITY / 量产可行性

### 4.1 Process-Material Matrix / 工艺-材料矩阵

| Zone / 区域 | Material / 材料 | Primary Process / 一次工艺 | Secondary Process / 二次工艺 | Est. Cycle Time / 估算周期 | Yield Rate (target) / 良率目标 | Key Quality Risk / 关键质量风险 |
|---|---|---|---|---|---|---|
| Body shell | ABS + wood fiber / stone powder composite | Injection molding (single gate, hot runner) | Matte texture from mold (no post-spray) | 45-55 sec/part | ≥95% | Wood fiber dispersion consistency — uneven fiber distribution creates visible streaking. Solution: pre-compounded masterbatch, not dry-blend at press. |
| Body shell (V3) | Bio-PP + wood fiber | Injection molding (lower melt temp than ABS) | Matte texture from mold | 50-60 sec/part | ≥92% | Bio-PP has narrower processing window. Color shift risk due to thermal sensitivity. Requires precise barrel temp control (±3°C). |
| Front grille | rPET / wool blend felt | Needle-punch nonwoven production (continuous roll) | Die-cut to shape, heat-sealed edges, tension-fit to frame | 8-12 sec/part (cutting) | ≥97% | Edge fraying after die-cut. Heat-seal edge treatment must be dialed per fabric lot. Fabric color lot-to-lot consistency — ΔE≤2.0 requires dope-dyed fiber source verification. |
| Base ring (V1) | Bamboo composite | Compression molding (heated press, 160-180°C) | CNC edge trim, fine sanding | 90-120 sec/part | ≥90% | Bamboo powder/PLA ratio affects color consistency. Moisture absorption before molding causes blistering — requires pre-drying. |
| Base ring (V2) | Walnut veneer + birch ply | Veneer press (hot press, water-based adhesive) | CNC cut, edge sand, matte sealer spray | 120-150 sec/part | ≥88% | Veneer delamination at curved edge — radius ≥5mm required. Color variation between veneer lots — sort by color grade. |
| Base ring (V3) | Cork composite | Compression molding (lower temp: 130-150°C) | Minimal finishing — raw surface, edge trim | 80-100 sec/part | ≥93% | Cork granule size consistency. Surface crumbling at thin edges — minimum wall thickness 3mm. |
| Control ring | Zirconia ceramic | Powder Injection Molding (PIM) — feedstock injection | Debinding + Sintering (1400-1500°C) + matte glaze dip | Injection: 30 sec, Sintering: 24-36 hrs (batch) | ≥85% (PIM ceramic has inherent shrinkage risk) | Sintering shrinkage (~20% linear) — tooling must compensate precisely. Color consistency of glazed surface across batches. Zirconia aging (low-temperature degradation) — yttria stabilization required. |
| LED diffuser | Frosted PMMA | Injection molding (optical grade mold) | Laser etching (micro-dot pattern, CO₂ or UV laser) | 35-45 sec/part (molding) + 15 sec (laser) | ≥96% | Laser etch depth consistency — variable depth = uneven light diffusion. PMMA yellowing under UV from LED — UV-stabilized grade required. |

### 4.2 Texture & Surface Specification / 纹理与表面规格

*Reference Standards: Mold-Tech (MT-xxxxx), SPI (A-1 ~ D-3), VDI 3400, Ra/Rz for objective roughness.*

| Zone / 区域 | Texture Standard / 纹理标准 | Reference Code / 参考编号 | Depth / 纹理深度 (μm) | Draft Angle Req. / 拔模要求 | Ra / 粗糙度Ra (μm) | Rz (μm) | Gloss @ 60° / 光泽度 | Tactile descriptor / 触感描述 |
|---|---|---|---|---|---|---|---|---|
| Body shell (V1, V3) | Mold-Tech | MT-11020 | 15-20 | ≥1.5° | 1.2-1.8 | 8-12 | 3-5 GU | Fine matte with subtle organic grain — like finely sanded wood |
| Body shell (V2) | Mold-Tech | MT-11030 | 20-25 | ≥1.5° | 1.5-2.2 | 10-16 | 2-4 GU | Medium matte with subtle mineral grain — like honed stone |
| Fabric grille (all variants) | Textile — N/A to mold standards | N/A | N/A | N/A | N/A | N/A | Matte | Soft felt, fiber density 380-400g/m², thickness 4mm |
| Base — Bamboo (V1) | Natural — sanded | 220 grit equivalent | N/A | N/A | 2.0-3.0 | — | 2-4 GU | Fine sanded bamboo grain, open-pore |
| Base — Walnut (V2) | Natural — sanded | 240 grit equivalent | N/A | N/A | 1.5-2.5 | — | 2-4 GU | Smooth walnut grain, open-pore, furniture-grade |
| Base — Cork (V3) | Natural — raw | N/A | N/A | N/A | 3.0-5.0 | — | 1-3 GU | Raw cork, slight granular texture, warm |
| Control ring (all) | As-fired ceramic matte | Post-sinter, pre-glaze | N/A | ≥0.5° (PIM mold) | 0.8-1.2 | 4-8 | 2-5 GU | Cool smooth ceramic, dense, like matte glazed pottery |
| LED diffuser | Laser-etched PMMA | Custom dot matrix | 100 (etch depth) | ≥1° | 0.5-0.8 (un-etched areas) | — | Translucent | Smooth matte with micro-texture from etch dots |

### 4.3 Durability & Testing Requirements / 耐久与测试要求

| Test Item / 测试项目 | Standard / 测试标准 | Requirement / 要求 | Affected Zones / 涉及区域 | Notes / 备注 |
|---|---|---|---|---|
| Abrasion / 耐磨 | Taber CS-10, 500g load, 500 cycles | Weight loss ≤20mg, no visible wear-through | Body shell, control ring | Wood-fiber composite may show slightly higher wear than pure ABS — within spec |
| UV Stability / 紫外老化 | QUV (ASTM G154), 200 hrs | ΔE ≤ 3.0 (body), ΔE ≤ 4.0 (fabric), no chalking | All exterior zones | Bio-PP (V3) is more UV-sensitive — requires UV stabilizer package. Fabric colorfastness to light: Grade 4 minimum (ISO 105-B02) |
| Chemical Resistance / 耐化学 | ISO 2812 / GB/T 9274 | No visible change after 24hr contact with: household cleaner (neutral pH), 50% ethanol, cooking oil vapor | Body shell, control ring, base ring | Kitchen placement means exposure to cooking oil aerosol — body must resist oil staining |
| Adhesion / 附着力 | ISO 2409 (Cross-hatch) | Class 0-1 | Not applicable — no coatings on most zones. Walnut base sealer only. | Walnut base: matte sealer adhesion, Class 1 minimum |
| Scratch Resistance / 耐刮擦 | Pencil Hardness (ASTM D3363) / Erichsen scratch | ≥HB for body shell, ≥H for control ring | Body shell, control ring | Ceramic ring significantly outperforms requirement (zirconia = ~8H) — a quality signal |
| Impact / 冲击 | IEC 60068-2-31 drop test | 0.5m drop onto hardwood floor, no structural failure, minor cosmetic scuff acceptable | All zones | Weight of unit (~5-6kg) means higher impact energy than handheld products |
| Salt Spray / 盐雾 | ISO 9227 | N/A — not applicable (indoor product, no exposed metal) | N/A | Coastal market note: high-humidity indoor environments (e.g., Shanghai summer) — test fabric for mold/mildew resistance (AATCC 30) |
| Fabric Cleanability / 织物可清洁性 | Internal standard | Vacuum-cleanable, surface dust removal ≥90% in 30 sec vacuum pass | Front grille | User-facing: communicate "vacuum monthly, hand-wash filter frame every 6 months" |
| Flammability / 阻燃 | UL 94 / GB 4943.1 (IT equipment) | HB minimum for enclosure | All plastic zones, fabric grille | Fabric grille: add flame-retardant treatment (phosphorus-based, halogen-free per EU market requirement) |

### 4.4 Mass Production Cost Breakdown / 量产成本分解

*Estimated at 50K annual volume, single-shift production, Shenzhen/Dongguan supply base.*

| Zone / 区域 | Material Cost / 材料成本 (¥/unit) | Process Cost / 加工成本 (¥/unit) | Finishing Cost / 表面处理 (¥/unit) | Assembly / 装配 (¥/unit) | Subtotal / 小计 (¥/unit) | % of BOM |
|---|---|---|---|---|---|---|
| Body shell | ¥18.50 (wood-fiber ABS compound) | ¥8.00 (injection molding) | ¥0 (mold texture, no post-spray) | ¥3.00 | ¥29.50 | 17% |
| Front grille (fabric) | ¥16.00 (rPET felt sheet) | ¥15.00 (die-cut + heat-seal + tension frame) | ¥4.00 (flame retardant treatment) | ¥5.00 | ¥40.00 | 23% |
| Base ring (avg. across V1-V3) | ¥8.00 (bamboo/cork/walnut materials) | ¥12.00 (compression molding / veneer press / CNC) | ¥3.00 (sanding, sealer) | ¥2.00 | ¥25.00 | 14% |
| Control ring | ¥12.00 (zirconia feedstock) | ¥22.00 (PIM + sintering, batch) | ¥5.00 (matte glaze) | ¥3.00 | ¥42.00 | 24% |
| LED diffuser | ¥3.00 (UV-stabilized optical PMMA) | ¥6.00 (injection molding) | ¥4.00 (laser etching) | ¥2.00 | ¥15.00 | 9% |
| Internal structure + rear panel | ¥12.00 (standard ABS, non-cosmetic) | ¥8.00 (injection molding) | ¥0 | ¥3.00 | ¥23.00 | 13% |
| **TOTAL / 合计** | | | | | **¥174.50** | **100%** |

**BOM vs. Target / 物料成本 vs. 目标:** ¥174.50 vs. ≤ ¥180.00 — **On target, ¥5.50 under.** The ceramic control ring is the costliest single zone (24% of BOM) but is the primary daily touchpoint; cost is justified. Savings from no-paint body (mold texture only) offset the ceramic investment.

**Cost Down Roadmap (for 100K+ volume):**
- Control ring: PIM feedstock price drops ~15% at double volume → save ¥3.30
- Fabric grille: automated tension-fit assembly replaces manual → save ¥4.00
- Base ring: compression mold with 4-cavity instead of 2 → save ¥3.00
- **Target BOM at scale: ¥164.20** (9% reduction)

### 4.5 Sustainability Assessment / 可持续性评估

| Dimension / 维度 | Status / 状态 | Details / 详情 |
|---|---|---|
| Recycled Content / 回收含量 | 30-40% PCR in body shell (varies by variant: V1 40% PCR ABS, V2 30% PCR + post-industrial stone powder, V3 bio-PP) | GRS certification for PCR content. V2 uses post-industrial recycled stone powder (quarry waste stream) — a unique sustainability story. |
| Bio-based Materials / 生物基材料 | V1: Bamboo composite base (60% bio-based binder). V3: Bio-PP body (ISCC PLUS), cork base (carbon-negative raw material). | V3 is the "hero" sustainability variant — bio-PP body + recycled wool felt + cork base. Carbon footprint estimated 35% lower than V1 baseline. |
| Recyclability / 可回收性 | Designed for disassembly: snap-fit grille frame, screw-attached base ring, clip-in control ring. All major plastics are mono-material per zone — no mixed-material bonding. | Fabric grille = PET (easily recycled in PET stream). Ceramic ring = technically recyclable but collection infrastructure limited. Internal electronics require separate e-waste handling. |
| Packaging / 包装 | FSC certified molded pulp (recycled paper fiber), no plastic windows, soy-based ink printing. Unboxing: fabric wrap instead of plastic bag. | Molded pulp cushioning eliminates EPS foam. Packaging weight reduction vs. industry avg: 28%. |
| Carbon Footprint / 碳足迹 | Estimated ~48kg CO₂e/unit (cradle-to-gate), excluding electronics. Industry average for this category: ~65kg CO₂e. Reduction driver: no paint line, lower-temp processing (bio-PP), natural material components that sequester carbon (wood fiber, cork). | 26% below category average. V3 variant leads at ~38kg CO₂e/unit. |

---

## PHASE 5: DELIVERABLES / 产出清单

### 5.1 AI Image Generation Prompts / AI生图提示词

#### Phase 1 — Research & Inspiration (研究阶段)

**Trend Mood Board — Biophilic Interiors:**
```
Editorial mood board composition, combining interior design photography and material samples,
warm oak wood grain textures, heathered oatmeal wool felt swatches, matte ceramic surfaces,
Japanese and Scandinavian interior references, soft natural daylight,
biophilic design aesthetic, warm minimalism, material-focused editorial,
clean white background with curated sample arrangement,
commercial mood board photography style, 8K --ar 16:9
```

**Competitor Landscape Visualization:**
```
Product comparison shot, five air purifiers in a row on a clean white surface,
left to right: Dyson Pure Cool (white/silver sculptural), Molekule Air Mini (aluminum + leather strap),
IKEA Starkvind (gray fabric + white plastic), Coway Airmega (white plastic appliance),
Blueair DustMagnet (gray fabric + steel),
same lighting, same angle, product lineup for competitive analysis,
commercial product photography, 8K --ar 16:9
```

#### Phase 2 — Concept Exploration (方案探索)

**3-Scheme Comparison Render:**
```
Three identical cylindrical air purifier towers side by side,
same form, same camera angle (front 3/4), same soft studio lighting,
left: warm white stone-textured monolithic body with sandblasted aluminum base — "Tech Seamless",
center: warm oak beige wood-fiber body + oatmeal felt grille + bamboo base + ceramic ring — "Natural Home",
right: terrazzo-pattern body (cream+amber+charcoal aggregate) + brass ring + smoked oak base — "Sculptural Earth",
clean white studio background, product comparison format,
photorealistic 8K PBR rendering, identical perspective --ar 16:9
```

#### Phase 3 — Final CMF (最终方案)

**Hero Product Render — V1 Warm Oak:**
```
Photorealistic product rendering of a premium smart air purifier,
minimalist cylindrical tower form (height ~65cm, diameter ~28cm),
warm oak beige wood-fiber composite body with subtle visible wood particles,
fine matte finish, oatmeal heathered gray recycled PET acoustic felt front grille,
natural bamboo composite base ring with open-pore matte finish,
matte warm white ceramic control ring on top surface,
frosted PMMA LED diffuser — invisible when off, etched micro-dot pattern barely visible on close inspection,
placed in a bright Scandinavian-style living room corner,
soft natural window light from left, a few plants visible in background,
light oak flooring, cream linen curtains, biophilic home setting,
8K editorial interior photography, PBR materials, commercial quality --ar 4:3
```

**Hero Product Render — V2 Slate Mist:**
```
Premium air purifier in minimalist cylindrical tower form,
warm mid-gray stone-powder composite body with subtle micro-texture,
dark heathered charcoal recycled PET felt front grille,
rich dark FSC walnut veneer base ring with visible wood grain, open-pore finish,
matte charcoal ceramic control ring on top,
frosted PMMA diffuser glowing warm amber (2700K) — barely visible ambient light,
placed in a modern Japandi-style living room with dark wood furniture,
dramatic soft window light creating gentle shadow play across textured surfaces,
dark oak flooring, linen sofa in charcoal, minimal decor,
8K editorial interior photography, PBR materials --ar 4:3
```

**Hero Product Render — V3 Nordic Moss:**
```
Air purifier in soft sage green bio-polypropylene body with subtle wood-fiber texture,
light moss heathered wool blend felt grille with natural fiber variation,
warm cork composite base ring — raw cork surface, visible granule texture,
matte cream ceramic control ring on top,
frosted PMMA diffuser glowing soft white (3000K),
bright airy Nordic apartment setting, morning light streaming through sheer curtains,
multiple indoor plants visible (monstera, ficus, trailing pothos),
light oak flooring, white walls, woven natural fiber rug,
biophilic interior, fresh and organic atmosphere,
8K editorial interior photography, PBR materials --ar 4:3
```

**3-Variant Color Comparison:**
```
Three identical air purifiers in a line against a warm light gray studio background,
left: warm oak beige body + oatmeal felt + bamboo base (V1 Warm Oak),
center: warm gray body + dark charcoal felt + walnut base (V2 Slate Mist),
right: sage green body + moss felt + cork base (V3 Nordic Moss),
same front 3/4 angle, same soft daylight-balanced studio lighting,
clean product lineup photography for catalog/e-commerce,
8K PBR rendering, commercial quality --ar 16:9
```

#### Phase 4 — Technical Documentation (技术文档)

**CMF Specification Swatch Board — V1:**
```
CMF specification presentation board, professional product design format,
left column: physical material samples arranged vertically —
  wood-fiber composite plaque (warm oak beige, MT-11020 texture, matte),
  recycled PET felt swatch (oatmeal heathered, 400g/m²),
  bamboo composite chip (natural tone, open-pore matte, fine sanded),
  ceramic color chip (matte warm white, zirconia, as-fired surface),
right column: corresponding color swatches with Pantone labels and CIELAB values printed below,
top: "AETHER V1 — WARM OAK / 暖橡木" title,
studio lighting, clean white background, CMF industry standard presentation,
8K, sharp focus on material details --ar 3:4
```

**Texture Detail Board — All Variants:**
```
CMF texture specification board, three-column layout for three variants,
each column showing macro photography of key surface textures:
  V1 column: wood-fiber composite texture (MT-11020), oatmeal felt weave, bamboo grain,
  V2 column: stone-powder texture (MT-11030), charcoal felt weave, walnut veneer grain,
  V3 column: bio-PP matte texture, moss wool felt, raw cork surface,
each texture with Mold-Tech/VDI reference code and Ra value callout labels,
professional CMF documentation style, even studio lighting,
8K macro photography, technical reference quality --ar 16:9
```

**Exploded Material View:**
```
Technical exploded view of a cylindrical air purifier,
showing material zones separated vertically:
1. Control ring (ceramic, top) — floating above body
2. LED diffuser (frosted PMMA with visible micro-dot pattern) — below ring
3. Front grille (acoustic felt, curved panel) — separated from body
4. Body shell (wood-fiber composite, main cylinder) — central
5. Base ring (bamboo/walnut/cork, bottom) — below body
clean isometric view, light gray background, material callout lines with labels,
technical documentation style, 8K, sharp focus --ar 1:1
```

### 5.2 Render Shot List / 渲染镜头清单

| # | Shot / 镜头描述 | Type / 类型 | Phase / 对应阶段 |
|---|---|---|---|
| 1 | Trend mood board — Biophilic interiors + material samples | Moodboard | Phase 1 |
| 2 | Competitor CMF comparison grid (Dyson, Molekule, IKEA, Coway, Blueair) | Research | Phase 1 |
| 3 | 3-scheme comparison render — Tech Seamless vs. Natural Home vs. Sculptural Earth | Exploration | Phase 2 |
| 4 | Hero in living room — V1 Warm Oak (Scandinavian interior context) | Hero | Phase 3 |
| 5 | Hero in living room — V2 Slate Mist (Japandi interior context) | Hero | Phase 3 |
| 6 | Hero in sunlit room — V3 Nordic Moss (biophilic interior with plants) | Hero | Phase 3 |
| 7 | 3-variant color comparison lineup (front 3/4, studio background) | Comparison | Phase 3 |
| 8 | Material transition detail: wood-fiber body → felt grille → ceramic ring (V1) | Transition | Phase 3 |
| 9 | Material transition detail: stone-powder body → charcoal felt → walnut base (V2) | Transition | Phase 3 |
| 10 | Material transition detail: bio-PP body → wool felt → cork base (V3) | Transition | Phase 3 |
| 11 | Texture macro — wood-fiber composite surface with visible particles (MT-11020) | Material | Phase 4 |
| 12 | Texture macro — heathered rPET felt (oatmeal, 400g/m² fiber structure) | Material | Phase 4 |
| 13 | Texture macro — matte ceramic ring surface (as-fired zirconia, Ra 0.8-1.2μm) | Material | Phase 4 |
| 14 | Texture macro — natural bamboo grain vs. walnut grain vs. cork surface (3-panel) | Material | Phase 4 |
| 15 | CMF swatch board — V1 Warm Oak (all materials + color chips + Pantone/CIELAB labels) | Spec | Phase 4 |
| 16 | Texture specification board — all 3 variants with MT/VDI codes and Ra values | Spec | Phase 4 |
| 17 | Exploded material view — isometric, zone separation, material callouts | Info | Phase 4 |
| 18 | LED ambient glow at night — warm amber, soft room context, invisible-when-off transition | Context | Phase 3 |
| 19 | In-room lifestyle — person reading near purifier, natural interaction, not staged product demo | Context | Phase 3 |
| 20 | Packaging & unboxing — FSC molded pulp, fabric wrap, sustainability story visible | Context | Phase 4 |

---

## APPENDIX: CMF SPECIFICATION SHEET / 附录：CMF规格书

*Refer to the full spec template at `02_Assets/CMF_Spec_Template.md` for production-grade documentation. This appendix provides per-variant summary spec sheets.*

### V1 Warm Oak / 暖橡木 — Quick Spec / 快速规格

| | Zone 1: Body Shell | Zone 2: Front Grille | Zone 3: Base Ring | Zone 4: Control Ring | Zone 5: LED Diffuser |
|---|---|---|---|---|---|
| **Material** | ABS + 30% wood-fiber composite | Recycled PET acoustic felt | Bamboo composite | Zirconia ceramic | Frosted PMMA |
| **Grade** | PCR ≥40%, FSC wood fiber | GRS, 70% post-consumer PET | FSC bamboo, bio-binder ≥60% | Yttria-stabilized ZrO₂ | UV-stabilized optical grade |
| **Pantone** | 15-1215 TCX | 14-1107 TCX | 16-1333 TCX | 11-0601 TCX | — |
| **CIELAB** | L*=68, a*=6, b*=18 | L*=72, a*=3, b*=8 | L*=63, a*=10, b*=28 | L*=91, a*=1, b*=4 | L*=88 (translucent) |
| **ΔE Tolerance** | ±1.5 | ±2.0 | ±2.0 | ±1.0 | — |
| **Finish** | Mold texture, no post-coat | Needle-punched, heat-sealed edge | Open-pore matte, sanded | Matte glaze | Laser-etched micro-dot |
| **Texture Ref** | MT-11020 | Textile — 400g/m² | 220 grit sanded | As-fired matte | Custom dot matrix |
| **Ra (μm)** | 1.2-1.8 | N/A (textile) | 2.0-3.0 | 0.8-1.2 | 0.5-0.8 |
| **Gloss @ 60°** | 3-5 GU | Matte | 2-4 GU | 3-5 GU | Translucent matte |
| **Hardness** | HB (ASTM D3363) | N/A (textile) | — | ~8H (zirconia) | — |
| **Supplier** | TBD (Shenzhen/Dongguan) | TBD (Jiangsu textile cluster) | TBD (Zhejiang bamboo processing) | TBD (Dongguan ceramic PIM) | TBD (Shenzhen optical) |

### V2 Slate Mist / 薄雾灰 — Quick Spec / 快速规格

| | Zone 1: Body Shell | Zone 2: Front Grille | Zone 3: Base Ring | Zone 4: Control Ring | Zone 5: LED Diffuser |
|---|---|---|---|---|---|
| **Material** | ABS + 30% stone-powder composite | Recycled PET acoustic felt | FSC walnut veneer + birch ply | Zirconia ceramic | Frosted PMMA |
| **Grade** | PCR ABS ≥30%, post-industrial stone | GRS, 80% post-consumer PET | FSC 100% walnut, water-based sealer | Yttria-stabilized ZrO₂ | UV-stabilized optical grade |
| **Pantone** | 16-3802 TCX | 19-3909 TCX | 19-1213 TCX | 19-3911 TCX | — |
| **CIELAB** | L*=52, a*=2, b*=3 | L*=28, a*=2, b*=0 | L*=32, a*=8, b*=12 | L*=30, a*=1, b*=-1 | L*=85 (amber glow) |
| **ΔE Tolerance** | ±1.5 | ±2.0 | ±2.0 | ±1.0 | — |
| **Finish** | Mold texture, no post-coat | Needle-punched, heat-sealed edge | Veneer press, open-pore matte | Matte glaze | Laser-etched micro-dot |
| **Texture Ref** | MT-11030 | Textile — 400g/m² | 240 grit sanded | As-fired matte | Custom dot matrix |
| **Ra (μm)** | 1.5-2.2 | N/A (textile) | 1.5-2.5 | 0.8-1.2 | 0.5-0.8 |
| **Gloss @ 60°** | 2-4 GU | Matte | 2-4 GU | 2-4 GU | Translucent matte |
| **Hardness** | HB | N/A | — | ~8H | — |
| **Supplier** | TBD | TBD | TBD (Zhejiang wood processing) | TBD | TBD |

### V3 Nordic Moss / 北欧苔绿 — Quick Spec / 快速规格

| | Zone 1: Body Shell | Zone 2: Front Grille | Zone 3: Base Ring | Zone 4: Control Ring | Zone 5: LED Diffuser |
|---|---|---|---|---|---|
| **Material** | Bio-PP + 30% wood fiber | Recycled wool blend felt | Cork composite | Zirconia ceramic | Frosted PMMA |
| **Grade** | ISCC PLUS bio-PP, FSC wood | 60% recycled wool, 40% rPET, GRS | FSC cork, bio-PU binder ≥50% | Yttria-stabilized ZrO₂ | UV-stabilized optical grade |
| **Pantone** | 15-6315 TCX | 16-0613 TCX | 15-1214 TCX | 12-0601 TCX | — |
| **CIELAB** | L*=65, a*=-8, b*=12 | L*=60, a*=-4, b*=15 | L*=58, a*=8, b*=22 | L*=89, a*=2, b*=10 | L*=90 (soft white) |
| **ΔE Tolerance** | ±1.5 | ±2.0 | ±2.0 | ±1.0 | — |
| **Finish** | Mold texture, no post-coat | Needle-punched, heat-sealed edge | Raw cork, uncoated | Matte glaze | Laser-etched micro-dot |
| **Texture Ref** | MT-11020 | Textile — 380g/m² | Natural raw | As-fired matte | Custom dot matrix |
| **Ra (μm)** | 1.2-1.8 | N/A (textile) | 3.0-5.0 | 0.8-1.2 | 0.5-0.8 |
| **Gloss @ 60°** | 3-5 GU | Matte | 1-3 GU | 3-5 GU | Translucent matte |
| **Hardness** | HB | N/A | — | ~8H | — |
| **Supplier** | TBD | TBD | TBD (Zhejiang cork processing) | TBD | TBD |

---

*Document generated with reference to: CMF_Crash_Course.md (color science, STEEP, material-process knowledge), CMF_Spec_Template.md (production spec structure), AI_Image_Generation_Guide.md (prompt engineering for CMF visualization).*
*本文档参考内置知识库生成：色彩科学、趋势方法论、材料工艺对照、量产规格结构。*
