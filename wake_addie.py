import os
import requests
from dotenv import load_dotenv

# 1. Open the Vault
load_dotenv()

# 2. Grab the Keys
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# 3. Formulate the Message
message = "🟢 S25 SYSTEM ALERT: Addie is awake. Vault connection secured."

# 4. Fire the Signal to Your Phone
url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
payload = {
    "chat_id": TELEGRAM_CHAT_ID,
    "text": message
}

print("Initiating handshake with Telegram...")
response = requests.post(url, json=payload)

if response.status_code == 200:
    print("SUCCESS: Check your Telegram app!")
else:
    print(f"FAILED: Telegram rejected the handshake. Error {response.status_code}")

