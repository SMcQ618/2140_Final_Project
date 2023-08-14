import unittest
import numpy as np
from linear_equations import Linear_Eqs, SystemOfEQs

class Test_linear(unittest.TestCase):

    def test_solve_for_variable(self):
            equation = Linear_Eqs([2], 8)
            solution = equation.solve_for_variable()
            expected = np.array([4])
            np.testing.assert_allclose(solution, expected)

    def test_empty_coefficients(self):
        equation = Linear_Eqs([], 8)
        with self.assertRaises(ValueError):
            equation.solve_for_variable()

    def test_string_representation(self):
        equation = Linear_Eqs([2, -3, 1], 7)
        result = str(equation)
        expected = "1x^2 + -3x^1 + 2x^0 = 7"
        self.assertEqual(result, expected)

class TestSystemOfEQs(unittest.TestCase):

    def test_solve_eq(self):
        equation1 = Linear_Eqs([2, -1], 5)
        equation2 = Linear_Eqs([1, 1], 3)
        system = SystemOfEQs()
        system.add_equation(equation1)
        system.add_equation(equation2)
        solutions = system.solve_eq()
        expected = np.array([2, 1])
        np.testing.assert_allclose(solutions, expected)

    def test_empty_system(self):
        system = SystemOfEQs()
        with self.assertRaises(ValueError):
            system.solve_eq()

if __name__ == '__main__':
    unittest.main()        