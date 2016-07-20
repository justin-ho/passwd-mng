import sys


def quit_m(message):
    print message
    sys.exit(2)


def check_passwd(passwd):
    # Empty function stub
    return True


def get_username():
    # get the username from the user
    return 'username'


def get_password():
    # authentication error message
    auth_message = '[ERROR] Failed to authenticate. Incorrect password.'
    # get the password from the user
    password = raw_input('Please enter your password to access the password manager: ')
    if not check_passwd(password):
        quit_m(auth_message)
    return password


def get_identifier():
    # get the identifier from the user
    return 'identifier'
