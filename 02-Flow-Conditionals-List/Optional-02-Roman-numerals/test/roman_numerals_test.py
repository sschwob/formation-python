import unittest
from lib.roman_numerals import new_roman_numeral, old_roman_numeral

class TestRomanNumerals(unittest.TestCase):
  def test_01_old_roman_numeral_1_to_4(self):
    self.assertEqual(old_roman_numeral(1), "I")
    self.assertEqual(old_roman_numeral(2), "II")
    self.assertEqual(old_roman_numeral(3), "III")
    self.assertEqual(old_roman_numeral(4), "IIII")

  def test_02_old_roman_numeral_5_to_9(self):
    self.assertEqual(old_roman_numeral(5), "V")
    self.assertEqual(old_roman_numeral(6), "VI")
    self.assertEqual(old_roman_numeral(7), "VII")
    self.assertEqual(old_roman_numeral(8), "VIII")
    self.assertEqual(old_roman_numeral(9), "VIIII")

  def test_03_old_roman_numeral_10_to_49(self):
    self.assertEqual(old_roman_numeral(10), "X")
    self.assertEqual(old_roman_numeral(11), "XI")
    self.assertEqual(old_roman_numeral(12), "XII")
    self.assertEqual(old_roman_numeral(13), "XIII")
    self.assertEqual(old_roman_numeral(14), "XIIII")
    self.assertEqual(old_roman_numeral(15), "XV")
    self.assertEqual(old_roman_numeral(19), "XVIIII")
    self.assertEqual(old_roman_numeral(20), "XX")
    self.assertEqual(old_roman_numeral(21), "XXI")
    self.assertEqual(old_roman_numeral(25), "XXV")
    self.assertEqual(old_roman_numeral(29), "XXVIIII")
    self.assertEqual(old_roman_numeral(49), "XXXXVIIII")

  def test_04_old_roman_numeral_50_to_99(self):
    self.assertEqual(old_roman_numeral(50), "L")
    self.assertEqual(old_roman_numeral(51), "LI")
    self.assertEqual(old_roman_numeral(99), "LXXXXVIIII")

  def test_05_old_roman_numeral_100_to_499(self):
    self.assertEqual(old_roman_numeral(100), "C")
    self.assertEqual(old_roman_numeral(101), "CI")
    self.assertEqual(old_roman_numeral(149), "CXXXXVIIII")
    self.assertEqual(old_roman_numeral(199), "CLXXXXVIIII")
    self.assertEqual(old_roman_numeral(200), "CC")
    self.assertEqual(old_roman_numeral(499), "CCCCLXXXXVIIII")

  def test_06_old_roman_numeral_500_to_999(self):
    self.assertEqual(old_roman_numeral(500), "D")
    self.assertEqual(old_roman_numeral(501), "DI")
    self.assertEqual(old_roman_numeral(600), "DC")
    self.assertEqual(old_roman_numeral(700), "DCC")
    self.assertEqual(old_roman_numeral(999), "DCCCCLXXXXVIIII")

  def test_07_old_roman_numeral_above_1000(self):
    self.assertEqual(old_roman_numeral(1000), "M")
    self.assertEqual(old_roman_numeral(1001), "MI")
    self.assertEqual(old_roman_numeral(1100), "MC")
    self.assertEqual(old_roman_numeral(1500), "MD")
    self.assertEqual(old_roman_numeral(2000), "MM")
    self.assertEqual(old_roman_numeral(3000), "MMM")

  def test_08_new_roman_numeral_1_to_4(self):
    self.assertEqual(new_roman_numeral(1), "I")
    self.assertEqual(new_roman_numeral(2), "II")
    self.assertEqual(new_roman_numeral(3), "III")
    self.assertEqual(new_roman_numeral(4), "IV")

  def test_09_new_roman_numeral_5_to_9(self):
    self.assertEqual(new_roman_numeral(5), "V")
    self.assertEqual(new_roman_numeral(6), "VI")
    self.assertEqual(new_roman_numeral(7), "VII")
    self.assertEqual(new_roman_numeral(8), "VIII")
    self.assertEqual(new_roman_numeral(9), "IX")

  def test_10_new_roman_numeral_10_to_49(self):
    self.assertEqual(new_roman_numeral(10), "X")
    self.assertEqual(new_roman_numeral(11), "XI")
    self.assertEqual(new_roman_numeral(12), "XII")
    self.assertEqual(new_roman_numeral(13), "XIII")
    self.assertEqual(new_roman_numeral(14), "XIV")
    self.assertEqual(new_roman_numeral(15), "XV")
    self.assertEqual(new_roman_numeral(19), "XIX")
    self.assertEqual(new_roman_numeral(20), "XX")
    self.assertEqual(new_roman_numeral(21), "XXI")
    self.assertEqual(new_roman_numeral(25), "XXV")
    self.assertEqual(new_roman_numeral(29), "XXIX")
    self.assertEqual(new_roman_numeral(49), "XLIX")

  def test_11_new_roman_numeral_50_to_99(self):
    self.assertEqual(new_roman_numeral(50), "L")
    self.assertEqual(new_roman_numeral(51), "LI")
    self.assertEqual(new_roman_numeral(99), "XCIX")

  def test_12_new_roman_numeral_100_to_499(self):
    self.assertEqual(new_roman_numeral(100), "C")
    self.assertEqual(new_roman_numeral(101), "CI")
    self.assertEqual(new_roman_numeral(149), "CXLIX")
    self.assertEqual(new_roman_numeral(199), "CXCIX")
    self.assertEqual(new_roman_numeral(200), "CC")
    self.assertEqual(new_roman_numeral(499), "CDXCIX")

  def test_13_new_roman_numeral_500_to_999(self):
    self.assertEqual(new_roman_numeral(500), "D")
    self.assertEqual(new_roman_numeral(501), "DI")
    self.assertEqual(new_roman_numeral(600), "DC")
    self.assertEqual(new_roman_numeral(700), "DCC")
    self.assertEqual(new_roman_numeral(999), "CMXCIX")

  def test_14_new_roman_numeral_above_1000(self):
    self.assertEqual(new_roman_numeral(1000), "M")
    self.assertEqual(new_roman_numeral(1001), "MI")
    self.assertEqual(new_roman_numeral(1100), "MC")
    self.assertEqual(new_roman_numeral(1500), "MD")
    self.assertEqual(new_roman_numeral(2000), "MM")
    self.assertEqual(new_roman_numeral(3000), "MMM")

if __name__ == "__main__":
  unittest.main()
