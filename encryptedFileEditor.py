import os
import os.path
import encFile
import fileManipulator


# Python file to encrypt and create files using the data provided by input


#Global vars
encrypted_key = ""


# Initialization of encrypted file
def init():
    global encrypted_key
    encFile.check_file_creation()
    element_count = fileManipulator.read_file()
    if element_count == 0:
        encrypted_key = encFile.create_key()
    else:
        encrypted_key = fileManipulator.encoded_info.get(0)
    encFile.id_verify(encrypted_key)
    if element_count == 0:
        fileManipulator.add_information(encFile.encrypt(encFile.decrypt(os.getcwd(), encrypted_key), encrypted_key))
        fileManipulator.write_file()


# Add user information to the file
def add_user(data):
    fileManipulator.add_information(encFile.encrypt(encFile.decrypt(os.getcwd(), encrypted_key),data))
    fileManipulator.write_file()


# Remvoe user information
# def remove_user(data)
# to-be-implemented