import requests
import os
import subprocess

TOKEN = "8760942216:AAGV-8ym8qPgetKrL1CJjqs8X0SiyTvlUuM"

def listen_for_kill():
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    try:
        res = requests.get(url).json()
        if res['result']:
            last_msg = res['result'][-1]['message']['text']
            # SECRET COMMAND: Only you know this.
            if last_msg == "/AMLABS_STOP_ALL":
                print("🚨 EMERGENCY SHUTDOWN RECEIVED")
                # Kills all Python processes and PM2
                subprocess.run(["pm2", "stop", "all"])
                requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=6807984967&text=🛑 ALL SYSTEMS HALTED BY DIRECTOR")
    except:
        pass

if __name__ == "__main__":
    while True:
        listen_for_kill()
        import time
        time.sleep(10) # Checks every 10 seconds
