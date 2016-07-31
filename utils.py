#!/usr/bin/python

import sys
import getpass
import hashlib
import os
import authenticateException


def check_passwd(passwd):
    """Checks the validity of the password with the password file"""
    # open the file object
    fileobj = open('.eta', 'rb')
    # split the elements by the $ delimeter
    elements = fileobj.read().split('$')
    try:
        # verify the users password hash with the stored password hash
        if hashlib.pbkdf2_hmac('SHA512', passwd, elements[1], 100000) != elements[2]:
            return False
    finally:
        # flush and close the file object stream
        fileobj.flush()
        fileobj.close()
        # write over the data held in the elements list
        elements[1] = 0
        elements[2] = 0
    return True


def authenticate():
    """Gets the password to authenticate the user
    and allow them to use the password manager"""

    # authentication error message
    auth_message = '[ERROR] Failed to authenticate. Incorrect password.'

    # User gets 3 tries
    for count in range(0, 3):
        # get the authentication password from the user
        password = getpass.getpass('Please enter your password to access the password manager: ')
        if check_passwd(password):
            break
        else:
            print auth_message + ' Attempt ' + str(count + 1) + ' of 3'
            if count == 2:
                raise authenticateException
                #sys.exit(2)


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
    """Prints a banner to the screen"""
    fileobj = open('banner.ascii', 'r')
    print fileobj.read()
    fileobj.close()


def new_passwd(passwd='+35+Pass()'):
    """Creates a new password for authentication"""
    # open the file object for writing
    fileobj = open('.eta', 'wb')
    # obtain the salt
    salt = os.urandom(16)
    while salt.find('$') != -1:
        salt = os.urandom(16)
    # write the salt +  the password hash to the file
    fileobj.write('$' + salt + '$' + hashlib.pbkdf2_hmac('SHA512', passwd, salt, 100000))
    # flush and close the file stream, and write over the salt and the password variables
    salt = 0
    passwd = 0
    fileobj.flush()
    fileobj.close()
