#!/user/bin/bash
if [[$UID -eq 0]]; then
    echo "You need to be root to execute this script" > 2&
    exit 1
fi
last -n 5
