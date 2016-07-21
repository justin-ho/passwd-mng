import os
import os.path
# File encryption python

# Global Vars
storageFile = "stroage.enc"

# Check that file exists
def check():
    path = os.getcwd()
    #Check for windows
    if path.find(":\\"):
        openFile = open(path + "\\" + storageFile, "wb")
        openFile.close()
    #Linux
    else:
        openFile = open("./" + storageFile, "wb")
        openFile.close()

# Verify that the file is correct
def verify():