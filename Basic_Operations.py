import math
#Holds all the basic opperations that will be used in teh calclulator

class Operations:
    """This class will contain the basic operations that a calculator contains.
      THe more advance will be in their own class.
    """
    def __init__(self, x, y, n, value, numerator, denominator, angle, mode = "radians",):
        self.mode = mode.lower()
        self.x = x
        self.y = y
        self.n = n
        self.value = value
        self.numerator = numerator
        self.denominator = denominator
        self.angle = angle

        #sotres the mode as a lowercase

    def select_mode(self):
        """Allows the user to select if they want to be in radians or degree mode

        Returns:
            string : returns the mode either radians or degrees
        """
        #have the user be able to select whether radians or degree
        while True:
            mode = input("Select mode (radians or degrees): ").lower()
            if mode in ["radians", "degrees"]:
                return mode
            else:
                print("Invalid mode. Please choose 'radians' or 'degrees'.")

    def _convert_angle(self) -> float:
        """Converts an angle between degrees and radians based on the current mode.
        Args:
            angle (float): the anlge to be converted
        Returns:
            float: The angle converted in degrees or radians
        """
        if self.mode == "degrees":
            return math.degrees(self.angle)
        else:
            return math.radians(self.angle)

    def add(self) -> int:
        """Is going to be the addition method for the calculator
        Intputs:
            int: two numbers that are both integers
        Returns:
            int: Is the sum of two numbers
        """
        return self.x + self.y
    
    def subtract(self) -> int:
        """Is going to be the subtraction method for the calculator
        Intputs:
            int: two numbers that are both integers
        Returns:
            int: Is the difference of two numbers
        """
        return self.x - self.y 
        #should work even if the the output is a negative number
    
    def multiply(self)-> int:
        """Is going to be the multiplication method for the calculator
        Intputs:
            int: two numbers that are both integers
        Returns:
            int: Is the product of two numbers
        """
        return self.x * self.y
    
    def divide(self, x, y)-> int:
        #wasn't sure if i wanted all the functions to use the self method so i did a mix
        """Is going to be the division method for the calculator
        Intputs:
            int: two numbers that are both integers
        Returns:
            int: Is the quotient of two numbers
        """
        if y != 0:
            return x / y
        else:
            raise ValueError("Cannot divide by zero")
        
    def modulus(self)-> int:
        """Yields the remainder when the number is divided by another number

        Returns:
            int: The remainder of the two numbers
        """
        return self.x % self.y
    
    def power(self, x, y)-> int:
        """Takes the power of 2 numbers

        Args:
            x (Int): A integer, that can be either positive or negative
            y (Int): A integer, that can be either positive or negative

        Returns:
            Int: A new number that is multiplied y number of times to itself
        """
        return x ** y
    
    def square_root(self)-> int:
        """The square root method for the calculator/

        Raises:
            ValueError: If the number is 0 then raises a error due to assuming positve real #s

        Returns:
            int: returns the square root of the inputed number
        """
        if self.x >= 0:
            return math.sqrt(self.x)
        else:
            raise ValueError(f"Cannot compute square root of {self.x}")
    
    def factorial(self)-> int:
        """THe factorial method of the calulcator

        Args:
            n (int): Represents the number you are taking the factorial of

        Raises:
            ValueError: if the number is less than 0, there wil lbe a value error

        Returns:
            Int: A new value that is the facoritial of the inputted value
        """
        if self.n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        return math.factorial(self.n)
    
    def exponential(self, n)-> int:
        """Takes a number and takes the e exponential

        Args:
            n (int): the inputted value

        Returns:
            int: Returns E raised to the power of n
        """
        return math.exp(n)
    #uses the e exponential not like the power function
    
    def sin(self, angle)-> int:
        """Part of the trigonometry methods for the caluclator

        Args:
            angle (int): a number representing the angle of something

        Returns:
            float: returns either the degree value or the radian value of some integer
        """
        angle = self._convert_angle()
        return math.sin(angle)
    
    def cos(self, angle)-> int:
        """Part of the trigonometry methods for the caluclator

        Args:
            angle (int): a number representing the angle of something

        Returns:
            float: returns either the degree value or the radian value of some integer
        """
        angle = self._convert_angle()
        return math.cos(angle)
    
    def tan(self, angle)-> int:
        """Part of the trigonometry methods for the caluclator

        Args:
            angle (int): a number representing the angle of something

        Returns:
            float: returns either the degree value or the radian value of some integer
        """
        angle_radians = self._convert_angle()
        tangent_value = math.tan(angle_radians)
        if self.mode == "degrees":
            return math.degrees(tangent_value)
        return tangent_value 
    
    def absolute_value(self, x) -> int:
        """Takes the absolue value of any integer

        Args:
            x (Int): A number that can be positive or negative

        Returns:
            int: The result is the inputted number but positive
        """
        return abs(x)
    
    def invcos(self)-> int:
        """Part of the trigonometry methods for the caluclator

        Args:
            angle (int): a number representing the angle of something

        Returns:
            int: returns either the degree value or the radian value of some integer
        """
        result = math.acos(self.value)
        if self.mode == "degrees":
            return math.degrees(result)
        return result
    
    def invsin(self)-> int:
        """Part of the trigonometry methods for the caluclator

        Args:
            angle (int): a number representing the angle of something

        Returns:
            int: returns either the degree value or the radian value of some integer
        """
        result = math.asin(self.value)
        if self.mode == "degrees":
            return math.degrees(result)
        return result

    def invtan(self)-> int:
        """Part of the trigonometry methods for the caluclator

        Args:
            angle (int): a number representing the angle of something

        Returns:
            int: returns either the degree value or the radian value of some integer
        """
        result = math.atan(self.value)
        if self.mode == "degrees":
            return math.degrees(result)
        return result
    
    def log(self, x, base = 10)-> int:
        return math.log(x, base)
    
    def natural_log(self, x):
        return math.log(x)
    
    #fractions are its own class
    
    def to_decimal(self, fraction) -> float:
        """Converts a fraction into a decimal

        Args:
            fraction (int): has a numberator and a denominator

        Returns:
            float: the decimal version of the fraction
        """
        return float(fraction)
    
    def round_digits(self, number, digits) -> float:
        """rounds the a decimal to a certain number of digits based on the user

        Args:
            number (float): the decimal that is trying to be rounded 
            digits (int): represents the number of decimal points desired

        Returns:
            float: the rounded number of the decimal
        """
        return round(number, digits)
    
    def cube_root(self, x, index):
        """The cubed root method of the calulator

        Args:
            x (int): the radicand inside the radical
            index (int): indicates the root

        Returns:
            int: A (double) value that is the answer to what you are rooting
        """
        return x ** (1 / index)
    #this is done so that any index for the root can be done
    
    def solve_quadratic_equations(self, a, b, c) -> tuple:
        """Creates and solves the quadratic equation

        Args:
            a (int): Coefficient of x^2
            b (int): Coefficient of x
            c (int): Constant term

        Returns:
            tuple: A tuple containg the rootsof the 
            quadratic eqution
        """
        discriminant = b ** 2 - 4 * a * c

        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return root1, root2
        elif discriminant == 0:
            root = -b / (2 * a)
            return root, 
        else:
            return "Complex roots"
    
    def log_with_base(self, x, base) -> int:
        """Creates the log base

        Args:
            x (int): A value that your are using for the log
            base (int): can be either base 10 or another number for the log

        Returns:
            _type_: _description_
        """
        return math.log(x, base)
    
    def negate(self, x) -> int: 
        """Makes a number a negative

        Args:
            x (int): x has to be a integer for it to be negated

        Returns:
            int: returns a negative version of the inputted number
        """
        return -x 