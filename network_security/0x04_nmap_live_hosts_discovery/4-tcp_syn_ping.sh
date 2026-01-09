#!/bin/bash
sudo nmap -sS -PS 22,80,443 $1
