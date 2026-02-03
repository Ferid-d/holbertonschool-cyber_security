#!/bin/bash
find "$1" -type f -perm /6000 -o /4000 -mtime -1 -exec ls -la {} + 2>/dev/null
