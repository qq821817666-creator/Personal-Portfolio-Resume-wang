# A1: Lumina — 射频美容仪 CMF
# RF Facial Device | 美妆科技

---

## PHASE 0: BUSINESS CONTEXT / 商业背景

### 0.1 Brand & Market Positioning / 品牌与市场定位

Lumina is a D2C beauty-tech brand positioned at the intersection of dermatological science and self-care ritual. It competes in the fast-growing at-home beauty device market against established players (Yaman, Tripollar) and trendy newcomers (Foreo, NuFace). Lumina differentiates through **clinical credibility expressed through luxury material language** — not a medical device that happens to be beautiful, but a beauty object built to medical standards.

- **Brand Tone / 品牌调性:** Clinical luxury. Dermatologist-grade precision. Science-meets-self-care.
- **Market Tier / 市场层级:** Mass-Premium (accessible luxury)
- **Retail Price / 零售价区间:** ¥1,800 – ¥2,800 | $250 – $400 *(设计假设, based on competitive benchmarking: Tripollar Stop ¥2,688, Yaman Bloom ¥2,999, NuFace Trinity $339)*
- **Annual Volume / 年产量:** 50,000 – 100,000 units/year *(设计假设)*
- **Target Margin / 目标利润率:** 50-55% (beauty-tech industry standard)
- **BOM Cost Target / 物料成本目标:** ≤ ¥120 / unit (excl. packaging & electronics)
- **Key Markets / 主要市场:** China (primary, 60%), Japan + Korea (25%), EU/US export (15%)

### 0.2 Target User Persona / 目标用户画像

**The Skincare Investor / 护肤投资者**

Female, 25-40, urban professional, household income ¥250K+. She follows dermatologists on Xiaohongshu, reads ingredient labels, and tracks her skincare routine like a regimen. She already spends ¥2,000+/year on serums and facials. The RF device is her upgrade from topicals to tech — she sees it as "preventative investment," not vanity. She keeps the device on her vanity, not hidden in a drawer. It must: (1) look clinical enough to trust, (2) feel luxurious enough to gift, (3) photograph beautifully for her lifestyle content.

### 0.3 Business Constraints → CMF Framework / 商业约束 → CMF推导

