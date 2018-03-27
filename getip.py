#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
import re
import netaddr
import argparse

__description__ = "This script returns ip range of chosen country"
__author__ = "n3tr4k"
__version__ = "0.1"


def parse_arguments():
    parser = argparse.ArgumentParser(description=__description__, add_help=False)
    parser.add_argument('-l', '--list', action='store_true', dest='list', default=False)
    parser.add_argument('-c', '--country', action='store', dest='country', type=str, default="Canada")
    parser.add_argument('-n', '--number', action='store', dest='country_num', type=int, default=None)
    parser.add_argument('-f', '--format', action='store', dest='format', type=str, choices=["cidr","nmap","simple"], default="cidr")
    parser.add_argument('--version', action='version', version='Version: ' + __version__ + '; Author: ' + __author__)
    parser.add_argument('-h', '--help', action='store_true', dest='help', default=False)

    args = parser.parse_args()

    if args.help == True:
        print_help(parser, args)
        sys.exit(0)

    return args


def print_help(parser, args):
    print(parser.description)
    print("")
    print("  -l, --list\t" + "No IPs, just list all countries")
    print("  -c, --country\t" + "Name of country to get IP range")
    print("  -n, --country_num\t" + "Number of country to get IP range")
    print("  -f, --format\t" + "In what fornat to print ips, 'cidr', 'nmap', 'simple'")
    print("  --version\t" + "Show script vesion")
    print("  -h, --help\t" + "Prints this message")
    print("")
    print("Examples:")
    print("  ./" + parser.prog + " -c Canada -f cidr")


def convert_to_range(ip1, ip2):
    ip_1 = re.search(r'([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})', ip1)
    ip_2 = re.search(r'([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})', ip2)
    iprange = ""

    for i in range(1, 5):
        if (int(ip_1.group(i)) < int(ip_2.group(i))):
            iprange += ip_1.group(i) + "-" + ip_2.group(i)
        else:
            iprange += ip_1.group(i)
        if i < 4: iprange += "."

    return iprange


def main(args):
    req = requests.get('https://www.nirsoft.net/countryip/')
    main = req.text.encode('utf-8')
    rawlist = re.findall(r'(<td><a\ href=")([a-z]{2,}\.html)">([A-Z,\�\'\.\(\)\ a-z\-]*)<\/a>', main)

    if args.list == True:
        for i, data in enumerate(rawlist):
            print(str(i) + " - " + data[2])
        return 0

    # get url by country name
    if args.country_num == None:
        url_c = ""
        for k, data in enumerate(rawlist):
            if args.country in data:
                url_c = data[1]
                break
        req = requests.get('https://www.nirsoft.net/countryip/' + url_c)
    else:
        req = requests.get('https://www.nirsoft.net/countryip/' + rawlist[args.country_num][1])

    iphtml = req.text.encode('utf-8')

    iplistraw = re.findall(r'(<tr> <td>)([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})(\ <td>)([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})', iphtml)

    for iprange in iplistraw:
        if args.format == 'cidr':
            cidr = netaddr.iprange_to_cidrs(iprange[1], iprange[3])
            print(cidr[0])
        elif args.format == 'nmap':
            ip = convert_to_range(iprange[1], iprange[3])
            print(ip)
        elif args.format == 'simple':
            print(iprange[1] + " - " + iprange[3])

    return 0


if __name__ == "__main__":
    args = parse_arguments()

    err = main(args)

    if err != 0:
        print("[-] Script failed with error code %s" % str(err))

    sys.exit(0)

