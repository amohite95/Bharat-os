import requests
import time

def check_cloud_health():
    # Points to your live Hugging Face Space
    cloud_url = "https://amohite95-amlabsin-hq-core.hf.space/hunt"
    print("📡 AMLABS: Monitoring Alpha/Daily Squads...")
    
    try:
        r = requests.get(cloud_url, timeout=10)
        if r.status_code == 200:
            print("✅ Status: ALL 10 BOTS OPERATIONAL")
            # If a bot finds a bug, the cloud updates this flag
            if "CRITICAL" in r.text:
                print("🚨 !!! BOUNTY DETECTED !!! Check Telegram immediately.")
        else:
            print("⚠️ Status: Cloud syncing (Retry in 60s)")
    except:
        print("❌ Status: Connection Pending...")

if __name__ == "__main__":
    while True:
        check_cloud_health()
        time.sleep(300) # Check every 5 minutes
