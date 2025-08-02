import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 15), 25)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 5), -5)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, -3), -3)
        self.assertEqual(self.calc.add(2.5, 3.7), 6.2)
        self.assertEqual(self.calc.add(-1.5, 2.8), 1.3)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(3, 10), -7)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-2, -8), 6)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 3), -3)
        self.assertEqual(self.calc.subtract(5.7, 2.3), 3.4)
        self.assertEqual(self.calc.subtract(-1.5, 3.2), -4.7)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(7, 8), 56)
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-5, -6), 30)
        self.assertEqual(self.calc.multiply(8, -2), -16)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(10, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        self.assertEqual(self.calc.multiply(7, 1), 7)
        self.assertEqual(self.calc.multiply(1, -9), -9)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertEqual(self.calc.multiply(-1.5, 3), -4.5)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(15, 3), 5.0)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-15, -3), 5.0)
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -3), 0.0)
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertEqual(self.calc.divide(-9.6, 3.2), -3.0)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333333333333)
        self.assertAlmostEqual(self.calc.divide(2, 3), 0.6666666666666666)

    def test_division_by_zero_edge_cases(self):
        test_cases = [1, -1, 100, -100, 0.5, -0.5, 1000000, -1000000]
        for num in test_cases:
            with self.subTest(dividend=num):
                self.assertIsNone(self.calc.divide(num, 0))

    def test_large_numbers(self):
        large_num1 = 1000000
        large_num2 = 999999
        
        self.assertEqual(self.calc.add(large_num1, large_num2), 1999999)
        self.assertEqual(self.calc.subtract(large_num1, large_num2), 1)
        self.assertEqual(self.calc.multiply(large_num1, large_num2), 999999000000)
        self.assertAlmostEqual(self.calc.divide(large_num1, large_num2), 1.000001000001)

    def test_small_decimal_precision(self):
        result = self.calc.add(0.1, 0.2)
        self.assertAlmostEqual(result, 0.3, places=10)
        
        result = self.calc.subtract(0.3, 0.1)
        self.assertAlmostEqual(result, 0.2, places=10)
        
        result = self.calc.multiply(0.1, 0.2)
        self.assertAlmostEqual(result, 0.02, places=10)
        
        result = self.calc.divide(0.3, 0.1)
        self.assertAlmostEqual(result, 3.0, places=10)


if __name__ == '__main__':
    unittest.main()
