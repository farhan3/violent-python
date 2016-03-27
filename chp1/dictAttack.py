#!/usr/bin/env python

"""
Perform Dictionary Attack using the provided password file and dictionary, 
along with the algorithm, e.g. DES, SHA512.

Usage:
    dictAttack.py dictAttack [-v] <passwdFileName> <dictionary> <algorithm>
    dictAttack.py dictAttackExample [-v]
    dictAttack.py -h | --help
    dictAttack.py --version

Options:
    -v          verbose
    -h --help   Show this screen.
    --version   Show version.

Examples:
    dictAttack.py dictAttack passwords.txt dictionary.txt DES

"""
import sys
sys.path.insert(0, '../')

from docopt import docopt
from utils import *

import crypt


def checkDict(dictFileName, passwdHash, algorithm='DES'):
    """
    Generate hashes for the words in the dictionary file, using the first
    two bytes of the passwdHash as the salt.

    If a matching word is found in the dictionary, return it, otherwise return
    None.
    """
    salt = passwdHash[0:2]

    dictFile = open(dictFileName, 'r')
    for word in dictFile.readlines():
        word = word.strip()
        hashValue = crypt.crypt(word, salt)
        if hashValue == passwdHash:
            ok('Found password: ' + word)
            return word

    warn('Password not found.')
    return None


def dictAttack(passwdFileName, dictFileName, algorithm='DES'):
    """
    Try to crack the passwords in the password file by using a dictionary 
    attack. The words to use are provide dby the dictionary file.
    """
    passwdFile = open(passwdFileName)
    for line in passwdFile.readlines():
        if verbose:
            info('Processing line in ' + passwdFileName + ': ' + line)

        if ':' in line:
            splits = line.split(':')
            uid = splits[0].strip()
            passwdHash = splits[1].strip()

            info('Cracking password of user: ' + uid)
            checkDict(dictFileName, passwdHash, algorithm)


def dictAttackExample():
    dictAttack('res/passwords.txt', 'res/dictionary.txt', algorithm='DES')


def main():
    if args['dictAttack']:
        print dictAttack(args['<passwdFileName>'],
                         args['<dictionary>'], args['<algorithm>'])
    elif args['dictAttackExample']:
        dictAttackExample()


if __name__ == '__main__':
    args = docopt(__doc__, version='0.1')
    verbose = args['-v']

    main()
