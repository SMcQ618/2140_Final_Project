#will hold all the Laplace transforms and 1rst and 2nd order equations
#will the user have to know the final answer or just give the final answer?
import sympy
import math
from sympy.abc import f,g,k,n,s,t,y,x
from sympy.integrals import laplace_transform 
from sympy.integrals import inverse_laplace_transform
from sympy import init_printing #this will show the fraction expression
from sympy import factorial, exp, symbols
import sys #this doe the delta symbol

#to use Euler's 'e' i have to use exp() hopefully I dont get confused
init_printing() 
sys.getdefaultencoding()

class Laplace_transforms:
    """Will convert a function f(t) and/or g(t) into a function in the Laplace domain"""
    def __init__(self, expression) -> None:
        self.expression = expression
        self.function = {
            'k': 'k/s',
            't**n': 'factorial(n) / s**(n + 1)',
            'exp(at)': '1 / (s - a)',
            't**n * exp(at)': 'factorial(n) / (s - a)**(n + 1)',
            'cos(kt)': 's / (s**2 + k**2)',
            'sin(kt)': 'k / (s**2 + k**2)',
            'exp(at) * cos(kt)': '(s - a) / ((s - a)**2 + k**2)',
            'exp(at) * sin(kt)': 'k / ((s - a)**2 + k**2)',
            't * sin(kt)': '2*k*s / (s**2 + k**2)**2',
            't * cos(kt)': '(s**2 - k**2) / (s**2 + k**2)**2',
            'u(t-a)': 'exp(-a*s) / s',
            '\u03B4(t-a)': 'exp(-a*s)'#this is lowercase delta
            }
        self.inverse_tran = {
            'k/s': 'k',
            'factorial(n) / s**(n + 1)': 't**n',
            '1 / (s - a)': 'exp(at)',
            's / (s**2 + b**2)': 'cos(b*t)',
            'b / (s**2 + b**2)': 'sin(b*t)',
            'k / (s**2 + k**2)': 'sin(kt)',
            '(s - a) / ((s - a)**2 + k**2)': 'exp(at) * cos(kt)',
            'k / ((s - a)**2 + k**2)': 'exp(at) * sin(kt)',
            '2*k*s / (s**2 + k**2)**2': 't * sin(kt)',
            '(s**2 - k**2) / (s**2 + k**2)**2': 't * cos(kt)',
            'exp(-a*s) / s': 'u(t-a)',
            'exp(-a*s)': '\u03B4(t-a)'}
    
    def l_tranform(self):
        s, t = sympy.symbols('s t')

        transformed_expression = sympy.sympify(self.expression)

        for func, transform in self.function.items():
            transformed_expression = transformed_expression.replace(func, sympy.sympify(transform))

        laplace_expr = laplace_transform(transformed_expression, t, s)
        return laplace_expr

    def inverse_transform(self):
        inverse_expression = sympy.sympify(self.expression)

        for transform, inverse_func in self.inverse_tran.items():
            inverse_expression = inverse_expression.replace(sympy.sympify(transform), sympy.sympify(inverse_func))
            #takes the transform and switches with the function

        return inverse_laplace_transform(inverse_expression, s, t)
        #this should change s into t
U = laplace_transform(5, k, s)
# 5 -> 5/s
print(U[0])

V = laplace_transform(math.cos(3 * t), t, s)
print(V)
expression = 't**2 + exp(-2*t)'
lt = Laplace_transforms(expression)
laplace_result = lt.l_tranform()
inverse_laplace_result = lt.inverse_transform()

print("Laplace Transform:", laplace_result)
print("Inverse Laplace Transform:", inverse_laplace_result)
