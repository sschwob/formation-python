import unittest
from lib.croupier import state_of_the_game, end_game_message

class TestCroupier(unittest.TestCase):
  def test_state_of_the_game_returns_string(self):
    self.assertIsInstance(state_of_the_game(1, 2), str)

  def test_state_of_the_game_contains_scores(self):
    self.assertRegex(state_of_the_game(1, 2), r'score is:? 1', msg = "Should contain player's score")
    self.assertRegex(state_of_the_game(1, 2), r"bank('s)?( score)? is:? 2", msg = "Should contain bank's score")

  def test_end_game_message_returns_string(self):
    self.assertIsInstance(end_game_message(2, 16), str)

  def test_end_game_message_lost_when_over_21(self):
    self.assertRegex(end_game_message(22, 16), r'los[et]', msg = "Should indicate a loss when score is over 21")

  def test_end_game_message_blackjack_when_21(self):
    self.assertRegex(end_game_message(21, 16), r'Black Jack', msg = "Should return 'Black Jack' when score is exactly 21")

  def test_end_game_message_push_on_draw(self):
    self.assertRegex(end_game_message(18, 18), r'push', msg = "Should indicate 'Push' when scores are equal")

  def test_end_game_message_win_when_higher_than_bank(self):
    self.assertRegex(end_game_message(20, 18), r'win', msg = "Should indicate a win when player's score is higher")

  def test_end_game_message_loss_when_lower_than_bank(self):
    self.assertRegex(end_game_message(17, 20), r'lose', msg = "Should indicate a loss when player's score is lower than bank's")

if __name__ == '__main__':
  unittest.main()
