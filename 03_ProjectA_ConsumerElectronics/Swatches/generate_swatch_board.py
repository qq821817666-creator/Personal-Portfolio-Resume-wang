#!/usr/bin/env python3
"""ProjectA AURA CMF Swatch Board — Warm Prism Material Lexicon"""

from PIL import Image, ImageDraw, ImageFont
import math, os

W, H = 2560, 1440
BG = '#1C1C1A'
img = Image.new('RGB', (W, H), BG)
draw = ImageDraw.Draw(img)

FONT_DIR = os.path.expanduser('~/.claude/skills/canvas-design/canvas-fonts')
try:
    young = ImageFont.truetype(f'{FONT_DIR}/YoungSerif-Regular.ttf', 38)
    crimson = ImageFont.truetype(f'{FONT_DIR}/CrimsonPro-Regular.ttf', 28)
    crimson_bold = ImageFont.truetype(f'{FONT_DIR}/CrimsonPro-Bold.ttf', 24)
    work = ImageFont.truetype(f'{FONT_DIR}/WorkSans-Regular.ttf', 17)
    work_bold = ImageFont.truetype(f'{FONT_DIR}/WorkSans-Bold.ttf', 17)
    work_sm = ImageFont.truetype(f'{FONT_DIR}/WorkSans-Regular.ttf', 14)
    work_xs = ImageFont.truetype(f'{FONT_DIR}/WorkSans-Regular.ttf', 12)
except:
    young = crimson = crimson_bold = work = work_bold = work_sm = work_xs = ImageFont.load_default()

zh_title = ImageFont.truetype('/System/Library/Fonts/STHeiti Medium.ttc', 26)
zh_label = ImageFont.truetype('/System/Library/Fonts/STHeiti Medium.ttc', 16)
zh_sm = ImageFont.truetype('/System/Library/Fonts/STHeiti Light.ttc', 14)
zh_xs = ImageFont.truetype('/System/Library/Fonts/STHeiti Light.ttc', 12)

WHITE = '#E8E4DC'
MID = '#A09890'
DIM = '#706860'
ACCENT = '#C48058'

def draw_circle(cx, cy, r, fill=None, outline=None, width=1):
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=fill, outline=outline, width=width)

def blend(c1, c2, f):
    r1,g1,b1 = int(c1[1:3],16), int(c1[3:5],16), int(c1[5:7],16)
    r2,g2,b2 = int(c2[1:3],16), int(c2[3:5],16), int(c2[5:7],16)
    return f'#{int(r1+(r2-r1)*f):02x}{int(g1+(g2-g1)*f):02x}{int(b1+(b2-b1)*f):02x}'

def text_c(x, y, text, font, fill=WHITE):
    b = draw.textbbox((0,0), text, font=font)
    draw.text((x-(b[2]-b[0])/2, y-(b[3]-b[1])/2), text, font=font, fill=fill)

def text_l(x, y, text, font, fill=WHITE):
    draw.text((x, y), text, font=font, fill=fill)

def gradient_rect(x, y, w, h, top_color, bottom_color):
    """Draw a vertical gradient rectangle"""
    for i in range(h):
        f = i / h
        c = blend(top_color, bottom_color, f)
        draw.line([(x, y+i), (x+w, y+i)], fill=c)

