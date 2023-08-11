#topics will inclide: slving a linear equation, matrix from the module i created, Systems of Equations and Matrices ch4, cofactors expansion, Eigenvalues and Eigenvectors,  
class Linear_Eqs:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
    def solve_linear_equations(self):
        """Solves a linear equation of the form ax + b = 0.

        Args:
            a (float): Coefficient of x.
            b (float): Constant term.

        Returns:
            str or float: Returns "Infinite solutions" if the equation has infinite solutions,
            "No solutions" if the equation has no solution, and the solution (a float)
            if a unique solution exists.
        """
        if self.a == 0:
            if self.b == 0:
                return "Infinite solutions"
            return "No solutions"
        return -self.b / self.a