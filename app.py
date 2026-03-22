from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/hunt")
def hunt_status():
    return jsonify({
        "status": "OPERATIONAL",
        "squad_alpha": {"bots": 5, "priority": "AI_BONUS_25", "targets": ["airbnb-ai", "netflix-core"]},
        "squad_daily": {"bots": 5, "priority": "RAPID_CASH", "targets": ["microsites", "js-leaks"]},
        "goal_daily": "00",
        "goal_bonus": "₹2.9 Lakh"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    app.run(host="0.0.0.0", port=port)
