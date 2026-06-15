import unittest

from src.primesum import is_prime, solve


class TestPrimeSum(unittest.TestCase):
    def test_is_prime_for_small_numbers(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))

    def test_sum_of_primes_in_range(self):
        self.assertEqual(solve(2, 10), '17')
        self.assertEqual(solve(3, 5), '8')
        self.assertEqual(solve(10, 20), '60')

    def test_swapped_bounds(self):
        self.assertEqual(solve(10, 2), '17')
        self.assertEqual(solve(5, 3), '8')

    def test_non_prime_ranges(self):
        self.assertEqual(solve(14, 16), '0')
        self.assertEqual(solve(1, 1), '0')


if __name__ == '__main__':
    unittest.main()
