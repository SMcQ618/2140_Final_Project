import tkinter as tk
import sympy as sp
import Differential_Equations1

class DifferentialEquationSolver:
    def __init__(self, master):
        #initialize the gui 
        self.master = master
        self.master.title("Differential Equation Solver")
        #labeling
        self.order_label = tk.Label(master, text="Order:")
        self.order_label.grid(row = 0, column= 0, sticky= "w")

        self.order_entry = tk.Entry(master)
        self.order_entry.grid(row = 0, column = 1)

        self.variable_label = tk.Label(master, text="Variable:")
        self.variable_label.grid(row = 1, column = 0, sticky = "w")

        self.variable_entry = tk.Entry(master)
        self.variable_entry.grid(row = 1, column = 1)

        self.equation_label = tk.Label(master, text="Equation:")
        self.equation_label.grid(row = 2, column = 0, sticky = "w")

        self.equation_entry = tk.Entry(master)
        self.equation_entry.grid(row = 2, column = 1)
        #the button to solve the diff eq
        self.solve_button = tk.Button(master, text="Solve", command=self.solve_differential_eq)
        self.solve_button.grid(row = 3, column = 2)
        #labeling the display
        self.results_label = tk.Label(master, text="", font=("Helvetica", 12))
        self.results_label.grid(row = 4, columnspan = 2)

        self.close_button = tk.Button(master, text="Close", command=master.destroy)
        self.close_button.grid(row = 5, columnspan = 2)

    def solve_differential_eq(self):
        """_summary_Solves the diff eq based on the user input"""
        order = int(self.order_entry.get())
        variable_symbol = self.variable_entry.get()
        variable = sp.Function(variable_symbol)(sp.symbols('x'))
        equation = sp.simplify(self.equation_entry.get())
        #calls the diffeq function to solve
        diff_eq = Differential_Equations1(order, equation, variable)
        general_solution = diff_eq.general_solution()

        self.display_results(order, general_solution)

    def display_results(self, order, result):
        """DIsplays the result for the dff eq solver

        Args:
            order (int): The order of the diff eq
            result (str): the result of the gen solution
        """
        self.results_label.config(text=f"Order: {order} \n General Solution:\n{result}")

root = tk.Tk()
app = DifferentialEquationSolver(root)

root.mainloop()