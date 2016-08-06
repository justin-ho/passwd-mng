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
