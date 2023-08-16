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

        self.calculate_button = tk.Button(master, text="Calculate Transform", command=self.calculate_transform)
        self.calculate_button.pack()

        self.result_label = tk.Label(master, text="", font=("Helvetica", 12))
        self.result_label.pack()

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
        calculator.input_equation(equation_str)

        result_type, result = calculator.calculate_transform()
        self.display_result(result_type, result)

    def display_result(self, result_type, result):
        self.result_label.config(text=f'{result_type}\n{result}')