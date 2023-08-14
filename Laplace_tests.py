import unittest
import sympy as sp
from Laplace_ import Laplace_transforms

class Test_Laplace(unittest.TestCase):

    def setUp(self):
        self.laplace = Laplace_transforms()

    def test_laplace_transform(self):
        equation = sp.sin(self.laplace.t) * sp.exp(-self.laplace.t)
        self.laplace.equation = equation
        result = self.laplace.calculate_transform()
        expected = ("Regular Laplace Transform:", sp.laplace_transform(equation, self.laplace.t, self.laplace.s)[0])
        self.assertEqual(result, expected)

    def test_inverse_laplace_transform(self):
        equation = 1 / (self.laplace.s**2 + 1)
        self.laplace.equation = equation
        result = self.laplace.calculate_transform()
        inverse_equation = sp.inverse_laplace_transform(equation, self.laplace.s, self.laplace.t)
        expected = ("Inverse Laplace Transform:", inverse_equation)
        self.assertEqual(result, expected)

    def test_constant_laplace_transform(self):
        equation = 5
        self.laplace.equation = equation
        result = self.laplace.calculate_transform()
        expected = ("Laplace Transform:", sp.laplace_transform(equation, self.laplace.t, self.laplace.s)[0])
        self.assertEqual(result, expected)

    def test_no_equation(self):
        result = self.laplace.calculate_transform()
        expected = "No equation was inputted"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
