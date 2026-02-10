#!/bin/bash
find / -type d -perm -0002 -not -path "/proc/*" -not -path "/sys/*" -not -path "/dev/*" 2>/dev/null | xargs -r chmod o-w
