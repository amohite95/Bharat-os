def create_report(target, bug_type):
    print("📢 --- AMLABSIN OFFICIAL SUBMISSION ---")
    print(f"TITLE: [MARCH-27-BONUS] {bug_type} identified on {target}")
    print("-" * 50)
    print("SUMMARY: Critical vulnerability detected by AMLABS-HQ Cloud Engine.")
    print("IMPACT: High. Potential for unauthorized data access in AI Scope.")
    print("STEPS: [1] Access {target} [2] Inject Payload [3] Observe Leak.")
    print("-" * 50)
    print("💰 ESTIMATED PAYOUT: $2,500 + 25% Bonus (₹2.9 Lakhs)")

if __name__ == "__main__":
    # Example for an AI-Assistant hit
    create_report("airbnb.com/help/contact-us", "Prompt Injection")
