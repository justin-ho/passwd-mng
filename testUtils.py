#!/usr/bin/python

import unittest
import os
from utils import check_passwd
from utils import new_passwd
from utils import authenticate


class TestUtils(unittest.TestCase):

    def setUp(self):
        new_passwd('unittestPassword')

    def test_check_passwd_invalid_input(self):
        self.assertFalse(check_passwd('test'))

    def test_check_passwd_valid_input(self):
        self.assertTrue(check_passwd('unittestPassword'))

    def test_authenticate(self):
        self.assertEqual(authenticate(), None)

    def tearDown(self):
        os.remove('.eta')


if __name__ == '__main__':
    unittest.main()
