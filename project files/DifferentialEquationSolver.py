import tkinter as tk
from tkinter import ttk
import sympy as sp
from sympy import symbols, Function, Eq, dsolve, Derivative, exp, cos, sin, tan, parse_expr, pprint

class DifferentialEquations:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Differential Equation Solver")

        self.create_widgets()

    def solve_ode(self, eq, var, order):
        """Solve a sungle ordinary differential equation.
        Args:
            eq (sympy.Expr): the differential equation
            var (str): The variable to solve for
            order (int): the order of the differential equaiton (1 or 2)
        Returns:
            list: A list of solutions corresponding to the given order
        """
        #have the code recognize 't' as a symbol so it doesn't break
        t = symbols("t")
        #To create an undefined function, pass a string name to Function
        y = Function(var)(t)

        #create a sympy fucntion representing the given dff eq
        solution = dsolve(eq, y)
        return [solution]
        #using a list, allows the function to return a list of solutions
        #dolve is a sympy function that solves ordinary equations
        #returns an object that represents the gen solution with C1,C2 like in class

    def is_linear(self, eq, var):
        """Checks if a inputted equation is linear

        Args:
            eq (sympy.Expr): The differential equation
            var (str): the variable to check against

        Returns:
            bool: Returns true if the equation is linear, false otherwise
        """
        #checks if the equation i slinear by each term
        t = symbols("t")
        y = Function(var)(t)
        for term in eq.args:
            if term.has(Derivative(y, t)):
                #if the coeff of the deriv term is non-zero
                if term.coeff(Derivative(y, t)) != 0:
                    return False
                #then check for a higher power
                for var_pow in term.as_poly().terms():
                    if var_pow[1] > 1:
                        return False
            elif term.has(y):
                #check if the coeff is non-zero
                if term.coeff(y) != 0:
                    return False
        return True

    def solve_button_click(self):
        equation_str = self.equation_entry.get()
        var_str = self.variable_entry.get()
        order = self.order_entry.get()

        t = symbols("t")
        y = Function(var_str)(t)
        eq = Eq(Derivative(y, t, order) + 2*y - 3*sin(t), 0)
        #eq = parse_expr(equation_str)

        if self.is_linear(eq, var_str):
            self.result_label.config(text= "The differential equation is linear.")
        else:
            self.result_label.config(text= "The differential equation is not linear.")

        solutions = self.solve_ode(eq, var_str, order)
        solutions_text = "" 
        for solution in solutions:
            solutions_text += str(solution) + "\n"
        self.solutions_label.config(text = solutions_text)

    def create_widgets(self):
        equation_label = ttk.Label(self.root, text= "Enter the equation:")
        equation_label.pack()

        self.equation_entry = ttk.Entry(self.root)
        self.equation_entry.pack()

        variable_label = ttk.Label(self.root, text= "Enter the variable:")
        variable_label.pack()

        self.variable_entry = ttk.Entry(self.root)
        self.variable_entry.pack()

        order_label = ttk.Label(self.root, text= "Enter the order:")
        order_label.pack()

        self.order_entry = ttk.Entry(self.root)
        self.order_entry.pack()

        solve_button = ttk.Button(self.root, text= "Solve", command= self.solve_button_click)
        solve_button.pack()

        self.result_label = ttk.Label(self.root, text= "")
        self.result_label.pack()

        self.solutions_label = ttk.Label(self.root, text="")
        self.solutions_label.pack()

if __name__ == '__main__':
    root = tk.Tk()
    app =DifferentialEquations(root)
    
    #example_equation = "Derivative(y, t) + 2*y - 3*sin(t) = 0"
    #example_variable = "y"
    #example_order = 1

    #app.equation_entry.insert(0, example_equation)
    #app.variable_entry.insert(0, example_variable)
    #app.order_entry.insert(0, str(example_order))

    root.mainloop()




'''
class DifferentialEquationSolver:
    def __init__(self, root):
        #initialize the gui 
        self.root = root
        self.root.title('Dfferential Equation Solver /n')
        
        self.order_label = tk.Label(root, text = 'Order')
        self.order_label.pack()

        self.order_entry = tk.Entry()
        self.order_entry.pack()

        self.variable_label = tk.Label(root, text = 'What Variable do you want to solve')
        self.variable_label.pack()

        self.variable_entry = tk.Entry()
        self.variable_entry.pack()

        self.equation_label = tk.Label(root, text = 'Equation: ')
        self.equation_label.pack()

        self.equation_entry = tk.Entry()
        self.equation_entry.pack()

        self.solve_button = tk.Button(root, text='Solve', command = self.solve_equation)
        self.solve_button.pack()

    def parse_equation(self, equation, variable):
        equation = equation.replace("y'", "Derivative(y, t)")
        return equation
    
    def solve_equation(self):
        """Solves the diff eq based on the user input"""
        try:
            order = int(self.order_entry.get())
            variable = self.variable_entry.get()
            equation = self.equation_entry.get()

            t = sp.symbols('t')
            y = sp.Function(variable)(t)

            parsed_equation = self.parse_equation(equation, variable)
            print(parsed_equation)
            eq = sp.sympify(parsed_equation)
#            eq = sp.Eq(sp.sympify(parsed_equation))
            
            if is_linear(eq, variable):
                solutions = solve_ode(eq, variable, order)
                solution_text = '\n'.join([str(solution) for solution in solutions])
                messagebox.showinfo('Solutions (linear)', solution_text)
            else:
                messagebox.showerror('Error: The differential equation is not linear')
        except Exception as e:
            messagebox.showerror('Error', str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = DifferentialEquationSolver(root)
    root.mainloop()'''