#!/bin/bash
john "$1" --format=Raw-SHA256 && john --show "$1" --format=Raw-SHA256 | awk -F: 'NF>1 {print $2}' > 6-password.txt
