import unittest
from datetime import date, timedelta

from lib.age_in_days import age_in_days

class AgeInDaysTest(unittest.TestCase):
  def test_01_age_in_days_int(self):
    result = age_in_days(1, 1, 2000)
    self.assertIsInstance(result, int)
  
  def test_02_age_in_days_return(self):
    target_age = 365 * 25
    birthdate = date.today() - timedelta(days = target_age)
    result = age_in_days(birthdate.day, birthdate.month, birthdate.year)
    self.assertEqual(result, target_age)

if __name__ == "__main__":
  unittest.main()
