import unittest
from lib.coach_answer import coach_answer, coach_answer_enhanced

class TestCoachAnswer(unittest.TestCase):
  def test_returns_a_string(self):
    self.assertIsInstance(coach_answer("Hello Coach!"), str)

  def test_replies_with_dont_care_for_statement(self):
    self.assertEqual(coach_answer("I would love to eat some pizza!"), "I don't care, get dressed and go to work!")

  def test_replies_with_silly_question_for_question(self):
    self.assertEqual(coach_answer("Can I eat some pizza?"), "Silly question, get dressed and go to work!")

  def test_replies_with_empty_string_for_work_statement(self):
    self.assertEqual(coach_answer("I am going to work right now!"), "")

class TestCoachAnswerEnhanced(unittest.TestCase):
  def test_returns_a_string(self):
    self.assertIsInstance(coach_answer_enhanced("Hello Coach!"), str)

  def test_replies_with_dont_care_for_statement_non_shouting(self):
    self.assertEqual(coach_answer_enhanced("I would love to eat some pizza!"), "I don't care, get dressed and go to work!")

  def test_replies_with_silly_question_for_question_non_shouting(self):
    self.assertEqual(coach_answer_enhanced("Can I eat some pizza?"), "Silly question, get dressed and go to work!")

  def test_replies_with_empty_string_for_work_statement_non_shouting(self):
    self.assertEqual(coach_answer_enhanced("I am going to work right now!"), "")

  def test_replies_with_motivation_for_shouted_statement(self):
    self.assertEqual(coach_answer_enhanced("I WOULD LOVE SOME PIZZA!"), "I can feel your motivation! I don't care, get dressed and go to work!")

  def test_replies_with_motivation_for_shouted_question(self):
    self.assertEqual(coach_answer_enhanced("CAN I EAT SOME PIZZA?"), "I can feel your motivation! Silly question, get dressed and go to work!")

  def test_replies_with_empty_string_for_shouted_work_statement(self):
    self.assertEqual(coach_answer_enhanced("I AM GOING TO WORK RIGHT NOW!"), "")

if __name__ == '__main__':
  unittest.main()
