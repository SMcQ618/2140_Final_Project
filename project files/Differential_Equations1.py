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
        order (int): the order of the differential equaiton either 1 or 2

    Returns:
        list: A list of solutions corresponding to the given order
    """
    #have the code recognize 't' as a symbol so it doesn't break
    t = symbols('t')#To create an undefined function, pass a string name to Function
    y = Function(var)(t)

    #create a sympy equation representing the given dff eq
    diff_eq = Eq(Derivative(y, t, order), eq)

    if order == 1:
        #for first order use the dsolve direction
        solution = dsolve(diff_eq)
        #dolve is a sympy function that solves ordinary equations
        #returns an object that represents the gen solution with C1,C2 like in class
    else:
        #second or higher converts to a system to solve
        system_eq = [diff_eq.subs(Derivative(t, y, 1), symbols(f'{var}^{i}'))for i in range(order)]
        system = dsolve_system(system_eq, funcs=[y])
        #dsolve_system is another method to solve
        solution = [eq.rhs for eq in system[0]]

    return solution

def is_linear(eq, var):
    """Checks if a inputted equation is linear

    Args:
        eq (sympy.Expr): The differential equation
        var (str): the variable to check against

    Returns:
        bool: Returns true if the equation is linear, false otherwise
    """
    t = symbols('t')
    y = Function(var)(t)
    for term in eq.args:
        if term.has(Derivative(y, t)):
            if term.coeff(Derivative(y, t)) != 0:
                return False
            for var_pow in term.as_poly().terms():
                if var_pow[1] > 1:
                    return False
        elif term.has(y):
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

'''def main():
    print('Differential Equation solver\n')
    
    eq_str = input('Enter the differential equation: ')
    order = int(input('What order is the equation (must be 1st or 2nd): '))
    var = input('Enter the variable to solve for: ')

    t = symbols('t')
    y = Function(var)(t)
    eq = parse_expr(eq_str)

    if is_linear(eq, var):
        print('The differential equation is linear.')
    else:
        print('The differential equation is not linear.')

    pprint(eq, use_unicode = True)
    pprint(solve_ode(eq, var, order), use_unicode = True)

if __name__ == '__main__':
    main()'''

