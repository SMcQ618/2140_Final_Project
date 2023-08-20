import tkinter as tk
from sympy import Function, Eq, Derivative, dsolve, pprint
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, implicit_multiplication_application)
import Differential_Equations1

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

        self.answer_label = tk.Label(root, text = 'Answer:')
        self.answer_label.pack()

        self.answer_text = tk.Text(root, height = 7, width = 40)
        self.answer_text.pack()

    def solve_differential_eq(self):
        """_summary_Solves the diff eq based on the user input"""
        order = int(self.order_entry.get())
        variable = self.variable_entry.get()
        equation_str = self.equation_entry.get()

        #call the dsolve the func 
        result = sp.dsolve(equation, variable)

        self.display_results(order, result)

    def display_results(self, order, result):
        """DIsplays the result for the dff eq solver

        Args:
            order (int): The order of the diff eq
            result (str): the result of the gen solution
        """
        self.results_label.config(text=f"Order: {order} \nGeneral Solution:\n{result}")

def main():
    root = tk.Tk()
    app = DifferentialEquationSolver(root)
    root.mainloop()

if __name__ == "__main__":
    main()