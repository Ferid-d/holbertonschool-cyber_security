#!/bin/bash
grep -E "public|private" /etc/snmp/snmpd.conf | grep -v "^#"
