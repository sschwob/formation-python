import unittest
from lib.class_sort import class_sort

class TestWagonSort(unittest.TestCase):
  def test_01_empty_array(self):
    self.assertEqual(class_sort([]), [])

  def test_02_all_caps_sort(self):
    self.assertEqual(class_sort(["BOB", "ALICE", "CHARLIE"]), ["ALICE", "BOB", "CHARLIE"])

  def test_03_case_insensitive_sort(self):
    self.assertEqual(class_sort(["BOB", "alice", "CHARLIE"]), ["alice", "BOB", "CHARLIE"])

if __name__ == "__main__":
  unittest.main()
