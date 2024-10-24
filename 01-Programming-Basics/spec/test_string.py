import unittest

from lib.test import *

class TestString(unittest.TestCase):
  def test_hello(self):
    result = hello()
    self.assertEqual(result, 'Hello')

if __name__ == "__main__":
  unittest.main()
