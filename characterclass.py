#Created a Username class
class User:

#created a class constructor
    def __init__(self, username, password, identifier):
        #sets the username, password, and identifiers to variables.
        self.username = username
        self.password = password
        self.identifier = identifier

    def tostring(self):
        print "Here is your identifer: ", self.identifier
        print "Here is your username: ", self.username
        print "Here is your password: ", self.password