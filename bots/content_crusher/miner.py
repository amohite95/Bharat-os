import datetime

# This is the "Mining Map" - high-value sectors for 2026
RESOURCE_MAP = {
    "short_form_video": "https://pictory.ai",
    "ai_automation_leads": "https://n8n.io",
    "digital_products": "https://gumroad.com"
}

def generate_money_report():
    today = datetime.date.today()
    report = f"# am_labs Money Mining Report - {today}\n\n"
    report += "## Current High-Value Tasks:\n"
    report += "1. **Faceless YouTube Channels** (Pictory/CapCut)\n"
    report += "2. **AI Lead Gen for Local Business** (n8n/Google Maps)\n"
    report += "3. **Digital Template Flipping** (Notion/Gumroad)\n\n"
    report += "## Resource Links Cleared for use:\n"
    for sector, link in RESOURCE_MAP.items():
        report += f"- {sector.upper()}: {link}\n"
    
    with open('MONEY_MINING_REPORT.md', 'w') as f:
        f.write(report)
    print("✅ Money Mining Report generated for CEO.")

if __name__ == "__main__":
    generate_money_report()
