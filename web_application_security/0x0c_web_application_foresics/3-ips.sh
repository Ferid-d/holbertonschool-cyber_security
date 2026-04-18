#!/bin/bash
cat auth.log | grep -E 'sshd.*Accepted password for root' | awk '{print $11}' | sort -n | uniq | wc -l
