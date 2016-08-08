#!/usr/bin/python

import utils
from UACC_Class import UACC
import encryptedFileEditor
import os
from authenticateException import authenticationError
from userAccountException import UserAccountNotFoundError


def main():
    """User interface for the Password manager"""
    utils.print_splash()
    try:
        datastore = 'storage.enc'
        # if there is no existing file get a new password for authentication
        if os.path.isfile('.eta'):
            # Get the password from the user
            utils.authenticate()
        else:
            print 'Welcome to ETA Password Manager!'
            if os.path.isfile(datastore):
                answer = raw_input('A prior instance of the password manager has been found.\n' \
                'If you are creating a new account, the previous data from the password manager will be overwritten.\n' \
                'Are you sure you would like to overwrite the previous data? [y/n] ').strip().lower()
                if answer == 'y':
                    os.remove(datastore)
                else:
                    raise authenticationError("[ERROR] Failed to authenticate. " \
                    "Previous data detected, and .eta file missing.")
            print 'Please enter a password you want to use to access your account. '
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
                identifier = utils.get_identifier()
                username =utils.get_username()
                passwd = utils.get_passwd()
                user_account = UACC(identifier,username, passwd)
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
                # cause a pause after running.
                del identifier
                del username
                del passwd
                del user_account
                raw_input("Press enter to continue...")

            elif user_option == '2':
                print '********Get Credentials********'
                identifier = utils.get_identifier()
                try:
                    # Use the identifier to get the username and password for the authenticated user
                    user_info = encryptedFileEditor.get_user_info(identifier)
                    user_array = user_info.split(" ")
                    del user_info
                    if len(user_array) == 3:
                        print ""
                        print "Username: ", user_array[1]
                        print "Password: ", user_array[2]
                        del user_array
                    else:
                        print "Identifier not found."
                except UserAccountNotFoundError:
                    print '[WARNING] User account could not be found using identifier: \"' + identifier + \
                          '\" skipping retrial.'
                raw_input("Press enter to continue...")

            elif user_option == '3':
                print '********Update Credentials********'
                identifier = utils.get_identifier()
                try:
                    user_info = encryptedFileEditor.get_user_info(identifier)
                    user_array = user_info.split(" ")
                    user_info = ""
                    if len(user_array) == 3:
                        getting_identification = user_array[0]
                        old_useraccount = UACC(getting_identification,user_array[1],user_array[2])
                        print 'Please enter a new username'
                        new_username = utils.get_username()
                        print 'Please enter a new password'
                        new_passwd = utils.get_passwd()
                        new_useraccount = UACC(getting_identification, new_username, new_passwd)
                        print "\n"
                        if new_useraccount.identifier_is_valid():
                            if new_useraccount.username_is_valid():
                                if new_useraccount.password_is_valid():
                                    print "Added New Credentials"
                                    encryptedFileEditor.update_user(getattr(new_useraccount, 'identifier'),new_useraccount.tostring())
                                    del old_useraccount
                                    del new_useraccount
                                    del new_username
                                    del new_passwd
                                    del getting_identification
                                else:
                                    print "Password does not meet requirements. Make sure it has:\n" \
                                          "- 8-16 characters long\n" \
                                          "- No whitespace\n"
                            else:
                                print "Username does not meet requirements. Make sure it has:\n" \
                                      "- Less than 16 characters\n" \
                                      "- No whitespace\n" \
                                      "- Is not blank\n"
                                if new_useraccount.password_is_valid() == False:
                                    print "Password does not meet requirements. Make sure it has:\n" \
                                          "- 8-16 characters long\n" \
                                          "- No whitespace\n"
                        else:
                            print "Identifier does not meet requirements. Make sure it has:\n" \
                                  "- No digits\n" \
                                  "- No white space\n" \
                                  "- Is not blank. \n"
                            if new_useraccount.username_is_valid() == False:
                                print "Username does not meet requirements. Make sure it has:\n" \
                                      "- Less than 16 characters\n" \
                                      "- No whitespace\n" \
                                      "- Is not blank\n"
                                if new_useraccount.password_is_valid() == False:
                                    print "Password does not meet requirements. Make sure it has:\n" \
                                          "- 8-16 characters long\n" \
                                          "- No whitespace\n"

                except UserAccountNotFoundError:
                    print '[WARNING] User account could not be found using identifier: \"' + identifier + \
                          '\" skipping update.'
                raw_input("Press enter to continue...")


            elif user_option == '4':
                print '********Remove Credentials********'
                # Use the identifier and remove the credentials from the datastore
                identifier = utils.get_identifier()
                user_account = UACC(identifier, '', '')
                try:
                    if user_account.identifier_is_valid():
                        encryptedFileEditor.remove_user(identifier)
                    else:
                        print "Identifier does not meet requirements. Make sure it has:\n" \
                              "- No digits\n" \
                              "- No white space\n" \
                              "- Is not blank. \n"
                except UserAccountNotFoundError:
                    print '[WARNING] User account could not be found using identifier: \"' + identifier + \
                      '\" skipping removal.'
                finally:
                    print 'Deleted credentials'
                    del identifier
                    del user_account
                raw_input("Press enter to continue...")
    except authenticationError, autherr:
        print autherr.message
    except (KeyboardInterrupt, EOFError):
        print "\nDetected Keyboard Interrupt, Quitting pass-mgr..."
    finally:
        print "Have a nice day!"


if __name__ == "__main__":
    main()