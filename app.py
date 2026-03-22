from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "🏛️ AMLABSIN HQ CORE: ONLINE"

@app.route("/hunt")
def hunt_status():
    return jsonify({"status": "Hunting", "engine": "Cloud-V1", "targets": ["Airbnb", "Netflix"]})

if __name__ == "__main__":
    # CRITICAL: 0.0.0.0 and Port 7860 are required for Hugging Face 2026
    port = int(os.environ.get("PORT", 7860))
    app.run(host="0.0.0.0", port=port)
