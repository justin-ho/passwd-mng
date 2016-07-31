#!/usr/bin/python

import unittest
import os
from utils import check_passwd
from utils import new_passwd
from utils import authenticate
from authenticateException import authenticationError


class TestUtils(unittest.TestCase):

    # setup code to run before each test
    def setUp(self):
        new_passwd('unittestPassword')

    # test check_passwd function with invalid input
    def test_check_passwd_invalid_input(self):
        self.assertFalse(check_passwd('test'))

    # Test the check_passwd function with valid input
    def test_check_passwd_valid_input(self):
        self.assertTrue(check_passwd('unittestPassword'))

    # Test the authenticate function with good input
    def test_authenticate_good(self):
        print 'Authenticate_good test, password to enter: unittestPassword'
        self.assertEqual(authenticate(), None)

    # Test the authenticate function with bad input
    def test_authenticate_bad(self):
        print 'Authenticate_bad test, DO NOT enter: unittestPassword'
        self.assertRaises(authenticationError, authenticate())

    # tear down function to run after each test to cleanup
    def tearDown(self):
        os.remove('.eta')


if __name__ == '__main__':
    unittest.main()
