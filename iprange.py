#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
from netaddr import IPNetwork, iprange_to_cidrs

__description__ = "This script is converting ip ranges"


def parse_arguments():
    parser = argparse.ArgumentParser(description=__description__, \
            add_help=False)
    parser.add_argument('-l', '--iplist', action='store', dest='iplist')
    parser.add_argument('-r', '--iprange', nargs='+', action='store', \
            dest='iprange')
    parser.add_argument('-h', '--help', action='store_true', dest='help', \
            default=False)

    args = parser.parse_args()

    if args.help == True:
        print_help(parser, args)
        sys.exit(0)

    return args


def print_help(parser, args):
    print(parser.description)
    print("")
    print("-l, --iplist\t" + "Converts CIDR ip range into IP list devided "\
                             "by newline.")
    print("-r, -iprange\t" + "Converts IP range to CIDR format,\n " \
                             "input range should contain start IP address " \
                             "and end IP address.")
    print("  -h, --help\t" + "Prints this message")
    print("")
    print("Examples:")
    print("  ./" + parser.prog + " --iplist 192.168.0.1/24")
    print("  ./" + parser.prog + " --iprange 192.168.0.0 192.168.0.255")



def convert2list(args):
    for ip in IPNetwork(args.iplist):
        print(ip)


def range2cidr(args):
    ip1 = args.iprange[0]
    ip2 = args.iprange[1]
    data = iprange_to_cidrs(ip1, ip2)
    for ip in data:
        print(ip)


def main():
    args = parse_arguments()
    if args.iplist:
        convert2list(args)

    if args.iprange:
        range2cidr(args)


if __name__ == "__main__":
    main()
