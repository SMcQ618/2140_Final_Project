import math
import numpy as np
import sympy as sp
import scipy.integrate 
from Advance_abstr import Calculations

#Holds the more advance methods for a calculator

class Adv_Methods:
    """Will contain the more complex and advance opperations for calculator. 
    This includes matricies, more on integration, probability, plotting and graphing, 
    vectors, stats, probability, financial calculatos"""

    def __init__(self,  lower_lim, upper_lim,data, expression,num_intervals,step_size=0.001):
        self.lower_lim = lower_lim
        self.upper_lim = upper_lim
        self.expression = expression
        self.step_size = step_size
        self.data = data
        self.num_intervals = num_intervals


    def def_integration(self):
        """Calculates the definite integral of an expression over a specifiedinterval. 
           Uses symbol integration to evaluate the definite integral of an expression with respect 
           to usually 'x' over the interval [lower_lim, upper_lim]

        Returns:
            float: The result of the definite integral
        """
        x = sp.Symbol('x')
        integral_exp = sp.sympify(self.expression)
        result = sp.integrate(integral_exp, (x, self.lower_lim, self.upper_lim))
        return result 
    
    def summation(self, start, end, expression):
        """Calculates the summation of an expression for a specified range

        Args:
            start (int): The starting value of the range
            end (int): The ending value of the range
            expression (str): The expression to be evaluated for each value in the range.
            Using 'x' as the palceholder for the variable

        Returns:
            float: The summation result
        """
        total = 0
        for i in range(start, end + 1):
            total += eval(expression.replace('x', str(i)))
        return total
        
    @staticmethod
    def mean(self) -> float:
        """Calculates the mean (average) of a dataset.

        Args:
            data (list): A list of numeric values.

        Returns:
            float: The calculated mean of the dataset.
        """
        return sum(self.data) / len(self.data)
    
    @staticmethod
    def median(self) -> float:
        """Calculate the median of the set

        Args:
            data(list): A list of the numeric values

        Returns:
            float: The calulated median of the set
        """
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            mid_sec1 = n // 2 - 1
            mid_sec2 = n // 2
            return (sorted_data[mid_sec1] + sorted_data[mid_sec2]) /2
        else:
            mid_sec = n // 2
            return sorted_data[mid_sec]
        
    @staticmethod
    def mode(self) -> list:
        """Calculated the mode of the set

        Args:
            data (list): A list of values.

        Returns:
            list: A list of mode values in the dataset.
        """
        frequency = {}
        for value in self.data:
            frequency[value] = frequency.get(value, 0) + 1
        max_frequency = max(frequency.values())
        mode_values = [value for value, freq in frequency.items() if freq == max_frequency]
        return mode_values
    
    #add rieman sum or Laplace?
    def Riemann_sum(self, method = 'left'):
        """Approximates the definite integral using Riemann Sum.

        Args:
            expression (str): The expression to be integrated.
            lower_limit (float): The lower limit of integration.
            upper_limit (float): The upper limit of integration.
            num_intervals (int): The number of intervals or subintervals.
            method (str, optional): The Riemann Sum method: 'left', 'right', or 'midpoint'.
                                    Defaults to 'left'.

        Returns:
            float: The approximate result of the definite integral using Riemann Sum.
        """
        x = sp.Symbol('x')
        integral_exp = sp.sympify(self.expression)
        interval_size = (self.upper_lim - self.lower_lim) / self.num_intervals

    def integrand(x):
            """Helper function to represent the integrand of the expression. And valuates the
            intergrand at the specified value of x 

            Args:
                x (float): The value of teh variable of integration

            Returns:
                float: The value of the integrand expression at the given x value.
            """
            return integral_exp.subs(x, x)
        
        total_sum = 0
            for i in range(self.num_intervals):
                if method == 'left':
                    value = integrand(self.lower_limit + i * interval_size)
                elif method == 'right':
                    value = integrand(self.lower_limit + (i + 1) * interval_size)
                elif method == 'midpoint':
                    value = integrand(self.lower_limit + (i + 0.5) * interval_size)
                total_sum += value
        #calculate teh approximate integral using the rieman sum
            approximate_integral =  total_sum * interval_size
    return approximate_integral
    
print(int("43"))