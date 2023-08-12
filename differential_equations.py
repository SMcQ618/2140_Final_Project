#will hold all the diff eq stuff and some more vector operations
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp
from scipy.integrate import ode
from scipy.integrate import odeint


class DifferentialEqs:
    def __init__(self, order, is_linear = True):
        self.order = order
        self.is_linear = is_linear

    def describe(self):
        """Describes the properties of the differential equation"""
        linearity = ['linear' if self.is_linear else 'nonlinear']
        print(f'This is a {self.order}-th order, {linearity} differential eqution')

    def solve_ode(self):
        """Solves the ordianary differential equations"""
        if self.is_linear:
            print('Solving the differential equation....')
        else:
            print('Solving the non;inear differential equation...')
        
    def solve_ivp(self, initial_conditions):
        """Solves the equation given the initial condition

        Args:
            initial_conditions (dict): Inital condition for the problem
        """
        print
        print("Solving the initial value problem...")
        print("Initial Conditions:", initial_conditions)