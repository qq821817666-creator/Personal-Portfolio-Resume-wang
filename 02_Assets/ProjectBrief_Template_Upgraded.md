# {Project Code}: {Project Name} — {Product Type} CMF
# {English Subtitle} | {Chinese Category}

> **Template Version:** v2.0 | 完整闭环版
> **Instructions:** 每个 `{...}` 占位符需替换为具体内容。标注 `[N/A]` 的段落表示该项目不适用，保留标题但写明原因。

---

## PHASE 0: BUSINESS CONTEXT / 商业背景

### 0.1 Brand & Market Positioning / 品牌与市场定位

{Brand description. What does this fictional brand stand for? What market tier does it occupy? Who does it compete against? 2-3 sentences.}

- **Brand Tone / 品牌调性:** {3-5 keywords}
- **Market Tier / 市场层级:** {Mass / Mass-Premium / Premium / Luxury}
- **Retail Price / 零售价区间:** ¥{XXX} – ¥{XXX} | ${XXX} – ${XXX} *(设计假设, based on competitive benchmarking)*
- **Annual Volume / 年产量:** {XX,XXX – XXX,XXX} units/year *(设计假设)*
- **Target Margin / 目标利润率:** {XX%}
- **BOM Cost Target / 物料成本目标:** ≤ ¥{XX} / unit
- **Key Markets / 主要市场:** {China, EU, North America, etc.}

### 0.2 Target User Persona / 目标用户画像

{3-4 sentences describing the archetypal user: demographics, lifestyle, values, pain points, purchase motivations, and usage context. This persona drives all subsequent CMF decisions.}

### 0.3 Business Constraints → CMF Framework / 商业约束 → CMF推导

| Constraint / 约束 | Value / 数值 | CMF Implication / CMF推导 |
|---|---|---|
| Retail Price / 零售价 | ¥{XXX-XXX} | {What material/process tier this enables} |
| BOM Budget / 物料预算 | ≤ ¥{XX}/unit | {How budget is allocated across zones} |
| Annual Volume / 年产量 | {XX}K units | {Process selection: high-volume molding vs. low-volume finishing} |
| Key Markets / 主要市场 | {Regions} | {Regulatory requirements (REACH, RoHS, GB standards), cultural color preferences} |
| Brand Position / 品牌定位 | {Tier} | {Expected finish quality, defect tolerance, CMF complexity budget} |
| User Touchpoints / 用户触点 | {High-touch zones} | {Where premium materials are justified vs. where cost-saving is acceptable} |

---

## PHASE 1: MARKET & TREND RESEARCH / 市场与趋势研究

### 1.1 Market Demand Analysis / 市场需求分析

{150-200 words. What problem does this product solve? What's the market gap? What are users frustrated with in existing products' CMF? What CMF attributes drive purchase decisions in this category? Reference specific data points and market signals.}

### 1.2 Industry CMF Trend Research / 行业CMF趋势调研

*Framework: STEEP Analysis (Social / Technological / Economic / Environmental / Political)*

**Trend 1: {Trend Name} / {趋势名}**
- **Driver / 驱动力:** {S/T/E/E/P}
- **Keywords / 关键词:** {3-5 keywords}
- **CMF Manifestation / CMF表现:** {How this trend translates into colors, materials, finishes, textures}

**Trend 2: {Trend Name} / {趋势名}**
- **Driver / 驱动力:** {S/T/E/E/P}
- **Keywords / 关键词:** {3-5 keywords}
- **CMF Manifestation / CMF表现:** {...}

**Trend 3: {Trend Name} / {趋势名}**
- **Driver / 驱动力:** {S/T/E/E/P}
- **Keywords / 关键词:** {3-5 keywords}
- **CMF Manifestation / CMF表现:** {...}

### 1.3 Competitor CMF Audit / 竞品CMF审计

