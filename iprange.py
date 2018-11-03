#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
from netaddr import IPNetwork

__description__ = "This script is converting ip ranges"


def parse_arguments():
    parser = argparse.ArgumentParser(description=__description__, \
            add_help=False)
    parser.add_argument('-l', '--iplist', action='store', dest='iplist')
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
    print("  -h, --help\t" + "Prints this message")
    print("")
    print("Examples:")
    print("  ./" + parser.prog + " --iplist 192.168.0.1/24")


def convert2list(args):
    for ip in IPNetwork(args.iplist):
        print(ip)


def main():
    args = parse_arguments()
    if args.iplist:
        convert2list(args)

if __name__ == "__main__":
    main()
