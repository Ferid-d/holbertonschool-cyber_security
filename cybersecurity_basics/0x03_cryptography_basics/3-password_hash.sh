#!/bin/bash
SALT=$(openssl rand -base64 12 | cut -c1-16)
echo -n "${SALT}$1" | openssl dgst -sha512 > 3_hash.txt
