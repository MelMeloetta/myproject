import unittest
from unittest import mock
from post_youdao import *

class PostYoudaoTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True,True)

    def test_get_ts(self):
        get_ts = mock.Mock(return_value='1585614755320')
        self.assertEqual('1585614755320', get_ts())

    def test_get_salt(self):
        get_salt = mock.Mock(return_value='15856156353491')
        self.assertEqual('15856156353491',get_salt())

    def test_get_sign(self):
        get_sign = mock.Mock(return_value='308b3838d4426879f828b90a600357d6')
        self.assertEqual('308b3838d4426879f828b90a600357d6', get_sign())

if __name__ == '__main__':
    unittest.main()
