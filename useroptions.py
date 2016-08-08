import encryptedFileEditor
from UACC_Class import UACC
from userAccountException import UserAccountNotFoundError
import utils


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


def add_creds(user_account):
    """Adds the credentials to the datastore if they are valid."""
    try:
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
    finally:
        del user_account


def get_creds(identifier):
    """Gets the credentials from the datastore using the given identifier if the identifier is valid."""
    try:
        # NOT DEAD CODE, prevents an UnboundLocalError from happening
        user_account = 0
        user_array = 0
        user_info = 0
        user_account = UACC(identifier, '', '')
        if user_account.identifier_is_valid():
            user_info = encryptedFileEditor.get_user_info(identifier)
            user_array = user_info.split(" ")
            if len(user_array) == 3:
                print "\nUsername: ", user_array[1]
                print "Password: ", user_array[2]
            else:
                print "Identifier not found."
        else:
            print identifier_error_message
    except UserAccountNotFoundError, error:
        print error.message
    finally:
        del user_account
        del user_array
        del user_info
        del identifier


def update_creds(identifier):
    """Updates the credentials given the identifier and the new username and password."""
    # NOT DEAD CODE, prevents an UnboundLocalError from happening
    old_useraccount = 0
    new_useraccount = 0
    new_username = 0
    new_passwd = 0
    getting_identification = 0
    user_info = 0
    try:
        tempuser = UACC(identifier, '', '')
        if tempuser.identifier_is_valid():
            user_info = encryptedFileEditor.get_user_info(identifier)
            user_array = user_info.split(" ")
            if len(user_array) == 3:
                getting_identification = user_array[0]
                old_useraccount = UACC(getting_identification, user_array[1], user_array[2])
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
                            encryptedFileEditor.update_user(getattr(new_useraccount, 'identifier'),
                                                            new_useraccount.tostring())
                        else:
                            print password_error_message
                    else:
                        print username_error_message
                        if not new_useraccount.password_is_valid():
                            print password_error_message
                else:
                    print identifier_error_message
                    if not new_useraccount.username_is_valid():
                        print username_error_message
                        if not new_useraccount.password_is_valid():
                            print password_error_message
        else:
            print identifier_error_message
    except UserAccountNotFoundError:
        print '[WARNING] User account could not be found using identifier: \"' + identifier + \
              '\" skipping update.'
    finally:
        del old_useraccount
        del new_useraccount
        del new_username
        del new_passwd
        del getting_identification
        del user_info
        del tempuser


def remove_creds(identifier):
    """Removes the credentials using the given identifier."""
    user_account = UACC(identifier, '', '')
    try:
        if user_account.identifier_is_valid():
            encryptedFileEditor.remove_user(identifier)
        else:
            print identifier_error_message
    except UserAccountNotFoundError:
        print '[WARNING] User account could not be found using identifier: \"' + identifier + \
              '\" skipping removal.'
    finally:
        del identifier
        del user_account
