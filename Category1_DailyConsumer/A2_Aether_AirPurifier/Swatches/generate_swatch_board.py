#!/usr/bin/env python3
"""A2 Aether CMF Swatch Board — Material Lexicon philosophy"""

from PIL import Image, ImageDraw, ImageFont
import math, os

# ── Canvas ──────────────────────────────────────────
W, H = 2560, 1440  # 16:9 at high res
img = Image.new('RGB', (W, H), '#FAFAF7')  # warm paper white
draw = ImageDraw.Draw(img)

# ── Fonts ───────────────────────────────────────────
FONT_DIR = os.path.expanduser('~/.claude/skills/canvas-design/canvas-fonts')
try:
    young = ImageFont.truetype(f'{FONT_DIR}/YoungSerif-Regular.ttf', 42)
    young_sm = ImageFont.truetype(f'{FONT_DIR}/YoungSerif-Regular.ttf', 28)
    work = ImageFont.truetype(f'{FONT_DIR}/WorkSans-Regular.ttf', 20)
    work_bold = ImageFont.truetype(f'{FONT_DIR}/WorkSans-Bold.ttf', 20)
    work_sm = ImageFont.truetype(f'{FONT_DIR}/WorkSans-Regular.ttf', 16)
    work_xs = ImageFont.truetype(f'{FONT_DIR}/WorkSans-Regular.ttf', 14)
    crimson = ImageFont.truetype(f'{FONT_DIR}/CrimsonPro-Regular.ttf', 32)
    crimson_bold = ImageFont.truetype(f'{FONT_DIR}/CrimsonPro-Bold.ttf', 28)
except:
    young = young_sm = work = work_bold = work_sm = work_xs = crimson = crimson_bold = ImageFont.load_default()

# Chinese fonts
zh_title = ImageFont.truetype('/System/Library/Fonts/STHeiti Medium.ttc', 32)
zh_label = ImageFont.truetype('/System/Library/Fonts/STHeiti Medium.ttc', 18)
zh_sm = ImageFont.truetype('/System/Library/Fonts/STHeiti Light.ttc', 16)
zh_xs = ImageFont.truetype('/System/Library/Fonts/STHeiti Light.ttc', 14)

# ── Colors ──────────────────────────────────────────
BG = '#FAFAF7'
RULE = '#D4D0C8'
TEXT_DARK = '#2B2B28'
TEXT_MID = '#6B6B65'
TEXT_LIGHT = '#9B9B95'

# ── Helper functions ────────────────────────────────

def draw_circle(cx, cy, r, fill=None, outline=None, width=1):
    """Draw a perfect circle"""
    x0, y0 = cx - r, cy - r
    x1, y1 = cx + r, cy + r
    draw.ellipse([x0, y0, x1, y1], fill=fill, outline=outline, width=width)

