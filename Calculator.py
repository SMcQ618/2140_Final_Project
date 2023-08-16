import tkinter as tk
from tkinter import messagebox
import math
from matriX import MatriX
from Matrix_operations import Matrix_Operations
from laplaceG import LaplaceTrsG
from EquationSolver import EquationSolver


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

        #fix teh row and column weights for resizing
        for i in range(5):
            self.button_frame.grid_rowconfigure(i, weight=1)
            self.button_frame.grid_columnconfigure(i, weight=1)
        

    def advance_calculator(self):
        adv_calc_window = tk.Toplevel(self.master)
        adv_oper_app = Advance_calculator(adv_calc_window) 

    def open_laplace_view(self):
        laplace_window = tk.Toplevel(self.master)
        laplace_app = LaplaceTrsG(laplace_window)

    #this is for mathcing the back arrow, clear, and clear all
    def on_button_click(self, button):
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
        matrix_operations_button = tk.Button(self.button_frame, text="M_Operations", width=10, command=self.open_matrix_view)
        matrix_operations_button.grid(row=3, column=8, columnspan=2, padx=5, pady=5)
        
        #creates buttons for lapalce view
        laplace_transforms_button = tk.Button(self.button_frame, text="Transforms", width = 10, command=self.open_laplace_view)
        laplace_transforms_button.grid(row=4, column=8, columnspan=2, padx=5, pady=5)
        
        #create methods for advance for linear
        equation_solver_button = tk.Button(self.button_frame, text="Equation Solver", width=10, command=self.open_equation_solver)
        equation_solver_button.grid(row=1, column=8, columnspan=2, padx=5, pady=5)  # Adjust the row and column as needed

    #@classmethod
    def open_equation_solver(self):
        equation_solver_window = tk.Toplevel(self.master)
        equation_solver_app = EquationSolver(equation_solver_window)

    def open_matrix_view(self):
        matrix_operation_window = tk.Toplevel(self.master)
        matrix_operations_app = Matrix_Operations(matrix_operation_window)   

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
            # ... handle sine calculation ...
            try:
                radians = eval(current)
                result = math.sin(radians)
                self.equation.delete(0, tk.END)
                self.equation.insert(0, str(result))
            except:
                self.equation.delete(0, tk.END)
                self.equation.insert(0, "Error")
        elif text == "cos":
            # ... handle cosine calculation ...
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
            # ... handle tangent calculation ...
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
            # ... handle logarithm calculation ...
            try:
                radians = eval(current)
                result = math.log(radians)
                self.equation.delete(0, tk.END)
                self.equation.insert(0, str(result))
            except:
                self.equation.delete(0, tk.END)
                self.equation.insert(0, "Error")
        elif text == "(":
            # ... handle opening parenthesis ...
            self.equation.insert(tk.END, "(")

        elif text == ")":
            # ... handle closing parenthesis ...
            self.equation.insert(tk.END, ")")

        elif text == "π":
            # ... handle pi constant ...
            self.equation.insert(tk.END, str(math.pi))

        elif text == "e":
            # ... handle Euler's number 
            self.equation.insert(tk.END, str(math.e))
        elif text == "Matrix":
            self.open_matrix_view()
        elif text == "Laplace":
            self.open_laplace_view()

'''def main():
    root = tk.Tk()
    app = Calculator(root)

    menubar = tk.Menu(root)
    root.config(menu=menubar)

    #Create a "File" menu with an "Exit" option
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=file_menu)

    #creates the "view" menu look with the different option
    view_menu = tk.Menu(menubar, tearoff=0)
    view_menu.add_command(label="Advanced Calculator", command=app.advance_calculator)
    view_menu.add_command(label="Matrix Calculator", command=app.advance_calculator)  # Add this line
    view_menu.add_command(label="Laplace", command=app.open_laplace_view)
    # Inside the main method where you create the "View" menu
    view_menu.add_command(label="Equation Solver", command=app.open_equation_solver)

    menubar.add_cascade(label="View", menu=view_menu)

    root.mainloop()

if __name__ == "__main__":
    main()'''
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
    view_menu.add_command(label="Advanced Calculator", command=app.advance_calculator)
    view_menu.add_command(label="Matrix Calculator", command=app.open_matrix_view)
    view_menu.add_command(label="Laplace", command=app.open_laplace_view)
    view_menu.add_command(label="Equation Solver", command=app.open_equation_solver)  # Add this line
    menubar.add_cascade(label="View", menu=view_menu)

    root.mainloop()

if __name__ == "__main__":
    main()
