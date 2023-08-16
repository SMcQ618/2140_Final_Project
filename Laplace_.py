#will hold all the Laplace transforms and 1rst and 2nd order equations
#will the user have to know the final answer or just give the final answer?
import sympy as sp
from sympy import init_printing 

class Laplace_transforms:
    def __init__(self):
        self.s = sp.symbols('s')
        self.t = sp.symbols('t', positive = True)
        self.eqation = None

    def input_equation(self) -> None:
        """The user will input their equation, with no output."""
        # This should allow the user to input their equation in terms of t or s
        equation_str = input('Enter the equation: ')
        self.equation = sp.sympify(equation_str)

   
    def calculate_laplace(self):
        """Uses sympy to calculate the Laplace transform and the inverse Laplace transform.

        Returns:
            Expression: Depending on what the user inputs, the outputted expression 
            is a result from the Laplace transform.
        """
        if self.equation is not None:
            if self.s in self.equation.free_symbols:
                laplace_transform = sp.laplace_transform(self.equation, self.t, self.s)
                return "Regular Laplace Transform:", laplace_transform[0]
            elif self.t in self.equation.free_symbols:
                # Handling of trigonometric functions and inverse Laplace transform
                equation_exp = self.equation.rewrite(sp.cos, sp.sin, sp.tan)
                inverse_laplace_expr = sp.inverse_laplace_transform(equation_exp, self.s, self.t)
                return "Inverse Laplace Transform:", inverse_laplace_expr
            else:
                # If neither s nor t is in the equation, treat it as a constant
                laplace_of_constant = sp.laplace_transform(self.equation, self.t, self.s)
                return "Laplace Transform:", laplace_of_constant[0]
        else:
            return "No equation was inputted"