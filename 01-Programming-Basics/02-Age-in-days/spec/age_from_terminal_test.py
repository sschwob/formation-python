import unittest
import subprocess
from lib.age_in_days import age_in_days

class TestInterface(unittest.TestCase):
  def test_should_print_out_age_calculated(self):
    y, m, d = 1986, 11, 18
    
    # Lancer le script interface.py via subprocess
    process = subprocess.Popen(
        ["python3", "lib/interface.py"], 
        stdin  = subprocess.PIPE, 
        stdout = subprocess.PIPE, 
        stderr = subprocess.PIPE,
        text   = True
    )
    
    # Envoyer les entrées (année, mois, jour)
    stdout, _ = process.communicate(input = f"{y}\n{m}\n{d}\n")
    
    # Calculer l'âge avec la fonction
    age = age_in_days(d, m, y)
    
    # Vérifier que la sortie correspond à ce qui est attendu
    self.assertRegex(stdout, rf"You are {age} days old")

if __name__ == '__main__':
    unittest.main()
