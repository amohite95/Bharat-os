#!/bin/bash
echo "🔍 Checking amlabs.in status..."
if ping -c 1 amlabs.in &> /dev/null; then
  echo "🚀 STATUS: GLOBAL LIVE!"
else
  echo "⏳ STATUS: Still Propagating. Check back in 1 hour."
fi
