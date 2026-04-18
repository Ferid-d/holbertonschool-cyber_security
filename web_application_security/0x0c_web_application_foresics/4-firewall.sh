#!/bin/bash
cat auth.log | grep -i 'iptables' | grep -i 'input' | wc -l
