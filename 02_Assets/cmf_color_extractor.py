"""
CMF Color Palette Extractor
CMF色彩调色板提取工具

Extracts dominant colors from a folder of trend/reference images,
converts to estimated CIELAB values, and suggests harmonious palettes.
从趋势/参考图片文件夹中提取主要颜色，转换为CIELAB值，建议和谐调色板。

Usage:
    python3 cmf_color_extractor.py /path/to/images/folder/

Dependencies:
    pip3 install Pillow numpy scipy colorthief
"""

import os
import sys
import json
import colorsys
from pathlib import Path

try:
    from colorthief import ColorThief
    HAS_COLORTHIEF = True
except ImportError:
    HAS_COLORTHIEF = False
    print("Warning: colorthief not installed. Run: pip3 install colorthief")

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False


# ── RGB → CIELAB (simplified conversion via XYZ) ──────────────────────────

def rgb_to_xyz(r, g, b):
    """Convert sRGB (0-255) to CIE XYZ."""
    r, g, b = [x / 255.0 for x in (r, g, b)]

    def linearize(c):
        if c <= 0.04045:
            return c / 12.92
        return ((c + 0.055) / 1.055) ** 2.4

    r, g, b = [linearize(x) * 100 for x in (r, g, b)]

    # sRGB → XYZ (D65 reference white, 2° observer)
    x = r * 0.4124564 + g * 0.3575761 + b * 0.1804375
    y = r * 0.2126729 + g * 0.7151522 + b * 0.0721750
    z = r * 0.0193339 + g * 0.1191920 + b * 0.9503041

    return x, y, z


def xyz_to_lab(x, y, z):
    """Convert CIE XYZ to CIE L*a*b* (D65 reference white)."""
    # D65 reference white
    xn, yn, zn = 95.047, 100.000, 108.883

    def f(t):
        delta = 6 / 29
        if t > delta ** 3:
            return t ** (1/3)
        return t / (3 * delta ** 2) + 4 / 29

    L = 116 * f(y / yn) - 16
    a = 500 * (f(x / xn) - f(y / yn))
    b = 200 * (f(y / yn) - f(z / zn))

    return round(L, 1), round(a, 1), round(b, 1)


def rgb_to_lab(r, g, b):
    """Convert sRGB (0-255) to CIE L*a*b*."""
    return xyz_to_lab(*rgb_to_xyz(r, g, b))


def rgb_to_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"


def delta_e_76(lab1, lab2):
    """CIE76 (simplest) Delta E calculation."""
    return round(np.sqrt(sum((a - b) ** 2 for a, b in zip(lab1, lab2))), 2)


# ── Palette Generation ────────────────────────────────────────────────────

def generate_complementary(r, g, b):
    """Generate complementary color."""
    h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
    h2 = (h + 0.5) % 1.0
    r2, g2, b2 = [int(x * 255) for x in colorsys.hsv_to_rgb(h2, s * 0.7, v)]
    return r2, g2, b2


def generate_analogous(r, g, b, angle=30):
    """Generate analogous colors (±angle degrees)."""
    h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
    offset = angle / 360.0

    colors = []
    for delta in [-offset, 0, offset]:
        h2 = (h + delta) % 1.0
        r2, g2, b2 = [int(x * 255) for x in colorsys.hsv_to_rgb(h2, s, v)]
        colors.append((r2, g2, b2))
    return colors


def generate_triadic(r, g, b):
    """Generate triadic color harmony (3 colors 120° apart)."""
    h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
    colors = []
    for offset in [0, 120, 240]:
        h2 = (h + offset/360) % 1.0
        r2, g2, b2 = [int(x * 255) for x in colorsys.hsv_to_rgb(h2, s * 0.8, v)]
        colors.append((r2, g2, b2))
    return colors


def suggest_palettes(dominant_colors):
    """Generate CMF palette suggestions from dominant colors."""
    palettes = []

    for i, (r, g, b) in enumerate(dominant_colors[:5]):
        lab = rgb_to_lab(r, g, b)
        hex_code = rgb_to_hex(r, g, b)
        comp = generate_complementary(r, g, b)
        comp_lab = rgb_to_lab(*comp)
        analog = generate_analogous(r, g, b)

        palettes.append({
            "name": f"Palette {i+1} (from {hex_code})",
            "primary": {
                "rgb": (r, g, b),
                "hex": hex_code,
                "cielab": {"L*": lab[0], "a*": lab[1], "b*": lab[2]}
            },
            "complementary": {
                "rgb": comp,
                "hex": rgb_to_hex(*comp),
                "cielab": {"L*": comp_lab[0], "a*": comp_lab[1], "b*": comp_lab[2]}
            },
            "analogous_triad": [
                {"rgb": c, "hex": rgb_to_hex(*c), "cielab": dict(zip(["L*", "a*", "b*"], rgb_to_lab(*c)))}
                for c in analog
            ]
        })

    return palettes


