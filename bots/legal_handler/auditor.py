import os

REQUIRED_DOCS = [
    "PAN_CARD.pdf",
    "AADHAAR_FRONT.pdf",
    "AADHAAR_BACK.pdf",
    "CANARA_PASSBOOK.pdf",
    "UDYAM_CERTIFICATE.pdf"
]

def generate_report():
    present = os.listdir('docs/legal')
    missing = [doc for doc in REQUIRED_DOCS if doc not in present]
    
    with open('DAILY_LEGAL_REPORT.md', 'w') as f:
        f.write("# am_labs Daily Legal Audit\n")
        f.write(f"Status: {'✅ READY' if not missing else '⚠️ ACTION REQUIRED'}\n\n")
        f.write("## Missing Documents:\n")
        if not missing:
            f.write("- All legal documents are securely placed.\n")
        else:
            for m in missing:
                f.write(f"- [ ] {m}\n")
        f.write("\n*Next Step: Upload missing files to /docs/legal folder.*")

if __name__ == "__main__":
    generate_report()
