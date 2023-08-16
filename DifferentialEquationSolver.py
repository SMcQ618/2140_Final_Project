import tkinter as tk
import sympy as sp
from differential_equations import DifferentialEqs

class DifferentialEquationSolver:
    def __init__(self, master):
        self.master = master
        self.master.title("Differential Equation Solver")

        self.order_label = tk.Label(master, text="Order:")
        self.order_label.pack()

        self.order_entry = tk.Entry(master)
        self.order_entry.pack()

        self.variable_label = tk.Label(master, text="Variable:")
        self.variable_label.pack()

        self.variable_entry = tk.Entry(master)
        self.variable_entry.pack()

        self.equation_label = tk.Label(master, text="Equation:")
        self.equation_label.pack()

        self.equation_entry = tk.Entry(master)
        self.equation_entry.pack()

        self.solve_button = tk.Button(master, text="Solve", command=self.solve_differential_eq)
        self.solve_button.pack()

        self.results_label = tk.Label(master, text="", font=("Helvetica", 12))
        self.results_label.pack()

        self.close_button = tk.Button(master, text="Close", command=master.destroy)
        self.close_button.pack()

    def solve_differential_eq(self):
        order = int(self.order_entry.get())
        variable_symbol = self.variable_entry.get()
        variable = sp.symbols(variable_symbol)
        equation = self.equation_entry.get()

        diff_eq = DifferentialEqs(order, variable, equation)
        general_solution = diff_eq.general_solution()

        self.display_results(general_solution)

    def display_results(self, result):
        self.results_label.config(text=f"General Solution:\n{result}")