# ── Color Naming ──────────────────────────────────────────────────────────

def suggest_color_name(r, g, b):
    """Suggest a human-readable color name based on RGB values."""
    lab = rgb_to_lab(r, g, b)
    L, a, b_val = lab

    names = []

    # Lightness
    if L < 15:
        names.append("Deep")
    elif L < 30:
        names.append("Dark")
    elif L < 50:
        names.append("Mid")
    elif L < 70:
        names.append("Light")
    elif L < 90:
        names.append("Pale")
    else:
        names.append("Bright")

    # Hue description
    if abs(a) < 5 and abs(b_val) < 5:
        names.append("Neutral")
        if L < 30:
            names.append("Black" if L < 10 else "Charcoal")
        elif L > 80:
            names.append("White")
        else:
            names.append("Gray")
    elif a > 10 and b_val > 10:
        names.append("Warm" if a > b_val else "Golden")
    elif a > 10 and b_val < -5:
        names.append("Rose" if L > 40 else "Burgundy")
    elif a < -5 and b_val > 10:
        names.append("Teal" if a < -10 else "Sage")
    elif a < -5 and b_val < -5:
        names.append("Navy" if L < 40 else "Sky")
    elif b_val > 15:
        names.append("Mustard" if L < 60 else "Cream")
    elif b_val < -10:
        names.append("Indigo" if L < 30 else "Lavender")

    return " ".join(names)


# ── Main ──────────────────────────────────────────────────────────────────

def analyze_image(image_path, num_colors=10):
    """Extract dominant colors from a single image."""
    if not HAS_COLORTHIEF:
        print(f"Skipping {image_path}: colorthief required")
        return []

    try:
        ct = ColorThief(image_path)
        palette = ct.get_palette(color_count=num_colors)
        return palette
    except Exception as e:
        print(f"Error analyzing {image_path}: {e}")
        return []


def analyze_folder(folder_path, colors_per_image=5):
    """Analyze all images in a folder and aggregate colors."""
    image_extensions = {'.jpg', '.jpeg', '.png', '.webp', '.bmp'}
    all_colors = []

    for file in Path(folder_path).iterdir():
        if file.suffix.lower() in image_extensions:
            print(f"Analyzing: {file.name}")
            colors = analyze_image(str(file), num_colors=colors_per_image)
            all_colors.extend(colors)

    return all_colors


def print_palette_report(palettes):
    """Pretty-print palette suggestions."""
    print("\n" + "=" * 60)
    print("CMF COLOR PALETTE REPORT")
    print("=" * 60)

    for palette in palettes:
        print(f"\n🎨 {palette['name']}")
        print(f"   Primary: {palette['primary']['hex']} "
              f"CIELAB(L*={palette['primary']['cielab']['L*']}, "
              f"a*={palette['primary']['cielab']['a*']}, "
              f"b*={palette['primary']['cielab']['b*']})")
        print(f"   → {suggest_color_name(*palette['primary']['rgb'])}")

        print(f"   Complementary: {palette['complementary']['hex']} "
              f"→ {suggest_color_name(*palette['complementary']['rgb'])}")

        an = palette['analogous_triad']
        print(f"   Analogous Triad: {an[0]['hex']} / {an[1]['hex']} / {an[2]['hex']}")

    print("\n" + "=" * 60)
    print(f"Total palettes: {len(palettes)}")
    print("=" * 60)
    return palettes


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 cmf_color_extractor.py <image_folder_path>")
        print("Example: python3 cmf_color_extractor.py ~/Desktop/trend_images/")
        sys.exit(1)

    folder = sys.argv[1]
    if not os.path.isdir(folder):
        print(f"Error: '{folder}' is not a valid directory")
        sys.exit(1)

    if not HAS_COLORTHIEF or not HAS_NUMPY:
        print("Please install dependencies:")
        print("  pip3 install Pillow numpy colorthief")
        sys.exit(1)

    print(f"Analyzing images in: {folder}")
    colors = analyze_folder(folder)

    if not colors:
        print("No colors extracted. Check your image folder.")
        sys.exit(1)

    # Aggregate unique colors (simple deduplication by rounding)
    unique_colors = []
    seen = set()
    for c in colors:
        key = (c[0]//10, c[1]//10, c[2]//10)
        if key not in seen:
            seen.add(key)
            unique_colors.append(c)

    print(f"Extracted {len(unique_colors)} unique colors from {len(colors)} total")

    # Generate and print palette suggestions
    palettes = suggest_palettes(unique_colors[:10])
    print_palette_report(palettes)

    # Export to JSON for Figma/design tool import
    output_path = os.path.join(folder, "..", "extracted_colors.json")
    with open(output_path, 'w') as f:
        json.dump(palettes, f, indent=2)
    print(f"\nPalette data exported to: {output_path}")
