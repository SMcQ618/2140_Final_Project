import math
import numpy as np
import sympy as sp
#import scipy

#having trouble with scipy..nevermind


class Adv_Methods:
    """Will contain the more complex and advance opperations for calculator. 
    This includes matricies, more on integration, probability, plotting and graphing, 
    vectors, stats, probability, financial calculatos"""
    #notes: should add matrix, 
    def __init__(self, matrix1, matrix2, lower_lim, upper_lim,data, expression,step_size=0.001):
        self.matrix1 = matrix1
        self.martrix2 = matrix2
        self,lower_lim = lower_lim
        self.upper_lim = upper_lim
        self.expression = expression
        self.step_size = step_size
        self.data = data

        

    def matrix_addition(self, matrix1, matrix2):
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise ValueError('Matrix dimensions must match')
        
        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix1[0])):
                row.append(matrix1[i][j] + matrix2[i][j])
            result.append(row)
            return result
    
    def matrix_multiply(self, matrix1, matrix2):
        if len(matrix1[0]) != len(matrix2):
            raise ValueError('Matrix dimensions do not match')
        
        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix2[0])):
                value = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))
                row.append(value)
            result.append(row)
        
        return result
    
    def def_integration(self):#, expression, lower_lim, upper_lim):
        x = sp.Symbol('x')
        integral_exp = sp.sympify(self.expression)
        result = sp.integrate(integral_exp, (x, self.lower_lim, self.upper_lim))
        return result 

        '''x = 0
        x = self.lower_lim
        while x < self.upper_lim:
            total_area += function(x) + self.step_size
            x += self.step_size
        return total_area'''
    
    def summation(self, start, end, expression):
        total = 0
        for i in range(start, end + 1):
            total += eval(expression.replace('x', str(i)))
        return total
    
    def standard_deviation(self, data):
        return np.std(data)
    
    def probability(self, distribution, x):
        return distribution.pdf(x)
    
    def solve_quadratic(self, a,b,c):
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return root1, root2
        elif discriminant == 0:
            root = -b / (2 * a)
            return root
        else:
            return "Complex roots"
        
    def mean(self, data):
        return sum(self.data) / len(self.data)
    
    def mean(self, data):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            mid_sec1 = n // 2 - 1
            mid_sec2 = n // 2
            return (sorted_data[mid_sec1] + sorted_data[mid_sec2]) /2
        else:
            mid_sec = n // 2
            return sorted_data[mid_sec]
        
    def mode(self, data):
        frequency = {}
        for value in data:
            frequency[value] = frequency.get(value, 0) + 1
        max_frequency = max(frequency.values())
        mode_values = [value for value, freq in frequency.items() if freq == max_frequency]
        return mode_values