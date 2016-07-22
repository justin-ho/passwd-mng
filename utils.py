#!/usr/bin/python

import sys
import getpass


def quit_m(message):
    """Print the message, then quit the program"""
    print message
    sys.exit(2)


def check_passwd(passwd):
    # Empty function stub
    return True


def authenticate():
    """Gets the password to authenticate the user
    and allow them to use the password manager"""

    # authentication error message
    auth_message = '[ERROR] Failed to authenticate. Incorrect password.'

    for count in range(0, 3):
        # get the authentication password from the user
        password = getpass.getpass('Please enter your password to access the password manager: ')
        if check_passwd(password):
            break
        else:
            print auth_message + ' Attempt ' + str(count + 1) + ' of 3'
            if count == 2:
                sys.exit(2)


def get_identifier():
    """Gets the unique site identifier from the user"""
    # get the identifier from the user
    identifier = raw_input('Identifier:')
    return identifier


def get_username():
    """Gets the username from the user"""
    # get the username from the user
    user = raw_input('Username: ')
    return user


def get_passwd():
    """Gets the password from the user"""
    # get the password from the user
    return getpass.getpass('Password:')


def print_splash():
    fo = open('banner.ascii', 'r')
    print fo.read()
    fo.close()
