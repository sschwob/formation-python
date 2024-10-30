import unittest
from lib.colorful import is_colorful

class TestColorful(unittest.TestCase):
  def test_01_non_number_input(self):
    self.assertEqual(is_colorful("not_a_number_but_a_string"), False)

  def test_02_colorful_numbers(self):
    colorful_numbers = [0, 1, 23, 263, 987]
    for number in colorful_numbers:
      with self.subTest(number=number):
        self.assertEqual(is_colorful(number), True)

  def test_03_not_colorful_numbers(self):
    not_colorful_numbers = [10, 236, 999]
    for number in not_colorful_numbers:
      with self.subTest(number=number):
        self.assertEqual(is_colorful(number), False)

if __name__ == "__main__":
  unittest.main()
