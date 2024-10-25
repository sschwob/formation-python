import unittest
import subprocess

class TestComputeName(unittest.TestCase):
  def test_name_from_terminal(self):
    process = subprocess.Popen(
        ["python3", "./lib/interface.py"],
        stdin  = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text   = True
    )

    stdout, stderr = process.communicate(input = "Jean\nMichel\nSardou\n")

    self.assertRegex(stdout, r"Jean Michel Sardou")

if __name__ == '__main__':
  unittest.main()
