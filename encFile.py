import os
try:
	import pwd
except ImportError:
	pass

from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto import Random
import os.path
import time
import sys
import base64

# File encryption python

# Global Vars
storage_file = "storage.enc"
# 0 is linux 1 is windows
os_version = 0
# Username of person
username = ""
# Encrypted key
encrypted_key = ""


# Check that file exists
def check_file_creation():
	global os_version
	path = os.getcwd()
	os_version = get_os()
	# Check for windows
	if path.find(":\\") != -1:
		if not os.path.isfile(storage_file):
			openfile = open(path + "\\" + storage_file, "wb")
			id = id_create()
			openfile.write(id)
			openfile.write("\n")
			key = create_key()
			openfile.write(key)
			openfile.write("\n")
			openfile.close()
		os_version = 1
	# Linux
	else:
		if not os.path.isfile(storage_file):
			openfile = open("./" + storage_file, "wb")
			id = id_create()
			openfile.write(id)
			openfile.write("\n")
			key = create_key()
			openfile.write(key)
			openfile.write("\n")
			openfile.close()

			
# Get OS Type
def get_os():
	global os_version
	path = os.getcwd()
	# Check for windows
	if path.find(":\\") != -1:
		os_version = 1
	return os_version	

	
# Get username
def get_username():
	global username
	get_os()
	# Windows
	if os_version == 1:
		path = os.path.join(os.path.expandvars("%userprofile%"), "Documents and Settings")
		pathsplit = path.split("\\")
		username = pathsplit[3]
	# Linux
	else:
		username = pwd.getpwuid(os.getuid()).pw_name
	return username



# Verify that the file is correct by submitting the verify id from the file
def verify(verify_id):
	result = id_verify(verify_id)
	if not result:
		print "ERROR: INVALID FILE"
		exit()



# Verify unique ID
def id_verify(check_id):
	return id_create() is check_id


# Creation of unique ID for verification
def id_create():
	get_username()
	newhash = SHA256.new()
	newhash.update(username + os.getcwd())
	newid = newhash.digest()
	return newid


# Debugger print function
def debugger():
	print username
	
	
	
# Store encrypted key as global var
def current_key(currentkey):
	global encrypted_key
	encrypted_key = currentkey



# Get key from provided line - recommended to store key in encrypted form until it is needed
def obtain_key(line):
	key = os.getcwd()
	while len(key) < 32:
		key += os.getcwd()
	return decrypt(key[:32], line)


# Create key for file - temporary key generation method
def create_key():
	# Python time code from http://stackoverflow.com/questions/35318841/python-how-to-get-location-time-in-windows
	utc_offset = time.strftime('%z')
	tz_name = time.tzname[0]
	key = os.getcwd()
	while len(key) < 32:
		key += os.getcwd()
	current_key(encrypt(key[:32], username + os.getcwd()))
	return encrypt(key[:32], username + os.getcwd()) # May not be needed


# Encryption from http://stackoverflow.com/questions/12524994/encrypt-decrypt-using-pycrypto-aes-256
bs = 16


# Padding
def pad(s):
	return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)


# Unpadding
def unpad(s):
	return s[:-ord(s[len(s)-1:])]


# Encrypt information
def encrypt(key, raw):
	raw = pad(raw)
	key1 = key[:32]
	key2 = key1.encode("ASCII", 'ignore')
	key3 = key2[:32]
	iv = Random.new().read(AES.block_size)
	cipher = AES.new(key3, AES.MODE_CBC, iv)
	return base64.b64encode(iv + cipher.encrypt(raw))


# Decrypt information
def decrypt(key, enc):
	if enc is None:
		return ""
	enc = base64.b64decode(enc)
	key1 = key[:32]
	key2 = key1.encode("ASCII", 'ignore')
	key3 = key2[:32]
	iv = enc[:16]
	cipher = AES.new(key3, AES.MODE_CBC, iv)
	return unpad(cipher.decrypt(enc[16:]))
