#!/bin/bash
curl -s -H "Head: $1" -d "$3" "$2" -X "POST"
