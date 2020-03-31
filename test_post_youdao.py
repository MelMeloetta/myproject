import unittest
from unittest import mock
from post_youdao import *

class PostYoudaoTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True,True)

    def test_get_ts(self):
        get_ts=mock.Mock(return_value= '1585615635349')
        self.assertEqual('1585615635349',get_ts())


if __name__ =='__main__':
    unittest.main()