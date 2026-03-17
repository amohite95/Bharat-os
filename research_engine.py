import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

# THE VAULT
API_KEY = os.getenv("AI_API_KEY") 
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")

def addie_research(topic):
    print(f"🔍 Addie is initiating full-throttle research on: {topic}...")
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [{"parts": [{"text": f"Conduct a professional technical analysis on: {topic}. Provide zero-error data and revenue-focused insights."}]}]
    }

    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()['candidates'][0]['content']['parts'][0]['text']
        return result
    else:
        return f"Error: {response.status_code} - {response.text}"

def send_to_ceo(report):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": f"📊 NEW RESEARCH REPORT:\n\n{report[:4000]}"}
    requests.post(url, json=payload)

if __name__ == "__main__":
    target = input("Enter Research Target (e.g., Kolhapur AI Market): ")
    report = addie_research(target)
    print("\n✅ Research Complete. Sending to your Telegram...")
    send_to_ceo(report)

