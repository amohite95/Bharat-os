from flask import Flask, jsonify
import requests
import datetime

app = Flask(__name__)

# DIRECTOR'S TARGETS
MONTHLY_GOAL_INR = 100000
TOKEN = "8760942216:AAGV-8ym8qPgetKrL1CJjqs8X0SiyTvlUuM"
CHAT = "6807984967"

def send_tg(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT, "text": msg, "parse_mode": "Markdown"})

@app.route("/ledger")
def view_ledger():
    # This will pull from your real HackerOne/Stripe balance soon
    current_earned_inr = 0 
    remaining = MONTHLY_GOAL_INR - current_earned_inr
    return jsonify({
        "Goal": f"₹{MONTHLY_GOAL_INR}",
        "Earned": f"₹{current_earned_inr}",
        "Remaining_to_Salary": f"₹{remaining}",
        "Status": "💰 HUNTING FOR SALARY BUGS"
    })

@app.route("/bounties")
def salary_hunter():
    # HUNTING FOR API BOLA & CRITICALS (,000+)
    try:
        res = requests.get("https://api.github.com/advisories?severity=critical&per_page=15")
        data = res.json()
        for bug in data:
            if "api" in bug['summary'].lower() or "bola" in bug['summary'].lower():
                msg = f"🌟 *SALARY ALERT: HIGH VALUE FOUND*\n\n*Target:* {bug['summary']}\n*Est. Payout:* $1,200 (₹1,00,000+)\n*Action:* Draft report for amohite95@gmail.com"
                send_tg(msg)
        return jsonify({"mode": "Salary_Hunting", "engine": "Active"})
    except:
        return jsonify({"status": "error"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
