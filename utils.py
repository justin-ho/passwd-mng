#!/usr/bin/python

import getpass
import hashlib
import os
from authenticateException import authenticationError
import encryptedFileEditor
from UACC_Class import UACC

# shared error messages to use when validating user input
password_error_message = "Password does not meet requirements. Make sure it has:\n" \
                      "- 8-16 characters long\n" \
                      "- No whitespace\n"
identifier_error_message = "Identifier does not meet requirements. Make sure it has:\n" \
              "- No digits\n" \
              "- No white space\n" \
              "- Is not blank. \n"
username_error_message = "Username does not meet requirements. Make sure it has:\n" \
                  "- Less than 16 characters\n" \
                  "- No whitespace\n" \
                  "- Is not blank\n"


def check_passwd(passwd):
    """Checks the validity of the password with the password file."""
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
        del elements
    return True


def authenticate():
    """Gets the password to authenticate the user
    and allow them to use the password manager."""

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
                raise authenticationError("[ERROR] Failed to authenticate. Max amount of tries reached.")


def get_identifier():
    """Gets the unique site identifier from the user."""
    # get the identifier from the user
    identifier = raw_input('Identifier:')
    return identifier


def get_username():
    """Gets the username from the user."""
    # get the username from the user
    user = raw_input('Username: ')
    return user


def get_passwd():
    """Gets the password from the user."""
    # get the password from the user
    return getpass.getpass('Password:')


def print_splash():
    """Prints a banner to the screen."""
    fileobj = open('banner.ascii', 'r')
    print fileobj.read()
    fileobj.close()


def new_passwd(passwd='+35+Pass()'):
    """Creates a new password for authentication."""
    # open the file object for writing
    fileobj = open('.eta', 'wb')
    # obtain the salt
    salt = os.urandom(16)
    while salt.find('$') != -1:
        salt = os.urandom(16)
    # write the salt +  the password hash to the file
    fileobj.write('$' + salt + '$' + hashlib.pbkdf2_hmac('SHA512', passwd, salt, 100000))
    # flush and close the file stream, and write over the salt and the password variables
    del salt
    del passwd
    fileobj.flush()
    fileobj.close()


def add_creds(user_account):
    """Adds the credentials to the datastore if they are valid."""
    if user_account.identifier_is_valid():
        if user_account.username_is_valid():
            if user_account.password_is_valid():
                encryptedFileEditor.add_user(getattr(user_account, 'identifier'), user_account.tostring())
                print "Added Credentials"
            else:
                print password_error_message
        else:
            print username_error_message
            if not user_account.password_is_valid():
                print password_error_message
    else:
        print identifier_error_message
        if not user_account.username_is_valid():
            print username_error_message
            if not user_account.password_is_valid():
                print password_error_message


def get_creds(identifier):
    """Gets the credentials from the datastore using the given identifier if the identifier is valid."""
    user_account = UACC(identifier, '', '')
    if user_account.identifier_is_valid():
        user_info = encryptedFileEditor.get_user_info(identifier)
        user_array = user_info.split(" ")
        del user_info
        if len(user_array) == 3:
            print "\nUsername: ", user_array[1]
            print "Password: ", user_array[2]
            del user_array
        else:
            print "Identifier not found."
    else:
        print identifier_error_message

# TODO implement update_creds
# def update_creds(identifier, username, passwd):
    """Updates the credentials given the identifier and the new username and password."""

# TODO implement remove_creds
# def remove_creds(identifier):
    """Removes the credentials using the given identifier."""

