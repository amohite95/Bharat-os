#!/bin/bash
echo "--- AM_LABS SYSTEM DIAGNOSIS ---"
echo "1. Checking Local Folders..."
[ -d ~/Bharat-os ] && echo "✅ Folder: Bharat-os EXISTS" || echo "❌ Folder: Bharat-os MISSING"
echo "2. Checking Domain (amlabs.in)..."
ping -c 1 amlabs.in &> /dev/null && echo "✅ Domain: REACHABLE" || echo "⏳ Domain: PROPAGATING (Wait 1-4 hours)"
echo "3. Checking Git Sync..."
[ -f ~/.gitconfig ] && echo "✅ Git: CONFIGURED" || echo "⚠️ Git: NEEDS SETUP"
echo "--- DIAGNOSIS COMPLETE ---"
