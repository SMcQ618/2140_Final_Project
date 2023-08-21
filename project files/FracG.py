import tkinter as tk
from fractions import Fraction
#uses the fraction library

class FractionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Fraction Calculator")

        self.frame = tk.Frame(root)
        self.frame.pack()
        #creates a window so a user can input their fraction
        self.input_label1 = tk.Label(self.frame, text="Enter Fraction 1:")
        self.input_label1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry1 = tk.Entry(self.frame)
        self.entry1.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.input_label2 = tk.Label(self.frame, text="Enter Fraction 2:")
        self.input_label2.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.entry2 = tk.Entry(self.frame)
        self.entry2.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        #make sure it shows that specific operation result
        self.add_button = tk.Button(self.frame, text="Add", command=self.show_add_result)
        self.add_button.grid(row=2, column=0, padx=10, pady=10)

        self.subtract_button = tk.Button(self.frame, text="Subtract", command=self.show_subtract_result)
        self.subtract_button.grid(row=2, column=1, padx=10, pady=10)

        self.multiply_button = tk.Button(self.frame, text="Multiply", command=self.show_multiply_result)
        self.multiply_button.grid(row=2, column=2, padx=10, pady=10)

        self.divide_button = tk.Button(self.frame, text="Divide", command=self.show_divide_result)
        self.divide_button.grid(row=2, column=3, padx=10, pady=10)

        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0, weight=1)

    def perform_operation(self, fraction1, fraction2, operation):
        """Performs the operation of the fraction if it matches key
        Args:
            fraction1 (floating-ponit): represents the first fraction
            fraction2 (floating-ponit): represents the second fraction
            operation (floating-ponit): is the operation

        Returns:
            Floating-point: Will show a fraction or a whole num
        """
        if operation == "+":
            return fraction1 + fraction2
        elif operation == "-":
            return fraction1 - fraction2
        elif operation == '*':
            return fraction1 * fraction2
        elif operation == '/':
            return fraction1 / fraction2

    def show_result_window(self, result):
        """Creates a pop-up window with the result

        Args:
            result (Int): will be a number with a '/' or a whole number
        """
        result_window = tk.Toplevel(self.root)
        result_window.title("Result")

        result_label = tk.Label(result_window, text=f"Result: {result}")
        result_label.pack(padx=20, pady=20)

    def show_add_result(self):
        """Shows the result from the addtion operation"""
        input_text1 = self.entry1.get()
        input_text2 = self.entry2.get()
        self.show_result(input_text1, input_text2, "+")

    def show_subtract_result(self):
        """Shows the result from the subtraction operation"""
        input_text1 = self.entry1.get()
        input_text2 = self.entry2.get()
        self.show_result(input_text1, input_text2, "-")
    
    def show_multiply_result(self):
        """Shows the result from the multiplication operation"""
        input_text1 = self.entry1.get()
        input_text2 = self.entry2.get()
        self.show_result(input_text1, input_text2, "*")
    
    def show_divide_result(self):
        """Shows the result from the division operation, using fraction module"""
        input_text1 = self.entry1.get()
        input_text2 = self.entry2.get()
        try:
            fraction1 = Fraction(input_text1)
            fraction2 = Fraction(input_text2)
            result_fraction = self.perform_operation(fraction1, fraction2, "/")
            self.show_result_window(result_fraction)
        except (ValueError, ZeroDivisionError):
            #makes sure if there is a 0 division it will output an error
            self.show_result_window("Invalid input")

    def show_result(self, input_text1, input_text2, operation):
        """Shows the result of the fractions and their corresponding operation

        Args:
            input_text1 (floating-point): represents the first input fraction
            input_text2 (floating-poing): represents the second input fraction
            operation (String): Matches with the string operations above and computes
        """
        try:
            fraction1 = Fraction(input_text1)
            fraction2 = Fraction(input_text2)
            result_fraction = self.perform_operation(fraction1, fraction2, operation)
            self.show_result_window(result_fraction)
        except (ValueError, ZeroDivisionError):
            self.show_result_window("Invalid input")

if __name__ == "__main__":
    root = tk.Tk()
    app = FractionGUI(root)
    root.mainloop()
