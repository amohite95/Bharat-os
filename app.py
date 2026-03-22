from flask import Flask, jsonify
import requests

app = Flask(__name__)

def get_targets():
    with open("target_list.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

@app.route("/hunt")
def targeted_hunt():
    targets = get_targets()
    # The Brain's 2026 Scanning Logic
    print(f"🚀 AMLABSIN is now hunting: {targets}")
    return jsonify({"status": "Hunting", "scope": targets, "goal": "₹20,000"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
