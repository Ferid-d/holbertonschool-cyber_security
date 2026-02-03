#!/bin/bash
find "$1" -type f -mtime -1 -perm /4000 -o /6000 2>/dev/null | ls -la
