import unittest

from lib.experiment import *

class ExperimentTest(unittest.TestCase):
  def test_say_hello(self):
    result = say_hello('Max')
    self.assertEqual(result, 'Hello Max!')
  
  def test_uppercase_a_string(self):
    result = uppercase_a_string('Hello World')
    self.assertEqual(result, 'HELLO WORLD')

  def test_concatenated_strings(self):
    result = concatenated_strings('le lapin', 'mange', 'le chien')
    self.assertEqual(result, 'le chien le lapin mange')
  
  def test_replace_str(self):
    result = replace_str('casanova', 'a', 'o')
    self.assertEqual(result, 'cosonovo')

  def test_get_rid_of_surrounding_whitespaces(self):
    result = get_rid_of_surrounding_whitespaces("   hello   ")
    self.assertEqual(result, "hello")

  def test_it_starts_with(self):
    result = it_starts_with("welcome", "we")
    self.assertEqual(result, True)
  
  def test_add_an_element(self):
    result = add_an_element([2, 3, 7], 1)
    self.assertEqual(result, [2, 3, 7, 1])

  def test_join_two_lists(self):
    result = join_two_lists([1, 2, 3], [4, 5])
    self.assertEqual(result, [1, 2, 3, 4, 5])

  def test_count_number_of(self):
    result = count_number_of(['a', 'b', 'a', 'c'], 'a')
    self.assertEqual(result, 2)

  def test_choose_a_random_number(self):
    list = [1, 4, 6, 9]
    result = choose_a_random_number(list)
    self.assertIn(result, list)

if __name__ == "__main__":
  unittest.main()
