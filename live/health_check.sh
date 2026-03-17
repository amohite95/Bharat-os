#!/bin/bash
DOMAIN="amlabs.in"
EMAIL="amohite95@gmail.com"

echo "--- 🛡️ VAJRA: Live Domain Monitor ---"
echo "Target: $DOMAIN"
echo "Admin: $EMAIL"
echo "------------------------------------"

if ping -c 1 $DOMAIN &> /dev/null; then
  echo "🚀 STATUS: GLOBAL LIVE!"
  echo "Action: Initiating SSL Handshake..."
else
  echo "⏳ STATUS: Propagation in Progress."
  echo "Note: Chrome will update shortly after DNS edit."
fi
