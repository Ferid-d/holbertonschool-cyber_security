#!/bin/bash
nmap --script http-vuln-cve2017-5638 "$1" | tee vuln_scan_results.txt
