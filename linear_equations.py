#topics will inclide: slving a linear equation, matrix from the module i created, Systems of Equations and Matrices ch4, cofactors expansion, Eigenvalues and Eigenvectors,  
import sympy as sp

class Linear_Eqs:
    """Class that represents a linear equation."""
    def __init__(self, a, b,coefficients, constant) -> None:
        self.a = a
        self.b = b
        self.coefficents = coefficients
        self.constant = constant
    
    def solve_linear_equations(self):
        """Solves a linear equation and should return real solutions or none.
        Args:
            a (float): Coefficient of x.
            b (float): Constant term.
        Returns:
            str or float: Returns "Infinite solutions" if the equation has infinite solutions,
            "No solutions" if the equation has no solution, and the solution (a float)
            if a unique solution exists.
        """
        x = sp.symbol('x')
        polynomial = sum(coeff * x ** exp for exp, coeff in enumerate(self.coefficents[::-1]))
        solutions = sp.solve(polynomial, x)

        #filter out the complex solutions
        real_solutions = [sol for sol in solutions if sol.is_real]
        return real_solutions
        
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
        self.solutions = []

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
        
        solutions = []
        for equation in self.equations:
            solution = equation.solve_for_variable()
            solutions.append(solution)
       
        return solution
