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
		key = os.getcwd()
		while len(key) < 32:
			key += os.getcwd()
		fileManipulator.add_information(encFile.encrypt(encFile.decrypt(key[:32], encrypted_key), encrypted_key))
		del key
		fileManipulator.write_file()
	else:
		for index in range(0, element_count + 1):
			encrypted_info = fileManipulator.encoded_info.get(index)
			if index == 0:
				decrypted_list.update({"-id-": encrypted_info})
			elif index == 1:
				decrypted_list.update({"-key-": encrypted_info})
			else:
				key = os.getcwd()
				while len(key) < 32:
					key += os.getcwd()
				decrypted_info = encFile.decrypt(encFile.decrypt(key[:32], encrypted_key), encrypted_info)
				del key
				decrypted_info_list = str(decrypted_info).split(" ")
				decrypted_list.update({decrypted_info_list[0]: encrypted_info})
			decrypted_info_list = "" # Extraneous setting to prevent reading from memory


# Add user information to the file
def add_user(identifier, data):
	key = os.getcwd()
	while len(key) < 32:
		key += os.getcwd()
	decrypted_list.update({identifier: encFile.encrypt(encFile.decrypt(key[:32], encrypted_key), data)})
	fileManipulator.add_information(encFile.encrypt(encFile.decrypt(key[:32], encrypted_key), data))
	del key
	fileManipulator.write_file()


# Returns encoded_info
def get_user_info(identifier):
	key = os.getcwd()
	while len(key) < 32:
		key += os.getcwd()
	return encFile.decrypt(encFile.decrypt(key[:32], encrypted_key), decrypted_list.get(identifier))




# Remvoe user information
# def remove_user(data)
# to-be-implemented
