#!/bin/bash
echo "------------------------------------------"
echo "🏛️ AMLABSIN: CLOUD COMMAND CENTER"
echo "------------------------------------------"
echo "1) ALPHA MODE (10 Bots on AI Jackpot - ₹2.9L)"
echo "2) DAILY MODE (10 Bots on Cash Crunch - $100/day)"
echo "3) HYBRID MODE (5 Alpha / 5 Daily)"
read -p "Select Deployment Strategy [1-3]: " choice

if [ $choice -eq 1 ]; then
    sed -i "s/squad_alpha\": {\"bots\": 5/squad_alpha\": {\"bots\": 10/" app.py
    sed -i "s/squad_daily\": {\"bots\": 5/squad_daily\": {\"bots\": 0/" app.py
elif [ $choice -eq 2 ]; then
    sed -i "s/squad_alpha\": {\"bots\": 5/squad_alpha\": {\"bots\": 0/" app.py
    sed -i "s/squad_daily\": {\"bots\": 5/squad_daily\": {\"bots\": 10/" app.py
fi

# Push the command to the cloud
git add app.py
git commit -m "⚡ CEO OVERRIDE: Deployment Strategy Updated"
git push origin main --force
echo "✅ CLOUD RECONFIGURED. 10 BOTS UPDATED."
