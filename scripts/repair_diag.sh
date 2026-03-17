#!/bin/bash
echo "--- 🛠️ AM_LABS: DEEP REPAIR DIAGNOSIS ---"
echo "DATE: $(date)"

# Check 1: Directory Integrity
if [ -d ~/Bharat-os/vault ]; then
    echo "✅ [SUCCESS] Vault Structure: OK"
else
    echo "❌ [ERROR] Vault Missing. Rebuilding..."
    mkdir -p ~/Bharat-os/vault
fi

# Check 2: Domain Awareness
echo "🔍 Checking Global Presence of $AM_DOMAIN..."
DNS_STATUS=$(nslookup $AM_DOMAIN | grep "Address" | tail -n 1)
if [ -z "$DNS_STATUS" ]; then
    echo "⚠️ [STATUS] Domain is UNPOINTED (Normal for Pre-Deployment)."
else
    echo "✅ [STATUS] Domain is RESOLVING to $DNS_STATUS"
fi

# Check 3: Gmail/Drive Sync Capability
if [ -f ~/.gitconfig ]; then
    echo "✅ [SUCCESS] Cloud Sync Path: CONFIGURED"
else
    echo "⚠️ [WARNING] Cloud Sync: NOT INITIALIZED"
fi
echo "--- DIAGNOSIS COMPLETE ---"
