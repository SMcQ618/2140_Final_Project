import tkinter as tk
from tkinter import messagebox
from linear_equations import Linear_Eqs, SystemOfEQs
import numpy as np
class EquationSolver:
    def __init__(self, master):
        self.master = master
        self.master.title("Equation Solver")

        self.equation_label = tk.Label(master, text="Enter coefficients and constant for each equation:")
        self.equation_label.pack()

        self.coefficient_entries = []
        for i in range(2):  # Assuming you want to solve a system of 2 equations
            equation_frame = tk.Frame(master)
            equation_frame.pack()

            coeff_label = tk.Label(equation_frame, text=f"Equation {i+1}: Coefficients (space-separated):")
            coeff_label.pack()

            coeff_entry = tk.Entry(equation_frame)
            coeff_entry.pack()

            const_label = tk.Label(equation_frame, text=f"Equation {i+1}: Constant:")
            const_label.pack()

            const_entry = tk.Entry(equation_frame)
            const_entry.pack()

            self.coefficient_entries.append((coeff_entry, const_entry))

        solve_button = tk.Button(master, text="Solve", command=self.solve_equations)
        solve_button.pack()

    def solve_equations(self):
        equations = []
        for coeff_entry, const_entry in self.coefficient_entries:
            coefficients = [float(coeff) for coeff in coeff_entry.get().split()]
            constant = float(const_entry.get())
            equation = Linear_Eqs(coefficients, constant)
            equations.append(equation)

        system = SystemOfEQs()
        for equation in equations:
            system.add_equation(equation)

        try:
            coefficient_matrix = np.array([equation.coefficients for equation in system.equations])
            constant_matrix = np.array([equation.constant for equation in system.equations])

            solutions = np.linalg.lstsq(coefficient_matrix, constant_matrix, rcond=None)[0]

            solution_list = []
            for i, solution in enumerate(solutions):
                solution_list.append(f"{solution:.3f}")
            
            messagebox.showinfo("Solution", f"Solutions:\n{solution_list}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