def draw_circle_with_gloss(cx, cy, r, base_color, gloss_intensity=0.10):
    """Draw a circle with subtle matte highlight (wood composite style)"""
    draw_circle(cx, cy, r, base_color)
    for i in range(r, 0, -1):
        alpha = gloss_intensity * (1 - i / r) ** 2.5
        if alpha < 0.005:
            break
        color = blend_colors(base_color, '#FFFFFF', alpha)
        draw_circle(cx, cy - r//5, i, color)

def draw_felt_rect(x, y, w, h, color):
    """Draw a fabric-textured rectangle for acoustic felt"""
    draw.rectangle([x, y, x+w, y+h], fill=color, outline=None)
    import random
    random.seed(42)
    # Heathered effect — subtle multi-color flecks
    for _ in range(int(w * h * 0.02)):
        px = x + random.randint(2, w-2)
        py = y + random.randint(2, h-2)
        # Mix between lighter and darker flecks
        alpha = random.uniform(0.02, 0.08)
        shift = random.choice(['#FFFFFF', '#000000', blend_colors(color, '#D4C8B8', 0.3)])
        dot_color = blend_colors(color, shift, alpha)
        draw.point((px, py), fill=dot_color)

def draw_wood_rect(x, y, w, h, color):
    """Draw a wood-textured rectangle for bamboo/walnut/cork base"""
    draw.rectangle([x, y, x+w, y+h], fill=color)
    import random
    random.seed(99)
    # Subtle grain lines
    for ly in range(y + 3, y + h - 3, 3):
        alpha = 0.05 * (0.4 + 0.6 * math.sin(ly * 0.15 + random.uniform(-0.5, 0.5)))
        line_color = blend_colors(color, '#3D2E1F', alpha)
        draw.line([(x + 3, ly), (x + w - 3, ly)], fill=line_color, width=1)

def draw_ceramic_rect(x, y, w, h, color):
    """Draw a smooth ceramic rectangle (matte glaze)"""
    draw.rectangle([x, y, x+w, y+h], fill=color)
    # Subtle specular edge highlight (glazed ceramic rim)
    highlight = blend_colors(color, '#FFFFFF', 0.08)
    draw.line([(x + 4, y + 2), (x + w - 4, y + 2)], fill=highlight, width=1)

def blend_colors(c1, c2, factor):
    """Blend two hex colors by factor (0 = c1, 1 = c2)"""
    r1, g1, b1 = int(c1[1:3], 16), int(c1[3:5], 16), int(c1[5:7], 16)
    r2, g2, b2 = int(c2[1:3], 16), int(c2[3:5], 16), int(c2[5:7], 16)
    r = int(r1 + (r2 - r1) * factor)
    g = int(g1 + (g2 - g1) * factor)
    b = int(b1 + (b2 - b1) * factor)
    return f'#{r:02x}{g:02x}{b:02x}'

def text_bbox(draw, text, font):
    """Get text bounding box"""
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[0], bbox[1], bbox[2] - bbox[0], bbox[3] - bbox[1]

def draw_text_c(x, y, text, font, fill=TEXT_DARK):
    """Draw text centered at x, y"""
    _, _, tw, th = text_bbox(draw, text, font)
    draw.text((x - tw/2, y - th/2), text, font=font, fill=fill)

def draw_text_l(x, y, text, font, fill=TEXT_DARK):
    """Draw text left-aligned at x, y"""
    draw.text((x, y), text, font=font, fill=fill)

# ── Layout calculation ──────────────────────────────
TOP_MARGIN = 80
HEADER_Y = TOP_MARGIN
TITLE_Y = HEADER_Y + 10
SUBTITLE_Y = TITLE_Y + 52
RULE_Y = SUBTITLE_Y + 38

COL_W = 740
COL_GAP = 40
COL_START_X = (W - (3 * COL_W + 2 * COL_GAP)) // 2
COL_CENTER_X = [COL_START_X + COL_W//2 + i*(COL_W + COL_GAP) for i in range(3)]

CONTENT_START_Y = RULE_Y + 50

# Column layout — 5 material zones
VARIANT_Y = CONTENT_START_Y
CIRCLE_BODY_Y = VARIANT_Y + 60
CIRCLE_BODY_R = 95

RECT_FELT_Y = CIRCLE_BODY_Y + 140
RECT_FELT_H = 65
RECT_FELT_W = 250

RECT_BASE_Y = RECT_FELT_Y + 130
RECT_BASE_H = 50
RECT_BASE_W = 250

RECT_CERAMIC_Y = RECT_BASE_Y + 115
RECT_CERAMIC_H = 40
RECT_CERAMIC_W = 180

# ── Data — Three Variants ──────────────────────────

variants = [
    {
        'id': 'V1', 'name_en': 'Warm Oak', 'name_zh': '暖橡木',
        'body_color': '#B8A089', 'body_pantone': '15-1215 TCX', 'body_lab': 'L*=68, a*=6, b*=18',
        'body_mat': 'ABS + Wood Fiber', 'body_mat_zh': 'ABS+木纤复合', 'body_finish': 'Fine Matte, MT-11020', 'body_gloss': '3–5 GU', 'body_ra': 'Ra 1.2–1.8μm',
        'felt_color': '#C0B7A8', 'felt_pantone': '14-1107 TCX', 'felt_lab': 'L*=72, a*=3, b*=8',
        'felt_mat': 'rPET Acoustic Felt', 'felt_mat_zh': '再生PET声学毡', 'felt_finish': 'Needle-Punched, 400g/m²',
        'base_color': '#B8956C', 'base_pantone': '16-1333 TCX', 'base_lab': 'L*=63, a*=10, b*=28',
        'base_mat': 'Bamboo Composite', 'base_mat_zh': '竹复合材料', 'base_finish': 'Open-Pore, Fine Sanded',
        'ceramic_color': '#EDE8E0', 'ceramic_pantone': '11-0601 TCX', 'ceramic_lab': 'L*=91, a*=1, b*=4',
        'ceramic_mat': 'ZrO₂ Ceramic', 'ceramic_mat_zh': '氧化锆陶瓷', 'ceramic_finish': 'PIM + Matte Glaze', 'ceramic_ra': 'Ra 0.8–1.2μm',
        'led_temp': '2700K Warm Amber', 'led_temp_zh': '2700K 暖琥珀',
        'accent': '#B8A089',  # warm oak
    },
    {
        'id': 'V2', 'name_en': 'Slate Mist', 'name_zh': '薄雾灰',
        'body_color': '#8A8682', 'body_pantone': '16-3802 TCX', 'body_lab': 'L*=52, a*=2, b*=3',
        'body_mat': 'ABS + Stone Powder', 'body_mat_zh': 'ABS+石粉复合', 'body_finish': 'Micro-Textured, MT-11030', 'body_gloss': '2–4 GU', 'body_ra': 'Ra 1.5–2.2μm',
        'felt_color': '#4A4848', 'felt_pantone': '19-3909 TCX', 'felt_lab': 'L*=28, a*=2, b*=0',
        'felt_mat': 'rPET Acoustic Felt', 'felt_mat_zh': '再生PET声学毡', 'felt_finish': 'Needle-Punched, 400g/m²',
        'base_color': '#5C4A40', 'base_pantone': '19-1213 TCX', 'base_lab': 'L*=32, a*=8, b*=12',
        'base_mat': 'FSC Walnut Veneer', 'base_mat_zh': 'FSC胡桃木贴皮', 'base_finish': 'Open-Pore, 240 Grit',
        'ceramic_color': '#4D4E50', 'ceramic_pantone': '19-3911 TCX', 'ceramic_lab': 'L*=30, a*=1, b*=-1',
        'ceramic_mat': 'ZrO₂ Ceramic', 'ceramic_mat_zh': '氧化锆陶瓷', 'ceramic_finish': 'PIM + Matte Glaze', 'ceramic_ra': 'Ra 0.8–1.2μm',
        'led_temp': '2700K Warm Amber', 'led_temp_zh': '2700K 暖琥珀',
        'accent': '#6B6560',  # muted slate
    },
    {
        'id': 'V3', 'name_en': 'Nordic Moss', 'name_zh': '北欧苔绿',
        'body_color': '#9EAB8C', 'body_pantone': '15-6315 TCX', 'body_lab': 'L*=65, a*=-8, b*=12',
        'body_mat': 'Bio-PP + Wood Fiber', 'body_mat_zh': '生物基PP+木纤', 'body_finish': 'Fine Matte, MT-11020', 'body_gloss': '3–5 GU', 'body_ra': 'Ra 1.2–1.8μm',
        'felt_color': '#9A9478', 'felt_pantone': '16-0613 TCX', 'felt_lab': 'L*=60, a*=-4, b*=15',
        'felt_mat': 'Wool Blend Felt', 'felt_mat_zh': '羊毛混纺毡', 'felt_finish': 'Needle-Punched, 380g/m²',
        'base_color': '#A8886B', 'base_pantone': '15-1214 TCX', 'base_lab': 'L*=58, a*=8, b*=22',
        'base_mat': 'Cork Composite', 'base_mat_zh': '软木复合材料', 'base_finish': 'Raw Cork, Uncoated',
        'ceramic_color': '#E4DDCA', 'ceramic_pantone': '12-0601 TCX', 'ceramic_lab': 'L*=89, a*=2, b*=10',
        'ceramic_mat': 'ZrO₂ Ceramic', 'ceramic_mat_zh': '氧化锆陶瓷', 'ceramic_finish': 'PIM + Matte Glaze', 'ceramic_ra': 'Ra 0.8–1.2μm',
        'led_temp': '3000K Soft White', 'led_temp_zh': '3000K 柔白',
        'accent': '#8FAF9A',  # muted sage
    }
]

# ── Draw ────────────────────────────────────────────

# Rule line
draw.line([(COL_START_X, RULE_Y), (COL_START_X + 3*COL_W + 2*COL_GAP, RULE_Y)], fill=RULE, width=2)

# Title
draw_text_l(COL_START_X, TITLE_Y, 'AETHER', young, TEXT_DARK)
draw_text_l(COL_START_X + 220, TITLE_Y + 4, '— CMF Strategy', crimson, TEXT_MID)
draw_text_l(COL_START_X + 520, TITLE_Y + 8, 'CMF策略', zh_title, TEXT_MID)

# Subtitle
draw_text_l(COL_START_X, SUBTITLE_Y, 'Natural Home', crimson, TEXT_MID)
draw_text_l(COL_START_X + 220, SUBTITLE_Y + 2, '/ 自然家居', zh_label, TEXT_LIGHT)

# Column rule lines (subtle)
for i in range(2):
    rx = COL_START_X + (i+1)*COL_W + i*COL_GAP + COL_GAP//2
    draw.line([(rx, RULE_Y + 20), (rx, H - TOP_MARGIN - 30)], fill=RULE, width=1)

# Draw each variant column
for i, v in enumerate(variants):
    cx = COL_CENTER_X[i]
    lx = COL_START_X + i*(COL_W + COL_GAP)

    # ── Variant identifier ──
    draw_text_c(cx, VARIANT_Y, f"{v['id']} {v['name_en']}", crimson_bold, v['accent'])
    draw_text_c(cx, VARIANT_Y + 28, v['name_zh'], zh_sm, TEXT_MID)

    # ── Body color circle (large, dominant — wood-fiber composite) ──
    body_cy = CIRCLE_BODY_Y
    draw_circle_with_gloss(cx, body_cy, CIRCLE_BODY_R, v['body_color'], gloss_intensity=0.07)
    draw_circle(cx, body_cy, CIRCLE_BODY_R, outline=RULE, width=2)

    label_y = body_cy + CIRCLE_BODY_R + 18
    draw_text_c(cx, label_y, "BODY SHELL / 机身外壳", work_bold, TEXT_DARK)
    draw_text_c(cx, label_y + 22, f"{v['body_mat']} / {v['body_mat_zh']}", work_sm, TEXT_MID)
    draw_text_c(cx, label_y + 40, f"Pantone {v['body_pantone']}   {v['body_lab']}", work_xs, TEXT_LIGHT)
    draw_text_c(cx, label_y + 56, f"{v['body_finish']}   {v['body_gloss']}   {v['body_ra']}", work_xs, TEXT_LIGHT)

    # ── Felt grille rectangle ──
    felt_rect_x = cx - RECT_FELT_W//2
    draw_felt_rect(felt_rect_x, RECT_FELT_Y, RECT_FELT_W, RECT_FELT_H, v['felt_color'])
    draw.rectangle([felt_rect_x, RECT_FELT_Y, felt_rect_x+RECT_FELT_W, RECT_FELT_Y+RECT_FELT_H], outline=RULE, width=1)

    label_y = RECT_FELT_Y + RECT_FELT_H + 18
    draw_text_c(cx, label_y, "FRONT GRILLE / 前面网", work_bold, TEXT_DARK)
    draw_text_c(cx, label_y + 22, f"{v['felt_mat']} / {v['felt_mat_zh']}", work_sm, TEXT_MID)
    draw_text_c(cx, label_y + 40, f"Pantone {v['felt_pantone']}   {v['felt_lab']}", work_xs, TEXT_LIGHT)
    draw_text_c(cx, label_y + 56, f"{v['felt_finish']}", work_xs, TEXT_LIGHT)

    # ── Base ring rectangle ──
    base_rect_x = cx - RECT_BASE_W//2
    draw_wood_rect(base_rect_x, RECT_BASE_Y, RECT_BASE_W, RECT_BASE_H, v['base_color'])
    draw.rectangle([base_rect_x, RECT_BASE_Y, base_rect_x+RECT_BASE_W, RECT_BASE_Y+RECT_BASE_H], outline=RULE, width=1)

    label_y = RECT_BASE_Y + RECT_BASE_H + 18
    draw_text_c(cx, label_y, "BASE RING / 底部环", work_bold, TEXT_DARK)
    draw_text_c(cx, label_y + 22, f"{v['base_mat']} / {v['base_mat_zh']}", work_sm, TEXT_MID)
    draw_text_c(cx, label_y + 40, f"Pantone {v['base_pantone']}   {v['base_lab']}", work_xs, TEXT_LIGHT)
    draw_text_c(cx, label_y + 56, f"{v['base_finish']}", work_xs, TEXT_LIGHT)

    # ── Ceramic ring rectangle ──
    cer_rect_x = cx - RECT_CERAMIC_W//2
    draw_ceramic_rect(cer_rect_x, RECT_CERAMIC_Y, RECT_CERAMIC_W, RECT_CERAMIC_H, v['ceramic_color'])
    draw.rectangle([cer_rect_x, RECT_CERAMIC_Y, cer_rect_x+RECT_CERAMIC_W, RECT_CERAMIC_Y+RECT_CERAMIC_H], outline=RULE, width=1)

    label_y = RECT_CERAMIC_Y + RECT_CERAMIC_H + 18
    draw_text_c(cx, label_y, "CONTROL RING / 控制环", work_bold, TEXT_DARK)
    draw_text_c(cx, label_y + 22, f"{v['ceramic_mat']} / {v['ceramic_mat_zh']}", work_sm, TEXT_MID)
    draw_text_c(cx, label_y + 40, f"Pantone {v['ceramic_pantone']}   {v['ceramic_lab']}", work_xs, TEXT_LIGHT)
    draw_text_c(cx, label_y + 56, f"{v['ceramic_finish']}   {v['ceramic_ra']}", work_xs, TEXT_LIGHT)

    # ── LED indicator (small spec) ──
    led_y = RECT_CERAMIC_Y + RECT_CERAMIC_H + 78
    draw_text_c(cx, led_y, "LED DIFFUSER / 散光板", work_bold, TEXT_DARK)
    draw_text_c(cx, led_y + 22, "Frosted PMMA · Laser-Etched Micro-Dot", work_sm, TEXT_MID)
    draw_text_c(cx, led_y + 40, f"Hidden-When-Off · {v['led_temp']}", work_xs, TEXT_LIGHT)

# ── Footer ──────────────────────────────────────────
footer_y = H - 50
draw_text_c(W//2, footer_y, "A2 AETHER · CMF SPECIFICATION BOARD · PHASE 3 FINAL STRATEGY · DESIGN ASSUMPTION", work_xs, TEXT_LIGHT)

# ── Save ────────────────────────────────────────────
output_path = '/Users/wang/Desktop/CMF作品集/Category1_DailyConsumer/A2_Aether_AirPurifier/Swatches/A2_Aether_CMF_Swatch_Board.png'
img.save(output_path, 'PNG', dpi=(300, 300))
print(f'Saved: {output_path}')
print(f'Size: {W}x{H}')
