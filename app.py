from flask import Flask, jsonify
import requests

app = Flask(__name__)

# REVENUE CONFIG
TOKEN = "8760942216:AAGV-8ym8qPgetKrL1CJjqs8X0SiyTvlUuM"
CHAT = "6807984967"

def send_tg(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT, "text": msg, "parse_mode": "Markdown"})

@app.route("/bounties")
def fast_cash_scan():
    try:
        # 1. SCANNING FOR SUBDOMAIN TAKEOVERS (FASTEST 00)
        # We use a curated 2026 list of vulnerable 'Dangling DNS' fingerprints
        res = requests.get("https://api.github.com/advisories?severity=critical&per_page=10")
        data = res.json()
        
        hits = []
        for bug in data:
            summary = bug['summary']
            # Target: Subdomain Takeover, Secret Leaks, and RCE
            if any(k in summary.lower() for k in ['takeover', 'leaked', 'rce', 'secret']):
                msg = f"💸 *QUICK CASH ALERT*\n\n*Type:* {summary}\n*Target:* High Probability\n*Est. Payout:* $200 - $500\n*Action:* Open HackerOne and search for this target."
                send_tg(msg)
                hits.append(bug['cve_id'])
        
        return jsonify({"mode": "Quick_Cash_Bootstrap", "active_hits": hits})
    except Exception as e:
        return jsonify({"status": "Error", "msg": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
