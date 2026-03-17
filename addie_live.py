import os, requests, time, subprocess

TOKEN = "8760942216:AAGV-8ym8qPgetKrL1CJjqs8X0SiyTvlUuM"
AI_KEY = "AIzaSyDZNseNbz-C5JA08771HLbVFpQDgZr0YP4"
ADMIN_ID = "6807984967"

def get_vault_data():
    try:
        return subprocess.check_output("cat vault/technical_specs/CORE_MANIFEST.md", shell=True).decode()
    except: return "Vault manifest not found."

def get_payload(topic):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={AI_KEY}"
    manifest = get_vault_data()
    prompt = f"CEO: amohite95@gmail.com. Site: am_labs.in. Manifest: {manifest}. Task: Generate technical roadmap for {topic}."
    try:
        r = requests.post(url, json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=30)
        return r.json()['candidates'][0]['content']['parts'][0]['text']
    except: return "🔄 S25 Healing: Retrying sync..."

OFFSET = 0
while True:
    try:
        r = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset={OFFSET}&timeout=20").json()
        for u in r.get("result", []):
            OFFSET = u["update_id"] + 1
            if str(u["message"]["chat"]["id"]) == ADMIN_ID:
                msg = u["message"].get("text", "Status Audit")
                requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": ADMIN_ID, "text": "🛰️ amLabs-HQ: Syncing Standalone Environment..."})
                res = get_payload(msg)
                requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": ADMIN_ID, "text": res[:4000]})
    except: time.sleep(5)
