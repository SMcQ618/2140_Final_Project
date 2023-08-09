import math
import numpy
import scipy

#having trouble with scipy..nevermind


class Adv_Methods:
    """Will contain the more complex and advance opperations for calculator. 
    This includes matricies, more on integration, probability, plotting and graphing, 
    vectors, stats, probability, financial calculatos"""
    #notes: should add matrix, 
    def __init__(self, matrix1, matrix2, lower_lim, upper_lim, step_size=0.001):
        self.matrix1 = matrix1
        self.martrix2 = matrix2
        self,lower_lim = lower_lim
        self.upper_lim = upper_lim
        self.step_size = step_size
        

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
    
    def integration(self, function):
        total_area = 0
        x = self.lower_lim
        while x < self.upper_lim:
            total_area += function(x) + self.step_size
            x += self.step_size
        return total_area