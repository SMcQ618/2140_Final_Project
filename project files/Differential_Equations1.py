import sympy as sp

class DifferentialEqs:
    def __init__(self, equation, function):
        self.equation = equation
        self.function = function
        self.variable = function.args[0]
        self.solution = None
        self.is_linear = self.check_linear()

    def check_linear(self):
        return sp.linear_eq_to_matrix(self.equation.rhs, [self.function.diff()])[0] is not None

    def solve(self):
        self.solution = sp.dsolve(self.equation, self.function)
        return self.solution

    def solve_initial_condition(self, initial_conditions):
        if self.solution is None:
            self.solve()
        if not self.is_linear:
            raise ValueError("Initial condition solving is currently supported only for linear ODEs.")

        # initial_conditions_f = {
        #     self.function: initial_conditions[self.function],
        #     self.function.diff(): initial_conditions[self.function.diff()]}
        
        constants = sp.solve([self.solution.rhs.subs(initial_conditions),
                              self.solution.lhs.subs(initial_conditions)])
        particular_solution = self.solution.subs(constants)
        return particular_solution

    def general_solution(self):
        if not self.solution:
            self.solve()
        return self.solution

# Example usage
if __name__ == "__main__":
    x = sp.symbols('x')
    f = sp.Function('f')(x)
    eq = sp.Eq(x * f.diff(x) + 2 * f, 0)

    diff_eq_solver = DifferentialEqs(eq, f)
    
    solution = diff_eq_solver.solve()
    print("General solution:", solution)
    
    print("Is linear:", diff_eq_solver.is_linear)
    
    initial_condition = {f: sp.Function('f')(0), f.diff(): 1}  # Adjust initial conditions
    particular_solution = diff_eq_solver.solve_initial_condition(initial_condition)
    print("Particular solution with initial conditions:", particular_solution)