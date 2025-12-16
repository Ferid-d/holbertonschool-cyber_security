#!/bin/bash
echo "$(sha256sum "$1" | cut -d' ' -f1) $1" | sha256sum -c <(echo "$2  -") 2>/dev/null
