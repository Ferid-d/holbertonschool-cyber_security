#!/bin/bash
CONFIG=$(postconf -h smtpd_tls_security_level 2>/dev/null)
if [ -z "$CONFIG" ] || [ "$CONFIG" == "none" ]; then
    echo "STARTTLS not configured"
else
    echo "smtpd_tls_security_level = $CONFIG"
fi
