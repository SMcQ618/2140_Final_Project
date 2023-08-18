#will hold all the diff eq stuff and some more vector operations
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.integrate import ode
from scipy.integrate import odeint


class DifferentialEqs:
    def __init__(self, order, variable_symbol, equation):
        """Initializing components of DiffEq

        Args:
            order (int): The order of the differential equation 
            variable: The symbol representing the variable in teh equaiton
            equation (str): the equation has to be a string with all the terms
        """
        self.order = order
        #store the order of the equation(s)
        self.variable_symbol = variable_symbol
        self.variable = sp.Function(variable_symbol)
        #stores the variable symbol
        self.equation = sp.sympify(equation) 
        #converts the equation to a string

    def is_linear(self):
        """
        Determines if the differential equation is linear

        Returns:
            bool: True if the equaiton is linear, otherwise false
        """
        #need to check the highest order
        highest_derivative = self.variable.diff() ** self.order
        linear_check = sp.expand(self.equation - highest_derivative).is_linear(self.variable)
        #in the linear check calls the funciotn, recursive on itself
        return linear_check

    def describe(self):
        """Describes the properties of the differential equation"""
        linearity = ['linear' if self.is_linear else 'nonlinear']
        print(f'This is a {self.order}-th order, {linearity} differential eqution')

    def solve_ode(self):
        """Solves the ordianary differential equations
        
        Returns:
            Eq: the general solution of the ODE.
            """
        solution = sp.dsolve(self.equation, self.variable(self.variable_symbol))
        #use the dsolve to find the solution
        return solution        
    
    def solve_ivp(self, initial_conditions):
        """Solves the equation given the initial condition

        Args:
            initial_conditions (dict): Inital condition for the problem
        
        Returns:
            Eq: the solution of teh IVP
        """
        #define the constants
        constants = sp.symbols('C1: ' + str(self.order + 1))
        #want a particular solution
        particular_solution = self.solve_ode().rhs.subs(constants, sp.solve(self.solve_ode().subs(initial_conditions), constants))
        return particular_solution
    
    def particular_solution(self, particular_conditions):
        """
        Find the particular solution of the differential equation.

        Args:
            particular_conditions (dict): Dictionary of particular conditions {variable: value}.

        Returns:
            sympy.Eq: The particular solution of the differential equation.
        """
        constants = sp.symbols('C1:' + str(self.order + 1))
        particular_solution = self.solve_ode().rhs.subs(constants, sp.solve(self.solve_ode().subs(particular_conditions), constants))
        return particular_solution

    def general_solution(self):
        """
        Find the general solution of the differential equation.

        Returns:
            sympy.Eq: The general solution of the differential equation.
        """
        constants = sp.symbols('C1:' + str(self.order + 1))
        general_solution = self.solve_ode().rhs.subs(constants, constants)
        #solve the equation and gets the gen solu
        return general_solution