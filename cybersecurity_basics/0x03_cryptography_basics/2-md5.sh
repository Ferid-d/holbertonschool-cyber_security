#!/bin/bash
echo -n "$1" | md5sum | awk '{print $1}' | tr -d '\n' > 2_hash.txt
