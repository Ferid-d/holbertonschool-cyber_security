#!/bin/bash
for i in {1..255}; do sudo nmap -sn -PR 192.168.65.$i; done
