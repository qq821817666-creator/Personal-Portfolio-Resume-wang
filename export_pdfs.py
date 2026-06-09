#!/usr/bin/env python3
"""Export project portfolio HTML pages to PDF"""
import weasyprint
import os

PROJECTS = [
    {
        "name": "A3_Trailux_OutdoorHeadlamp",
        "title": "A3 Trailux — Outdoor Headlamp CMF",
        "dir": "Category1_DailyConsumer/A3_Trailux_OutdoorHeadlamp",
    },
    {
        "name": "A2_Aether_AirPurifier",
        "title": "A2 Aether — Smart Air Purifier CMF",
        "dir": "Category1_DailyConsumer/A2_Aether_AirPurifier",
    },
    {
        "name": "A1_Lumina_BeautyDevice",
        "title": "A1 Lumina — RF Beauty Device CMF",
        "dir": "Category1_DailyConsumer/A1_Lumina_BeautyDevice",
    },
]

BASE = "/Users/wang/Desktop/CMF作品集"
OUTPUT_DIR = os.path.join(BASE, "05_Portfolio", "PDF_Exports")
os.makedirs(OUTPUT_DIR, exist_ok=True)

for proj in PROJECTS:
    html_path = os.path.join(BASE, proj["dir"], "portfolio.html")
    pdf_path = os.path.join(OUTPUT_DIR, f"{proj['name']}_Portfolio.pdf")

    if not os.path.exists(html_path):
        print(f"SKIP: {html_path} not found")
        continue

    print(f"Generating: {proj['name']} ...")
    doc = weasyprint.HTML(filename=html_path)
    doc.write_pdf(pdf_path)
    size_kb = os.path.getsize(pdf_path) / 1024
    print(f"  -> {pdf_path} ({size_kb:.0f} KB)")

print(f"\nDone! PDFs saved to: {OUTPUT_DIR}")
