#!/bin/bash
echo -n "[*] Input the range(xx.xx.nn.xx):"
read range
echo "[*] Now waitng..."
nmap -sn 172.30.8$range.1-254 | grep -o --color=always "172\..*\..*\..*"
echo -e "[*] The end."
