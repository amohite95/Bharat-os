#!/bin/bash
echo "🚀 AMLABSIN: Launching 10-Bot Workflow..."
for i in {1..10}
do
   # We assign each bot a unique 'Role' via environment variables
   pm2 start app.py --name "BOT_" --env ROLE="Hunter_"
done
pm2 save
echo "✅ Farm is Live. Use 'pm2 list' to see your 10 hunters."
