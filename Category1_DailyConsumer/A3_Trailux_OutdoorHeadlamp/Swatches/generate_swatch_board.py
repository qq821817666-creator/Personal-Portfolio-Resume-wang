#!/usr/bin/env python3
"""A3 Trailux CMF Swatch Board — Alpine Geology Material Lexicon"""

from PIL import Image, ImageDraw, ImageFont
import math, os

# ── Canvas ──────────────────────────────────────────
W, H = 2400, 1600
BG = '#2B2B28'

img = Image.new('RGB', (W, H), BG)
draw = ImageDraw.Draw(img)

# ── Fonts ───────────────────────────────────────────
FONT_DIR = os.path.expanduser('~/.claude/skills/canvas-design/canvas-fonts')
try:
    young = ImageFont.truetype(f'{FONT_DIR}/YoungSerif-Regular.ttf', 38)
    crimson = ImageFont.truetype(f'{FONT_DIR}/CrimsonPro-Regular.ttf', 30)
    crimson_bold = ImageFont.truetype(f'{FONT_DIR}/CrimsonPro-Bold.ttf', 26)
    work = ImageFont.truetype(f'{FONT_DIR}/WorkSans-Regular.ttf', 18)
    work_bold = ImageFont.truetype(f'{FONT_DIR}/WorkSans-Bold.ttf', 18)
    work_sm = ImageFont.truetype(f'{FONT_DIR}/WorkSans-Regular.ttf', 15)
    work_xs = ImageFont.truetype(f'{FONT_DIR}/WorkSans-Regular.ttf', 13)
except:
    young = crimson = crimson_bold = work = work_bold = work_sm = work_xs = ImageFont.load_default()

zh_title = ImageFont.truetype('/System/Library/Fonts/STHeiti Medium.ttc', 28)
zh_label = ImageFont.truetype('/System/Library/Fonts/STHeiti Medium.ttc', 17)
zh_sm = ImageFont.truetype('/System/Library/Fonts/STHeiti Light.ttc', 15)
zh_xs = ImageFont.truetype('/System/Library/Fonts/STHeiti Light.ttc', 13)

TEXT_WHITE = '#E8E4DC'
TEXT_MID = '#A09890'
TEXT_DIM = '#706860'
ACCENT_ORANGE = '#E06030'

# ── Helpers ─────────────────────────────────────────
def draw_circle(cx, cy, r, fill=None, outline=None, width=1):
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=fill, outline=outline, width=width)

def draw_rect(x, y, w, h, fill):
    draw.rectangle([x, y, x+w, y+h], fill=fill)

def blend(c1, c2, f):
    r1, g1, b1 = int(c1[1:3],16), int(c1[3:5],16), int(c1[5:7],16)
    r2, g2, b2 = int(c2[1:3],16), int(c2[3:5],16), int(c2[5:7],16)
    return f'#{int(r1+(r2-r1)*f):02x}{int(g1+(g2-g1)*f):02x}{int(b1+(b2-b1)*f):02x}'

def text_c(x, y, text, font, fill=TEXT_WHITE):
    b = draw.textbbox((0,0), text, font=font)
    tw, th = b[2]-b[0], b[3]-b[1]
    draw.text((x-tw/2, y-th/2), text, font=font, fill=fill)

def text_l(x, y, text, font, fill=TEXT_WHITE):
    draw.text((x, y), text, font=font, fill=fill)

def stone_circle(cx, cy, r, color):
    """Draw a stone-textured circle"""
    import random
    random.seed(42)
    draw_circle(cx, cy, r, color)
    for _ in range(int(r*r*0.04)):
        px = cx + random.randint(-r+3, r-3)
        py = cy + random.randint(-r+3, r-3)
        dist = math.sqrt((px-cx)**2 + (py-cy)**2)
        if dist < r-2:
            shift = random.choice(['#FFFFFF', blend(color, '#000000', 0.5)])
            dot_color = blend(color, shift, random.uniform(0.02, 0.06))
            draw.point((px, py), fill=dot_color)

def metal_circle(cx, cy, r, color):
    """Draw a metallic ring-like circle"""
    draw_circle(cx, cy, r, color)
    draw_circle(cx, cy, r-3, outline=blend(color, '#FFFFFF', 0.15), width=2)

