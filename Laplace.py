#will hold all the Laplace transforms and 1rst and 2nd order equations
#will the user have to know the final answer or just give the final answer?
import sympy
from sympy.abc import f,g,k,n,s,t,y,x
from sympy.integrals import laplace_transform, inverse_laplace_transform
from sympy import init_printing #this will show the fraction expression
import sys #this doe the delta symbol

#to use Euler's 'e' i have to use exp() hopefully I dont get confused
init_printing() 
sys.getdefaultencoding()

class Laplace_transforms:
    """Will convert a function f(t) and/or g(t) into a function in the Laplace domain"""
    def __init__(self, f, g, k, n, s, t, x, y, expression) -> None:
        self.f = f
        self.g = g
        self.k = k
        self.n = n
        self.s = s
        self.t = t
        self.x = x
        self.y = y
        self.function = {
            'k' : ('k/s'),
            't**n' : ('n!/s ** n + 1'), 
            'exp(at)' : ('1 / (s - a)'),
            't**n * exp(at)' : ('n!/ (s - a) ** n + 1'),
            'cos(kt)' : ('s / s**2 + k**2'),
            'sin(kt)' : ('k/s**2 + k**2'),
            'exp(at) * cos(kt)' : ('s-a / (s-a)**2 + k**2'),
            'exp(at) * sin(kt)' : ('k / (s-a)**2 + k**2'),
            't * sin(kt)' : ('2ks/(s**2 + k**2)**2'),
            't * cos(kt)' : ('s**2 - k**2 /(s**2 + k**2)**2'),
            'u(t-a)' : ('(exp(-as))/s'),
            '\u03B4(t-a)' : ('exp(-as)') #this is lowercase delta
            }
        '''self.inverse_tran = {
            'k/s' : 'k',
            'n!/s ** n + 1': ,
            '1 / (s - a)' : ,

        }'''
        self.expression = expression
    
    def tranform(self):
        s, t = sympy.symbol('s, t')
        expression = self.expression

        for func, (transform, i) in self.tranform.items():
            transformed_expression = expression.replace(func, transform)

        laplace_expr = sympy.laplace_transform(transformed_expression, t, s)
        return laplace_expr
    
    def inverse_transform(self):
        inverse_expression = self.expression

        for transform, inverse_func in self.inverse_transforms.items():
            inverse_expression = inverse_expression.replace(transform, inverse_func)

        return inverse_expression
#U = laplace_transform(5, k, s)
# 5 -> 5/s
#print(U[0])

