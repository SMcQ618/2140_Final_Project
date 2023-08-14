import unittest
import numpy as np
import math
from Basic_Operations import Operations

class TestOperations(unittest.TestCase):

    def setUp(self):
        self.operations = Operations(x=5, y=3, n=5, value=0.5, numerator=1, denominator=2, angle=45)

    def test_add(self):
        result = self.operations.add()
        self.assertEqual(result, 5 + 3)

    def test_subtract(self):
        result = self.operations.subtract()
        self.assertEqual(result, 5 - 3)

    def test_multiply(self):
        result = self.operations.multiply()
        self.assertEqual(result, 5 * 3)

    def test_divide(self):
        result = self.operations.divide(10, 2)
        self.assertEqual(result, 5)

    def test_modulus(self):
        result = self.operations.modulus()
        self.assertEqual(result, 5 % 3)

    def test_power(self):
        result = self.operations.power(2, 3)
        self.assertEqual(result, 2 ** 3)

    def test_square_root(self):
        result = self.operations.square_root()
        self.assertEqual(result, 5 ** 0.5)

    def test_factorial(self):
        result = self.operations.factorial()
        self.assertEqual(result, 5 * 4 * 3 * 2 * 1)

    def test_exponential(self):
        result = self.operations.exponential(2)
        self.assertAlmostEqual(result, 7.3890560989306495)

    def test_sin(self):
        result = self.operations.sin(45)
        self.assertAlmostEqual(result, math.sin(math.radians(45)))

    def test_cos(self):
        result = self.operations.cos(45)
        self.assertAlmostEqual(result, math.cos(math.radians(45)))
        
    def test_tan(self):
        result = self.operations.tan(30)  # Angle in degrees
        self.assertEqual(result, math.tan(math.radians(30))) #0.5773502691896257)

    def test_absolute_value(self):
        result = self.operations.absolute_value(-5)
        self.assertEqual(result, 5)

    def test_invcos(self):
        result = self.operations.invcos()
        self.assertAlmostEqual(result, 1.0471975511965979)

    def test_invsin(self):
        result = self.operations.invsin()
        self.assertAlmostEqual(result, 0.5235987755982989)

    def test_invtan(self):
        result = self.operations.invtan()
        self.assertAlmostEqual(result, 0.4636476090008061)

    def test_log(self):
        result = self.operations.log(100, 10)
        self.assertEqual(result, 2.0)

    def test_natural_log(self):
        result = self.operations.natural_log(2.718281828459045)
        self.assertEqual(result, 1.0)

    def test_to_decimal(self):
        result = self.operations.to_decimal(1/2)
        self.assertEqual(result, 0.5)

    def test_round_digits(self):
        result = self.operations.round_digits(3.14159, 2)
        self.assertEqual(result, 3.14)

    def test_cube_root(self):
        result = self.operations.cube_root(27, 3)
        self.assertEqual(result, 3.0)

    def test_solve_quadratic_equations(self):
        result = self.operations.solve_quadratic_equations(1, -3, 2)
        self.assertEqual(result, (2.0, 1.0))

    def test_log_with_base(self):
        result = self.operations.log_with_base(8, 2)
        self.assertEqual(result, 3.0)

    def test_negate(self):
        result = self.operations.negate(5)
        self.assertEqual(result, -5)

if __name__ == '__main__':
    unittest.main()
