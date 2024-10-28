import unittest
from lib.simple_looping import sum_with_for, sum_with_while

class TestSumWithFor(unittest.TestCase):
  def test_correct_sum_1_to_100(self):
    result = sum_with_for(1, 101)
    self.assertEqual(result, 5050)

  def test_min_greater_than_max(self):
    result = sum_with_for(101, 101)
    self.assertEqual(result, -1)

class TestSumWithWhile(unittest.TestCase):
  def test_correct_sum_1_to_100(self):
    result = sum_with_while(1, 101)
    self.assertEqual(result, 5050)

  def test_correct_sum_7_to_42(self):
    result = sum_with_while(7, 43)
    self.assertEqual(result, 882)

  def test_min_greater_than_max(self):
    result = sum_with_while(101, 100)
    self.assertEqual(result, -1)

if __name__ == '__main__':
  unittest.main()
