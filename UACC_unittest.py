# imports regular expressions
import re
import unittest
import UACC_Class

#Here is the correct inputs for the UACC class functions. This would be accepted by the class
correct_inputs = UACC_Class.UACC("Python", "TeamETA", "Password")

#Below are tests for the identifier funtions only:
    #Requirements for identifier function:
        #Cannot be blank
        #Cannot have whitespace
        #Cannot have digits
Blank_identifier = UACC_Class.UACC("","TeamETA", "Password")
whitespace_identifier = UACC_Class.UACC("Testing Whitespace","TeamETA", "Password")
nodigits_identifier = UACC_Class.UACC("Testing123", "TeamETA", "Password")

#Below are the tests for the username functions only:
    #Requirements for username function:
        #Cannot be blank
        #Cannot be more than 16 characters long
        #Cannot have whitespace
Blank_username = UACC_Class.UACC("Python","", "Password")
lengthtest_username = UACC_Class.UACC("Python","morethansixteencharacterslong", "Password")
exactlengthtest_username = UACC_Class.UACC("Python","exactsixteenchar", "Password")
whitespace_username = UACC_Class.UACC("Python","Team ETA", "Password")

#Below are the tests for the password functions only:
    #Requirements for password function:
        #Cannot be more than 16 characters long
        #Cannot be less than 8 characters long
        #Cannot have whitespace
Blank_password = UACC_Class.UACC("Python","TeamETA", "")
longlength_password = UACC_Class.UACC("Python","TeamETA", "morethansixteencharacterslong")
shortlength_password = UACC_Class.UACC("Python","TeamETA", "four")
exactly16_password = UACC_Class.UACC("Python","TeamETA", "sixteencharacter")
exaclty8_password = UACC_Class.UACC("Python","TeamETA", "haseight")
whitespace_password = UACC_Class.UACC("Python","TeamETA", "Contains Whitespace")

#Below are extra test cases


# Created a Username class
class TestUACC(unittest.TestCase):

    #Identification Tests
    def test_identifier_blank(self):
        identifiertest = UACC_Class.UACC.identifier_is_valid(Blank_identifier)
        self.assertFalse(identifiertest)
    def test_identifier_whitespace(self):
        identifiertest1 = UACC_Class.UACC.identifier_is_valid(whitespace_identifier)
        self.assertFalse(identifiertest1)
    def test_identifier_nodigits(self):
        identifiertest2 = UACC_Class.UACC.identifier_is_valid(nodigits_identifier)
        self.assertFalse(identifiertest2)

    #Username Tests
    def test_username_blank(self):
        usernametest = UACC_Class.UACC.username_is_valid(Blank_username)
        self.assertFalse(usernametest)
    def test_username_length(self):
        usernametest1 = UACC_Class.UACC.username_is_valid(lengthtest_username)
        self.assertFalse(usernametest1)
        #When the user inputs exactly 8 characters long, this will be true because we are accepting 8 or more characters
    def test_username_exactlength(self):
        usernametest2 = UACC_Class.UACC.username_is_valid(exactlengthtest_username)
        self.assertTrue(usernametest2)
    def test_username_whitespace(self):
        usernametest3 = UACC_Class.UACC.username_is_valid(whitespace_username)
        self.assertFalse(usernametest3)

    #Password Tests
    def test_password_blank(self):
        passwordtest = UACC_Class.UACC.password_is_valid(Blank_password)
        self.assertFalse(passwordtest)
    def test_password_longinput(self):
        passwordtest1 = UACC_Class.UACC.password_is_valid(longlength_password)
        self.assertFalse(passwordtest1)
    def test_password_shortinput(self):
        passwordtest2 = UACC_Class.UACC.password_is_valid(shortlength_password)
        self.assertFalse(passwordtest2)
    def test_password_exactly16(self):
        passwordtest3 = UACC_Class.UACC.password_is_valid(exactly16_password)
        self.assertTrue(passwordtest3)
    def test_password_exaclty8(self):
        passwordtest4 = UACC_Class.UACC.password_is_valid(exaclty8_password)
        self.assertTrue(passwordtest4)
    def test_password_whitespace(self):
        passwordtest5 = UACC_Class.UACC.password_is_valid(whitespace_password)
        self.assertFalse(passwordtest5)

if __name__ == "__main__":
    unittest.main()

