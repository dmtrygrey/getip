# ABOUT:

IP toolkit. Returns IP ranges of couties in different format. Converts IP ranges.

## getip
This script returns county ip range in 3 formats: cidr, nmap and simple. It can be directly called from tool like nmap to pass country range for scanning. Useful to use in conjunction with different tools like nmap.
> This script works only with python2 now.

## iprange
Convert IP range in one of the formats:
* From CIDR to IP list divided by newline.
* From IP range to CIDR format.

## REQUIREMENTS
* python 2.7.14+
* requests==2.18.4+
* netaddr==0.7.19+

## LINUX INSTALL:
```bash
./install.sh
```

## USAGE
```
python2 getip.py -l                   :list all countries
python2 getip.py -c Canada -f nmap    :get Canada ip ranges in nmap format
python2 getip.py -n 70 -f cidr        :get Germany ip ranges in cidr format

nmap -n -sn -sL `python getip.py -n 197`

python3 iprange.py -l 192.168.0.1/24  :produce a list of IPs divided by newline
python3 iprange.py -r 192.168.0.0 192.168.0.255 :produce a list of IPs in CIDR format divided by newline
```

## LICENSE:
This software is released under the GNU General Public License v3.0. See LICENSE.md for details.
