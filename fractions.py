class Fractions:
    """This is a class that respresents a fraction and all its math"""
    def __init__(self, numerator, denominator) -> None:
        self.numerator = numerator
        if denominator == 0:
            raise ZeroDivisionError('Denominator cannot be 0')
        self.denominator = denominator
        self._simplify()

    def _simplify(self):
        common_divisor = self._find_common_divi(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    def _find_common_divi(self,a,b):
        while b != 0:
            a,b = b, a % b
        return a   

    def _find_lcm(self, a, b):
        return abs(a * b) // self._find_common_divi(a,b)
    
    def __add__(self, other):
        return Fractions(self.numerator* other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)
        
    def __sub__(self, other):
        return Fractions(self.numerator* other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)
        
    def __mul__(self, other):
        #numerator = self.numerator * other.numerator
        #denominator = self.denominator * other.denominator
        return Fractions(self.numerator * other.denominator, self.denominator * other.numerator)
    
    def _equa(self, other) -> bool:
        return self.numerator * other.denominator == self.denominator * other.numerator
    
    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"