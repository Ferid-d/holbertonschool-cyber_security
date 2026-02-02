#!/bin/bash
echo -n "$1" | sha256sum | awk '{print $1}' | tr -d '\n' > 1_hash.txt
