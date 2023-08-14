import tkinter as tk
from Basic_Operations import Operations
from Advance_methods import Adv_Methods
from differential_equations import DifferentialEqs
from linear_equations import Linear_Eqs, SystemOfEQs
from matrix import Matrix
from new_fractions import NewFractions
from Laplace_ import Laplace_transforms  # Import the new class

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.operations = Operations(0, 0, 0, 0, 0, 0, 0)  # Initialize the Operations class
        self.adv_methods = Adv_Methods(0, 0, [], "", 0)  # Initialize the Adv_Methods class
        self.differential_eqs = DifferentialEqs(0, '', '')  # Initialize the DifferentialEqs class
        self.linear_eqs = Linear_Eqs([], 0)  # Initialize the Linear_Eqs class
        self.system_of_eqs = SystemOfEQs()  # Initialize the SystemOfEQs class
        self.matrix = Matrix(0, 0, [])  # Initialize the Matrix class
        self.fractions = NewFractions(0, 1)  # Initialize the NewFractions class
        self.laplace_transforms = Laplace_transforms()  # Initialize the Laplace_transforms class

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.create_ui()

    def create_ui(self):
        result_label = tk.Label(self.root, textvariable=self.result_var, font=("Helvetica", 24))
        result_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # ... Create your buttons and layout here ...

    def on_button_click(self, button_text):
        current_text = self.result_var.get()

        if button_text == "=":
            try:
                result = eval(current_text)
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        else:
            if current_text == "0":
                self.result_var.set(button_text)
            else:
                self.result_var.set(current_text + button_text)

    # Create methods to handle the advanced, differential equation,
    # linear equation, matrix, fraction, and Laplace transform operations
    # using self.adv_methods, self.differential_eqs, self.linear_eqs,
    # self.matrix, self.fractions, self.laplace_transforms, and other classes

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop() 