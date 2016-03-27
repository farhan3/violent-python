#!/usr/bin/env python

import traceback
from colorama import Fore, init

HOST = "192.168.99.100"


def info(message):
    print '[*] ' + str(message).strip()


def ok(message):
    print Fore.GREEN + '[+] ' + str(message).strip() + Fore.RESET


def warn(message):
    print Fore.YELLOW + '[-] ' + str(message).strip() + Fore.RESET


def error(message):
    print Fore.RED + '[-] ' + str(message).strip() + Fore.RESET


def errorln(message):
    print error(message)
    print ''