| Constraint / 约束 | Value / 数值 | CMF Implication / CMF推导 |
|---|---|---|
| Retail Price / 零售价 | ¥1,800-2,800 | Allows premium materials (Ti, PVD, medical-grade polymers) but not precious metals or hand-finishing |
| BOM Budget (CMF only) / 物料预算 | ≤ ¥120/unit | ~40% to treatment head (Ti), 25% to body, 15% to grip, 10% to charging base, 10% to trim/LED |
| Annual Volume / 年产量 | 50-100K units | Injection molding for body (not CNC). PVD batch processing viable. LSR overmolding justified. |
| Key Markets / 主要市场 | China + Japan/Korea + EU | Must meet: GB 4706 (China), JIS (Japan), CE/REACH (EU), ISO 10993 biocompatibility for skin contact. Color palette: warm tones for Asian skin-tone compatibility, pink/rose gold preference in China, green/jade association in East Asia. |
| Brand Position / 品牌定位 | Mass-Premium | Defect tolerance: zero visible defects on treatment head and body A-surface. Acceptable: minor sink marks on internal surfaces. CMF complexity: 5-6 material zones with distinct finishes — rich but not gratuitous. |
| User Touchpoints / 用户触点 | Treatment head (continuous skin contact), body handle (held 10-15 min), grip inlay (index/middle finger), button (single press per session), charging base (daily dock) | Premium investment in Ti head (user's primary quality perception) and grip (ergonomic comfort). Body visible when displayed; base must match but can optimize cost. |

---

## PHASE 1: MARKET & TREND RESEARCH / 市场与趋势研究

### 1.1 Market Demand Analysis / 市场需求分析

The at-home beauty device market in China exceeded ¥30B in 2024, with RF devices representing the largest subcategory. Three demand signals drive CMF decisions:

1. **Trust through material cues:** Consumers cannot verify RF efficacy at purchase — they judge quality through visible material signals. Medical-grade terminology (ISO 10993, Titanium Grade 5) reassures. Clinical white alone is insufficient; it reads as "generic hospital," not "premium dermatology."

2. **Display-worthy design:** Unlike cleansing brushes (stored in showers), RF devices live on vanities and appear in social media content. CMF must be photogenic under warm bedroom lighting — the primary photography environment.

3. **Gift-market dynamics:** 30-40% of beauty device purchases are gifts (partner, mother, friend). Packaging and unboxing CMF must convey "thoughtful luxury." Pearl white + rose gold is the highest-converting gift colorway in China's beauty market (per Tmall category data).

**User Pain Points with Existing CMF:**
- Yaman: Functional but cold. "Looks like a blood pressure monitor." Too clinical.
- Tripollar: Warm gold accents but body feels lightweight/hollow. Perceived quality gap between marketing and in-hand feel.
- Foreo: Playful silicone but reads as "toy," not serious skincare. No premium weight.
- NuFace: Clean design but limited color options; feels mass-market at the price.

### 1.2 Industry CMF Trend Research / 行业CMF趋势调研

*Framework: STEEP Analysis*

**Trend 1: Skinmalism / 精简护肤**
- **Driver / 驱动力:** Social — post-COVID simplification, ingredient-conscious consumers
- **Keywords / 关键词:** Transparency, purity, fewer-but-better, clinical credibility, bioactive materials
- **CMF Manifestation / CMF表现:** Pearl whites, translucent finishes, clean matte surfaces that read as "sterile but not cold." Materials that reference skincare textures — gel-like silicones, serum-bottle gloss, cream-jar ceramics. Minimal color accents; let material quality speak.

**Trend 2: Warm Tech / 温暖科技**
- **Driver / 驱动力:** Technological — medical-grade materials democratizing into consumer products
- **Keywords / 关键词:** Titanium, ceramic coatings, soft-touch polymers, ISO-grade biocompatibility, haptics-first design
- **CMF Manifestation / CMF表现:** The aesthetic of precision medicine softened for home use. Brushed titanium replaces surgical steel. Soft-touch LSR replaces hard plastic grips. Warm metallic tones (rose gold, champagne, warm silver) replace cool clinical chrome. LED indicators glow warm, not cool blue.

**Trend 3: Ritual Objects / 仪式感物品**
- **Driver / 驱动力:** Social — wellness culture merging with product design, Japanese/Zen influences
- **Keywords / 关键词:** Jade, gua sha, spa rituals, vanity display, self-care as ceremony
- **CMF Manifestation / CMF表现:** Beauty devices designed as ritual objects, not tools. Colors reference traditional beauty materials — jade green, pearl white, amber. Texture transitions slow the user down: the cool weight of titanium, the velvet grip of silicone, the ceramic click of the button. The device feels like part of a spa treatment, not a chore.

### 1.3 Competitor CMF Audit / 竞品CMF审计

| Competitor / 竞品 | Model / 型号 | Key CMF Features / 关键CMF特征 | Strengths / 优势 | Weaknesses → Our Opportunity / 劣势→我们的机会 |
|---|---|---|---|---|
| Yaman | Bloom | White medical ABS body, silver metal treatment head, single-color minimal | Strong medical credibility, clean execution | Reads as "hospital equipment." No emotional warmth. No color variety. No luxury material cues. |
| Tripollar | Stop Vx | Dark gray body + gold-plated treatment head, compact form | Gold conveys premium. Recognizable silhouette. | Gold reads as dated/ostentatious to younger consumers. Body feels lightweight. Limited variant range. |
| Foreo | UFO 3 | Full silicone body, single-color pop palette (mint, fuchsia, black) | Playful, unthreatening, waterproof-friendly. Bold brand identity. | Silicone reads as "toy" or "cleansing brush." No premium weight. Medical credibility weak. |
| NuFace | Trinity | White ABS + silver treatment spheres + gray grip, modular attachments | Clean, professional. Accessible price aesthetic. | Mass-market feel. Plastic-y at the price point. Limited emotional range. |

**Competitive Insight / 竞争洞察:** The market is split between "too clinical" (Yaman, NuFace) and "too playful" (Foreo). Tripollar occupies the premium middle but with dated gold aesthetics. The opportunity: **genuine material luxury — titanium, ceramic finishes, soft silicone — at an accessible price point, with color variants that bridge clinical trust and self-care warmth.**

### 1.4 Inspiration Board / 灵感板

**Primary Inspiration Sources / 主要灵感来源:**
- **Skincare Textures:** Luxury serum bottles (frosted glass + glossy cap), cream jars (ceramic-like opacity, soft-touch lids), sheet mask packaging (pearl white with subtle iridescence)
- **Spa & Wellness:** Japanese onsen interiors (warm wood, stone, soft whites), jade rollers and gua sha tools (cool polished stone, translucent green), aromatherapy bottles (amber glass, minimal labels)
- **Medical Precision:** Dermatologist tools (brushed titanium, matte stainless), luxury dental clinics (warm whites, indirect lighting, ceramic surfaces), ISO-grade clean room aesthetics
- **Jewelry:** Rose gold watches (PVD on titanium, brushed concentric finishing), jade bracelets (translucent green with depth), pearl necklaces (iridescent white, organic warmth)

**Visual References / 视觉参考 (to be generated/curated):**

| Ref # | Source / 来源 | Description / 描述 | CMF Extraction / CMF提取 |
|---|---|---|---|
| 1 | Skincare Packaging | High-end serum frosted glass bottle with glossy pearl cap, soft-focus label | Pearl white gradient, frosted-to-gloss transition, minimal branding |
| 2 | Japanese Spa | Hinoki wood soaking tub, warm cream stone walls, indirect amber light | Warm cream stone tones (Pantone 11-0601), matte + wet contrast, amber glow as accent |
| 3 | Dermatology Tools | Brushed titanium surgical instrument, concentric circular grain, matte metallic luster | Grade 5 Ti with #320 circular brush, L=68-72, a=1-3, b=6-10 |
| 4 | Jade Jewelry | Translucent mutton-fat jade bracelet, soft green-white with depth, cool touch | Soft jade green, semi-translucent gloss, cool smooth haptics |

**Color Extraction Direction / 色彩提取方向:** Use Python `cmf_color_extractor.py` to run k-means (k=5) on curated reference image set of luxury skincare packaging + jade jewelry + spa interiors. Expected extraction: warm white base (L>90), rose/mauve accent (a=10-15), jade green support (a=-5 to -10, b=0-5), warm metallic mid-tone (L=65-75), deep navy anchor (L=20-30).

---

## PHASE 2: CONCEPT EXPLORATION / 方案探索

### 2.1 Design Strategy Formulation / 设计策略制定

*From Phase 1 research + Phase 0 constraints, three design pillars emerge:*

**Pillar 1: Clinical Credibility / 临床可信度**
- **Principle / 原则:** The device must visually communicate medical-grade quality — users evaluate efficacy with their eyes before their skin.
- **CMF Translation / CMF转化:** Medical-grade material grades (ISO 10993 ABS, Ti Grade 5), precision finishing (brushed concentric, diamond-cut chamfer), clean color palettes with precise Pantone/CIELAB references.

**Pillar 2: Ritual Warmth / 仪式温度**
- **Principle / 原则:** Using the device should feel like a self-care ritual, not a clinical procedure.
- **CMF Translation / CMF转化:** Warm metallic tones (rose gold, champagne) instead of surgical chrome. Soft-touch grip materials (liquid silicone rubber at Shore 40-50A) instead of hard plastic. Warm LED glow (2700-3000K) instead of cool blue.

**Pillar 3: Vanity Presence / 梳妆台存在感**
- **Principle / 原则:** The device lives on display, not in a drawer. It must photograph beautifully and coordinate with luxury skincare packaging.
- **CMF Translation / CMF转化:** High-gloss ceramic-like body finish, jewelry-grade metal finishing on visible surfaces, three curated color variants that coordinate with different interior/vanity aesthetics (warm, calm, dramatic).

### 2.2 Multi-Scheme Generation / 多方案生成

#### Scheme A: Clinical Purity / 临床纯净

| Dimension / 维度 | Description / 描述 |
|---|---|
| **Tagline / 一句话** | "Dermatologist-grade, nothing more." |
| **Emotional Response / 情感目标** | Trust, seriousness, medical authority |
| **Primary Material / 主材质** | Medical-grade ABS, all-white across all zones |
| **Core Palette / 核心配色** | Pure white (Pantone 11-0601) + Silver titanium + Clear PMMA |
| **Key Texture/Process / 核心工艺** | Matte white soft-touch body, bright silver brushed Ti head, no visible branding |
| **Estimated BOM / 估算BOM** | ¥95/unit (lowest — fewer materials, fewer finishing steps) |
| **Strengths / 优势** | Strongest medical credibility. Cleanest manufacturing. Lowest cost. Unambiguous positioning. |
| **Risks / 风险** | Reads as "hospital device," not beauty object. No gift appeal. No vanity-worthy presence. Indistinguishable from Yaman at retail shelf. Cannot command ¥2,500+ price point — too generic. |

#### Scheme B: Derma-Luxury / 肌肤奢华

| Dimension / 维度 | Description / 描述 |
|---|---|
| **Tagline / 一句话** | "Skincare, materialized." |
| **Emotional Response / 情感目标** | Indulgent self-care, clinical trust with emotional warmth, gift-worthy luxury |
| **Primary Material / 主材质** | Pearl-finish medical ABS + Titanium Grade 5 with warm PVD |
| **Core Palette / 核心配色** | Pearl white + Warm rose gold Ti + Dusty rose silicone + Champagne base metal |
| **Key Texture/Process / 核心工艺** | Ceramic-like high-gloss body, brushed concentric Ti head, velvet matte LSR grip, diamond-cut button, PVD base |
| **Estimated BOM / 估算BOM** | ¥115/unit (mid — more finishing steps, PVD adds cost) |
| **Strengths / 优势** | Bridges clinical and luxury. The texture palette references skincare — high-gloss = serum bottle, velvet silicone = cream texture, brushed Ti = precision tool. Strong gift appeal. Differentiated from all competitors. Photographs beautifully. |
| **Risks / 风险** | More complex supply chain (PVD vendor, LSR overmolding). Color consistency across Ti+ABS+silicone requires tight ΔE management. Higher BOM may stress margin at lower volume. |

#### Scheme C: Jewelry Object / 珠宝器物

| Dimension / 维度 | Description / 描述 |
|---|---|
| **Tagline / 一句话** | "Wearable beauty tech." |
| **Emotional Response / 情感目标** | Exclusivity, preciousness, fashion-forward status |
| **Primary Material / 主材质** | Full titanium body shell + 18K gold PVD throughout |
| **Core Palette / 核心配色** | 18K champagne gold + Mirror-polished Ti + Cream white LSR + Crystal PMMA |
| **Key Texture/Process / 核心工艺** | Mirror-polished Ti body (Ra<0.05μm), 18K PVD on all metal, diamond-cut faceted button, crystal-clear PMMA with faceted edge |
| **Estimated BOM / 估算BOM** | ¥195/unit (highest — full Ti body, extensive PVD, mirror polish) |
| **Strengths / 优势** | Maximum visual impact. Truly differentiated. Commands highest price point. Fashion and beauty media appeal. |
| **Risks / 风险** | BOM exceeds ¥120 target by 62% — would require ¥3,500+ retail to maintain margin, exiting mass-premium tier. Mirror polish shows fingerprints instantly. Full Ti body = heavier, colder to hold. Medical credibility weakened — reads as "fashion accessory," not "skincare device." Fingerprint magnet. |

### 2.3 Scheme Comparison Matrix / 方案对比矩阵

| Criterion / 评价标准 | Weight / 权重 | A: Clinical Purity | B: Derma-Luxury | C: Jewelry Object |
|---|---|---|---|---|
| Brand Alignment / 品牌匹配度 | 25% | ★★★☆☆ | ★★★★★ | ★★★☆☆ |
| Market Differentiation / 市场差异化 | 20% | ★★☆☆☆ | ★★★★★ | ★★★★★ |
| User Desirability / 用户吸引力 | 20% | ★★★☆☆ | ★★★★★ | ★★★★☆ |
| Production Feasibility / 量产可行性 | 20% | ★★★★★ | ★★★★☆ | ★★☆☆☆ |
| Cost Control / 成本可控性 | 15% | ★★★★★ | ★★★★☆ | ★☆☆☆☆ |
| **Weighted Score / 加权得分** | **100%** | **3.45** | **4.65** | **3.25** |

### 2.4 Elimination & Optimization / 淘汰与优化

**Eliminated / 淘汰:** Scheme C (Jewelry Object) — BOM exceeds target by 62%, pushing retail beyond mass-premium tier. Mirror-polish Ti is a fingerprint magnet incompatible with a handheld skincare device. More critically, the fashion-jewelry aesthetic undermines the essential "clinical credibility" pillar — the product reads as an accessory rather than an efficacious device.

**Eliminated / 淘汰:** Scheme A (Clinical Purity) — While cost-efficient and credible, it fails to differentiate from Yaman, the market leader. Pure white/silver reads as generic on retail shelves and lacks emotional warmth. Cannot justify the ¥2,000+ price positioning without visible material luxury cues.

**Winner / 胜出:** Scheme B (Derma-Luxury) — Scores highest on brand alignment. The strategy of translating skincare textures into product CMF (gloss = serum, velvet = cream, brushed Ti = precision tool) is both emotionally resonant and rationally defendable. It bridges the gap between clinical trust (medical-grade materials) and self-care indulgence (warm colors, soft textures) that no competitor currently occupies.

**Post-Selection Refinements / 定案后优化:**
- V2 (Jade Calm) absorbs a muted version of Scheme C's precious-stone concept — jade green instead of gold, maintaining medical credibility
- V3 (Midnight Serum) added to capture the dramatic/evening vanity aesthetic — serves users who prefer darker, moodier interiors and enables a higher-contrast option for the male gift-giver segment
- Titanium treatment head upgraded from bright silver to warm titanium (V1), maintaining the medical-grade story while adding warmth — the industry's first warm-toned Ti treatment head
- Charging base material upgraded from standard ABS to zinc alloy + silicone pad — users see the base daily, and a heavy metal base reinforces quality perception during the docking action

---

## PHASE 3: FINAL CMF STRATEGY / 最终CMF策略

### 3.1 Core Direction / 核心方向

**Derma-Luxury / 肌肤奢华**

"Skincare, materialized." The Lumina device translates skincare textures into product CMF — the high-gloss body recalls a luxury serum bottle, the velvet silicone feels like a rich cream texture, the brushed titanium treatment head is precision-engineered like a dermatologist's tool. Warm metallic tones (rose gold, champagne) add emotional warmth to the clinical material base, making the device feel like self-care, not a medical procedure. Each of the three color variants maps to a different skincare ritual mood: morning freshness (Pearl Rose), calming evening (Jade Calm), and night-time treatment (Midnight Serum).

### 3.2 Color Variants / 色彩方案

#### V1: Pearl Rose / 珍珠玫瑰

| Zone / 区域 | Material / 材料 | Material Grade & Supplier Ref / 材料等级 | Color / 颜色 | Pantone / NCS | CIELAB D65/10° (±ΔE Tol.) | Finish & Process / 表面处理 | Texture Spec / 纹理参数 | Gloss / 光泽度 | Haptics / 触感 | Touch Freq. / 接触频率 | Cost Tier / 成本 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Body handle / 机身主体 | Medical-grade ABS | ISO 10993-5/-10 certified, Sabic Cycoloy C1200HF or equiv. | Pearl white / 珍珠白 | Pantone 11-0601 TCX | L*=95, a*=0, b*=2 (±ΔE≤1.0) | High-gloss injection + UV hardcoat, ceramic-like depth | SPI A-2 mold polish (Ra ≤0.05μm on cavity) | 85-90 GU @ 60° | Cool, smooth, glass-like | High (held 10-15 min) | ¥¥ |
| Treatment head / 护理头 | Titanium Grade 5 (Ti-6Al-4V) | ASTM B348, biocompatible, ISO 5832-3 | Warm titanium / 暖钛色 | — (metal, no Pantone) | L*=68, a*=3, b*=8 (±ΔE≤1.5) | Brushed concentric circles, #320 grit, clear anti-fingerprint nano-coat | Circular brush #320, Ra 0.3-0.5μm | 15-25 GU @ 60° | Cool, smooth, fine grain palpable | Continuous (skin contact) | ¥¥¥ |
| Grip inlay / 握持嵌片 | Liquid Silicone Rubber (LSR) | Wacker Elastosil LR 3003 or equiv., ISO 10993 | Dusty rose / 烟熏玫瑰 | Pantone 14-1312 TCX | L*=75, a*=12, b*=5 (±ΔE≤1.5) | Overmolded onto ABS body, velvet matte finish | Mold-Tech MT-11010 (fine velvet), Ra 0.8-1.2μm | 2-4 GU @ 60° | Warm, velvety, anti-slip, Shore A 45-50 | High (index + middle finger) | ¥¥ |
| Control button / 控制按钮 | Titanium Grade 5 | ASTM B348 | Matching warm Ti / 暖钛同色 | — | L*=68, a*=3, b*=8 (±ΔE≤1.0) | Diamond-cut chamfer edge (0.3mm), PVD coated to match head | Chamfer: mirror (Ra ≤0.05μm); Top: brushed #320 | Chamfer: >90 GU; Top: 15-25 GU @ 60° | Cool metal, click feedback, chamfer tactile | Low (single press per session) | ¥¥ |
| LED halo / LED光环 | Frosted PMMA (Acrylic) | Evonik Acrylite Frosted or equiv. | Warm white glow / 暖白光 | — | L*=88, a*=1, b*=3 (when lit, 2700K) | Laser-etched micro-dot pattern, hidden-when-off | Dot pitch 0.1mm, diameter 0.05mm, depth 0.03mm | 50-60 GU (off), diffuse glow (on) | Smooth, seamless transition to body | None (visual only) | ¥ |
| Charging base / 充电底座 | Zinc alloy + Silicone pad | Zamak 3 (ZnAl4) + matte silicone | Warm champagne / 暖香槟 | Pantone 15-1218 TCX | L*=70, a*=5, b*=18 (±ΔE≤1.5) | PVD coating (alloy body) + matte silicone insert | Alloy: brushed #220, Ra 0.4-0.6μm; Silicone: MT-11020 | Alloy: 20-30 GU; Silicone: 2-4 GU @ 60° | Weighty base, soft silicone dock | Medium (daily docking) | ¥¥ |

**Color Palette / 色彩面板:**

| Swatch / 色板 | Pantone | NCS (if applicable) | CIELAB (L*, a*, b*) | Hex (ref only) | Role / 角色 |
|---|---|---|---|---|---|
| Body / 机身 | 11-0601 TCX | — | L*=95, a*=0, b*=2 | #F5F0EB | Dominant (60% visual area) |
| Titanium / 钛金属 | — | — | L*=68, a*=3, b*=8 | #B8A390 | Accent (25% visual area) |
| Silicone / 硅胶 | 14-1312 TCX | — | L*=75, a*=12, b*=5 | #C9AFA0 | Supporting (10% visual area) |
| Base metal / 底座 | 15-1218 TCX | — | L*=70, a*=5, b*=18 | #C4A882 | Supporting (5% visual area) |

#### V2: Jade Calm / 玉石静谧

| Zone / 区域 | Material / 材料 | Material Grade & Supplier Ref / 材料等级 | Color / 颜色 | Pantone / NCS | CIELAB D65/10° (±ΔE Tol.) | Finish & Process / 表面处理 | Texture Spec / 纹理参数 | Gloss / 光泽度 | Haptics / 触感 | Touch Freq. / 接触频率 | Cost Tier / 成本 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Body handle / 机身主体 | Medical-grade ABS | ISO 10993, Sabic Cycoloy or equiv. | Soft jade green / 软玉绿 | Pantone 13-6110 TCX | L*=82, a*=-8, b*=3 (±ΔE≤1.0) | Semi-gloss injection, ceramic-feel topcoat | SPI A-2 mold polish | 60-70 GU @ 60° | Cool, smooth, jade-like density | High | ¥¥ |
| Treatment head / 护理头 | Titanium Grade 5 | ASTM B348, ISO 5832-3 | Bright silver Ti / 亮银钛 | — | L*=72, a*=1, b*=2 (±ΔE≤1.5) | Brushed concentric #320, uncoated (native Ti oxide layer) | Circular brush #320, Ra 0.3-0.5μm | 20-30 GU @ 60° | Cool, smooth metallic, lighter feel than V1 | Continuous | ¥¥¥ |
| Grip inlay / 握持嵌片 | Liquid Silicone Rubber (LSR) | Wacker Elastosil, ISO 10993 | Matcha green / 抹茶绿 | Pantone 14-0216 TCX | L*=70, a*=-10, b*=15 (±ΔE≤1.5) | Velvet matte overmold | MT-11010, Ra 0.8-1.2μm | 2-4 GU @ 60° | Warm velvet, spring-like freshness, Shore A 45-50 | High | ¥¥ |
| Control button / 控制按钮 | Titanium Grade 5 | ASTM B348 | Bright silver / 亮银 | — | L*=72, a*=1, b*=2 (±ΔE≤1.0) | Diamond-cut chamfer (0.3mm), uncoated | Chamfer mirror, top brushed #320 | Chamfer >90 GU, top 20-30 GU | Cool, precise | Low | ¥¥ |
| LED halo / LED光环 | Frosted PMMA | Evonik Acrylite or equiv. | Cool white glow / 冷白光 | — | L*=88, a*=0, b*=0 (when lit, 4000K) | Laser-etched micro-dot | Dot pitch 0.1mm | 50-60 GU (off) | Smooth | None | ¥ |
| Charging base / 充电底座 | Zinc alloy + Silicone pad | Zamak 3 + matte silicone | Pale silver / 浅银 | Pantone 14-4201 TCX | L*=78, a*=1, b*=0 (±ΔE≤1.5) | Brushed alloy + matte silicone | Alloy: brushed #220, Ra 0.4-0.6μm; Silicone: MT-11020 | Alloy: 20-30 GU; Silicone: 2-4 GU | Lightweight metal, soft dock | Medium | ¥¥ |

**Color Palette / 色彩面板:**

| Swatch / 色板 | Pantone | NCS (if applicable) | CIELAB (L*, a*, b*) | Hex (ref only) | Role / 角色 |
|---|---|---|---|---|---|
| Body / 机身 | 13-6110 TCX | — | L*=82, a*=-8, b*=3 | #C5D5C8 | Dominant |
| Titanium / 钛金属 | — | — | L*=72, a*=1, b*=2 | #B8B5B0 | Accent |
| Silicone / 硅胶 | 14-0216 TCX | — | L*=70, a*=-10, b*=15 | #A8B58A | Supporting |
| Base metal / 底座 | 14-4201 TCX | — | L*=78, a*=1, b*=0 | #C5C5C5 | Supporting |

#### V3: Midnight Serum / 深夜精华

| Zone / 区域 | Material / 材料 | Material Grade & Supplier Ref / 材料等级 | Color / 颜色 | Pantone / NCS | CIELAB D65/10° (±ΔE Tol.) | Finish & Process / 表面处理 | Texture Spec / 纹理参数 | Gloss / 光泽度 | Haptics / 触感 | Touch Freq. / 接触频率 | Cost Tier / 成本 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Body handle / 机身主体 | Medical-grade ABS | ISO 10993, Sabic Cycoloy or equiv. | Deep indigo blue / 深靛蓝 | Pantone 19-3926 TCX | L*=25, a*=5, b*=-20 (±ΔE≤1.0) | High-gloss injection + UV hardcoat, glass-like depth | SPI A-2 mold polish | 85-90 GU @ 60° | Cool, heavy, glass-like, dramatic | High | ¥¥ |
| Treatment head / 护理头 | Titanium Grade 5 | ASTM B348, ISO 5832-3 | Dark gray Ti (PVD) / 暗灰钛 | — | L*=45, a*=1, b*=-1 (±ΔE≤1.5) | Radial brushed #320 + dark gray PVD coating | Radial brush #320, Ra 0.3-0.5μm | 10-20 GU @ 60° | Cool, dark, moody, precision feel | Continuous | ¥¥¥ |
| Grip inlay / 握持嵌片 | Liquid Silicone Rubber (LSR) | Wacker Elastosil, ISO 10993 | Dark navy / 深海军蓝 | Pantone 19-4019 TCX | L*=28, a*=2, b*=-12 (±ΔE≤1.5) | Velvet matte overmold | MT-11010, Ra 0.8-1.2μm | 2-4 GU @ 60° | Warm velvet with dark depth, Shore A 45-50 | High | ¥¥ |
| Control button / 控制按钮 | Titanium Grade 5 + PVD | ASTM B348 | Dark Ti / 暗钛色 | — | L*=45, a*=1, b*=-1 (±ΔE≤1.0) | Diamond-cut chamfer (0.3mm) + dark gray PVD | Chamfer mirror, top brushed #320 | Chamfer >90 GU, top 10-20 GU | Cool dark metal, dramatic click | Low | ¥¥ |
| LED halo / LED光环 | Frosted PMMA | Evonik Acrylite or equiv. | Warm amber glow / 暖琥珀光 | — | L*=85, a*=8, b*=30 (when lit, 2200K) | Laser-etched micro-dot | Dot pitch 0.1mm | 50-60 GU (off) | Smooth | None | ¥ |
| Charging base / 充电底座 | Zinc alloy + Silicone pad | Zamak 3 + matte silicone | Dark chrome / 暗铬色 | Pantone 19-4008 TCX | L*=32, a*=1, b*=-2 (±ΔE≤1.5) | Dark PVD coating (alloy) + matte silicone | Alloy: brushed #220, Ra 0.4-0.6μm; Silicone: MT-11020 | Alloy: 10-15 GU; Silicone: 2-4 GU | Heavy dark metal, soft dock contrast | Medium | ¥¥ |

**Color Palette / 色彩面板:**

| Swatch / 色板 | Pantone | NCS (if applicable) | CIELAB (L*, a*, b*) | Hex (ref only) | Role / 角色 |
|---|---|---|---|---|---|
| Body / 机身 | 19-3926 TCX | — | L*=25, a*=5, b*=-20 | #2D2D4B | Dominant |
| Titanium / 钛金属 | — | — | L*=45, a*=1, b*=-1 | #737272 | Accent |
| Silicone / 硅胶 | 19-4019 TCX | — | L*=28, a*=2, b*=-12 | #3D4260 | Supporting |
| Base metal / 底座 | 19-4008 TCX | — | L*=32, a*=1, b*=-2 | #504F50 | Supporting |

### 3.3 Color Harmony Analysis / 色彩和谐分析

**V1 Pearl Rose — Harmony Strategy: Analogous Warm**

| Relationship / 关系 | Zone Pair / 色区对 | ΔE | Perception / 感知效果 |
|---|---|---|---|
| Body ↔ Silicone | ABS → LSR | 22.5 | Strong value + chroma contrast — grip visually recedes from body, guiding hand placement |
| Body ↔ Titanium | ABS → Ti | 27.8 | High contrast — Ti head anchors visual weight at top, reads as functional core |
| Titanium ↔ Base | Ti → Zn Alloy | 10.2 | Moderate contrast — warm metallic family, base is slightly warmer/golder |
| Silicone ↔ Base | LSR → Zn Alloy | 15.3 | Clear zone distinction — soft silicone vs. metallic base, material differentiation |

**V2 Jade Calm — Harmony Strategy: Complementary Cool**

| Relationship / 关系 | Zone Pair / 色区对 | ΔE | Perception / 感知效果 |
|---|---|---|---|
| Body ↔ Silicone | ABS → LSR | 17.8 | Green-toned gradient — body is lighter/more neutral, grip is deeper/verdant |
| Body ↔ Titanium | ABS → Ti | 10.5 | Moderate — bright silver Ti reads as clean/precise against soft green body |
| Silicone ↔ Base | LSR → Zn Alloy | 18.2 | Clear organic (green silicone) vs. inorganic (silver metal) distinction |

**V3 Midnight Serum — Harmony Strategy: Monochromatic Depth**

| Relationship / 关系 | Zone Pair / 色区对 | ΔE | Perception / 感知效果 |
|---|---|---|---|
| Body ↔ Silicone | ABS → LSR | 10.3 | Deep tonal shift — indigo body vs. navy grip, subtle differentiation |
| Body ↔ Titanium | ABS → Ti | 30.2 | Maximum contrast — dark body makes the Ti head visually pop, defining the product architecture |
| Titanium ↔ Base | Ti → Zn Alloy | 13.1 | Dark metallic family — PVD Ti vs. PVD Zn, head slightly lighter for visual hierarchy |

**Metamerism Note / 同色异谱说明:** The pearl white body (V1, Pantone 11-0601) shows minimal metamerism (ΔE < 1.0 between D65 and A light sources) due to its near-neutral chromaticity. V3's deep indigo body (Pantone 19-3926) is more susceptible — ΔE ≈ 1.8 between D65 (daylight, blue tones emphasized) and A (incandescent, warmer, bluer tones recede). Under warm bedroom lighting (the primary usage environment), V3's blue tones will read as slightly deeper/more muted, which is intentional — the dramatic contrast is designed for evening use.

### 3.4 Material Narrative / 材料叙事

"Skincare, materialized." The Lumina device translates skincare textures into product CMF — the high-gloss body recalls a luxury serum bottle held up to the light, the velvet silicone grip feels like a rich cream melting between fingertips, the brushed titanium treatment head is precision-engineered like a dermatologist's tool. Warm metallic tones (rose gold, champagne) add emotional heat to the clinical material base — this is not a cold medical instrument, but a warm ritual object. The arc of interaction is choreographed: the cool, weighty titanium head makes first contact with skin (precision, trust), the warm velvet grip settles into the hand (comfort, ritual), the ceramic-smooth body catches ambient light on the vanity (beauty, display). Each material transition slows the user down, transforming a treatment into a moment of self-care. The three color variants map to three skincare moods: morning renewal (Pearl Rose), afternoon calm (Jade Calm), evening treatment (Midnight Serum).

---

## PHASE 4: PRODUCTION FEASIBILITY / 量产可行性

### 4.1 Process-Material Matrix / 工艺-材料矩阵

| Zone / 区域 | Material / 材料 | Primary Process / 一次工艺 | Secondary Process / 二次工艺 | Est. Cycle Time / 估算周期 | Yield Rate (target) / 良率目标 | Key Quality Risk / 关键质量风险 |
|---|---|---|---|---|---|---|
| Body handle / 机身 | Medical ABS | Injection molding, single cavity | UV hardcoat spray + UV cure | 45-55 sec/shot | ≥95% | Flow lines/weld lines visible on high-gloss pearl surface; gate vestige must be on parting line |
| Treatment head / 护理头 | Ti Grade 5 | CNC turning (concentric profile) | #320 circular brushing + PVD coating (V1, V3) or clear nano-coat (V2) | 120-180 sec/part (CNC) + 20 min batch (PVD) | ≥90% (CNC), ≥95% (PVD batch) | Concentric brush consistency across production batches; PVD shade matching between Ti head and Ti button |
| Grip inlay / 握持嵌片 | LSR | Two-shot injection molding (ABS substrate → LSR overmold) | None (self-bonding, no primer needed) | 60-75 sec/shot (total, both shots) | ≥92% | LSR flash at parting line; color matching between LSR and ABS body (different material bases → different color perception) |
| Control button / 控制按钮 | Ti Grade 5 | CNC turning, diamond-cut chamfer (0.3mm, 45°) | PVD coating to match head (V1, V3) or uncoated (V2) | 60-90 sec/part | ≥90% | Chamfer consistency; button-to-head Ti shade must match under all light sources (metamerism risk with PVD) |
| LED halo / LED光环 | PMMA | Injection molding, polished cavity | Laser etching (micro-dot array) | 30-40 sec/shot + 5 sec laser per part | ≥98% | Dot pattern registration around ring circumference; light diffusion uniformity |
| Charging base / 充电底座 | Zn alloy (Zamak 3) | Die casting | PVD coating + silicone pad insert (adhesive-backed) | 15-20 sec/shot (die cast) + 20 min batch (PVD) | ≥93% (casting), ≥95% (PVD) | Die casting porosity affecting PVD finish; silicone pad adhesive longevity |

### 4.2 Texture & Surface Specification / 纹理与表面规格

*Reference Standards: Mold-Tech (MT-xxxxx) for injection molding, SPI (A-1 ~ D-3) for mold polish, Ra for objective roughness.*

| Zone / 区域 | Texture Standard / 纹理标准 | Reference Code / 参考编号 | Depth / 纹理深度 (μm) | Draft Angle Req. / 拔模要求 | Ra / 粗糙度Ra (μm) | Rz (μm) | Gloss @ 60° / 光泽度 | Tactile descriptor / 触感描述 |
|---|---|---|---|---|---|---|---|---|
| Body (V1, V3) / 机身 | SPI Polish | SPI A-2 (mirror finish on cavity) | N/A (polished) | ≥1° | ≤0.05 | ≤0.3 | 85-90 GU | Glass-smooth, cool, ceramic-like |
| Body (V2) / 机身 | SPI Polish | SPI A-2 + semi-gloss topcoat | N/A | ≥1° | ≤0.05 | ≤0.3 | 60-70 GU | Smooth with subtle depth, jade-like |
| Grip inlay / 握持 | Mold-Tech | MT-11010 (fine velvet / 细绒面) | 25-35 | ≥3° (LSR self-releasing) | 0.8-1.2 | 5-8 | 2-4 GU | Velvet matte, warm, anti-slip, compressible |
| Treatment head / 护理头 | Circular Brushing | #320 grit brush, concentric pattern | ~5 (brush groove depth) | N/A (CNC, no draft) | 0.3-0.5 | 2-3 | 15-25 GU (uncoated), 10-20 GU (PVD) | Fine directional grain, cool, precision |
| Button chamfer / 按钮倒角 | Diamond-cut + polish | 0.3mm chamfer at 45°, mirror finish | N/A | N/A | ≤0.05 | ≤0.3 | >90 GU (chamfer) | Faceted gleam, tactile edge for blind operation |
| Charging base alloy / 底座合金 | Linear Brushing | #220 grit, linear direction | ~8 (brush groove depth) | N/A | 0.4-0.6 | 3-4 | 20-30 GU | Linear grain, weighty, cool |
| Charging base pad / 底座硅胶 | Mold-Tech | MT-11020 (fine matte / 细哑面) | 20-30 | ≥3° | 1.0-1.5 | 6-10 | 2-4 GU | Soft matte, non-slip, damped docking sound |

### 4.3 Durability & Testing Requirements / 耐久与测试要求

| Test Item / 测试项目 | Standard / 测试标准 | Requirement / 要求 | Affected Zones / 涉及区域 | Notes / 备注 |
|---|---|---|---|---|
| Biocompatibility / 生物相容性 | ISO 10993-5 (Cytotoxicity) | No cytotoxic effect | Treatment head, body, grip | Mandatory for skin-contact medical/beauty device. All skin-contact materials must pass. |
| Biocompatibility / 生物相容性 | ISO 10993-10 (Skin Irritation) | No skin irritation after 24hr contact | Treatment head, grip, body | Critical — prolonged skin contact (10-15 min per session) |
| Abrasion / 耐磨 | Taber CS-10, 500g load | ≤5 GU change after 500 cycles | Body (UV hardcoat), grip (LSR) | Body scratch resistance for vanity display life; grip wear from repeated hand contact |
| UV Stability / 紫外老化 | QUV accelerated weathering | 500 hrs, ΔE ≤ 2.0 | Body (all variants), silicone (V2 most sensitive) | Bathroom/vanity exposure to indirect sunlight; V2 jade green most color-sensitive |
| Chemical Resistance / 耐化学 | Custom: common skincare ingredients | No visible change after 1hr contact with: ethanol 70%, squalane, hyaluronic acid serum, sunscreen (SPF50), makeup foundation | Body, grip, base | Real-world vanity environment — product will contact skincare residues |
| Adhesion / 附着力 | ISO 2409 Cross-hatch | Class 0 (no detachment) | Body UV hardcoat, PVD on Ti button, PVD on base | PVD adhesion on Ti is generally excellent; UV hardcoat on ABS is the primary risk zone |
| Impact / 跌落 | IEC 60068-2-31 | 1.0m drop onto hardwood floor, 3 axes, no functional damage, minor cosmetic acceptable | Entire device | Bathroom/vanity drop — tile floor contact. ABS body designed to survive; Ti head must not deform |
| Scratch Resistance / 耐刮擦 | Pencil Hardness (ISO 15184) | ≥2H (body), ≥4H (Ti head PVD) | Body (UV hardcoat), Ti head | Body must survive vanity storage with other objects; Ti head must resist treatment product contact |
| Salt Spray / 盐雾 | ISO 9227 | 48 hrs, no pitting on Ti or Zn alloy | Ti head (V1, V3 PVD), base alloy | For Japan/coastal China markets with high humidity |
| LED Halo Durability / LED环耐久 | Custom | 10,000 on/off cycles, no yellowing or brightness drop | PMMA halo | Long-term reliability of the defining visual feature |

### 4.4 Mass Production Cost Breakdown / 量产成本分解

*(设计假设 — Based on typical tier-2 Chinese manufacturing costs at 50-100K annual volume)*

| Zone / 区域 | Material Cost / 材料成本 (¥/unit) | Process Cost / 加工成本 (¥/unit) | Finishing Cost / 表面处理 (¥/unit) | Assembly / 装配 (¥/unit) | Subtotal / 小计 (¥/unit) | % of CMF BOM |
|---|---|---|---|---|---|---|
| Body handle / 机身 | 8.50 (Medical ABS) | 5.00 (Injection) | 6.00 (UV hardcoat spray + cure) | — | 19.50 | 17.7% |
| Treatment head / 护理头 | 18.00 (Ti Grade 5 billet) | 12.00 (CNC turning) | 8.00 (Brushing + PVD/nano-coat) | — | 38.00 | 34.5% |
| Grip inlay (×2 sides) / 握持 | 4.00 (LSR material) | 8.00 (Two-shot overmolding) | — | — | 12.00 | 10.9% |
| Control button / 按钮 | 3.00 (Ti Grade 5) | 4.00 (CNC + diamond-cut) | 3.00 (PVD or uncoated) | — | 10.00 | 9.1% |
| LED halo / LED环 | 2.00 (PMMA) | 2.50 (Injection) | 3.00 (Laser etching) | — | 7.50 | 6.8% |
| Charging base / 底座 | 6.50 (Zamak 3 + silicone) | 4.00 (Die casting) | 5.00 (PVD + pad assembly) | — | 15.50 | 14.1% |
| Assembly & QC / 组装质检 | — | — | — | 7.50 (Manual assembly + visual QC) | 7.50 | 6.8% |
| **TOTAL / 合计** | **42.00** | **35.50** | **25.00** | **7.50** | **¥110.00** | **100%** |

**BOM vs. Target / 物料成本 vs. 目标:** ¥110.00 calculated vs. ≤ ¥120.00 target — **On target, ¥10.00 margin.** The treatment head is the dominant cost (34.5% of CMF BOM), reflecting its role as the user's primary quality perception point. Cost savings on the LED halo and charging base offset the Ti head investment.

### 4.5 Sustainability Assessment / 可持续性评估

| Dimension / 维度 | Status / 状态 | Details / 详情 |
|---|---|---|
| Recycled Content / 回收含量 | Partial — not on body | Zinc alloy base: 30% post-industrial recycled Zamak. ABS body: virgin medical-grade required (ISO 10993 prohibits PCR for skin-contact medical). |
| Bio-based Materials / 生物基材料 | N/A | No suitable bio-based medical-grade polymer available at required volume/price. Monitor PHA/PLA medical-grade developments. |
| Recyclability / 可回收性 | Moderate | Ti head and Zn alloy base are infinitely recyclable. ABS body is technically recyclable but medical-grade stream contamination limits practice. LSR grip is thermoset (not recyclable) — design should allow grip removal for material separation. |
| Packaging / 包装 | FSC-certified paper box, zero plastic | Molded pulp insert (bagasse/sugarcane fiber), soy-based ink printing, magnetic closure (reusable box as vanity storage). |
| Carbon Footprint / 碳足迹 | Moderate (estimate) | Ti Grade 5 has high embodied energy (≈200 MJ/kg for billet) but device lifetime of 5+ years and repairability (replaceable treatment head) offset initial impact vs. disposable beauty products. |
| Repairability / 可维修性 | Designed for service | Treatment head: mechanically fastened (not glued), replaceable by service center. Battery: accessible for recycling at end-of-life. |

---

## PHASE 5: DELIVERABLES / 产出清单

### 5.1 AI Image Generation Prompts / AI生图提示词

#### Phase 1 — Research & Inspiration (研究阶段)

**Trend Mood Board — Derma-Luxury:**
```
CMF trend mood board for luxury beauty device design, editorial layout,
top row: skincare texture details — frosted serum bottle, cream jar with soft-touch lid,
jade roller on white marble, brushed titanium surgical tool;
middle row: color swatches — pearl white, warm rose gold, dusty rose, champagne, soft jade green;
bottom row: material plaques — ceramic-gloss medical ABS, brushed titanium concentric,
velvet matte liquid silicone, frosted PMMA with micro-dot pattern;
clean white background, gallery museum lighting, color-calibrated, 8K --ar 16:9
```

**Competitor CMF Comparison Grid:**
```
Product photography grid, 4 premium RF beauty devices on white background,
left to right: Yaman Bloom (white/silver, clinical), Tripollar Stop (dark gray/gold, premium),
Foreo UFO (mint silicone, playful), NuFace Trinity (white/silver, clean),
identical top-down angle, consistent 5000K studio lighting,
each device on a labeled pedestal, catalog-style product comparison, 8K --ar 16:9
```

#### Phase 2 — Concept Exploration (方案探索)

**3-Scheme Comparison Render:**
```
Three identical RF beauty device forms in different CMF schemes, side by side,
left: Scheme A Clinical Purity — all-white body, bright silver Ti head, no color accents,
center: Scheme B Derma-Luxury — pearl white body, warm rose gold Ti head, dusty rose grip,
right: Scheme C Jewelry Object — mirror-polished Ti body, 18K gold PVD throughout,
same 3/4 angle, same 5000K studio lighting, same lens (85mm), white background,
photorealistic product comparison for internal design review, 8K --ar 16:9
```

#### Phase 3 — Final CMF (最终方案)

**Hero Render — V1 Pearl Rose:**
```
Photorealistic product rendering of a premium RF facial beauty device,
elegant handheld ergonomic form, pearl white high-gloss medical-grade ABS body with ceramic-like depth,
warm rose gold titanium treatment head with brushed concentric circle pattern (#320 grit, visible grain),
dusty rose velvet matte liquid silicone grip inlay (LSR, Shore A 45-50, Mold-Tech MT-11010 texture),
warm white illuminated LED halo ring (2700K, laser-etched micro-dot PMMA diffuser),
matching warm titanium control button with diamond-cut chamfer edge (0.3mm),
placed on white marble surface next to luxury serum bottle and jade roller,
soft glam lighting (key + fill + rim), shallow depth of field on background,
beauty tech product photography, 8K commercial quality --ar 4:3
```

**Hero Render — V2 Jade Calm:**
```
RF facial beauty device, soft jade green semi-gloss medical ABS body (Pantone 13-6110),
bright silver titanium treatment head with brushed concentric pattern,
matcha green velvet matte LSR grip (Pantone 14-0216),
cool white LED halo (4000K), silver titanium diamond-cut button,
placed on natural stone surface with bamboo tray and botanical skincare products,
fresh calm morning lighting, soft shadows, spa-like atmosphere, 8K --ar 4:3
```

**Hero Render — V3 Midnight Serum:**
```
RF beauty device, deep indigo blue high-gloss medical ABS body (Pantone 19-3926),
dark gray PVD-coated titanium treatment head with radial brushed pattern,
dark navy velvet matte LSR grip (Pantone 19-4019),
warm amber LED halo (2200K) casting moody glow,
dark chrome PVD zinc alloy charging base,
on black marble surface, dramatic moody lighting with warm golden highlights,
luxury beauty tech, cinematic product photography, 8K --ar 4:3
```

**3-Color Comparison (V1/V2/V3):**
```
Three identical Lumina RF facial devices in a line on white marble,
left: Pearl Rose (pearl white + rose gold Ti + dusty rose grip),
center: Jade Calm (soft jade green + silver Ti + matcha grip),
right: Midnight Serum (deep indigo + dark gray PVD Ti + navy grip),
same shooting angle (front 3/4), consistent 5000K studio lighting with soft fill,
clean minimal product photography, 8K --ar 16:9
```

#### Phase 4 — Technical Documentation (技术文档)

**Texture Specification Board — V1 Pearl Rose:**
```
CMF specification swatch board for beauty device, technical presentation layout,
top row: material sample plaques at 1:1 scale —
pearl white medical ABS (SPI A-2, 85-90 GU), warm titanium (brushed #320, Ra 0.3-0.5μm),
dusty rose LSR (MT-11010, Ra 0.8-1.2μm, 2-4 GU), warm champagne Zn alloy (brushed #220, PVD);
bottom row: texture plaques with callouts — Mold-Tech MT-11010 label on LSR,
SPI A-2 and Ra value on ABS, #320 grit and Ra value on Ti;
each swatch labeled with Pantone code, CIELAB values, gloss unit reading,
white background, even studio lighting, color-calibrated, 8K --ar 3:2
```

**Exploded Material View:**
```
Exploded view diagram of RF beauty device showing material composition,
6 components floating in assembly order:
charging base (Zn alloy + silicone pad) at bottom,
body handle (medical ABS, cutaway showing wall thickness) center,
grip inlays (LSR, shown detached from body) left/right,
treatment head (Ti Grade 5, showing concentric brush pattern) top,
control button (Ti, with diamond-cut chamfer detail callout) side,
LED halo ring (frosted PMMA) between body and head,
each component color-coded by material family with legend,
clean technical illustration style, white background, 8K --ar 3:2
```

### 5.2 Render Shot List / 渲染镜头清单

| # | Shot / 镜头描述 | Type / 类型 | Phase / 对应阶段 |
|---|---|---|---|
| 1 | Trend mood board — Derma-Luxury skincare textures + materials | Moodboard | Phase 1 |
| 2 | Competitor CMF comparison grid (Yaman, Tripollar, Foreo, NuFace) | Research | Phase 1 |
| 3 | 3-scheme comparison render (A: Clinical, B: Derma-Luxury, C: Jewelry) | Exploration | Phase 2 |
| 4 | Hero front 3/4 — V1 Pearl Rose on white marble with skincare | Hero | Phase 3 |
| 5 | Hero front 3/4 — V2 Jade Calm on stone with botanical skincare | Hero | Phase 3 |
| 6 | Hero front 3/4 — V3 Midnight Serum on black marble, dramatic lighting | Hero | Phase 3 |
| 7 | 3-variant color comparison lineup (same angle, consistent lighting) | Comparison | Phase 3 |
| 8 | Material transition detail: high-gloss ABS body → velvet LSR grip | Transition | Phase 3 |
| 9 | Titanium treatment head macro — concentric brush pattern, #320 grain visible | Material | Phase 4 |
| 10 | LSR silicone grip macro — MT-11010 velvet texture, Shore A 45-50 depth | Material | Phase 4 |
| 11 | CMF swatch board (all materials + color swatches + texture plaques, V1) | Spec | Phase 4 |
| 12 | LED halo glow detail — warm white 2700K, micro-dot PMMA diffuser, hidden-when-off | Detail | Phase 3 |
| 13 | Charging base detail — warm champagne PVD on Zn alloy + matte silicone dock | Detail | Phase 3 |
| 14 | In-hand usage — V1 held by user, index finger on grip, warm LED on | Context | Phase 3 |
| 15 | Exploded material view — 6 components, material-coded, technical style | Info | Phase 4 |
| 16 | Packaging & unboxing — FSC box, molded sugarcane pulp insert, device nestled | Context | Phase 4 |

---

## APPENDIX: CMF SPECIFICATION SHEET / 附录：CMF规格书

*For full production-grade documentation, see `02_Assets/CMF_Spec_Template.md`. This appendix provides per-variant quick-reference spec summaries.*

### V1 Pearl Rose — Quick Spec / 快速规格

| | Body / 机身 | Treatment Head / 护理头 | Grip / 握持 | Button / 按钮 | LED Halo / 光环 | Base / 底座 |
|---|---|---|---|---|---|---|
| **Material / 材料** | Medical ABS | Ti-6Al-4V | LSR | Ti-6Al-4V | PMMA | Zamak 3 + Silicone |
| **Grade / 等级** | ISO 10993-5/-10 | ASTM B348, ISO 5832-3 | Wacker LR 3003, ISO 10993 | ASTM B348 | Evonik Acrylite | ZnAl4 |
| **Pantone** | 11-0601 TCX | — | 14-1312 TCX | — | — | 15-1218 TCX |
| **CIELAB** | L*=95, a*=0, b*=2 | L*=68, a*=3, b*=8 | L*=75, a*=12, b*=5 | L*=68, a*=3, b*=8 | L*=88, a*=1, b*=3 (2700K on) | L*=70, a*=5, b*=18 |
| **ΔE Tolerance** | ±1.0 | ±1.5 | ±1.5 | ±1.0 | ±2.0 | ±1.5 |
| **Finish / 处理** | High-gloss + UV hardcoat | Brushed concentric + warm PVD | Velvet matte overmold | Diamond-cut chamfer + PVD | Laser-etched micro-dot | PVD + matte silicone pad |
| **Texture Ref / 纹理** | SPI A-2 | #320 circular brush | MT-11010 | SPI A-2 (chamfer) | Dot 0.05mm, pitch 0.1mm | #220 brush / MT-11020 |
| **Ra (μm)** | ≤0.05 | 0.3-0.5 | 0.8-1.2 | ≤0.05 (chamfer) | — | 0.4-0.6 / 1.0-1.5 |
| **Gloss @ 60°** | 85-90 GU | 15-25 GU | 2-4 GU | >90 GU (chamfer) | 50-60 GU | 20-30 / 2-4 GU |
| **Hardness / 硬度** | 2H (pencil) | 350 HV (Ti Grade 5) | Shore A 45-50 | 350 HV | — | 100 HV (Zamak) |
| **Supplier / 供应商** | [TBD — China, ISO 13485] | [TBD — China, ISO 13485] | [TBD — LSR specialist] | [TBD — Ti CNC shop] | [TBD — PMMA optics] | [TBD — die casting + PVD] |

### V2 Jade Calm — Quick Spec / 快速规格

| | Body / 机身 | Treatment Head / 护理头 | Grip / 握持 | Button / 按钮 | LED Halo / 光环 | Base / 底座 |
|---|---|---|---|---|---|---|
| **Material / 材料** | Medical ABS | Ti-6Al-4V | LSR | Ti-6Al-4V | PMMA | Zamak 3 + Silicone |
| **Grade / 等级** | ISO 10993-5/-10 | ASTM B348, ISO 5832-3 | Wacker LR 3003, ISO 10993 | ASTM B348 | Evonik Acrylite | ZnAl4 |
| **Pantone** | 13-6110 TCX | — | 14-0216 TCX | — | — | 14-4201 TCX |
| **CIELAB** | L*=82, a*=-8, b*=3 | L*=72, a*=1, b*=2 | L*=70, a*=-10, b*=15 | L*=72, a*=1, b*=2 | L*=88, a*=0, b*=0 (4000K on) | L*=78, a*=1, b*=0 |
| **ΔE Tolerance** | ±1.0 | ±1.5 | ±1.5 | ±1.0 | ±2.0 | ±1.5 |
| **Finish / 处理** | Semi-gloss + ceramic topcoat | Brushed concentric, uncoated | Velvet matte overmold | Diamond-cut chamfer, uncoated | Laser-etched micro-dot | Brushed alloy + matte silicone |
| **Texture Ref / 纹理** | SPI A-2 | #320 circular brush | MT-11010 | SPI A-2 (chamfer) | Dot 0.05mm, pitch 0.1mm | #220 brush / MT-11020 |
| **Ra (μm)** | ≤0.05 | 0.3-0.5 | 0.8-1.2 | ≤0.05 (chamfer) | — | 0.4-0.6 / 1.0-1.5 |
| **Gloss @ 60°** | 60-70 GU | 20-30 GU | 2-4 GU | >90 GU (chamfer) | 50-60 GU | 20-30 / 2-4 GU |
| **Hardness / 硬度** | 2H (pencil) | 350 HV | Shore A 45-50 | 350 HV | — | 100 HV |

### V3 Midnight Serum — Quick Spec / 快速规格

| | Body / 机身 | Treatment Head / 护理头 | Grip / 握持 | Button / 按钮 | LED Halo / 光环 | Base / 底座 |
|---|---|---|---|---|---|---|
| **Material / 材料** | Medical ABS | Ti-6Al-4V + PVD | LSR | Ti-6Al-4V + PVD | PMMA | Zamak 3 + PVD + Silicone |
| **Grade / 等级** | ISO 10993-5/-10 | ASTM B348, ISO 5832-3 | Wacker LR 3003, ISO 10993 | ASTM B348 | Evonik Acrylite | ZnAl4 |
| **Pantone** | 19-3926 TCX | — | 19-4019 TCX | — | — | 19-4008 TCX |
| **CIELAB** | L*=25, a*=5, b*=-20 | L*=45, a*=1, b*=-1 | L*=28, a*=2, b*=-12 | L*=45, a*=1, b*=-1 | L*=85, a*=8, b*=30 (2200K on) | L*=32, a*=1, b*=-2 |
| **ΔE Tolerance** | ±1.0 | ±1.5 | ±1.5 | ±1.0 | ±2.0 | ±1.5 |
| **Finish / 处理** | High-gloss + UV hardcoat | Radial brushed + dark gray PVD | Velvet matte overmold | Diamond-cut chamfer + dark PVD | Laser-etched micro-dot | Dark chrome PVD + matte silicone |
| **Texture Ref / 纹理** | SPI A-2 | #320 radial brush | MT-11010 | SPI A-2 (chamfer) | Dot 0.05mm, pitch 0.1mm | #220 brush / MT-11020 |
| **Ra (μm)** | ≤0.05 | 0.3-0.5 | 0.8-1.2 | ≤0.05 (chamfer) | — | 0.4-0.6 / 1.0-1.5 |
| **Gloss @ 60°** | 85-90 GU | 10-20 GU | 2-4 GU | >90 GU (chamfer) | 50-60 GU | 10-15 / 2-4 GU |
| **Hardness / 硬度** | 2H (pencil) | 350 HV + PVD hardness | Shore A 45-50 | 350 HV + PVD hardness | — | 100 HV + PVD hardness |

---

*Document generated with reference to: CMF_Crash_Course.md (color science, STEEP framework, Mold-Tech/SPI standards, material-process knowledge), CMF_Spec_Template.md (production spec structure, color harmony panel), AI_Image_Generation_Guide.md (prompt engineering for CMF visualization). Business data (pricing, BOM, volumes) marked as 设计假设 — estimated based on competitive benchmarking of Tripollar Stop Vx (¥2,688), Yaman Bloom (¥2,999), NuFace Trinity ($339).*
*本文档参考内置知识库生成。商业数据基于竞品对标估算，标注为设计假设。*
