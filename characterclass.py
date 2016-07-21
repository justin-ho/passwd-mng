#imports regular expressions
import re

#Created a Username class
class User:

#created a class constructor
    def __init__(self, identifier, username, password):
        #sets the username, password, and identifiers to variables.
        self.identifier = identifier
        self.username = username
        self.password = password

#This while loop checks to see if the identifier meets our requirements. Identifier inputs must not be: blank and only cointains letters
        #any(str.isdigit(c) for c in identifier)== True checks for digits in the user's inputs
        #not identifier checks to see if the user inputs something
        #re.search(r'[\s]', identifier)checks if there is any whitespace in the user's input
        while(any(str.isdigit(c) for c in identifier) == True or not identifier or re.search(r'[\s]', identifier)):
            identifier = raw_input("Please insert an identifier that contains no numbers and contains atleast one character. ")
        self.identifier = identifier

#This while loop checks to see if the username meets our requirements. Username must not be: blank and no longer than 16 characters long
        #len(username) checks the length of the input
        while(not username or len(username) > 16 or re.search(r'[\s]', username)):
            username = raw_input("Please insert a username that contains atleast one character and is less than 16 characters long. ")
        self.username = username

#This while loop checks to see if the password meets our requirements.
# Password must not be: blank and no longer than 16 characters long and not shorter than 8 characters long
        while(len(password) > 16 or len(password)< 8 or re.search(r'[\s]', password)):
            password = raw_input("Please insert a password that contains 8-16 characters and uses no white space.")
        self.password = password


#This tostring prints out the information that it has.
    def tostring(self):
        print "Identifier: ", self.identifier
        print "Username: ", self.username
        print "Password: ", self.password

#Below is test code to test if class is working
#def main():
#    user1 = User("", "", "")
#    User.tostring(user1)
#main()