#!/usr/bin/bash
LENGTH={1:-16}
cat /dev/urandom | tr -dc [:alnum:] | head -c$LENGTH
