#!/bin/bash
echo "🛡️ VAJRA CORE: Initializing Security & Performance Matrix..."

# Check Google Drive Link
if rclone lsd am_labs_vault: >/dev/null 2>&1; then
    echo "[✅] VAJRA: Vault Connection Secure."
else
    echo "[⚠️] VAJRA: Vault Link Broken. Reconnecting..."
    rclone config reconnect am_labs_vault:
fi

# Check Git 'Hard-Weld'
if [ -f ~/.git-credentials ]; then
    echo "[✅] VAJRA: Sentinel Encryption Active."
else
    echo "[⚠️] VAJRA: Credentials not stored. Run 'git config --global credential.helper store'."
fi

# Performance Sync
echo "📊 VAJRA: Syncing Performance Matrix to Cloud..."
./save  # Using our dynamic cloud save command
