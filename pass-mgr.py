#!/usr/bin/python

import utils
from UACC_Class import UACC
import encryptedFileEditor
import os
from authenticateException import authenticationError
import useroptions


def main():
    """User interface for the Password manager"""
    utils.print_splash()
    # Menu that the user will see
    menu = '\nWhat would you like to do?\n\n' \
           '1. Add Credentials\n' \
           '2. Get Credentials\n' \
           '3. Update Credentials\n' \
           '4. Remove Credentials\n' \
           '5. Quit\n\n' \
           'Please enter the integer of your choice: '
    # user options
    options = ['1', '2', '3', '4', '5']
    user_option = 0
    try:
        # if there is no existing file get a new password for authentication
        if os.path.isfile('.eta'):
            # Get the password from the user
            utils.authenticate()
        else:
            print 'Welcome to ETA Password Manager! Please enter a password you want to use to access your account.'
            utils.new_passwd(utils.get_passwd())
        # add init here
        encryptedFileEditor.init()
        path = os.getcwd()

        # Run until the user quits the program
        while user_option != '5':
            # Get the Users input option, input must be a valid integer 1, 2, 3, or 4
            user_option = raw_input(menu)
            # User input must be valid to continue
            while user_option not in options:
                print '[ERROR] Improper input, please enter a valid integer (1 - 5).'
                user_option = raw_input(menu)

            # Perform the action based on the users choice
            if user_option == '1':
                print '********Add Credentials********'
                # add uacc object
                identifier = utils.get_identifier()
                username = utils.get_username()
                passwd = utils.get_passwd()
                user_account = UACC(identifier,username, passwd)
                print "\n"
                # Add the credentials using the given identifier, username, password combo
                useroptions.add_creds(user_account)
                # Remove sensitive information from memory
                del user_account
                del identifier
                del username
                del passwd
                # cause a pause after running.
                raw_input("Press enter to continue...")

            elif user_option == '2':
                print '********Get Credentials********'
                # Use the identifier to get the username and password for the authenticated user
                identifier = utils.get_identifier()
                # Call the get_creds function with the given identifier
                useroptions.get_creds(identifier)
                del identifier
                raw_input("Press enter to continue...")

            elif user_option == '3':
                print '********Update Credentials********'
                # Use the identifier and update the username and password for that identifier
                identifier = utils.get_identifier()
                # Get the new username and password to update
                username = utils.get_username()
                passwd = utils.get_passwd()
                # TODO call update_creds function
                del identifier
                del username
                del passwd
                raw_input("Press enter to continue...")

            elif user_option == '4':
                print '********Remove Credentials********'
                # Use the identifier and remove the credentials from the datastore
                identifier = utils.get_identifier()
                # Call remove_creds function
                useroptions.remove_creds(identifier)
                del identifier

                raw_input("Press enter to continue...")
    except authenticationError:
        print '[ERROR] Failed to authenticate. Max amount of tries reached.'
    except (KeyboardInterrupt, EOFError):
        print "\nDetected Keyboard Interrupt, Quitting pass-mgr..."
    finally:
        print "Have a nice day!"


if __name__ == "__main__":
    main()
