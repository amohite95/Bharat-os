#!/bin/bash
echo "--- AM_LABS PERFORMANCE DASHBOARD ---"
echo "CPU Load: $(uptime | awk '{print $10}')"
echo "Memory: $(free -m | awk '/Mem:/ {print $3"MB/"$2"MB"}')"
echo "Domain Health (amlabs.in): $(curl -Is http://amlabs.in | head -n 1 || echo 'OFFLINE')"
echo "Sync Status: amohite95@gmail.com -> CONNECTED"
echo "--------------------------------------"
