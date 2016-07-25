import os
import os.path
import encFile

# File writer/reader


# Global Vars
storage_file = "storage.enc"
encoded_info = {}


# Reads file - returns the count of elements
def read_file():
    count = 0
    encFile.check_file_creation()
    with open(storage_file) as openedFile:
        for line in openedFile:
            encoded_info.update({count: line})
            count += 1
    return count + 1


# Appends current file with new information
# reads file before writing to confirm that it is not appending or reading the wrong file.
def write_file():
    length = read_file()
    with open(storage_file, "r+") as openedFile:
        for i in range(length + 1, len(encoded_info) + 2):
            if encoded_info.has_key(i):
                openedFile.write(encoded_info.get(i))


# Takes in information to update encoded_info dictionary
# -Assumes that data is encoded already
def add_information(data):
    count = len(encoded_info)
    count += 1 # Since we are using 0 as the first index value
    data = str(data)
    encoded_info.update({count + 1, data})


# Removing information
# def remove_information(key):