| Competitor / 竞品 | Model / 型号 | Key CMF Features / 关键CMF特征 | Strengths / 优势 | Weaknesses → Our Opportunity / 劣势→我们的机会 |
|---|---|---|---|---|
| {Brand 1} | {Model} | {Materials, colors, finishes used} | {What they do well} | {What's missing — our opening} |
| {Brand 2} | {Model} | {...} | {...} | {...} |
| {Brand 3} | {Model} | {...} | {...} | {...} |

**Competitive Insight / 竞争洞察:** {1-2 sentences synthesizing the key gap/opportunity from the audit.}

### 1.4 Inspiration Board / 灵感板

**Primary Inspiration Sources / 主要灵感来源:**
- {Category}: {Specific reference, e.g., "Japanese Zen gardens — raked sand textures, moss greens, natural stone grays"}
- {Category}: {...}
- {Category}: {...}

**Visual References / 视觉参考 (to be generated/curated):**

| Ref # | Source / 来源 | Description / 描述 | CMF Extraction / CMF提取 |
|---|---|---|---|
| 1 | {Nature/Architecture/Art/Fashion} | {What it is, visual characteristics} | {Colors, textures, material cues extracted} |
| 2 | {...} | {...} | {...} |
| 3 | {...} | {...} | {...} |
| 4 | {...} | {...} | {...} |

**Color Extraction Direction / 色彩提取方向:** {Tool reference: Python cmf_color_extractor.py — k-means clustering on reference images to derive initial palette seeds.}

---

## PHASE 2: CONCEPT EXPLORATION / 方案探索

### 2.1 Design Strategy Formulation / 设计策略制定

*From Phase 1 research insights + Phase 0 business constraints, derive 3 design pillars.*

**Pillar 1: {Name} / {中文名}**
- **Principle / 原则:** {1-sentence design principle}
- **CMF Translation / CMF转化:** {How this pillar manifests in color, material, texture choices}

**Pillar 2: {Name} / {中文名}**
- **Principle / 原则:** {...}
- **CMF Translation / CMF转化:** {...}

**Pillar 3: {Name} / {中文名}**
- **Principle / 原则:** {...}
- **CMF Translation / CMF转化:** {...}

### 2.2 Multi-Scheme Generation / 多方案生成

*Three competing CMF directions, generated BEFORE narrowing to final variants.*

#### Scheme A: {Name} / {中文名}

| Dimension / 维度 | Description / 描述 |
|---|---|
| **Tagline / 一句话** | {Memorable positioning statement} |
| **Emotional Response / 情感目标** | {How the user should feel holding/using this} |
| **Primary Material / 主材质** | {Dominant material choice} |
| **Core Palette / 核心配色** | {2-3 colors with Pantone references} |
| **Key Texture/Process / 核心工艺** | {Defining surface treatment} |
| **Estimated BOM / 估算BOM** | ¥{XX}/unit |
| **Strengths / 优势** | {What this scheme does better than alternatives} |
| **Risks / 风险** | {Where this scheme might fail or face production challenges} |

#### Scheme B: {Name} / {中文名}

| Dimension / 维度 | Description / 描述 |
|---|---|
| **Tagline / 一句话** | {...} |
| **Emotional Response / 情感目标** | {...} |
| **Primary Material / 主材质** | {...} |
| **Core Palette / 核心配色** | {...} |
| **Key Texture/Process / 核心工艺** | {...} |
| **Estimated BOM / 估算BOM** | ¥{XX}/unit |
| **Strengths / 优势** | {...} |
| **Risks / 风险** | {...} |

#### Scheme C: {Name} / {中文名}

| Dimension / 维度 | Description / 描述 |
|---|---|
| **Tagline / 一句话** | {...} |
| **Emotional Response / 情感目标** | {...} |
| **Primary Material / 主材质** | {...} |
| **Core Palette / 核心配色** | {...} |
| **Key Texture/Process / 核心工艺** | {...} |
| **Estimated BOM / 估算BOM** | ¥{XX}/unit |
| **Strengths / 优势** | {...} |
| **Risks / 风险** | {...} |

### 2.3 Scheme Comparison Matrix / 方案对比矩阵

| Criterion / 评价标准 | Weight / 权重 | Scheme A / 方案A | Scheme B / 方案B | Scheme C / 方案C |
|---|---|---|---|---|
| Brand Alignment / 品牌匹配度 | 25% | ★★★★☆ | ★★★★☆ | ★★★☆☆ |
| Market Differentiation / 市场差异化 | 20% | ★★★☆☆ | ★★★★★ | ★★★★☆ |
| User Desirability / 用户吸引力 | 20% | ★★★★☆ | ★★★★★ | ★★★☆☆ |
| Production Feasibility / 量产可行性 | 20% | ★★★★★ | ★★★☆☆ | ★★★★☆ |
| Cost Control / 成本可控性 | 15% | ★★★★★ | ★★★☆☆ | ★★★☆☆ |
| **Weighted Score / 加权得分** | **100%** | **X.X** | **X.X** | **X.X** |

### 2.4 Elimination & Optimization / 淘汰与优化

**Eliminated / 淘汰:** Scheme {X} ({Name}) — {Reason for elimination, specific weakness that couldn't be resolved.}

**Partially Absorbed / 部分吸收:** {Aspects of eliminated schemes that were merged into the winner.}

**Winner / 胜出:** Scheme {Y} ({Name}) — {Why it won. Key strengths that aligned with brand and user needs.}

**Post-Selection Refinements / 定案后优化:**
- {Specific refinement 1 made to the winning scheme after selection}
- {Specific refinement 2}
- {Specific refinement 3}

---

## PHASE 3: FINAL CMF STRATEGY / 最终CMF策略

### 3.1 Core Direction / 核心方向

**{Strategy Name} / {中文策略名}**

{Expanded design philosophy paragraph — what this CMF strategy communicates, what emotions it evokes, how it differentiates the product. 2-3 sentences connecting to Phase 0 brand positioning and Phase 1 trend insights.}

### 3.2 Color Variants / 色彩方案

#### V1: {Name} / {中文名}

| Zone / 区域 | Material / 材料 | Material Grade & Supplier Ref / 材料等级 | Color / 颜色 | Pantone / NCS | CIELAB D65/10° (±ΔE Tol.) | Finish & Process / 表面处理 | Texture Spec / 纹理参数 | Gloss / 光泽度 | Haptics / 触感 | Touch Freq. / 接触频率 | Cost Tier / 成本 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| {Zone 1} | {Material} | {Grade, supplier spec} | {Color name} | {Pantone xxx} | L*={x}, a*={x}, b*={x} (±ΔE≤{x}) | {Process name} | {MT-xxxxx / VDI xx / SPI x} | {x} GU @ 60° | {Descriptor} | {High/Med/Low} | {¥/$$$} |
| {Zone 2} | {...} | {...} | {...} | {...} | {...} | {...} | {...} | {...} | {...} | {...} | {...} |

**Color Palette / 色彩面板:**

| Swatch / 色板 | Pantone | NCS (if applicable) | CIELAB (L*, a*, b*) | Hex (ref only) | Role / 角色 |
|---|---|---|---|---|---|
| {Color 1} | {Pantone xxx} | {NCS xxxx} | L*={x}, a*={x}, b*={x} | #{xxxxxx} | {Dominant / Accent / Supporting} |
| {Color 2} | {...} | {...} | {...} | {...} | {...} |

#### V2: {Name} / {中文名}

{Same table structure as V1 — every variant must have complete CIELAB values and texture specs.}

#### V3: {Name} / {中文名}

{Same table structure as V1.}

### 3.3 Color Harmony Analysis / 色彩和谐分析

| Relationship / 关系 | Zone Pair / 色区对 | ΔE | Perception / 感知效果 |
|---|---|---|---|
| {e.g., Body ↔ Accent} | {Zone A} → {Zone B} | {ΔE value} | {e.g., Strong contrast draws attention to accent} |
| {e.g., Body ↔ Grip} | {...} | {...} | {...} |

**Metamerism Note / 同色异谱说明:** {Any metamerism risks identified across D65 (daylight) vs. A (incandescent) lighting. Note if any color pairs show significant shift.}

### 3.4 Material Narrative / 材料叙事

{3-5 sentences. Poetic but technically grounded. Describe the CMF philosophy using material metaphors. Connect to brand tone, user experience, and the emotional arc of interacting with the product. Reference specific textures, temperatures, weights, and material transitions.}

---

## PHASE 4: PRODUCTION FEASIBILITY / 量产可行性

### 4.1 Process-Material Matrix / 工艺-材料矩阵

| Zone / 区域 | Material / 材料 | Primary Process / 一次工艺 | Secondary Process / 二次工艺 | Est. Cycle Time / 估算周期 | Yield Rate (target) / 良率目标 | Key Quality Risk / 关键质量风险 |
|---|---|---|---|---|---|---|
| {Zone 1} | {Material} | {e.g., Injection molding} | {e.g., UV coating, PVD} | {sec/part} | {XX%} | {Risk description} |
| {Zone 2} | {...} | {...} | {...} | {...} | {...} | {...} |

### 4.2 Texture & Surface Specification / 纹理与表面规格

*Reference Standards: Mold-Tech (MT-xxxxx) for injection molding, VDI 3400 for European automotive, SPI (A-1 ~ D-3) for mold polish, Ra/Rz for objective roughness.*

| Zone / 区域 | Texture Standard / 纹理标准 | Reference Code / 参考编号 | Depth / 纹理深度 (μm) | Draft Angle Req. / 拔模要求 | Ra / 粗糙度Ra (μm) | Rz (μm) | Gloss @ 60° / 光泽度 | Tactile descriptor / 触感描述 |
|---|---|---|---|---|---|---|---|---|
| {Zone 1} | {Mold-Tech / VDI / SPI} | {MT-xxxxx / VDI xx} | {xx} | {≥x°} | {x.x} | {x.x} | {x} GU | {e.g., Fine matte, velvety} |
| {Zone 2} | {...} | {...} | {...} | {...} | {...} | {...} | {...} | {...} |

### 4.3 Durability & Testing Requirements / 耐久与测试要求

| Test Item / 测试项目 | Standard / 测试标准 | Requirement / 要求 | Affected Zones / 涉及区域 | Notes / 备注 |
|---|---|---|---|---|
| Abrasion / 耐磨 | {Taber CS-10 / Martindale} | {cycles, wheel, load} | {Zones} | {...} |
| UV Stability / 紫外老化 | {QUV / Xenon Arc} | {hrs}, ΔE ≤ {x} | {Zones} | {...} |
| Chemical Resistance / 耐化学 | {ISO 2812 / Custom} | {Substances, duration} | {Zones} | {Sunscreen, hand cream, cleaning agents} |
| Adhesion / 附着力 | ISO 2409 (Cross-hatch) | Class {0-5} | {Zones} | {...} |
| Scratch Resistance / 耐刮擦 | {Pencil Hardness / Taber} | {H - XH} | {Zones} | {...} |
| Impact / 冲击 | {IEC 60068 / Drop test} | {Height, surface} | {Zones} | {...} |
| Salt Spray / 盐雾 | ISO 9227 | {hrs} | {Metal zones} | {For coastal/humid markets} |

### 4.4 Mass Production Cost Breakdown / 量产成本分解

| Zone / 区域 | Material Cost / 材料成本 (¥/unit) | Process Cost / 加工成本 (¥/unit) | Finishing Cost / 表面处理 (¥/unit) | Assembly / 装配 (¥/unit) | Subtotal / 小计 (¥/unit) | % of BOM |
|---|---|---|---|---|---|---|
| {Zone 1} | {x.xx} | {x.xx} | {x.xx} | {x.xx} | {x.xx} | {xx%} |
| {Zone 2} | {...} | {...} | {...} | {...} | {...} | {...} |
| **TOTAL / 合计** | | | | | **¥{xx.xx}** | **100%** |

**BOM vs. Target / 物料成本 vs. 目标:** ¥{calculated} vs. ≤ ¥{target} — {Status: On target / Over by ¥x, offset by {reason} / Under by ¥x}

### 4.5 Sustainability Assessment / 可持续性评估

| Dimension / 维度 | Status / 状态 | Details / 详情 |
|---|---|---|
| Recycled Content / 回收含量 | {XX% PCR in zone X} | {Material, certification (GRS, etc.)} |
| Bio-based Materials / 生物基材料 | {Yes/No, zones} | {Material specs} |
| Recyclability / 可回收性 | {Ease of disassembly, material separation} | {Notes} |
| Packaging / 包装 | {Approach} | {Materials, certifications} |
| Carbon Footprint / 碳足迹 | {Estimate if available} | {Comparison to baseline} |

---

## PHASE 5: DELIVERABLES / 产出清单

### 5.1 AI Image Generation Prompts / AI生图提示词

#### Phase 1 — Research & Inspiration (研究阶段)

**Trend Mood Board:**
```
{Detailed multimodal prompt for trend mood board generation, specifying:
- Visual style (editorial, swatch board, photographic)
- Key colors, textures, materials to include
- Composition and layout direction
- Technical specs: --ar, quality level}
```

#### Phase 2 — Concept Exploration (方案探索)

**3-Scheme Comparison Render:**
```
{Prompt for generating side-by-side comparison of all three schemes
in identical lighting and angle, showing their visual differentiation}
```

#### Phase 3 — Final CMF (最终方案)

{Preserved and expanded from existing project prompts — Hero renders for V1/V2/V3, material detail macros, 3-color comparison. Add explicit material/process keywords.}

#### Phase 4 — Technical Documentation (技术文档)

**Texture Specification Board:**
```
{Prompt for generating a CMF specification swatch board showing:
- Physical material samples for each zone
- Texture plaques with Mold-Tech/VDI reference callouts
- Color swatches with Pantone/CIELAB labels
- Standard CMF presentation board layout, studio lighting}
```

**Process Flow Diagram / Exploded View:**
```
{Prompt for manufacturing process visualization or exploded material view}
```

### 5.2 Render Shot List / 渲染镜头清单

| # | Shot / 镜头描述 | Type / 类型 | Phase / 对应阶段 |
|---|---|---|---|
| 1 | Trend mood board — {trend direction} | Moodboard | Phase 1 |
| 2 | Competitor CMF comparison grid | Research | Phase 1 |
| 3 | 3-scheme comparison render (same angle/lens/light) | Exploration | Phase 2 |
| 4 | Hero front 3/4 — V1 {variant name} | Hero | Phase 3 |
| 5 | Hero front 3/4 — V2 {variant name} | Hero | Phase 3 |
| 6 | Hero front 3/4 — V3 {variant name} | Hero | Phase 3 |
| 7 | 3-variant color comparison lineup | Comparison | Phase 3 |
| 8 | Material transition detail: {Zone A → Zone B} | Transition | Phase 3 |
| 9 | Texture macro — {dominant texture, e.g., brushed Ti} | Material | Phase 4 |
| 10 | Texture macro — {secondary texture, e.g., velvet silicone} | Material | Phase 4 |
| 11 | CMF swatch board (all materials + colors + texture plaques) | Spec | Phase 4 |
| 12 | Charging base / accessory detail | Detail | Phase 3 |
| 13 | In-hand usage / lifestyle context shot | Context | Phase 3 |
| 14 | Exploded material view / process diagram | Info | Phase 4 |
| 15 | Packaging & unboxing — {sustainability story} | Context | Phase 4 |

---

## APPENDIX: CMF SPECIFICATION SHEET / 附录：CMF规格书

*Refer to the full spec template at `02_Assets/CMF_Spec_Template.md` for production-grade documentation. This appendix provides per-variant summary spec sheets.*

### V1 {Name} — Quick Spec / 快速规格

| | Zone 1: {Name} | Zone 2: {Name} | Zone 3: {Name} |
|---|---|---|---|
| **Material** | | | |
| **Grade** | | | |
| **Pantone** | | | |
| **CIELAB** | | | |
| **ΔE Tolerance** | | | |
| **Finish** | | | |
| **Texture Ref** | | | |
| **Ra (μm)** | | | |
| **Gloss @ 60°** | | | |
| **Hardness** | | | |
| **Supplier** | | | |

{V2 and V3 spec sheets follow the same format.}

---

*Document generated with reference to: CMF_Crash_Course.md (color science, STEEP, material-process knowledge), CMF_Spec_Template.md (production spec structure), AI_Image_Generation_Guide.md (prompt engineering for CMF visualization).*
*本文档参考内置知识库生成：色彩科学、趋势方法论、材料工艺对照、量产规格结构。*
