#will hold all the Laplace transforms and 1rst and 2nd order equations
#will the user have to know the final answer or just give the final answer?
import sympy as sp
from sympy import init_printing 

class Laplace_transforms:
    def __init__(self):
        self.s = sp.symbols('s')
        self.t = sp.symbols('t', positive = True)
        self.eqation = None

    def input_equation(self):
        #this should allow the user to input thier equation in tersm of t or s
        equation_str = input('Enter the equation: ')
        self.equation = sp.sympify(equation_str)

   
    def calculate_transform(self):
        if self.equation is not None:
            if self.s in self.equation.free_symbols:
                # free_symbols is used to determine wheter a symbol is one or another in a expression
                laplace_transform = sp.laplace_transform(self.equation, self.t, self.s)
                return "Regular Laplace Transform:", laplace_transform[0]
            elif self.t in self.equation.free_symbols:
                #cos and i guess sine are not being handled well
                equation_exp = self.eqation.rewrite(sp.cos, sp.sin, sp.tan)
                inverse_laplace_expr = sp.inverse_laplace_transform(equation_exp, self.s, self.t)
                return "Inverse Laplace Transform:", inverse_laplace_expr
            else:
                laplace_of_constant = sp.laplace_transform(self.equation, self.t, self.s)
                return "Laplace Transform:", laplace_of_constant[0]
        else:
            return "No equation was inputted"

calculator = Laplace_transforms()

# Input an equation from the user
calculator.input_equation()

# Calculate and print Laplace transform or inverse Laplace transform
result_type, result = calculator.calculate_transform()
print(result_type, result)