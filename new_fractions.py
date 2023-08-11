class NewFractions:
    #this is the fraction class
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()

    def _simplify(self):
        """Simplifies the fraction by dividing both numerator and denominator by their common divisor."""
        common_divisor = self._find_common_divisor(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    def _find_common_divisor(self, a, b):
        """Finds the greatest common divisor of two numbers using the Euclidean algorithm."""
        while b != 0:
            a, b = b, a % b
        return a   

    def _find_lcm(self, a, b):
        """Finds the least common multiple of two numbers."""
        #has to be a multiple so find product that works
        return abs(a * b) // self._find_common_divisor(a, b)

    def __add__(self, other):
        """Adds two fractions."""
        return NewFractions(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)

    def __sub__(self, other):
        """Subtracts another fraction from this fraction."""
        return NewFractions(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)

    def __mul__(self, other):
        """Multiplies two fractions."""
        return NewFractions(self.numerator * other.numerator, self.denominator * other.denominator)

    def _equa(self, other) -> bool:
        """Checks if two fractions are equal."""
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __str__(self) -> str:
        """Returns the string representation of the fraction."""
        return f"{self.numerator}/{self.denominator}"
