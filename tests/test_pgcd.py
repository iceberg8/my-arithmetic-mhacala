import unittest
from src.my_arithmetic_mhacala.pgcd import pgcd

class TestPgcd(unittest.TestCase):

    def test_pgcd_positive_numbers(self):
        self.assertEqual(pgcd(48, 18), 6)
        self.assertEqual(pgcd(101, 103), 1)
        self.assertEqual(pgcd(56, 98), 14)

    def test_pgcd_negative_numbers(self):
        self.assertEqual(pgcd(-48, 18), 6)
        self.assertEqual(pgcd(48, -18), 6)
        self.assertEqual(pgcd(-48, -18), 6)

    def test_pgcd_with_zero(self):
        self.assertEqual(pgcd(0, 5), 5)
        self.assertEqual(pgcd(5, 0), 5)
        self.assertEqual(pgcd(0, 0), 0)

    def test_pgcd_same_numbers(self):
        self.assertEqual(pgcd(7, 7), 7)
        self.assertEqual(pgcd(0, 0), 0)

if __name__ == '__main__':
    unittest.main()