import os
import os.path
import encFile
import fileManipulator


# Python file to encrypt and create files using the data provided by input


#Global vars
encrypted_key = ""
id = ""
decrypted_list = {}
element_count = 0

# Initialization of encrypted file
def init():
    global encrypted_key, element_count, decrypted_list
    encFile.check_file_creation()
    element_count = fileManipulator.read_file()
    if element_count == 0:
        encrypted_key = encFile.create_key()
        id = encFile.id_create()
    else:
        encrypted_key = fileManipulator.encoded_info.get(0)
    encFile.id_verify(encrypted_key)
    if element_count == 0:
        fileManipulator.add_information(encFile.encrypt(encFile.decrypt(os.getcwd(), encrypted_key), encrypted_key))
        fileManipulator.write_file()
    else:
        for index in range(0, element_count + 1):
            encrypted_info = fileManipulator.encoded_info.get(index)
            decrypted_info = encFile.decrypt(encFile.decrypt(os.getcwd(), encrypted_key), encrypted_info)
            if index == 0:
                decrypted_list.update({"-key-": encrypted_info})
            else:
                decrypted_info_list = str(decrypted_info).split(" ")
                decrypted_list.update({decrypted_info_list[0]: encrypted_info})
            decrypted_info_list = "" # Extraneous setting to prevent reading from memory


# Add user information to the file
def add_user(identifier, data):
    decrypted_list.update({identifier, encFile.encrypt(encFile.decrypt(os.getcwd(), encrypted_key), data)})
    fileManipulator.add_information(encFile.encrypt(encFile.decrypt(os.getcwd(), encrypted_key), data))
    fileManipulator.write_file()


# Returns encoded_info
def get_user_info(identifier):
    return encFile.decrypt(decrypted_list.get(identifier))




# Remvoe user information
# def remove_user(data)
# to-be-implemented