import requests
import json
import os

def collect_evidence():
    print("🕵️ AMLABSIN: EVIDENCE COLLECTOR STARTING...")
    # This pulls from your CAI-powered Cloud Space
    cloud_url = "https://amohite95-amlabsin-hq-core.hf.space/hunt"
    
    try:
        response = requests.get(cloud_url)
        data = response.json()
        
        if data.get("status") == "AGENTIC_HUNT_ACTIVE":
            print("✅ CLOUD CONNECTED: CAI Agent is reasoning...")
            # If the agent marks a bug as 'VALIDATED'
            if "VALIDATED" in str(data):
                with open("poc_report.txt", "w") as f:
                    f.write(f"--- AMLABSIN POV REPORT ---\n")
                    f.write(f"SQUAD: {data.get('engine')}\n")
                    f.write(f"TARGET: {data.get('squad_alpha', {}).get('target')}\n")
                    f.write(f"EVIDENCE: {json.dumps(data, indent=2)}\n")
                print("🚨 EVIDENCE SAVED TO: poc_report.txt")
        else:
            print("⏳ No verified bugs yet. Continuing scan...")
    except Exception as e:
        print(f"❌ Connection Error: {e}")

if __name__ == "__main__":
    collect_evidence()
