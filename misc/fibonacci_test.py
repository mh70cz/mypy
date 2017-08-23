""" test fibonacci """
import unittest
import fibonacci as fib

class TestFib(unittest.TestCase):
    """ test basic functionality """

    fib_0_based_26 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233,
                      377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711,
                      28657, 46368, 75025]
    fib_1_based_26 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233,
                      377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711,
                      28657, 46368, 75025, 121393]

    def wrong_fake_method(self):
        pass

    def test_zero_based(self):
        self.assertEqual(fib.fib_runner(0, 26),
                         self.fib_0_based_26)
        self.assertEqual(fib.fib_runner(0, 26, fib.memo_fibonacci),
                         self.fib_0_based_26)
        self.assertEqual(fib.fib_runner(0, 26, fib.memo_decor_fibonacci),
                         self.fib_0_based_26)
        self.assertEqual(fib.fib_sequence(0, 26), self.fib_0_based_26)

    def test_one_based(self):
        self.assertEqual(fib.fib_runner(1, 27),
                         self.fib_1_based_26)
        self.assertEqual(fib.fib_runner(1, 27, fib.memo_fibonacci),
                         self.fib_1_based_26)
        self.assertEqual(fib.fib_runner(1, 27, fib.memo_decor_fibonacci),
                         self.fib_1_based_26)
        self.assertEqual(fib.fib_sequence(1, 27), self.fib_1_based_26)

    def test_wrong_input_type(self):
        self.assertIsNone(fib.fib_runner("abc", 10))
        self.assertIsNone(fib.fib_runner(1, "abc"))

    def test_wrong_input_values(self):
        self.assertIsNone(fib.fib_runner(-1, 10))        
        self.assertIsNone(fib.fib_runner(2, 1))

    def test_wrong_method(self):
        self.assertIsNone(fib.fib_runner(1, 10, self.test_wrong_method))

unittest.main() 