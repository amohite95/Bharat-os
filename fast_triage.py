def generate_report(target_type, domain):
    print("🚀 AMLABSIN FAST-TRIAGE REPORT (MARCH 2026)")
    print("-" * 40)
    if "ai" in target_type:
        print(f"TITLE: [CRITICAL-AI] Prompt Injection / Data Leakage on {domain}")
        print("IMPACT: Bypassing guardrails to access internal Airbnb data.")
    else:
        print(f"TITLE: [DAILY-CASH] Information Disclosure on {domain}")
        print("IMPACT: Leaked production keys in JavaScript assets.")
    print("-" * 40)
    print("STATUS: PoC Ready. Waiting for Triage.")

if __name__ == "__main__":
    # Example: When a bot hits an AI target
    generate_report("ai", "airbnb-ai-assistant.com")
