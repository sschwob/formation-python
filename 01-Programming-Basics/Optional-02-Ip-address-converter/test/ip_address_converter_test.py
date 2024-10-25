import unittest
from lib.ip import ip_to_num, num_to_ip

ips = {
  "37.160.113.170": 631271850,
  "192.168.0.1": 3232235521
}

class TestIPFunctions(unittest.TestCase):
    def test_ip_to_num(self):
      for ip_address, number in ips.items():
        with self.subTest(ip_address = ip_address, number = number):
          self.assertEqual(ip_to_num(ip_address), number)
    
    def test_num_to_ip(self):
      for ip_address, number in ips.items():
        with self.subTest(ip_address = ip_address, number = number):
          self.assertEqual(num_to_ip(number), ip_address)

if __name__ == '__main__':
  unittest.main()
