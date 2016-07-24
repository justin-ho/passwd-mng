#!/usr/bin/python

import utils
import UACC_Class
import encryptedFileEditor
import os


def main():
    """User interface for the Password manager"""
    utils.print_splash()
    # if there is no existing file get a new password for authentication
    if os.path.isfile('.eta'):
        # Get the password from the user
        utils.authenticate()
    else:
        utils.new_passwd(utils.get_passwd())
#add init here
    encryptedFileEditor.init()
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
            #add uacc object and pass to elliot
            identifiercheck = utils.get_identifier()
            usernamecheck = utils.get_username()
            passwordcheck = utils.get_passwd()
            userinformation = UACC_Class.UACC(identifiercheck, usernamecheck, passwordcheck)
            if(UACC_Class.UACC.identifier_is_valid(identifiercheck) == True):
                if(UACC_Class.Uacc.username_is_valid(usernamecheck)):
                    if(UACC_Class.UACC.password_is_valid(passwordcheck)):
                        encryptedFileEditor.add_user(identifiercheck, UACC_Class.Uacc.tostring(userinformation))
                    else:
                        print "Does not meet requirements. Make sure it is 8-16 characters long, and no whitespace"
                else:
                    print "Does not meet requirements. Make sure it has less than 16 characters, no whitespace, and is not blank"
            else:
                "Does not meet requirements. Make sure it has no digits, white space, and is not blank. "
        elif user_option == '2':
            print '********Get Credentials********'
            # Use the identifier to get the username and password for the authenticated user
            getidentifier = utils.get_identifier()
            encryptedFileEditor.get_user_info(getidentifier)

        elif user_option == '3':
            print '********Update Credentials********'
            # Use the identifier and update the username and password for that identifier
            utils.get_identifier()
            # Get the new username and password to update
            utils.get_username()
            utils.get_passwd()
        elif user_option == '4':
            print '********Remove Credentials********'
            # Use the identifier and remove the credentials from the datastore
            utils.get_identifier()

    print "Have a nice day!"


if __name__ == "__main__":
    main()
