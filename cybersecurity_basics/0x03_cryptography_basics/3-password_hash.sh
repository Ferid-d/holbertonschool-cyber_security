#!/bin/bash
echo -n "$(openssl rand -base64 12 | cut -c1-16)$1" | openssl dgst -sha512 > 3_hash.txt
