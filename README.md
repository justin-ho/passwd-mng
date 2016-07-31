# passwd-manager
Password Manager for ICS 491 Secure coding project

# Recommended Setup
Installation of PyCrypto 2.6.1 is required for the usage. We recommend installing PyCrypto with pip (pip install pycrypto). We have provided the installation source files in case there are any problems. To install, run the setup.py file. In case there are other problems with the installation, it is recommended to instally the Microsoft Visual C++ Compiler for Python 2.7 from this link: https://www.microsoft.com/en-us/download/details.aspx?id=44266.

# V1
# Brandon
* Implemented UACC class
* Integrated the UI with the rest of the modules

# Elliot
* Implemented encryption (encFile.py)
    * Creates UID for file
    * Handles data encoding
* Implemented file read/write (fileManipulation.py)
* Implemented module to handle file encryption using both python files (encryptedFileEditor.py)

# Justin 
* Implemented UI (pass-mgr.py)
    * Created Menu for the user
* Implemented helper functions for the UI (utils.py)
    * Implemented functions to get input from the user
    * Made it so that when a user enters a password it won't be shown in the terminal
    * Created functions to authenticate user and also create a new password for authentication
   

#V2

# Brandon
* Things done for this sprint

# Elliot
* Fixed Windows bugs 
* Created Unit testing for encFile.py

# Justin 
* Things done for this sprint


# To Be Completed
* Implement updating account credentials
* Implement removing an account