# ── Layout ──────────────────────────────────────────
COLS = 3
COL_W = 700
COL_GAP = 60
START_X = (W - (COLS * COL_W + (COLS-1) * COL_GAP)) // 2
COL_CX = [START_X + COL_W//2 + i*(COL_W + COL_GAP) for i in range(COLS)]

TOP_Y = 90
TITLE_Y = TOP_Y
RULE_Y = TITLE_Y + 55
CONTENT_Y = RULE_Y + 60

# ── Title ───────────────────────────────────────────
text_l(START_X, TITLE_Y, 'TRAILUX', young, TEXT_WHITE)
text_l(START_X + 240, TITLE_Y + 6, '— CMF Strategy', crimson, TEXT_MID)
text_l(START_X + 530, TITLE_Y + 10, 'CMF策略', zh_title, TEXT_MID)

text_l(START_X, RULE_Y - 25, 'Bio-Rugged / 生物机能', crimson, ACCENT_ORANGE)
text_l(START_X + 330, RULE_Y - 23, 'Alpine Geology Material Lexicon', work_sm, TEXT_MID)

# Rule line
RULE_COLOR = '#504840'
draw.line([(START_X, RULE_Y), (START_X + COLS*COL_W + (COLS-1)*COL_GAP, RULE_Y)], fill=RULE_COLOR, width=2)

# Column rules
for i in range(1, COLS):
    rx = START_X + i*COL_W + (i-1)*COL_GAP + COL_GAP//2
    draw.line([(rx, RULE_Y+20), (rx, H-100)], fill=RULE_COLOR, width=1)

# ── Variant Data ────────────────────────────────────
variants = [
    {
        'id': 'V1', 'name_en': 'Alpine Granite', 'name_zh': '高山花岗岩',
        'body_color': '#57585A', 'body_pantone': '18-4005 TCX', 'body_lab': 'L*=35 a*=1 b*=-2',
        'body_mat': 'PC/ABS', 'body_finish': 'MT-11030 Stone Texture', 'body_gloss': '2–3 GU',
        'ring_color': '#8A8C8B', 'ring_pantone': '16-3850 TCX', 'ring_lab': 'L*=55 a*=2 b*=-1',
        'ring_mat': 'Al 6061-T6', 'ring_finish': 'Clear Anodize + Laser-Etch', 'ring_gloss': '8–12 GU',
        'btn_color': '#E06030', 'btn_pantone': '16-1362 TCX', 'btn_lab': 'L*=48 a*=35 b*=55',
        'btn_mat': 'LSR Silicone', 'btn_finish': 'Matte Dome · 5% Glow Pigment',
        'band_color': '#6B6860', 'band_pantone': '17-1502 TCX', 'band_lab': 'L*=42 a*=3 b*=1',
        'band_mat': 'rPET Elastic Jacquard', 'band_finish': 'Orange Fleck + Reflective Tracer',
    },
    {
        'id': 'V2', 'name_en': 'Alpine Moss', 'name_zh': '高山苔藓',
        'body_color': '#3D4F3A', 'body_pantone': '18-0322 TCX', 'body_lab': 'L*=32 a*=-8 b*=12',
        'body_mat': 'Bio-PA (60% Castor)', 'body_finish': 'VDI 24 Sandblast Matte', 'body_gloss': '2–3 GU',
        'ring_color': '#B8A888', 'ring_pantone': '14-1110 TCX', 'ring_lab': 'L*=68 a*=4 b*=15',
        'ring_mat': 'Recycled Al 6061', 'ring_finish': 'Clear Anodize + Laser-Etch', 'ring_gloss': '10–15 GU',
        'btn_color': '#F5C800', 'btn_pantone': '13-0858 TCX', 'btn_lab': 'L*=72 a*=8 b*=85',
        'btn_mat': 'LSR Silicone', 'btn_finish': 'Matte Dome · Standard Pigment',
        'band_color': '#3A3F34', 'band_pantone': '19-0415 TCX', 'band_lab': 'L*=28 a*=-4 b*=6',
        'band_mat': 'rPET Elastic Jacquard', 'band_finish': 'Yellow Tracer + Reflective',
    },
    {
        'id': 'V3', 'name_en': 'Glacial Ice', 'name_zh': '冰川冰蓝',
        'body_color': '#A5ABB4', 'body_pantone': '14-4203 TCX', 'body_lab': 'L*=68 a*=-4 b*=-8',
        'body_mat': 'PC/ABS Soft-Touch', 'body_finish': 'MT-11010 Velvet Matte', 'body_gloss': '1.5–2.5 GU',
        'ring_color': '#C4C7CA', 'ring_pantone': '14-4002 TCX', 'ring_lab': 'L*=78 a*=0 b*=-2',
        'ring_mat': 'Al 6061-T6', 'ring_finish': 'Brushed #220 + Clear Anodize', 'ring_gloss': '15–20 GU',
        'btn_color': '#2DAAB5', 'btn_pantone': '15-4722 TCX', 'btn_lab': 'L*=58 a*=-18 b*=-22',
        'btn_mat': 'LSR Silicone', 'btn_finish': 'Matte Dome · 8% Glow Pigment',
        'band_color': '#A5ABB4', 'band_pantone': '14-4203 TCX', 'band_lab': 'L*=68 a*=-4 b*=-8',
        'band_mat': 'rPET Elastic Jacquard', 'band_finish': 'White Geometric + Reflective',
    },
]

# ── Draw Variants ───────────────────────────────────
for i, v in enumerate(variants):
    cx = COL_CX[i]
    lx = START_X + i*(COL_W + COL_GAP)

    # Variant header
    text_c(cx, CONTENT_Y, f"{v['id']} — {v['name_en']}", crimson_bold, ACCENT_ORANGE)
    text_c(cx, CONTENT_Y + 28, v['name_zh'], zh_label, TEXT_MID)

    cur_y = CONTENT_Y + 70

    # BODY — stone texture circle
    stone_circle(cx, cur_y + 65, 85, v['body_color'])
    text_c(cx, cur_y + 65, 'BODY', work_bold, TEXT_WHITE)
    text_c(cx, cur_y + 160, 'HOUSING / 外壳主体', work_bold, TEXT_WHITE)
    text_c(cx, cur_y + 182, f"{v['body_mat']}", work_sm, TEXT_MID)
    text_c(cx, cur_y + 202, f"Pantone {v['body_pantone']}  {v['body_lab']}", work_xs, TEXT_DIM)
    text_c(cx, cur_y + 220, f"{v['body_finish']}  {v['body_gloss']}", work_xs, TEXT_DIM)

    # LENS RING — metal ring
    ring_y = cur_y + 270
    metal_circle(cx, ring_y + 40, 60, v['ring_color'])
    text_c(cx, ring_y + 40, 'RING', work_bold, blend(v['ring_color'], '#000000', 0.3))
    text_c(cx, ring_y + 110, 'LENS RING / 镜头环', work_bold, TEXT_WHITE)
    text_c(cx, ring_y + 132, f"{v['ring_mat']}", work_sm, TEXT_MID)
    text_c(cx, ring_y + 152, f"Pantone {v['ring_pantone']}  {v['ring_lab']}", work_xs, TEXT_DIM)
    text_c(cx, ring_y + 170, f"{v['ring_finish']}  {v['ring_gloss']}", work_xs, TEXT_DIM)

    # BUTTON — small circle
    btn_y = ring_y + 210
    draw.ellipse([cx-22, btn_y+20, cx+22, btn_y+64], fill=v['btn_color'])
    text_c(cx, btn_y + 95, 'BUTTON / 按钮', work_bold, TEXT_WHITE)
    text_c(cx, btn_y + 117, f"{v['btn_mat']}", work_sm, TEXT_MID)
    text_c(cx, btn_y + 137, f"Pantone {v['btn_pantone']}  {v['btn_lab']}", work_xs, TEXT_DIM)
    text_c(cx, btn_y + 155, f"{v['btn_finish']}", work_xs, TEXT_DIM)

    # HEADBAND — rectangular swatch
    band_y = btn_y + 190
    draw.rectangle([cx-140, band_y, cx+140, band_y+36], fill=v['band_color'], outline=RULE_COLOR, width=1)
    text_c(cx, band_y + 65, 'HEADBAND / 头带', work_bold, TEXT_WHITE)
    text_c(cx, band_y + 87, f"{v['band_mat']}", work_sm, TEXT_MID)
    text_c(cx, band_y + 107, f"Pantone {v['band_pantone']}  {v['band_lab']}", work_xs, TEXT_DIM)
    text_c(cx, band_y + 125, f"{v['band_finish']}", work_xs, TEXT_DIM)

# ── Footer ──────────────────────────────────────────
text_c(W//2, H-55, 'A3 TRAILUX · CMF SPECIFICATION BOARD · PHASE 3 FINAL STRATEGY · ALL DATA = DESIGN ASSUMPTIONS', work_xs, TEXT_DIM)

output = '/Users/wang/Desktop/CMF作品集/Category1_DailyConsumer/A3_Trailux_OutdoorHeadlamp/Swatches/A3_Trailux_CMF_Swatch_Board.png'
img.save(output, 'PNG', dpi=(300, 300))
print(f'Saved: {output}')
print(f'Size: {W}x{H}')
