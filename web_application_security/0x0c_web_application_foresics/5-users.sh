#!/bin/bash
cat auth.log | grep -i 'useradd' | awk '{print $8}' | cut -d'=' -f2 | sort -u | sed 's/,//g' | paste -sd ',' -
