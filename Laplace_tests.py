import unittest
import sympy as sp
from tkinter import Tk
from LaplaceT import LaplaceTransforms

class Test_Laplace(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.app = LaplaceTransforms(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_laplace_transform(self):
        t, s = sp.symbols('t s')
        equation = sp.sin(t) * sp.exp(-t)
        self.app.equation_entry.delete(0, "end")
        self.app.equation_entry.insert(0, str(equation))
        self.app.transform_type.set("Laplace")
        self.app.calculate()
        result = self.app.result_text.get(1.0, "end-1c")
        expected = str(sp.laplace_transform(equation, t, s)[0])
        self.assertIn(expected, result)

    def test_inverse_laplace_transform(self):
        t, s = sp.symbols('t s')
        equation = 1 / (s**2 + 1)
        self.app.equation_entry.delete(0, "end")
        self.app.equation_entry.insert(0, str(equation))
        self.app.transform_type.set("Inverse")
        self.app.calculate()
        result = self.app.result_text.get(1.0, "end-1c")
        inverse_equation = sp.inverse_laplace_transform(equation, s, t).simplify().subs(sp.Heaviside(t), 1).subs(t, 't')
        self.assertEqual(result, str(inverse_equation))

    def test_constant_laplace_transform(self):
        t, s = sp.symbols('t s')
        equation = 5
        self.app.equation_entry.delete(0, "end")
        self.app.equation_entry.insert(0, str(equation))
        self.app.transform_type.set("Laplace")
        self.app.calculate()
        result = self.app.result_text.get(1.0, "end-1c")
        expected = str(5 / s)
        self.assertIn(expected, result)

    def test_no_equation(self):
        self.app.equation_entry.delete(0, "end")
        self.app.transform_type.set("Laplace")
        self.app.calculate()
        result = self.app.result_text.get(1.0, "end-1c")
        expected = "No equation was inputted"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
