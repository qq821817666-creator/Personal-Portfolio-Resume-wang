# CMF Designer Knowledge Crash Course

> 面向具备工业设计基础的快速转化指南。核心目标：将ID思维转化为CMF思维。

---

## 1. 色彩系统：从RGB到CIELAB

### 为什么ID设计师必须升级色彩认知

| 场景 | ID常用 | CMF必须 |
|------|--------|----------|
| 屏幕预览 | RGB/Hex | 参考而已，不可用于生产 |
| 印刷品 | CMYK | Pantone专色 |
| **实物生产** | "大概这个颜色" | **CIELAB值 + 光谱数据 + ΔE容差** |

### CIELAB色彩空间

CIELAB是设备无关的色彩空间，模拟人眼感知。

```
L* = 明度（0=黑, 100=白）
a* = 红绿轴（+a=红, -a=绿）
b* = 黄蓝轴（+b=黄, -b=蓝）
```

**关键概念：ΔE（色差）**
- ΔE < 1.0 → 人眼几乎无法分辨（高端品牌标准：Apple/Dyson）
- ΔE < 2.0 → 可接受偏差（常规消费品标准）
- ΔE < 3.0 → 明显可见色差（不合格）

**实际应用：** 你给工厂说"深空灰"，工厂做出来偏蓝。你说是灰色，他说是灰色。用CIELAB：
- 目标: L=45, a=0, b=-2
- 样品: L=45, a=1, b=-5
- ΔE = √(0² + 1² + 3²) = 3.16 → 不合格，需要重新调色

### 核心色彩系统速查

| 系统 | 全称 | 应用领域 | 标识格式 |
|------|------|----------|----------|
| **Pantone PMS** | Pantone Matching System | 印刷/图形 | Pantone 18-1750 Viva Magenta |
| **Pantone TCX** | Textile Cotton eXtended | 棉质纺织品 | Pantone 19-4052 TCX |
| **Pantone TPG** | Textile Paper Grade | 纸质纺织色卡 | Pantone 19-4052 TPG |
| **NCS** | Natural Color System | 建筑/涂料（欧洲主流）| NCS S 0580-Y30R |
| **RAL** | Reichsausschuß für Lieferbedingungen | 工业涂料（德国/欧盟）| RAL 9005 Jet Black |

**CMF工作中最常用的：**
- 消费电子：Pantone PMS + CIELAB数据
- 汽车内饰：NCS + CIELAB数据
- 纺织品：Pantone TCX/TPG

---

## 2. CMF规格书（CMF Specification Document）

### 这是CMF设计师的核心交付物

一份合格的CMF规格书包含以下信息（以消费电子产品为例）：

```
┌─────────────────────────────────────────────┐
│ CMF SPECIFICATION                           │
│ Product: [产品名]  Date: [日期]              │
│ Designer: [姓名]   Rev: [版本号]             │
├─────────────────────────────────────────────┤
│ PART A: EXTERIOR HOUSING                    │
│ ├ Material: PC/ABS alloy                    │
│ ├ Color: Pantone Cool Gray 7C               │
│ │  CIELAB: L*=48, a*=1, b*=-2 (±ΔE<1.5)   │
│ ├ Finish: Soft-touch matte                  │
│ ├ Texture: MT-11020 (Mold-Tech)             │
│ ├ Gloss: 2-4 GU @ 60°                       │
│ └ Notes: UV-stabilized, anti-fingerprint    │
├─────────────────────────────────────────────┤
│ PART B: DECORATIVE TRIM                     │
│ ├ Material: Aluminum 6061                   │
│ ├ Color: Champagne Gold                     │
│ │  CIELAB: L*=78, a*=4, b*=18 (±ΔE<1.0)   │
│ ├ Finish: PVD coating, brushed pattern      │
│ ├ Texture: Hairline #220 grit               │
│ └ Notes: Edge chamfer 0.5mm, no sharp edges │
├─────────────────────────────────────────────┤
│ PART C: BUTTONS / CONTROLS                  │
│ ...                                         │
└─────────────────────────────────────────────┘
```

### 常用参考标准

| 类别 | 标准 | 用途 |
|------|------|------|
| 模具纹理 | Mold-Tech / Yick Sang | 注塑件表面纹理标准 |
| 注塑光洁度 | SPI A1-A3, B1-B3, C1-C3, D1-D3 | 模具抛光等级 |
| 光泽度 | Gloss Units (GU) @ 60° | 高光>70GU, 半哑10-30GU, 哑光<5GU |
| 附着力 | Cross-hatch test (ISO 2409) | 涂层附着力测试 |
| 耐磨性 | Taber Abrasion / Martindale | 表面磨损测试 |

---

## 3. CMF趋势方法论

### STEEP分析框架

CMF趋势不是"我觉得好看"，而是基于宏观驱动力做系统推演：

| 维度 | 英文 | CMF影响 |
|------|------|---------|
| **社会** | Social | 人口结构变化、生活方式转变 → 色彩偏好迁移 |
| **技术** | Technological | 新材料/新工艺/新技术 → 可实现的新CMF效果 |
| **经济** | Economic | 消费能力变化、成本压力 → 材料选择约束 |
| **环境** | Environmental | 可持续发展要求 → 回收材料/生物基材料 |
| **政治** | Political | 法规政策（如CBAM碳关税2026）→ 供应链合规 |

