import unittest
import numpy as np
from linear_equations import Linear_Eqs, SystemOfEQs

class Test_linear(unittest.TestCase):
    def setUp(self) -> None:
         self.eq = Linear_Eqs(coefficients=[2,3], constant=5)

    def test_solve_for_variable(self):
            solution = self.eq.solve_for_variable()
            #solution = equation.solve_for_variable()
            #expected = np.array([4])
            self.assertAlmostEqual(solution, 2)

    def test_empty_coefficients(self):
        empty_eq = Linear_Eqs(coefficients=[], constant= 5)
        #equation = Linear_Eqs([], 8)
        with self.assertRaises(ValueError):
            empty_eq.solve_for_variable()

    def test_string_representation(self):
        eq_str = str(self.eq)
        self.assertEqual(eq_str, "2x^1 + 3x^0 = 5")
        #equation = Linear_Eqs([2, -3, 1], 7)
        #result = str(equation)
        #expected = "1x^2 + -3x^1 + 2x^0 = 7"
        #self.assertEqual(result, expected)

class TestSystemOfEQs(unittest.TestCase):
   def setUp(self):
        self.equation1 = Linear_Eqs(coefficients=[2, -1], constant=5)
        self.equation2 = Linear_Eqs(coefficients=[3, 2], constant=8)
        self.system = SystemOfEQs()
        self.system.add_equation(self.equation1)
        self.system.add_equation(self.equation2)
        
    def test_add_equation(self):
        self.assertEqual(len(self.system.equations), 2)
        self.assertEqual(self.system.equations[0], self.equation1)
        self.assertEqual(self.system.equations[1], self.equation2)

    def test_solve_eq(self):
        solutions = self.system.solve_eq()
        self.assertAlmostEqual(solutions[0], 3.0)
        self.assertAlmostEqual(solutions[1], 4.0)

    def test_solve_eq_no_equations(self):
        empty_system = SystemOfEQs()
        with self.assertRaises(ValueError):
            empty_system.solve_eq()

if __name__ == '__main__':
    unittest.main()        