#!/bin/bash
cat auth.log | grep from | grep port | awk '{print $11}' | head -n 1 | sort | uniq