### 趋势报告结构（参考WGSN/Pantone标准）

```
1. Executive Summary（概述）
2. Macro Trends（宏观趋势 3-5个）
   - 每个趋势: 名称 + 关键词 + 代表图像 + 200字叙述
3. Color Forecast（色彩预测）
   - 5-8个关键色，每个含Pantone/CIELAB值 + 情绪关键词
4. Material Directions（材料方向）
   - 材料叙事 + 纹理参考 + 制造工艺说明
5. CMF Application Examples（应用示例）
   - 每个趋势对应1-2个产品应用
```

### 如何高效做CMF趋势研究（利用AI加速）

1. **数据收集：** Pinterest/Designboom/Dezeen/Instagram 收集100-200张图
2. **AI辅助分析：** 用Claude/ChatGPT分析图片描述文本，提取高频关键词
3. **聚类：** 手动或AI辅助将趋势聚类为3-5个方向
4. **色彩提取：** Python (k-means聚类) 或 Adobe Color 从趋势图中提取调色板
5. **叙事构建：** 为每个趋势命名 + 写设计叙事

---

## 4. CMF核心材料知识速查

### 塑料类

| 材料 | 典型CMF应用 | 关键工艺 |
|------|------------|----------|
| PC/ABS alloy | 消费电子外壳 | 注塑 + 喷涂/IMD |
| PMMA (亚克力) | 透明面板、导光件 | 注塑 + 激光蚀刻 |
| TPU/TPE | 软触握持区、密封件 | 包胶注塑（Overmolding）|
| PCR塑料 | 可持续产品外壳 | 注塑（颜色控制更难）|
| 生物基塑料 (PLA/PHA) | 环保定位产品 | 注塑/3D打印 |

### 金属类

| 材料 | 典型CMF应用 | 表面处理 |
|------|------------|----------|
| 铝合金 6061/6063 | 消费电子机身、汽车装饰件 | 阳极氧化（喷砂+氧化）、PVD镀膜 |
| 不锈钢 304/316 | 高端装饰条、表壳 | PVD镀膜、抛光、拉丝 |
| 钛合金 | 高端穿戴设备 | PVD镀膜、喷砂+阳极氧化 |
| 镁合金 | 笔记本外壳 | 微弧氧化、喷涂 |

### 纺织/软材料

| 材料 | 典型CMF应用 | 关键参数 |
|------|------------|----------|
| Alcantara / 超纤 | 汽车座椅、耳机耳罩 | 耐磨性(Martindale)、色牢度 |
| 真皮 (Nappa/Nubuck) | 高端汽车内饰 | 粒面类型、染色工艺 |
| 3D针织 | 鞋面、座椅面料 | 纱线规格、编织密度 |
| 再生聚酯(rPET) | 可持续纺织品 | 回收来源、GRS认证 |

---

## 5. CMF行业术语中英对照

| 英文 | 中文 | 说明 |
|------|------|------|
| Color, Material, Finish | 色彩、材料、表面处理 | CMF全称 |
| Mood Board | 情绪板 | CMF设计第一步 |
| CMF Strategy | CMF策略 | 为产品线/品牌制定的CMF体系 |
| CMF Specification | CMF规格书 | 给工厂的详细CMF生产要求 |
| Trend Forecasting | 趋势预测 | 预测未来2-3年的CMF方向 |
| PBR (Physically Based Rendering) | 基于物理的渲染 | KeyShot/Substance的核心技术 |
| Delta E (ΔE) | 色差 | CIELAB空间中的色彩距离 |
| Metamerism | 同色异谱 | 不同光源下颜色表现不同的现象 |
| Gloss Units (GU) | 光泽度单位 | 60°角测量 |
| In-Mold Decoration (IMD) | 模内装饰 | 注塑时一体化装饰 |
| PVD (Physical Vapor Deposition) | 物理气相沉积 | 真空镀膜工艺 |
| Anodizing | 阳极氧化 | 铝合金表面处理 |
| Soft-touch Paint | 软触漆 | 手感柔和的弹性涂层 |
| Haptic | 触感 | CMF中越来越重要的用户体验维度 |
| Sustainability / Circular Design | 可持续/循环设计 | CMF核心趋势 |
| CMF Library | CMF材料库 | 实物材料样品的分类收藏 |
| Colorway | 配色方案 | 一个产品的具体色彩组合 |

---

## 6. 学习资源清单

### 日常关注
- **Instagram:** @material.connexion, @christopherlefteri, @material_lab, @trendtablet, @pantone, @wgsn
- **网站:** designboom.com, dezeen.com, core77.com
- **展会:** Milan Design Week (4月), CES (1月), IAA Mobility (9月)

### 深入阅读
- *Materials for Design* — Chris Lefteri (CMF材料圣经)
- *The Trend Forecaster's Handbook* — Martin Raymond
- *Interaction of Color* — Josef Albers (色彩感知经典)
- Material ConneXion 数据库 (materialconnexion.com)

### AI工具（你的优势领域）
- ComfyUI + ControlNet: 可控AI纹理生成
- Adobe Substance 3D Sampler: AI图像转PBR材质
- Claude/ChatGPT: 趋势文本分析
- Python + OpenCV/scikit-image: 色彩提取与分析
