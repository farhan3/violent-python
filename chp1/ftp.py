#!/usr/bin/env python

"""
Collection of FTP related functions.

Usage:
    ftp.py getBanner [-v] <host> <port>
    ftp.py getBannerExample [-v]
    ftp.py -h | --help
    ftp.py --version

Options:
    -v          verbose
    -h --help   Show this screen.
    --version   Show version.

Examples:
    ftp.py getBanner 192.168.99.100

"""
import sys
sys.path.insert(0, '../')

from docopt import docopt
from utils import *

import socket


def getBanner(host, port):
    """
    Connects to host:port and returns the banner.
    """
    try:
        s = socket.socket()
        s.connect((host, port))
        banner = s.recv(1024)

        return str(banner).strip()
    except Exception, e:
        error(str(host) + ':' + str(port) + ' ' + str(e))


def getBannerExample():
    ports = [21, 22, 25, 80, 110, 443]

    host = HOST

    for port in ports:
        if getBanner(host, port):
            ok(host + ':' + str(port) + ' ' + getBanner(host, port))


def main():
    socket.setdefaulttimeout(2)

    if args['getBanner']:
        print getBanner(args['<host>'], int(args['<port>']))
    elif args['getBannerExample']:
        getBannerExample()


if __name__ == '__main__':
    args = docopt(__doc__, version='0.1')

    main()
