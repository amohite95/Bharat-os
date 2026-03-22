from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/hunt")
def hunt_status():
    return jsonify({
        "status": "AGENTIC_HUNT_ACTIVE",
        "engine": "CAI-Framework-v0.6",
        "intelligence": "ReAct-Reasoning-Loop",
        "squad_alpha": {"power": "Exploit_Validation", "target": "Airbnb-AI"},
        "squad_daily": {"power": "Key_Verification", "target": "Netflix-API"}
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    app.run(host="0.0.0.0", port=port)
