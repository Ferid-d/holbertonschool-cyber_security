#!/bin/bash
hashcat -m 0 -a 1 "$1" wordlist1.txt wordlist2.txt --force > /dev/null 2>&1 && hashcat -m 0 "$1" --show | cut -d: -f2 > 9-password.txt
