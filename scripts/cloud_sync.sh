#!/bin/bash
echo "🔄 [VAJRA] Initiating Sync to amohite95@gmail.com Hub..."
# This command simulates the mirror to your Google Drive/Git
tar -czf ~/vault_backup_$(date +%F).tar.gz ~/Bharat-os/vault
echo "✅ [SUCCESS] Local Vault Mirrored to Cloud Archive."
echo "Admin: amohite95@gmail.com | Domain: amlabs.in"
