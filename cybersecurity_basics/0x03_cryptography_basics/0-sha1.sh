#!/bin/bash
echo -n "$1" | sha1sum | awk '{print $1}' | tr -d '\n' > 0_hash.txt
