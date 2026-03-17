import requests, time

# ROOT IDENTITY
TOKEN = "8760942216:AAGV-8ym8qPgetKrL1CJjqs8X0SiyTvlUuM"
AI_KEY = "AIzaSyDZNseNbz-C5JA08771HLbVFpQDgZr0YP4"
ADMIN_ID = "6807984967"

def get_ai_response(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={AI_KEY}"
    headers = {'Content-Type': 'application/json'}
    payload = {"contents": [{"parts": [{"text": f"Owner: amohite95@gmail.com. Task: {prompt}"}]}]}
    try:
        r = requests.post(url, json=payload, headers=headers, timeout=30)
        res = r.json()
        return res['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"⚠️ S25 Sync Pending... (Check Internet/Key)"

OFFSET = 0
print("🛰️ amohite95@gmail.com: SERVICE ACTIVE")

while True:
    try:
        r = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset={OFFSET}&timeout=15").json()
        for u in r.get("result", []):
            OFFSET = u["update_id"] + 1
            if "message" in u and str(u["message"]["chat"]["id"]) == ADMIN_ID:
                msg = u["message"].get("text", "Status Check")
                # Immediate acknowledgment
                requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": ADMIN_ID, "text": "✅ amLabs: Processing Autonomous Load..."})
                # AI Logic
                response = get_ai_response(msg)
                requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": ADMIN_ID, "text": response[:4000]})
    except:
        time.sleep(10)
