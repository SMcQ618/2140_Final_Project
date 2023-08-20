import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sympy as sp
#from sympy import symbols, Function, Eq, Derivative, dsolve, pprint
#from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, implicit_multiplication_application)
from Differential_Equations1 import solve_ode, is_linear

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

    def solve_differential_eq(self):
        """_summary_Solves the diff eq based on the user input"""
        try:
            order = int(self.order_entry.get())
            variable = self.variable_entry.get()
            equation = self.equation_entry.get()

            t = sp.symbols('t')
            y = sp.Function(variable)(t)
            eq = sp.Eq(sp.parse_expr(equation), 0)

            if is_linear(eq, variable):
                solutions = solve_ode(eq, variable, order)
                solution_text = '\n'.join([str(solution) for solution in solutions])
                messagebox.showinfo('Solutions (linear)', solution_text)
            else:
                messagebox.showerror('Error: The differential equation is not linear')
        except Exception as e:
            messagebox.showerror('Error', str(e))

def main():
    root = tk.Tk()
    app = DifferentialEquationSolver(root)
    root.mainloop()

if __name__ == '__name__':
    main()
    

# def display_results(self, order, result):
#       """DIsplays the result for the dff eq solver

#       Args:
#           order (int): The order of the diff eq
#           result (str): the result of the gen solution
#        """
#       self.results_label.config(text=f"Order: {order} \nGeneral Solution:\n{result}")