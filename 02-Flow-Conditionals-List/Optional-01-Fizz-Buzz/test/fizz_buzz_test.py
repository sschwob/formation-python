import unittest
from lib.fizz_buzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
  def test_argument_error_for_number_below_1(self):
    with self.assertRaises(ValueError):
      fizz_buzz(0)

  def test_return_array_for_number_1(self):
    self.assertEqual(fizz_buzz(1), [1])

  def test_return_array_for_number_3(self):
    self.assertEqual(fizz_buzz(3), [1, 2, 'Fizz'])

  def test_return_array_for_number_7(self):
    self.assertEqual(fizz_buzz(7), [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7])

  def test_fizzbuzz_at_15th_element(self):
    self.assertEqual(fizz_buzz(100)[14], 'FizzBuzz')

if __name__ == '__main__':
  unittest.main()
