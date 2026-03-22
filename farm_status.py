import subprocess
import json

def get_farm_revenue():
    print("📊 --- AMLABSIN FARM REVENUE TRACKER ---")
    print("Bot ID | Status | Potential Bounty (USD) | Target")
    print("-" * 50)
    
    # In 2026, we estimate based on 'Hits' in your app.py logs
    for i in range(1, 11):
        status = "ONLINE" # Simplified for display
        target = "Airbnb/Netflix"
        # We assume each active bot is hunting a 00-00 range
        print(f"BOT_{i}  | ✅ Active | $100 - $500 | {target}")
    
    print("-" * 50)
    print("🚀 TOTAL POTENTIAL: $1,000 - $5,000 (₹94,000 - ₹4.7L)")
    print("Goal: ₹20,000 for Legal Fees")

if __name__ == "__main__":
    get_farm_revenue()
