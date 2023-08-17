#will hold al the laplce transforms
import tkinter as tk
from tkinter import ttk
#ttk helps with tkinter widget theme sets, so the widget functions a little different than grid or pack
#used this as a test to see how it would work, not sure if tis a good idea
import sympy as sp

class LaplaceTransforms:
    def __init__(self, root):
        self.root = root
        self.root.title("Laplace Transform Calculator")

        self.equation_label = ttk.Label(root, text="Enter Equation with parenthesis around parts multiplying each other:")
        self.equation_label.pack()

        self.equation_entry = ttk.Entry(root)
        self.equation_entry.pack()

        self.transform_type = tk.StringVar()
        self.transform_type.set("Laplace")
        self.transform_radio_frame = ttk.Frame(root)
        self.laplace_radio = ttk.Radiobutton(self.transform_radio_frame, text="Laplace Transform", variable=self.transform_type, value="Laplace")
        self.inverse_laplace_radio = ttk.Radiobutton(self.transform_radio_frame, text="Inverse Laplace", variable=self.transform_type, value="Inverse")
        self.laplace_radio.pack(side="left")
        self.inverse_laplace_radio.pack(side="left")
        self.transform_radio_frame.pack()

        #creates the buttons
        self.calculate_button = ttk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        self.result_label = ttk.Label(root, text="Result:")
        self.result_label.pack()

        self.result_text = tk.Text(root, height=5, width=40)
        self.result_text.pack()

    def calculate(self):
        """Uses sympy to calculate the Laplace transform and the inverse Laplace transform."""
        equation = self.equation_entry.get()
        transform_type = self.transform_type.get()
        #gets the equation from the user to be calculated
        if transform_type == "Laplace":
            result = self.calculate_laplace(equation)
        else:
            result = self.calculate_inverse_laplace(equation)

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

    def calculate_laplace(self, equation):
        """Calculates the standard laplace transform
        Args:
            equation (Int): The expression is a mix of ints and variables
        Returns:
            String: Returns a string formatted of the calculated expression
        """
        if not equation:
            return "No equation was inputted"
        
        s, t = sp.symbols('s t')
        #need to havea way to recognize s and t
        expr = sp.sympify(equation)
        laplace_expr = sp.laplace_transform(expr, t, s)
        #used for regular laplace going from t to s
        return str(laplace_expr)

    def calculate_inverse_laplace(self, equation):
        """Calculates the inverse laplace transform
        Args:
            equation (Int): the equation is not a string but a mix of ints and variables
        Returns:
            str: Returns the transform as a string on a pop-up window"""
        s, t = sp.symbols('s t')
        expr = sp.sympify(equation)
        inverse_laplace_expr = sp.inverse_laplace_transform(expr, s, t)
        #to fix the Heaviside thing with e
        simplified_expr = inverse_laplace_expr.simplify()
        formatted_expr = simplified_expr.subs(sp.Heaviside(t), 1).subs(t,'t')
        return str(formatted_expr)

if __name__ == "__main__":
    root = tk.Tk()
    app = LaplaceTransforms(root)
    root.mainloop()
