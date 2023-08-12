#topics will inclide: slving a linear equation, matrix from the module i created, Systems of Equations and Matrices ch4, cofactors expansion, Eigenvalues and Eigenvectors,  
import numpy as np
import numpy.linalg

#need to write a way tp 
class Linear_Eqs:
    """Class that represents a linear equation."""
    def __init__(self,coefficients, constant) -> None:
        self.coefficents = coefficients
        self.constant = constant
    
    def solve_for_variable(self):
        """
        Solve for the linear equation for the variable.

        Args: 
        a (float): Coefficient of x
        b (float): Constant term

        Returns:
        float: the value of the variable x
        Raises:
        ValueError: if the coefficient list is empty
        """
        if self.coefficents:
            a = np.array([self.coefficents])
            b = np.array([self.constant])
            solution = np.linalg.solve(a, b)
            return solution
        else:
            raise ValueError('Coefficient list is empty')
        
    def __str__(self):
        """Return a formatted string representation of the equation.

        Returns:
            str: String representaion of the equation.
        """
        equation_str = " + ".join([f"{coeff}x^{exp}" for exp, coeff in enumerate(self.coefficients[::-1]) if coeff != 0])
        equation_str += f" = {self.constant}"
        return equation_str
    
class SystemOfEQs:
    """Class that represents a system of linear equartions"""
    def __init__(self) -> None:
        """Initializing an empty system of equations"""
        self.equations = []

    def add_equaiton(self, equation):
        """Add an equation to teh system.

        Args:
            equation (Linear_Eq): The equation to be added
        """
        self.equations.append(equation)

    def solve_eq(self):
        """Solve the system

        Raises:
            ValueError: If theres no equation in teh system

        Returns:
            list: A list of solutions for each equation in the system
        """
        if not self.equations:
            raise ValueError('No equation ni the system')
        
        coefficient_matrix = np.array([equation.coefficients for equation in self.equations])
        constant_matrix = np.array([equation.constant for equation in self.equations])
        solutions = np.linalg.solve(coefficient_matrix, constant_matrix)

        return solutions
