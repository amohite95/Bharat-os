import os, requests, time, subprocess

# MASTER DNA: amohite95@gmail.com
TOKEN = "8760942216:AAGV-8ym8qPgetKrL1CJjqs8X0SiyTvlUuM"
AI_KEY = "AIzaSyDZNseNbz-C5JA08771HLbVFpQDgZr0YP4"
ADMIN_ID = "6807984967"

def run_vault_query(command):
    # This connects the AI to your /vault/technical_specs
    try:
        res = subprocess.check_output(command, shell=True).decode()
        return res if res else "Vault record empty."
    except: return "Vault access error."

def get_ai_payload(topic):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={AI_KEY}"
    # Pulling context from your MSME documents automatically
    context = run_vault_query("cat vault/documents/LEGACY_MSME/details.txt | head -n 20")
    prompt = f"CEO amohite95@gmail.com. Context: {context}. Mission: Generate high-margin technical roadmap for {topic} for am_labs.in."
    
    try:
        r = requests.post(url, json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=30)
        return r.json()['candidates'][0]['content']['parts'][0]['text']
    except: return "🔄 S25 Auto-Healing: Connection reset. Retrying..."

OFFSET = 0
while True:
    try:
        r = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset={OFFSET}&timeout=20").json()
        for u in r.get("result", []):
            OFFSET = u["update_id"] + 1
            if str(u["message"]["chat"]["id"]) == ADMIN_ID:
                msg = u["message"].get("text", "Market Audit")
                requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": ADMIN_ID, "text": "🛰️ amLabs-HQ: Recursive Sync Active..."})
                payload = get_ai_payload(msg)
                requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": ADMIN_ID, "text": payload[:4000]})
    except: time.sleep(5)
