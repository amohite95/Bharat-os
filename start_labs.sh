#!/data/data/com.termux/files/usr/bin/bash

echo "=================================================="
echo "       am_labs // SYSTEM STARTUP SEQUENCE        "
echo "=================================================="
echo "[1] Initializing Bharat-os Heartbeat..."
python core_engine.py & 

echo "[2] Launching API Gateway on Port 8080..."
python api_gateway.py &

echo "[3] Initializing Global Tunnel..."
cloudflared tunnel --url http://localhost:8080 &

echo "=================================================="
echo " SYSTEM ONLINE. MASTER ADMIN: amohite95@gmail.com"
echo "=================================================="
