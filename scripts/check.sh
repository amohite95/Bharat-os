#!/bin/bash
echo "--- am_labs Vitals ---"
[ -d ~/Bharat-os ] && echo "✅ Directory: READY"
ping -c 1 amlabs.in &> /dev/null && echo "✅ Domain: LIVE" || echo "⏳ Domain: PROPAGATING"
