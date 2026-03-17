import os, requests, time, subprocess

# DNA: amohite95@gmail.com | am_labs.in
TOKEN = "8760942216:AAGV-8ym8qPgetKrL1CJjqs8X0SiyTvlUuM"
AI_KEY = "AIzaSyDZNseNbz-C5JA08771HLbVFpQDgZr0YP4"
ADMIN_ID = "6807984967"

def run_logic(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={AI_KEY}"
    # Pulling from your real Vault data
    context = ""
    try:
        context = subprocess.check_output("cat vault/technical_specs/CORE_MANIFEST.md vault/documents/LEGACY_MSME/details.txt | head -n 30", shell=True).decode()
    except: pass
    
    data = {"contents": [{"parts": [{"text": f"Context: {context}\nTask: {prompt}"}]}]}
    try:
        r = requests.post(url, json=data, timeout=30)
        return r.json()['candidates'][0]['content']['parts'][0]['text']
    except: return "⚠️ S25: Syncing Vault... please wait."

print("⚡ RUDRA-CHAKRA ENGINE: ONLINE")
OFFSET = 0
while True:
    try:
        r = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset={OFFSET}&timeout=10").json()
        for u in r.get("result", []):
            OFFSET = u["update_id"] + 1
            if "message" in u and str(u["message"]["chat"]["id"]) == ADMIN_ID:
                cmd = u["message"].get("text", "")
                requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": ADMIN_ID, "text": "🌀 Chakra: Processing Load..."})
                report = run_logic(cmd)
                requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": ADMIN_ID, "text": report[:4000]})
    except: time.sleep(10)
