#!/bin/bash
john "$1" --wordlist=/usr/share/wordlists/rockyou.txt && john --show "$1" | awk -F: 'NF>1 {print $2}' > 4-password.txt
