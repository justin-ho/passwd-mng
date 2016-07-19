#!/usr/bin/python

import getopt
from utils import *


def main(argv):
    qmessage = 'Usage: pass-mgr -p <password to access the password manager>'
    try:
        opts, args = getopt.getopt(argv, "p:")
    except getopt.GetoptError:
        quitm(qmessage)

    if len(opts) < 1:
        quitm(qmessage)

    passwd = ''

    #  get and set all the user defined options
    for opt, arg in opts:
        if opt == '-p':
            passwd = arg

    if not checkpasswd(passwd):
        quitm(qmessage)

    print passwd


if __name__ == "__main__":
    main(sys.argv[1:])
