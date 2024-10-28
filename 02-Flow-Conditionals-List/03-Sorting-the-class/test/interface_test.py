import unittest
import subprocess

class TestInterface(unittest.TestCase):
  def run_interface(self, inputs):
    process = subprocess.Popen(
      ["python3", "./lib/interface.py"],
      stdin  = subprocess.PIPE,
      stdout = subprocess.PIPE,
      stderr = subprocess.PIPE,
      text   = True
    )
    stdout, _ = process.communicate("\n".join(inputs) + "\n")
    return stdout

  def test_three_students(self):
    result = self.run_interface(["Alice", "charlie", "Bob", ""])
    self.assertRegex(result, r"3 students")
    self.assertRegex(result, r"Alice, Bob and charlie")

  def test_four_students(self):
    result = self.run_interface(["Alice", "charlie", "daniel", "Bob", ""])
    self.assertRegex(result, r"4 students")
    self.assertRegex(result, r"Alice, Bob, charlie and daniel")

  def test_one_student(self):
    result = self.run_interface(["Alice", ""])
    self.assertRegex(result, r"1 student")
    self.assertRegex(result, r"Alice")

if __name__ == "__main__":
  unittest.main()
