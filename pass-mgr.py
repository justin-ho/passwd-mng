#!/usr/bin/python

import utils
from UACC_Class import UACC
import encryptedFileEditor
import os
from authenticateException import authenticationError

def main():
    """User interface for the Password manager"""
    utils.print_splash()
    try:
        # if there is no existing file get a new password for authentication
        if os.path.isfile('.eta'):
            # Get the password from the user
            utils.authenticate()
        else:
            utils.new_passwd(utils.get_passwd())
        # add init here
        encryptedFileEditor.init()
        path = os.getcwd()
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
                # add uacc object and pass to elliot
                user_account = UACC(utils.get_identifier(), utils.get_username(), utils.get_passwd())
                print "\n"
                if user_account.identifier_is_valid():
                    if user_account.username_is_valid():
                        if user_account.password_is_valid():
                            print "Added Credentials"
                            encryptedFileEditor.add_user(getattr(user_account, 'identifier'), user_account.tostring())
                        else:
                            print "Password does not meet requirements. Make sure it has:\n" \
                                  "- 8-16 characters long\n"\
                                  "- No whitespace\n"
                    else:
                        print "Username does not meet requirements. Make sure it has:\n" \
                              "- Less than 16 characters\n" \
                              "- No whitespace\n" \
                              "- Is not blank\n"
                        if user_account.password_is_valid() == False:
                            print "Password does not meet requirements. Make sure it has:\n" \
                                "- 8-16 characters long\n" \
                                "- No whitespace\n"
                else:
                    print "Identifier does not meet requirements. Make sure it has:\n"\
                    "- No digits\n"\
                    "- No white space\n"\
                    "- Is not blank. \n"
                    if user_account.username_is_valid() == False:
                        print "Username does not meet requirements. Make sure it has:\n" \
                              "- Less than 16 characters\n" \
                              "- No whitespace\n" \
                              "- Is not blank\n"
                        if user_account.password_is_valid() == False:
                            print "Password does not meet requirements. Make sure it has:\n" \
                                  "- 8-16 characters long\n" \
                                  "- No whitespace\n"
                if path.find(":\\"):
                    os.system("pause")
                else:
                    os.system('read -s -n 1 -p "Press any key to continue..."')
                    print

            elif user_option == '2':
                print '********Get Credentials********'
                # Use the identifier to get the username and password for the authenticated user
                user_info = encryptedFileEditor.get_user_info(utils.get_identifier())
                user_array = user_info.split(" ")
                user_info = ""
                if len(user_array) == 3:
                    user_array[0] = ""
                    print ""
                    print "Username: ", user_array[1]
                    user_array[1] = ""
                    print "Password: ", user_array[2]
                    user_array[2] = ""
                else:
                    print "Identifier not found."
                if path.find(":\\"):
                    os.system("pause")
                else:
                    os.system('read -s -n 1 -p "Press any key to continue..."')
                    print

            elif user_option == '3':
                print '********Update Credentials********'
                # Use the identifier and update the username and password for that identifier
                utils.get_identifier()
                # Get the new username and password to update
                utils.get_username()
                utils.get_passwd()
                print "\nPress any key to continue..."
            elif user_option == '4':
                print '********Remove Credentials********'
                # Use the identifier and remove the credentials from the datastore
                utils.get_identifier()
                print "\nPress any key to continue..."
    except authenticationError:
        print '[ERROR] Failed to authenticate. Max amount of tries reached.'
    except KeyboardInterrupt:
        print "\nDetected Keyboard Interrupt, Quitting pass-mgr..."
    finally:
        print "Have a nice day!"


if __name__ == "__main__":
    main()
