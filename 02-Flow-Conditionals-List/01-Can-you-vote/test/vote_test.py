import unittest
from lib.vote import allowed_to_vote

class TestAllowedToVote(unittest.TestCase):
  def test_01_age_18_or_above(self):
    self.assertTrue(allowed_to_vote(18))
    self.assertTrue(allowed_to_vote(20))

  def test_02_age_below_18(self):
    self.assertFalse(allowed_to_vote(17))

if __name__ == '__main__':
  unittest.main()
