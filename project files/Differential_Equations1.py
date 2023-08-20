import sympy as sp
from sympy import symbols, Function, Eq, dsolve, Derivative, exp, cos, sin, tan, parse_expr, pprint
import numpy as np
from sympy.solvers.ode.systems import dsolve_system
#redoing the differential equation class

def solve_ode(eq, var, order):
    """Solve a sungle ordinary differential equation.

    Args:
        eq (sympy.Expr): the differential equation
        var (str): The variable to solve for
        order (int): the order of the differential equaiton (1 or 2)

    Returns:
        list: A list of solutions corresponding to the given order
    """
    #have the code recognize 't' as a symbol so it doesn't break
    t = symbols('t')
    #To create an undefined function, pass a string name to Function
    y = Function(var)(t)

    #create a sympy fucntion representing the given dff eq
    solution = dsolve(eq, y)
    return [solution]
    #using a list, allows the function to return a list of solutions
    #dolve is a sympy function that solves ordinary equations
    #returns an object that represents the gen solution with C1,C2 like in class


def is_linear(eq, var):
    """Checks if a inputted equation is linear

    Args:
        eq (sympy.Expr): The differential equation
        var (str): the variable to check against

    Returns:
        bool: Returns true if the equation is linear, false otherwise
    """
    #checks if the equation i slinear by each term
    t = symbols('t')
    y = Function(var)(t)
    for term in eq.args:
        if term.has(Derivative(y, t)):
            #if the coeff of the deriv term is non-zero
            if term.coeff(Derivative(y, t)) != 0:
                return False
            #then check for a higher power
            for var_pow in term.as_poly().terms():
                if var_pow[1] > 1:
                    return False
        elif term.has(y):
            #check if the coeff is non-zero
            if term.coeff(y) != 0:
                return False
    return True

#test to check
def main():
    print('Differential Equation solver\n')
    
    order = 1
    var = "y"

    t = symbols('t')
    y = Function(var)(t)
    #eq = parse_expr(eq_str)

    eq = Eq(Derivative(y, t, order) + 2*y, 0)
    
    if is_linear(eq, var):
        print('The differential equation is linear.')
    else:
        print('The differential equation is not linear.')

    print("Equation:")
    pprint(eq, use_unicode=True)
    
    solutions = solve_ode(eq, var, order)
    print("\nSolutions:")
    for solution in solutions:
        pprint(solution, use_unicode=True)

if __name__ == '__main__':
    main()