#!/bin/bash
echo "$1 ALL=(ALL) NOPASSWD: ALL" | tee /etc/sudoers.d/"$1"
