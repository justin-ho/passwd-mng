#!/usr/bin/python

import getopt
import utils


def main(argv):
    # Get the password from the user
    passwd = utils.get_password()

    # print passwd

    # prompt the user
    menu = '\nWhat would you like to do?\n' \
           '1. Add Credentials\n' \
           '2. Get Credentials\n' \
           '3. Update Credentials\n' \
           'Please enter the integer of your choice (1, 2, or 3): '
    # user options
    options = ['1', '2', '3']

    # Get the Users input option, input must be a valid integer 1, 2, or 3
    user_option = raw_input(menu)
    while user_option not in options:
        print '[ERROR] Improper input, please enter a valid integer.'
        user_option = raw_input(menu)

    if user_option == '1':
        print 'You chose to Add Credentials!!'
    elif user_option == '2':
        print 'You chose to Get Credentials!!'
    elif user_option == '3':
        print 'You chose to Update Credentials!!'


if __name__ == "__main__":
    main(utils.sys.argv[1:])
