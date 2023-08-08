import math
import numpy as np
from fractions import Fraction
#needed to add fractions
#this will hold all the basic opperations that will be used in teh calclulator

class Operations():
    """This class will contain the basic operations that a calculator contains.
      THe more advance will be in their own class.
    """
    def __init__(self, mode = "radians"):
        self.mode = mode.lower()
        #sotres the mode as a lowercase

    def select_mode(self):
        #have the user be able to select whether radians or degree
        while True:
            mode = input("Select mode (radians or degrees): ").lower()
            if mode in ["radians", "degrees"]:
                return mode
            else:
                print("Invalid mode. Please choose 'radians' or 'degrees'.")

    def _convert_angle(self, angle):
        if self.mode == "degrees":
            return math.radians(angle)
        return angle

    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            raise ValueError("Cannot divide by zero")
        
    def modulus(self,x, y):
        return x % y
    
    def power(self, x, y):
        return x ** y
    
    def square_root(self, x):
        if x >= 0:
            return math.sqrt(x)
        else:
            raise ValueError(f"Cannot compute square root of {x}")
    
    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        return math.factorial(n)
    
    def exponential(self, n):
        return math.exp(n)
    
    def sin(self, angle):
        angle = self._convert_angle(angle)
        return math.sin(angle)
    
    def cos(self, angle):
        angle = self._convert_angle(angle)
        return math.cos(angle)
    
    def tan(self, angle):
        angle = self._convert_angle(angle)
        return math.tan(angle)
    
    def absolute_value(self, x):
        return abs(x)
    
    def invcos(self, value):
        result = math.acos(value)
        if self.mode == "degrees":
            return math.degrees(result)
        return result
    
    def invsin(self, value):
        result = math.asin(value)
        if self.mode == "degrees":
            return math.degrees(result)
        return result

    def invtan(self, value):
        result = math.atan(value)
        if self.mode == "degrees":
            return math.degrees(result)
        return result
    
    def log(self, x, base = 10):
        return math.log(x, base)
    
    def natural_log(self, x):
        return math.log(x)
    
    def to_fractions(self, numerator, denominator):
        return Fraction(numerator, denominator)
    
    def to_decimal(self, fraction):
        return float(fraction)
    
    def round_digits(self, number, digits):
        return round(number, digits)
    
    def cube_root(self, x, index):
        return x ** (1 / index)
    #this is done so that any index for the root can be done

    def solve_linear_equations(self, a, b):
        if a == 0:
            if b == 0:
                return print("Infinite solutions")
            return print("No solutions")
        return -b / a
    
    def solve_quadratic_equations(self, a, b, c):
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
        
    def summation(self, start, end, expression):
        total = 0
        for i in range(start, end + 1):
            total += eval(expression.replace('x', str(i)))
        return total
    
    def log_with_base(self, x, base):
        return math.log(x, base)
    
    def negate(self, x):
        return -x
    