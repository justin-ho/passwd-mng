import encFile
import fileManipulator
from userAccountException import UserAccountNotFoundError


# Python file to encrypt and create files using the data provided by input


# Global vars
encrypted_key = ""
id = ""
decrypted_list = {}
element_count = 0


# Initialization of encrypted file
def init():
    global encrypted_key, element_count, decrypted_list
    encFile.check_file_creation()
    element_count = fileManipulator.read_file()
    # if element_count == 1:
    #	 encrypted_key = encFile.create_key()
    #	 id = encFile.id_create()
    # else:
    id = fileManipulator.encoded_info.get(0)
    encrypted_key = fileManipulator.encoded_info.get(1)
    if encrypted_key is None:
        print "ERROR: PROBLEM WITH KEY"
        exit(1)
    encFile.id_verify(id)
    if element_count == 1:
        fileManipulator.add_information(encFile.encrypt(encFile.obtain_key(encrypted_key), encrypted_key))
        fileManipulator.write_file()
    else:
        for index in range(0, element_count + 1):
            encrypted_info = fileManipulator.encoded_info.get(index)
            if index == 0:
                decrypted_list.update({"-id-": encrypted_info})
            elif index == 1:
                decrypted_list.update({"-key-": encrypted_info})
            else:
                decrypted_info = encFile.decrypt(encFile.obtain_key(encrypted_key), encrypted_info)
                decrypted_info_list = str(decrypted_info).split(" ")
                decrypted_list.update({decrypted_info_list[0]: encrypted_info})
                del decrypted_info_list # prevent reading from memory


# Add user information to the file
def add_user(identifier, data):
    decrypted_list.update({identifier: encFile.encrypt(encFile.obtain_key(encrypted_key), data)})
    fileManipulator.add_information(encFile.encrypt(encFile.obtain_key(encrypted_key), data))
    fileManipulator.write_file()


# Returns encoded_info
def get_user_info(identifier):
    return encFile.decrypt(encFile.obtain_key(encrypted_key), decrypted_list.get(identifier))


# Remove user information
def remove_user(identifier):
    """Assumes that decrepted_list and encoded_info maintain the same order."""
    if identifier in decrypted_list:
        fileManipulator.remove_information(decrypted_list.keys().index(identifier))
        del decrypted_list[identifier]
        fileManipulator.write_file()
    else:
        raise UserAccountNotFoundError("[WARNING] User account not found in decrypted store, skipping removal.")

def update_user(identifier, olddata, newdata):
    if identifier in decrypted_list:
        fileManipulator.remove_information(decrypted_list.keys().index(identifier))
        del decrypted_list[identifier]
        decrypted_list.update({identifier: encFile.encrypt(encFile.obtain_key(encrypted_key), newdata)})
        fileManipulator.add_information(encFile.encrypt(encFile.obtain_key(encrypted_key), newdata))
        fileManipulator.write_file()
    else:
        raise UserAccountNotFoundError("[WARNING] User account not found in decrypted store, skipping removal.")


