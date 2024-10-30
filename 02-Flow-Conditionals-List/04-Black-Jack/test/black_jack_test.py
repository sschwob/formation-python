import unittest
from lib.black_jack import pick_bank_score, pick_player_card

class TestBlackJack(unittest.TestCase):
  def test_01_pick_bank_score_returns_number(self):
    self.assertIsInstance(pick_bank_score(), (int, float), msg="Should return a number")

  def test_02_pick_bank_score_between_16_and_21(self):
    scores = [pick_bank_score() for _ in range(100)]
    for score in scores:
      self.assertIn(score, range(16, 22), msg="Score should be between 16 and 21")
      
  def test_03_pick_player_card_returns_number(self):
    self.assertIsInstance(pick_player_card(), (int, float), msg="Should return a number")

  def test_04_pick_player_card_between_1_and_11(self):
    scores = [pick_player_card() for _ in range(100)]
    for score in scores:
      self.assertIn(score, range(1, 12), msg="Score should be between 1 and 11")

if __name__ == '__main__':
  unittest.main()
