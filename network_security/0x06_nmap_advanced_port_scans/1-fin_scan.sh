#!/bin/bash
sudo nmap -sF -f -p 80-85 -T2 "$1"
