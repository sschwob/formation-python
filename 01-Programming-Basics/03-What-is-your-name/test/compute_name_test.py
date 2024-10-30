import unittest

from lib.compute_name import compute_name

class ComputeNameTest(unittest.TestCase):
  def test_01_compute_name_return_string(self):
    self.assertIsInstance(compute_name("", "", ""), str)

  def test_02_compute_name_interpolate_str(self):
    result = compute_name("Jean", "Baptiste", "Poquelin")
    self.assertEqual(result, "Jean Baptiste Poquelin")

if __name__ == "__main__":
  unittest.main()
