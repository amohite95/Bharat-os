# 🏛️ AMLABSIN PRIVATE LIMITED: OFFICIAL REWARD CLAIMANT
# Use this when a Super-Bot triggers a Telegram Alert.

def prepare_submission(bot_name, target):
    header = "--- AMLABSIN OFFICIAL VULNERABILITY REPORT ---"
    entity = "Entity: AMLABSIN PRIVATE LIMITED (In-Registration)"
    director = "Director: Geetanjali Arun Mohite"
    payout = "Payment: Via HackerOne / RazorpayX (Merchant: SRNL1xYp4hpnau)"
    
    print(header)
    print(f"Submitting Bot: {bot_name}")
    print(f"Target Found: {target}")
    print(entity)
    print(director)
    print(payout)
    print("-" * 47)

if __name__ == "__main__":
    # Test for Super_Bot_1
    prepare_submission("SUPER_BOT_1", "dev-api.airbnb.com")
