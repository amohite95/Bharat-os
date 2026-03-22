# 🏛️ AMLABSIN PRIVATE LIMITED: BUILD-FUND TRACKER
# GOAL: ₹20,000 (Legal Registration & Corporate Setup)

class BuildFund:
    def __init__(self, current_balance_usd):
        self.goal_inr = 20000
        self.current_inr = current_balance_usd * 83.5 # 2026 Avg Exchange Rate
        
    def report(self):
        progress = (self.current_inr / self.goal_inr) * 100
        remaining = self.goal_inr - self.current_inr
        print("--- 🛠️ AMLABS BUILD PROGRESS ---")
        print(f"Target: ₹{self.goal_inr}")
        print(f"Current: ₹{self.current_inr:.2f}")
        if remaining > 0:
            print(f"Need: ₹{remaining:.2f} more to finalize registration.")
        else:
            print("🚀 STATUS: GO FOR REGISTRATION!")

if __name__ == "__main__":
    # Update the 0.0 with your actual earnings when they arrive
    BuildFund(current_balance_usd=0.0).report()
