import requests
import time

TOKEN = "8760942216:AAGV-8ym8qPgetKrL1CJjqs8X0SiyTvlUuM"
CHAT = "6807984967"

def send_heartbeat():
    msg = "💓 *AMLABSIN HEARTBEAT*\n\n*Status:* Hunting for Build-Fund\n*Target:* ₹20,000\n*Mode:* 24/7 Autonomous"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": CHAT, "text": msg, "parse_mode": "Markdown"})
    except:
        pass

if __name__ == "__main__":
    # Send one immediately so you know it works
    send_heartbeat()
    # Then wait 24 hours
    while True:
        time.sleep(86400)
        send_heartbeat()
