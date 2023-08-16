import tkinter as tk
from tkinter import messagebox
import sympy as sp
from Laplace_ import Laplace_transforms

class LaplaceTrsG:
    """Creates a tkinter aplication for Laplace
    """
    def __init__(self, master):
        self.master = master
        self.master.title('Laplace Transforms')

        self.equation_label = tk.Label(master, text="Equation:")
        self.equation_label.pack()

        self.equation_entry = tk.Entry(master)
        self.equation_entry.pack()

        # self.calculate_button = tk.Button(master, text="Calculate Transform", command=self.calculate_laplace)
        # self.calculate_button.pack()

        self.result_label = tk.Label(master, text="", font=("Helvetica", 12))
        self.result_label.pack()
        
        self.solve_button = tk.Button(master, text="Solve Equation", command=self.solve_equation)
        self.solve_button.pack(pady=10)

        self.create_ui()

    def create_ui(self):
        """Creating the parts and labels for Laplace
        """
        self.equation_label = tk.Label(self.master, text="Enter the equation:")
        self.equation_label.pack()

        self.equation_entry = tk.Entry(self.master)
        self.equation_entry.pack()

        self.calculate_button = tk.Button(self.master, text="Calculate Laplace Transform", command=self.calculate_laplace)
        self.calculate_button.pack()

        self.result_label = tk.Label(self.master, text="", font=("Helvetica", 12))
        self.result_label.pack()
    
    def calculate_laplace(self):
        equation_str = self.equation_entry.get()
        calculator = Laplace_transforms()
        calculator.input_equation()
        
        result_type, result = calculator.calculate_laplace()
        self.display_result(result_type, result)

    def solve_equation(self):
        """Creating the solve button so it solves
        """
        equation_str = self.equation_entry.get()
        try:
            equation = sp.simplify(equation_str)
            solution = equation.simplify()
            self.display_result("Simplified Equation:", solution)
        except Exception as e:
            self.display_result("Error:", str(e))
    
    def display_result(self, result_type, result):
        self.result_label.config(text=f'{result_type}\n{result}')