#!/bin/bash
source ~/Bharat-os/config/domain.env
echo "🛠️ Validating $DOMAIN for $ADMIN_EMAIL..."
nslookup $DOMAIN | grep "Address" || echo "⚠️ DNS not yet linked to IP."