COLS = 3
COL_W = 760
COL_GAP = 50
START_X = (W - (COLS*COL_W + (COLS-1)*COL_GAP))//2
COL_CX = [START_X + COL_W//2 + i*(COL_W+COL_GAP) for i in range(COLS)]

TOP_Y, TITLE_Y, RULE_Y = 80, 80, 135
CONTENT_Y = RULE_Y + 50

text_l(START_X, TITLE_Y, 'AURA', young, WHITE)
text_l(START_X+190, TITLE_Y+6, '— CMF Strategy', crimson, MID)
text_l(START_X+470, TITLE_Y+10, 'CMF策略', zh_title, MID)
text_l(START_X, RULE_Y-25, 'Warm Prism / 暖棱镜', crimson, ACCENT)
RULE = '#504840'
draw.line([(START_X, RULE_Y), (START_X+COLS*COL_W+(COLS-1)*COL_GAP, RULE_Y)], fill=RULE, width=2)
for i in range(1, COLS):
    rx = START_X + i*COL_W + (i-1)*COL_GAP + COL_GAP//2
    draw.line([(rx, RULE_Y+20), (rx, H-90)], fill=RULE, width=1)

variants = [
    {
        'id':'V1','en':'Desert Dawn','zh':'沙漠黎明',
        'body':'#B8A898','body_p':'13-1014 TCX','body_l':'L*=70 a*=5 b*=15','body_m':'PC/ABS Soft-Touch','body_f':'MT-11010 · 3-5 GU',
        'arm':'#C48058','arm_p':'Copper PVD','arm_l':'L*=55 a*=18 b*=28','arm_m':'Al 6061','arm_f':'Sandblast #180 + PVD · 12-18 GU',
        'cush':'#A06040','cush_p':'17-1340 TCX','cush_l':'L*=45 a*=18 b*=25','cush_m':'Bio-PU Vegan Leather','cush_f':'Fine Grain · Micro-Perf · 2-4 GU',
        'mesh':'#D5CEC4','mesh_p':'12-1006 TCX','mesh_l':'L*=82 a*=3 b*=8','mesh_m':'Knit Textile','mesh_f':'Acoustic Transparent · 0.8mm Pitch',
        'band':'#B0A898','band_p':'15-1305 TCX','band_l':'L*=65 a*=3 b*=8','band_m':'Knit Textile (rPET)','band_f':'Heather Yarn · Silicone Cushion',
        'accent': ACCENT, 'top':None, 'btm':None,
    },
    {
        'id':'V2','en':'Midnight Prism','zh':'午夜棱镜', 'hero':True,
        'body':'#1C2D3D','body2':'#2D6058','body_p':'19-4027→17-5024','body_l':'L*=22→35 gradient','body_m':'Al 6061 Gradient Anodize','body_f':'Brush #320 + Gradient Dye · 15-25 GU',
        'arm':'#6A6B6C','arm_p':'Dark Chrome PVD','arm_l':'L*=42 a*=1 b*=-2','arm_m':'SS 316L','arm_f':'Micro-Blast + Dark PVD · 10-15 GU',
        'cush':'#1C2D3D','cush_p':'19-4027 TCX','cush_l':'L*=22 a*=2 b*=-12','cush_m':'Bio-PU Vegan Leather','cush_f':'Fine Grain · Micro-Perf · 2-4 GU',
        'mesh':'#1C2D3D','mesh_p':'19-4027 (+shimmer)','mesh_l':'L*=22 (dynamic)','mesh_m':'Microfiber + Iridescent','mesh_f':'Teal Shimmer Thread · Subtle',
        'band':'#1C2D3D','band_p':'19-4027 (base)','band_l':'L*=22 a*=2 b*=-12','band_m':'Jacquard Woven (rPET)','band_f':'Tonal Geometric Pattern',
        'accent':'#4DB8A0', 'top':'#1C2D3D', 'btm':'#2D6058',
    },
    {
        'id':'V3','en':'Arctic Haze','zh':'北极雾霭',
        'body':'#E2DDD8','body_p':'11-0601 + Pearl','body_l':'L*=88 a*=1 b*=2','body_m':'PC/ABS + 2% Pearl','body_f':'MT-11020 + Pearl · 5-8 GU',
        'arm':'#C8C8C8','arm_p':'Brushed Silver','arm_l':'L*=78 a*=0 b*=-2','arm_m':'Al 6061','arm_f':'Brush #220 + Clear Anodize · 18-25 GU',
        'cush':'#B5B5B4','cush_p':'14-4104 TCX','cush_l':'L*=72 a*=1 b*=-2','cush_m':'Bio-PU Vegan Leather','cush_f':'Fine Grain · Micro-Perf · 2-4 GU',
        'mesh':'#E2DDD8','mesh_p':'11-0601 (base)','mesh_l':'L*=88 a*=1 b*=2','mesh_m':'Knit Textile','mesh_f':'Silver Heather · Acoustic',
        'band':'#E0DDD8','band_p':'Translucent White','band_l':'L*=90 (translucent)','band_m':'Silicone Mesh','band_f':'Grid Pattern · 1.5mm Pitch · 5-10 GU',
        'accent':'#B8A0C8', 'top':None, 'btm':None,
    },
]

for i, v in enumerate(variants):
    cx, lx = COL_CX[i], START_X+i*(COL_W+COL_GAP)
    cur_y = CONTENT_Y

    # Header
    marker = ' ★ HERO' if v.get('hero') else ''
    text_c(cx, cur_y, f"{v['id']} — {v['en']}{marker}", crimson_bold, v['accent'])
    text_c(cx, cur_y+26, v['zh'], zh_label, MID)
    cur_y += 65

    # Earcup — gradient or solid
    if v.get('top') and v.get('btm'):
        gradient_rect(cx-80, cur_y, 160, 110, v['top'], v['btm'])
        draw.rectangle([cx-80, cur_y, cx+80, cur_y+110], outline=RULE, width=1)
        text_c(cx, cur_y+55, 'GRADIENT', work_bold, blend(v['top'], WHITE, 0.5))
    else:
        draw.rectangle([cx-80, cur_y, cx+80, cur_y+110], fill=v['body'], outline=RULE, width=1)
        text_c(cx, cur_y+55, 'EARCUP', work_bold, blend(v['body'], '#000000', 0.4))
    text_c(cx, cur_y+130, 'EARCUP SHELL / 耳罩外壳', work_bold, WHITE)
    text_c(cx, cur_y+150, v['body_m'], work_sm, MID)
    text_c(cx, cur_y+168, f"Pantone {v['body_p']}  {v['body_l']}", work_xs, DIM)
    text_c(cx, cur_y+184, v['body_f'], work_xs, DIM)
    cur_y += 215

    # Metal arm
    draw.rectangle([cx-90, cur_y, cx+90, cur_y+35], fill=v['arm'], outline=RULE, width=1)
    text_c(cx, cur_y+17, 'METAL ARM', work_bold, blend(v['arm'], '#000000', 0.4))
    text_c(cx, cur_y+55, 'METAL ARM / 金属臂', work_bold, WHITE)
    text_c(cx, cur_y+75, v['arm_m'], work_sm, MID)
    text_c(cx, cur_y+93, f"{v['arm_p']}  {v['arm_l']}", work_xs, DIM)
    text_c(cx, cur_y+109, v['arm_f'], work_xs, DIM)
    cur_y += 140

    # Ear cushion
    draw.rectangle([cx-90, cur_y, cx+90, cur_y+35], fill=v['cush'], outline=RULE, width=1)
    text_c(cx, cur_y+17, 'CUSHION', work_bold, blend(v['cush'], '#000000', 0.4))
    text_c(cx, cur_y+55, 'EAR CUSHION / 耳垫', work_bold, WHITE)
    text_c(cx, cur_y+75, v['cush_m'], work_sm, MID)
    text_c(cx, cur_y+93, f"Pantone {v['cush_p']}  {v['cush_l']}", work_xs, DIM)
    text_c(cx, cur_y+109, v['cush_f'], work_xs, DIM)
    cur_y += 140

    # Mesh + Headband
    draw.rectangle([cx-90, cur_y, cx+90, cur_y+25], fill=v['mesh'], outline=RULE, width=1)
    text_c(cx, cur_y+12, 'MESH', work_bold, blend(v['mesh'], '#000000', 0.4))
    text_c(cx, cur_y+43, 'MESH / 网面  |  HEADBAND / 头梁', work_bold, WHITE)
    text_c(cx, cur_y+61, f"{v['mesh_m']}  |  {v['band_m']}", work_sm, MID)
    text_c(cx, cur_y+79, f"Pantone {v['mesh_p']}  |  {v['band_p']}", work_xs, DIM)

# Footer
text_c(W//2, H-50, 'PROJECT AURA · CMF SPECIFICATION BOARD · PHASE 3 FINAL · ALL DATA = DESIGN ASSUMPTIONS', work_xs, DIM)

output = '/Users/wang/Desktop/CMF作品集/03_ProjectA_ConsumerElectronics/Swatches/AURA_CMF_Swatch_Board.png'
img.save(output, 'PNG', dpi=(300,300))
print(f'Saved: {output}')
print(f'Size: {W}x{H}')
