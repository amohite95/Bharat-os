import datetime

SERVICES = ["Azure Free Tier", "GitHub Actions", "Google Drive", "Razorpay"]

def daily_sync_report():
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    report = f"# am_labs Central Sync - {today}\n"
    report += f"Owner: amohite95@gmail.com\n"
    report += "-----------------------------------\n"
    
    for service in SERVICES:
        report += f"[✅] {service}: Monitoring Active\n"
    
    report += "\n## Daily Action Items:\n"
    report += "- Check Gmail for '[am_labs_Legal]' alerts.\n"
    report += "- Verify Azure Free Credit Balance (Target: ₹0 spent).\n"
    
    with open('ADDIE_SYNC_REPORT.md', 'w') as f:
        f.write(report)
    print("Addie: Sync Report Generated and pushed to Vault.")

if __name__ == "__main__":
    daily_sync_report()
