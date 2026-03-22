import subprocess

def check_earnings():
    print("💰 --- AMLABSIN LIVE CASH MONITOR ---")
    # This checks the logs of all running Super-Bots
    try:
        output = subprocess.check_output(["pm2", "logs", "--lines", "5", "--no-colors"])
        if "ALERT" in str(output):
            print("🔥 STATUS: BUG FOUND! Check Telegram immediately.")
        else:
            print("📡 STATUS: Hunting... (Airbnb/Netflix Cloud)")
    except:
        print("⚠️ Waiting for bots to sync...")

if __name__ == "__main__":
    check_earnings()
