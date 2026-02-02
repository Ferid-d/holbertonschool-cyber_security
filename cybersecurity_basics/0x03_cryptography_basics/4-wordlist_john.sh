#!/bin/bash
john --wordlist=/usr/share/wordlists/rockyou.txt "$1" --format=Raw-MD5 && john --show "$1" --format=Raw-MD5 | awk -F: 'NF>1 {print $2}' > 4-password.txt
