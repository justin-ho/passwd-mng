#imports regular expressions
import re

#Created a Username class
class UACC:

#created a class constructor
    def __init__(self, identifier, username, password):
        #sets the username, password, and identifiers to variables.
        self.identifier = identifier
        self.username = username
        self.password = password

#This function checks to see if the identifier meets our requirements. Identifier inputs must not be: blank and only cointains letters
        #any(str.isdigit(c) for c in identifier)== True checks for digits in the user's inputs
        #not identifier checks to see if the user inputs something
        #re.search(r'[\s]', identifier)checks if there is any whitespace in the user's input
    def identifier_is_valid(self):
        if(any(str.isdigit(c) for c in self.identifier) == True or not self.identifier or re.search(r'[\s]', self.identifier)):
            return False
        else:
            return True

#This function checks to see if the username meets our requirements. Username must not be: blank and no longer than 16 characters long
        #len(username) checks the length of the input
    def username_is_valid(self):
        if(not self.username or len(self.username) > 16 or re.search(r'[\s]', self.username)):
            return False
        else:
            return True

#This function checks to see if the password meets our requirements.
# Password must not be: blank and no longer than 16 characters long and not shorter than 8 characters long
    def password_is_valid(self):
       if(len(self.password) > 16 or len(self.password)< 8 or re.search(r'[\s]', self.password)):
            return False
       else:
            return True

#This tostring prints out the information that it has.
    def tostring(self):
        return self.identifier, self.username, self.password


#Below is test code to test if class is working
def main():
    user1 = UACC("", "", "")
    UACC.username_is_valid(user1)
    UACC.tostring(user1)


if __name__ == "__main__":
    main()
