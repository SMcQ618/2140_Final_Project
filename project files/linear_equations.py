#topics will inclide: solving a linear equation, matrix from the module i created, Systems of Equations and Matrices ch4, cofactors expansion, Eigenvalues and Eigenvectors,  
import numpy as np
import numpy.linalg

class Linear_Eqs:
    """Class that represents a linear equation."""
    def __init__(self, coefficients, constant):
        """
        Initialize a linear equation.

        Args:
            coefficients (list): List of coefficients for each term of the equation.
            constant (float): Constant term of the equation.
        """
        self.coefficients = coefficients
        self.constant = constant
    
    def solve_for_variable(self):
        """
        Solve for the variable in the linear equation.

        Returns:
            float: The value of the variable.
        
        Raises:
            ValueError: If the coefficient list is empty.
        """
        if self.coefficients:
            a = np.array([self.coefficients])
            b = np.array([self.constant])
            solution = np.linalg.solve(a, b)
            return solution[0]
        else:
            raise ValueError('Coefficient list is empty')
        
    def __str__(self):
        """
        Return a formatted string representation of the equation.

        Returns:
            str: String representation of the equation.
        """
        terms = []
        for exp, coeff in enumerate(self.coefficients[::-1]):
            if coeff != 0:
                if exp == 0:
                    terms.append(str(coeff))
                elif exp == 1:
                    terms.append(f"{coeff}x")
                else:
                    terms.append(f"{coeff}x^{exp}")
        equation_str = " + ".join(terms)
        equation_str += f" = {self.constant}"
        return equation_str

class SystemOfEQs:
    """Class that represents a system of linear equations."""
    def __init__(self):
        """Initialize an empty system of equations."""
        self.equations = []

    def add_equation(self, equation):
        """
        Add an equation to the system.

        Args:
            equation (Linear_Eq): The equation to be added.
        """
        self.equations.append(equation)

    def solve_system(self):
        """
        Solve the system of equations.

        Returns:
            list: A list of solutions for each equation in the system.
        
        Raises:
            ValueError: If there are no equations in the system.
        """
        if not self.equations:
            raise ValueError('No equations in the system')
        
        coefficient_matrix = np.array([equation.coefficients for equation in self.equations])
        constant_matrix = np.array([equation.constant for equation in self.equations])
        solutions = np.linalg.solve(coefficient_matrix, constant_matrix)

        return solutions

# Example usage
eq1 = Linear_Eqs([2, -3, 1], 4)
eq2 = Linear_Eqs([1, 2, -1], -1)

system = SystemOfEQs()
system.add_equation(eq1)
system.add_equation(eq2)

try:
    coefficient_matrix = np.array([equation.coefficients for equation in system.equations])
    constant_matrix = np.array([equation.constant for equation in system.equations])

    solutions = np.linalg.lstsq(coefficient_matrix, constant_matrix, rcond=None)[0]
    print("Solutions:", solutions)
    #solutions = system.solve_system()
    #print("Solutions:", solutions)
except ValueError as e:
    print(e)
