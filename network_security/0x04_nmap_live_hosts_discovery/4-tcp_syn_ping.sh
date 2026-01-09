#!/bin/bash
sudo nmap -sS -PE 22,80,443 $1
