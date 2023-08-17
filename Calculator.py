import tkinter as tk
from tkinter import messagebox
import math
#from matriX import MatriX
from Matrix_operations import Matrix_Operations
from LaplaceT import LaplaceTransforms
from EquationSolver import EquationSolver
from DifferentialEquationSolver import DifferentialEquationSolver
from FracG import FractionGUI


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        #the entry for displaying the equations
        self.equation = tk.Entry(master, width=20)
        self.equation.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="ew")

        #creates the frame
        self.button_frame = tk.Frame(master)
        self.button_frame.grid(row=1, column=0, sticky="nsew")

        self.create_buttons()

        #done for resizing the calculator
        for i in range(5):
            master.grid_rowconfigure(i, weight=1)
        for i in range(5):
            master.grid_columnconfigure(i, weight=1)

    #create the buttons for the numbers
    def create_buttons(self):
        """Creates the look for the calculator"""
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('⌫', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('+', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('=', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('Clear', 4, 2), ('Clear All', 4, 3), ('±', 4, 4)
        ]

        self.buttons = []

        #creates the buttons and the positions
        for button_info in buttons:
            value, row, col = button_info
            button = tk.Button(self.button_frame, text=value, width=9)
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            button.config(command=lambda b=button: self.on_button_click(b))
            self.buttons.append(button)

        #fix the row and column weights for resizing
        for i in range(5):
            self.button_frame.grid_rowconfigure(i, weight=1)
            self.button_frame.grid_columnconfigure(i, weight=1)
        
        # show_matrix_button = tk.Button(self.master, text="Show Matrix", command=self.show_matrix_values)
        # show_matrix_button.grid(row=5, column=4, padx=5, pady=5, sticky="nsew")
        # self.buttons.append(show_matrix_button)

    def show_matrix_values(self):
        """Display the matrix values in a new window"""
        matrix_values = []

        for row_entries in self.matrix_operations_app.matrix_entries:
            row_values = []
            for entry in row_entries:
                value = entry.get()
                row_values.append(value)
            matrix_values.append(row_values)

        matrix_text = "\n".join([" ".join(row) for row in matrix_values])

        matrix_window = tk.Toplevel(self.master)
        matrix_window.title("Matrix Values")
        matrix_label = tk.Label(matrix_window, text=matrix_text, font=("Helvetica", 12))
        matrix_label.pack()
     
    def advance_calculator(self):
        """Opns a advance calc window"""
        adv_calc_window = tk.Toplevel(self.master)
        adv_oper_app = Advance_calculator(adv_calc_window) 

    def open_laplace_view(self):
        """Opens a laplace window"""
        laplace_window = tk.Toplevel(self.master)
        laplace_app = LaplaceTransforms(laplace_window)

    def open_fraction_solver(self):
        """Opens fraction window"""
        fraction_window = tk.Toplevel(self.master)
        frac_app = FractionGUI(fraction_window)

    #this is for mathcing the back arrow, clear, and clear all
    def on_button_click(self, button):
        """when a button is clicked what to do"""
        text = button.cget("text")

        if text == "⌫":
            current = self.equation.get()
            self.equation.delete(len(current) - 1)
        elif text == "=":
            try:
                result = eval(self.equation.get())
                self.equation.delete(0, tk.END)
                self.equation.insert(0, str(result))
            except:
                self.equation.delete(0, tk.END)
                self.equation.insert(0, "Error")

            # Clear matrix entries after an operation
            if hasattr(self, "matrix_operations_app"):
                self.matrix_operations_app.clear_matrix_entries()
        elif text == "Clear":
            current = self.equation.get()
            self.equation.delete(0, tk.END)
            self.equation.insert(0, current[:-1])
        elif text == "Clear All":
            self.equation.delete(0, tk.END)
        elif text == "±":
            current = self.equation.get()
            if current and current[0] == '-':
                self.equation.delete(0)
            else:
                self.equation.insert(0, '-')
        else:
            current = self.equation.get()
            self.equation.delete(0, tk.END)
            self.equation.insert(0, current + text)

class Advance_calculator(Calculator):
    """Contains all the operations for the more advanced Calculator

    Args:
        Calculator (Class): Inherits from the main calculator with basic operations
    """
    def __init__(self, master):
        super().__init__(master)
        self.matrix_operations_app = None 

    def create_buttons(self):
        super().create_buttons()

        advanced_buttons = [
             ('sqrt', 1, 5), ('^2', 2, 5), ('^3', 3, 5), ('1/x', 4, 5),
            ('sin', 1, 6), ('cos', 2, 6), ('tan', 3, 6), ('log', 4, 6),
            ('(', 1, 7), (')', 2, 7), ('π', 3, 7), ('e', 4, 7),
            ('Matrix', 1, 8), ('Laplace', 2, 8)
        ]

        for button_info in advanced_buttons:
            value, row, col = button_info
            button = tk.Button(self.button_frame, text=value, width=9)
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            button.config(command=lambda b=button: self.on_advanced_button_click(b))
            self.buttons.append(button)
        
        matrix_operations_button = tk.Button(self.button_frame, text="Matrix", width=10, command=self.open_matrix_view)
        matrix_operations_button.grid(row=3, column=8, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.buttons.append(matrix_operations_button)

        #creates buttons for lapalce view
        laplace_transforms_button = tk.Button(self.button_frame, text="Transforms", width = 10, command=self.open_laplace_view)
        laplace_transforms_button.grid(row=4, column=8, columnspan=2, padx=5, pady=5, sticky="nsew")
        
        equation_solver_button = tk.Button(self.button_frame, text="LinEQ Solver", width=10, command=self.open_equation_solver)
        equation_solver_button.grid(row=1, column=9, columnspan=2, padx=5, pady=5, sticky="nsew")  # Adjust the row and column as needed

        #create methods for advance for linear
        diff_eq_button = tk.Button(self.button_frame, text="Diff EQ", width=10, command=self.open_diff_eq_solver)
        diff_eq_button.grid(row=4, column=10, columnspan=2, padx=5, pady=5, sticky="nsew")

        fraction_button = tk.Button(self.button_frame, text="Fractions", width= 10, command=self.open_fraction_solver)
        fraction_button.grid(row=2, column= 8, columnspan=2, padx=5, pady=5, sticky="nsew")
    #@classmethod
    def open_equation_solver(self):
        """where i call the linear equation window
        """
        equation_solver_window = tk.Toplevel(self.master)
        equation_solver_app = EquationSolver(equation_solver_window)

    def open_diff_eq_solver(self):
        """where the diiferential eqution window is called
        """
        diff_eq_window = tk.Toplevel(self.master)
        diff_eq_app = DifferentialEquationSolver(diff_eq_window)

    def open_matrix_view(self):
        """Opens the matrix window"""
        if self.matrix_operations_app is None or not self.matrix_operations_app.master.winfo_exists():
            matrix_operation_window = tk.Toplevel(self.master)
            self.matrix_operations_app = Matrix_Operations(matrix_operation_window)
        else:
            self.matrix_operations_app.master.lift()

    def open_laplace_view(self):
        laplace_window = tk.Toplevel(self.master)
        laplace_app = LaplaceTransforms(laplace_window) 

    def clear_matrix_entries(self):
        if hasattr(self, "matrix_operations_app"):
            self.matrix_operations_app.create_matrix_entries()
    
    def on_advanced_button_click(self, button):
        text = button.cget("text")
        current = self.equation.get()

        if text == "sqrt":
            try:
                result = eval(f"{current} ** 0.5")
                self.equation.delete(0, tk.END)
                self.equation.insert(0, str(result))
            except:
                self.equation.delete(0, tk.END)
                self.equation.insert(0, "Error")
        elif text == "^2":
            try:
                result = eval(f"{current} ** 2")
                self.equation.delete(0, tk.END)
                self.equation.insert(0, str(result))
            except:
                self.equation.delete(0, tk.END)
                self.equation.insert(0, "Error")
        elif text == "^3":
            try:
                result = eval(f"{current} ** 3")
                self.equation.delete(0, tk.END)
                self.equation.insert(0, str(result))
            except:
                self.equation.delete(0, tk.END)
                self.equation.insert(0, "Error")
        elif text == "1/x":
            try:
                result = eval(f"1 / {current}")
                self.equation.delete(0, tk.END)
                self.equation.insert(0, str(result))
            except:
                self.equation.delete(0, tk.END)
                self.equation.insert(0, "Error")
        elif text == "sin":
            try:
                radians = eval(current)
                result = math.sin(radians)
                self.equation.delete(0, tk.END)
                self.equation.insert(0, str(result))
            except:
                self.equation.delete(0, tk.END)
                self.equation.insert(0, "Error")
        elif text == "cos":
            try:
                radians = eval(current)
                result = math.cos(radians)
                self.equation.delete(0, tk.END)
                self.equation.insert(0, str(result))
            except:
                self.equation.delete(0, tk.END)
                self.equation.insert(0, "Error")
        elif text == "tan":
            try:
                radians = eval(current)
                result = math.tan(radians)
                self.equation.delete(0, tk.END)
                self.equation.insert(0, str(result))
            except:
                self.equation.delete(0, tk.END)
                self.equation.insert(0, "Error")
        elif text == "sin⁻¹":
            try:
                value = eval(current)
                result = math.asin(value)
                result_degrees = math.degrees(result)
                self.equation.delete(0, tk.END)
                self.equation.insert(0, str(result_degrees))
            except:
                self.equation.delete(0, tk.END)
                self.equation.insert(0, "Error")
        elif text == "cos⁻¹":
            try:
                value = eval(current)
                result = math.acos(value)
                result_degrees = math.degrees(result)
                self.equation.delete(0, tk.END)
                self.equation.insert(0, str(result_degrees))
            except:
                self.equation.delete(0, tk.END)
                self.equation.insert(0, "Error")
        elif text == "tan⁻¹":
            try:
                value = eval(current)
                result = math.atan(value)
                result_degrees = math.degrees(result)
                self.equation.delete(0, tk.END)
                self.equation.insert(0, str(result_degrees))
            except:
                self.equation.delete(0, tk.END)
                self.equation.insert(0, "Error")
        elif text == "log":
            try:
                radians = eval(current)
                result = math.log(radians)
                self.equation.delete(0, tk.END)
                self.equation.insert(0, str(result))
            except:
                self.equation.delete(0, tk.END)
                self.equation.insert(0, "Error")
        elif text == "(":
            
            self.equation.insert(tk.END, "(")

        elif text == ")":
            self.equation.insert(tk.END, ")")

        elif text == "π":
            self.equation.insert(tk.END, str(math.pi))
        elif text == "e":
            self.equation.insert(tk.END, str(math.e))
        elif text == "Matrix":
            self.open_matrix_view()
        elif text == "Laplace":
            self.open_laplace_view()
        elif text == "Diff EQ":
            self.open_diff_eq_solver()
        elif text == "Linear Algebra":
            self.open_equation_solver()
        elif text == "Fractions":
            self.open_fraction_solver()

    def display_matrix_result(self, result_matrix):
        result_window = tk.Toplevel(self.master)
        result_window.title("Matrix Result")

        result_label = tk.Label(result_window, text="Result:", font=("Helvetica", 12))
        result_label.pack()

        if isinstance(result_matrix, tuple):
            result_type, result = result_matrix
            result_label = tk.Label(result_window, text=f"{result_type}\n{result}", font=("Helvetica", 12))
            result_label.pack()
        # Display the result matrix using labels
        else:
            rows = len(result_matrix)
            cols = len(result_matrix[0])

            for i in range(rows):
                row_values = [str(result_matrix[i][j]) for j in range(cols)]
                row_label = tk.Label(result_window, text=" ".join(row_values), font=("Helvetica", 12))
                row_label.pack()
        
    def show_matrix_values(self):
        matrix_values = []

        for row_entries in self.matrix_operations_app.matrix_entries:
            row_values = []
            for entry in row_entries:
                value = entry.get()
                row_values.append(value)
            matrix_values.append(row_values)

        matrix_text = " \n".join([" ".join(row) for row in matrix_values])

        matrix_window = tk.Toplevel(self.master)
        matrix_window.title("Matrix Values")
        matrix_label = tk.Label(matrix_window, text=matrix_text, font=("Helvetica", 12))
        matrix_label.pack()

        if not hasattr(self, "show_matrix_button"):
            self.show_matrix_button = tk.Button(self.master, text="Show Matrix", command=self.show_matrix_values)
            self.show_matrix_button.grid(row=5, column=4, padx=5, pady=5, sticky="nsew")
            self.buttons.append(self.show_matrix_button)

def main():
    root = tk.Tk()
    app = Advance_calculator(root)  # Create an instance of Advance_calculator

    menubar = tk.Menu(root)
    root.config(menu=menubar)

    # Create a "File" menu with an "Exit" option
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=file_menu)

    # Create the "View" menu with the different options
    view_menu = tk.Menu(menubar, tearoff=0)
    #view_menu.add_command(label="Advanced Calculator", command=app.advance_calculator) #for the adv
    view_menu.add_command(label="Matrix Calculator", command=app.open_matrix_view) #for the matrix
    view_menu.add_command(label="Laplace", command=app.open_laplace_view) #for the laplace
    view_menu.add_command(label="Lin_Alg Solver", command=app.open_equation_solver)  # linear
    view_menu.add_command(label="DifferentialEQ", command=app.open_diff_eq_solver)
    menubar.add_cascade(label="View", menu=view_menu)

    root.mainloop()

if __name__ == "__main__":
    main()
