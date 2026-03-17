import os, requests
from dotenv import load_dotenv
load_dotenv()

def debug_send():
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    print(f"📡 Testing Token: {token[:10]}...")
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": "🚀 CEO, THE BRIDGE IS LIVE."}
    
    try:
        r = requests.post(url, json=payload, timeout=10)
        print(f"📡 Status: {r.status_code}")
        print(f"📡 Response: {r.text}")
    except Exception as e:
        print(f"❌ Connection Error: {e}")

if __name__ == "__main__":
    debug_send()

