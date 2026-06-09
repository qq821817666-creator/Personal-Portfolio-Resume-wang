#!/usr/bin/env python3
"""A1 Lumina CMF Swatch Board — Material Lexicon philosophy"""

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

def draw_circle_with_gloss(cx, cy, r, base_color, gloss_intensity=0.12):
    """Draw a circle with subtle gloss gradient (like a glossy body)"""
    # Base fill
    draw_circle(cx, cy, r, base_color)
    # Subtle radial highlight (simulating gloss)
    for i in range(r, 0, -1):
        alpha = gloss_intensity * (1 - i / r) ** 2
        if alpha < 0.01:
            break
        # Blend with white at decreasing intensity
        color = blend_colors(base_color, '#FFFFFF', alpha)
        draw_circle(cx, cy - r//4, i, color)

def draw_metallic_circle(cx, cy, r, base_color, highlight_pos='top-left'):
    """Draw a metallic circle with brushed sheen"""
    draw_circle(cx, cy, r, base_color)
    # Simulate brushed metallic with a subtle gradient overlay
    # Lighter band across the circle (simulated brushed metallic sheen)
    band_cy = int(cy - r//3) if highlight_pos == 'top-left' else int(cy)
    for dy in range(-int(r)//3, int(r)//3, 1):
        ratio = abs(dy) / (r/3)
        if ratio >= 1.0:
            continue
        alpha = float(0.08 * (1.0 - ratio) ** 1.5)
        if alpha < 0.01:
            continue
        color = blend_colors(base_color, '#FFFFFF', alpha)
        y = int(band_cy + dy)
        half_w_sq = r**2 - (y - cy)**2
        if half_w_sq <= 0:
            continue
        half_w = math.sqrt(half_w_sq)
        draw.ellipse([cx - half_w, y-2, cx + half_w, y+2], fill=color)

def draw_velvet_rect(x, y, w, h, color):
    """Draw a velvet-textured rectangle for silicone"""
    draw.rectangle([x, y, x+w, y+h], fill=color, outline=None)
    # Add subtle noise-like dots for velvet texture
    import random
    random.seed(42)
    for _ in range(int(w * h * 0.015)):
        px = x + random.randint(2, w-2)
        py = y + random.randint(2, h-2)
        alpha = random.uniform(0.03, 0.10)
        dot_color = blend_colors(color, '#FFFFFF' if random.random() > 0.5 else '#000000', alpha)
        draw.point((px, py), fill=dot_color)

def draw_metallic_rect(x, y, w, h, color):
    """Draw a metallic rectangle with brushed grain"""
    draw.rectangle([x, y, x+w, y+h], fill=color)
    # Horizontal brushed lines
    for ly in range(y + 3, y + h - 3, 2):
        alpha = 0.06 * (0.5 + 0.5 * math.sin(ly * 0.3))
        line_color = blend_colors(color, '#FFFFFF', alpha)
        draw.line([(x + 3, ly), (x + w - 3, ly)], fill=line_color, width=1)

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

# Column layout
VARIANT_Y = CONTENT_START_Y
CIRCLE_BODY_Y = VARIANT_Y + 60
CIRCLE_BODY_R = 100

CIRCLE_TI_Y = CIRCLE_BODY_Y + 150
CIRCLE_TI_R = 65

RECT_SILICONE_Y = CIRCLE_TI_Y + 110
RECT_SILICONE_H = 70
RECT_SILICONE_W = 260

RECT_BASE_Y = RECT_SILICONE_Y + 140
RECT_BASE_H = 50
RECT_BASE_W = 260

# ── Data — Three Variants ──────────────────────────

variants = [
    {
        'id': 'V1', 'name_en': 'Pearl Rose', 'name_zh': '珍珠玫瑰',
        'body_color': '#F5F0EB', 'body_pantone': '11-0601 TCX', 'body_lab': 'L*=95, a*=0, b*=2',
        'body_mat': 'Medical ABS', 'body_mat_zh': '医疗级ABS', 'body_finish': 'High-Gloss + UV Hardcoat', 'body_gloss': '85–90 GU',
        'ti_color': '#B8A390', 'ti_lab': 'L*=68, a*=3, b*=8',
        'ti_finish': 'Brushed #320 Concentric', 'ti_ra': 'Ra 0.3–0.5μm',
        'sil_color': '#C9AFA0', 'sil_pantone': '14-1312 TCX', 'sil_lab': 'L*=75, a*=12, b*=5',
        'sil_mat': 'LSR', 'sil_mat_zh': '液态硅胶', 'sil_finish': 'Velvet Matte MT-11010', 'sil_gloss': '2–4 GU', 'sil_shore': 'Shore A 45–50',
        'base_color': '#C4A882', 'base_pantone': '15-1218 TCX', 'base_lab': 'L*=70, a*=5, b*=18',
        'base_mat': 'Zn Alloy + Silicone Pad', 'base_mat_zh': '锌合金+硅胶垫', 'base_finish': 'PVD Brushed #220',
        'accent': '#D4A99A',  # warm rose
    },
    {
        'id': 'V2', 'name_en': 'Jade Calm', 'name_zh': '玉石静谧',
        'body_color': '#C5D5C8', 'body_pantone': '13-6110 TCX', 'body_lab': 'L*=82, a*=-8, b*=3',
        'body_mat': 'Medical ABS', 'body_mat_zh': '医疗级ABS', 'body_finish': 'Semi-Gloss Ceramic Topcoat', 'body_gloss': '60–70 GU',
        'ti_color': '#B8B5B0', 'ti_lab': 'L*=72, a*=1, b*=2',
        'ti_finish': 'Brushed #320 Concentric (Native Oxide)', 'ti_ra': 'Ra 0.3–0.5μm',
        'sil_color': '#A8B58A', 'sil_pantone': '14-0216 TCX', 'sil_lab': 'L*=70, a*=-10, b*=15',
        'sil_mat': 'LSR', 'sil_mat_zh': '液态硅胶', 'sil_finish': 'Velvet Matte MT-11010', 'sil_gloss': '2–4 GU', 'sil_shore': 'Shore A 45–50',
        'base_color': '#C5C5C5', 'base_pantone': '14-4201 TCX', 'base_lab': 'L*=78, a*=1, b*=0',
        'base_mat': 'Zn Alloy + Silicone Pad', 'base_mat_zh': '锌合金+硅胶垫', 'base_finish': 'Brushed #220 Uncoated',
        'accent': '#8FAF9A',  # muted jade
    },
    {
        'id': 'V3', 'name_en': 'Midnight Serum', 'name_zh': '深夜精华',
        'body_color': '#2D2D4B', 'body_pantone': '19-3926 TCX', 'body_lab': 'L*=25, a*=5, b*=-20',
        'body_mat': 'Medical ABS', 'body_mat_zh': '医疗级ABS', 'body_finish': 'High-Gloss + UV Hardcoat', 'body_gloss': '85–90 GU',
        'ti_color': '#737272', 'ti_lab': 'L*=45, a*=1, b*=-1',
        'ti_finish': 'Radial Brush #320 + Dark Gray PVD', 'ti_ra': 'Ra 0.3–0.5μm',
        'sil_color': '#3D4260', 'sil_pantone': '19-4019 TCX', 'sil_lab': 'L*=28, a*=2, b*=-12',
        'sil_mat': 'LSR', 'sil_mat_zh': '液态硅胶', 'sil_finish': 'Velvet Matte MT-11010', 'sil_gloss': '2–4 GU', 'sil_shore': 'Shore A 45–50',
        'base_color': '#504F50', 'base_pantone': '19-4008 TCX', 'base_lab': 'L*=32, a*=1, b*=-2',
        'base_mat': 'Zn Alloy + Silicone Pad', 'base_mat_zh': '锌合金+硅胶垫', 'base_finish': 'Dark PVD Brushed #220',
        'accent': '#5A5A8A',  # deep indigo accent
    }
]

# ── Draw ────────────────────────────────────────────

# Rule line
draw.line([(COL_START_X, RULE_Y), (COL_START_X + 3*COL_W + 2*COL_GAP, RULE_Y)], fill=RULE, width=2)

# Title
draw_text_l(COL_START_X, TITLE_Y, 'LUMINA', young, TEXT_DARK)
draw_text_l(COL_START_X + 210, TITLE_Y + 4, '— CMF Strategy', crimson, TEXT_MID)
draw_text_l(COL_START_X + 510, TITLE_Y + 8, 'CMF策略', zh_title, TEXT_MID)

# Subtitle
draw_text_l(COL_START_X, SUBTITLE_Y, 'Derma-Luxury', crimson, TEXT_MID)
draw_text_l(COL_START_X + 200, SUBTITLE_Y + 2, '/ 肌肤奢华', zh_label, TEXT_LIGHT)

# Column rule lines (subtle)
for i in range(2):
    rx = COL_START_X + (i+1)*COL_W + i*COL_GAP + COL_GAP//2
    draw.line([(rx, RULE_Y + 20), (rx, H - TOP_MARGIN - 30)], fill=RULE, width=1)

# Draw each variant column
for i, v in enumerate(variants):
    cx = COL_CENTER_X[i]
    lx = COL_START_X + i*(COL_W + COL_GAP)  # left edge of column

    # ── Variant identifier ──
    draw_text_c(cx, VARIANT_Y, f"{v['id']} {v['name_en']}", crimson_bold, v['accent'])
    draw_text_c(cx, VARIANT_Y + 28, v['name_zh'], zh_sm, TEXT_MID)

    # ── Body color circle (large, dominant) ──
    body_cy = CIRCLE_BODY_Y
    draw_circle_with_gloss(cx, body_cy, CIRCLE_BODY_R, v['body_color'])
    draw_circle(cx, body_cy, CIRCLE_BODY_R, outline=RULE, width=2)

    # Body label
    label_y = body_cy + CIRCLE_BODY_R + 18
    draw_text_c(cx, label_y, "BODY / 机身主体", work_bold, TEXT_DARK)
    draw_text_c(cx, label_y + 22, f"{v['body_mat']} / {v['body_mat_zh']}", work_sm, TEXT_MID)
    draw_text_c(cx, label_y + 40, f"Pantone {v['body_pantone']}   {v['body_lab']}", work_xs, TEXT_LIGHT)
    draw_text_c(cx, label_y + 56, f"{v['body_finish']}   {v['body_gloss']}", work_xs, TEXT_LIGHT)

    # ── Titanium circle (medium) ──
    ti_cy = CIRCLE_TI_Y
    draw_metallic_circle(cx, ti_cy, CIRCLE_TI_R, v['ti_color'])
    draw_circle(cx, ti_cy, CIRCLE_TI_R, outline=RULE, width=2)

    label_y = ti_cy + CIRCLE_TI_R + 18
    draw_text_c(cx, label_y, "TREATMENT HEAD / 护理头", work_bold, TEXT_DARK)
    draw_text_c(cx, label_y + 22, f"Ti Grade 5 (Ti-6Al-4V)", work_sm, TEXT_MID)
    draw_text_c(cx, label_y + 40, f"CIELAB {v['ti_lab']}", work_xs, TEXT_LIGHT)
    draw_text_c(cx, label_y + 56, f"{v['ti_finish']}   {v['ti_ra']}", work_xs, TEXT_LIGHT)

    # ── Silicone grip rectangle ──
    sil_rect_x = cx - RECT_SILICONE_W//2
    draw_velvet_rect(sil_rect_x, RECT_SILICONE_Y, RECT_SILICONE_W, RECT_SILICONE_H, v['sil_color'])
    draw.rectangle([sil_rect_x, RECT_SILICONE_Y, sil_rect_x+RECT_SILICONE_W, RECT_SILICONE_Y+RECT_SILICONE_H], outline=RULE, width=1)

    label_y = RECT_SILICONE_Y + RECT_SILICONE_H + 18
    draw_text_c(cx, label_y, "GRIP INLAY / 握持嵌片", work_bold, TEXT_DARK)
    draw_text_c(cx, label_y + 22, f"{v['sil_mat']} / {v['sil_mat_zh']}", work_sm, TEXT_MID)
    draw_text_c(cx, label_y + 40, f"Pantone {v['sil_pantone']}   {v['sil_lab']}", work_xs, TEXT_LIGHT)
    draw_text_c(cx, label_y + 56, f"{v['sil_finish']}   {v['sil_gloss']}   {v['sil_shore']}", work_xs, TEXT_LIGHT)

    # ── Base metal rectangle ──
    base_rect_x = cx - RECT_BASE_W//2
    draw_metallic_rect(base_rect_x, RECT_BASE_Y, RECT_BASE_W, RECT_BASE_H, v['base_color'])
    draw.rectangle([base_rect_x, RECT_BASE_Y, base_rect_x+RECT_BASE_W, RECT_BASE_Y+RECT_BASE_H], outline=RULE, width=1)

    label_y = RECT_BASE_Y + RECT_BASE_H + 18
    draw_text_c(cx, label_y, "CHARGING BASE / 充电底座", work_bold, TEXT_DARK)
    draw_text_c(cx, label_y + 22, f"{v['base_mat']} / {v['base_mat_zh']}", work_sm, TEXT_MID)
    draw_text_c(cx, label_y + 40, f"Pantone {v['base_pantone']}   {v['base_lab']}", work_xs, TEXT_LIGHT)
    draw_text_c(cx, label_y + 56, f"{v['base_finish']}", work_xs, TEXT_LIGHT)

# ── Footer ──────────────────────────────────────────
footer_y = H - 50
draw_text_c(W//2, footer_y, "A1 LUMINA · CMF SPECIFICATION BOARD · PHASE 3 FINAL STRATEGY · DESIGN ASSUMPTION", work_xs, TEXT_LIGHT)

# ── Save ────────────────────────────────────────────
output_path = '/Users/wang/Desktop/CMF作品集/Category1_DailyConsumer/A1_Lumina_BeautyDevice/Swatches/A1_Lumina_CMF_Swatch_Board.png'
img.save(output_path, 'PNG', dpi=(300, 300))
print(f'Saved: {output_path}')
print(f'Size: {W}x{H}')
