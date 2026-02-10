#!/bin/bash
find / -xdev -type d -perm -0002 2>/dev/null | tee /dev/tty | xargs -r chmod o-w
