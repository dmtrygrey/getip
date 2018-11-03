# ABOUT:

IP toolkit. Returns IP ranges of couties in different format. Converts IP ranges.

## getip
This script returns county ip range in 3 formats: cidr, nmap and simple. It can be directly called from tool like nmap to pass country range for scanning. Useful to use in conjunction with different tools like nmap.

## iprange
Convert IP range in one of the formats (from CIDR to list only now).

## REQUIREMENTS
* python 2.7.14+
* requests==2.18.4+
* netaddr==0.7.19+

## LINUX INSTALL:
```bash
./install.sh
chmod +x getip.py
```

## USAGE
```
./getip.py -l                   -  list all countries
./getip.py -c Canada -f nmap    -  get Canada ip ranges in nmap format
./getip.py -n 70 -f cidr        -  get Germany ip ranges in cidr format

nmap -n -sn -sL `python getip.py -n 197`

python3 iprange.py -l 192.168.0.1/24    - produce a list of IPs divided by newline
```

## DISCLAIMER
I'm not responsible if you use this tool in malicious purposes. Don't scan the whole ip country segments without permission or good reason.

## LICENSE:
This software is released under the GNU General Public License v3.0. See LICENSE.md for details.
