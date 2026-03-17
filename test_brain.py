import os, requests
from dotenv import load_dotenv
load_dotenv()

key = os.getenv("AI_API_KEY")
print(f"📡 Testing Key: {key[:10]}...")

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={key}"
payload = {"contents": [{"parts": [{"text": "Say: System Online"}]}]}

r = requests.post(url, json=payload)
print(f"📡 Response: {r.text}")

