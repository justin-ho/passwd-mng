import unittest
import encFile


class encfile_testing(unittest.TestCase):

    # Initialization
    def setUp(self):
        pass


    # Needs user input to test for username
    def username(self):
        username_from_user = raw_input("Please enter your username: ")
        self.assertEqual(username_from_user, encFile.get_username())


    # Needs user input to test for OS
    def os_version(self):
        os_from_user = raw_input("Please 0 for Linux and 1 for Windows: ")
        self.assertEqual(os_from_user, encFile.os_version())




if __name__ == "__main__":
    unittest.main()




