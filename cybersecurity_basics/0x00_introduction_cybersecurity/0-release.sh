#!/bin/bash
cat /etc/*-release | grep -i "distributor id" | cut -d= -f2 | tr -d '" ' | head -n1
