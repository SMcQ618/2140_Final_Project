import tkinter as tk
from tkinter import messagebox
from matriX import MatriX

class Matrix_Operations:
    def __init__(self, master) -> None:
        self.master = master
        self.master.title("Matrix Operations")

        self.rows_label = tk.Label(master, text="Rows:")
        self.rows_label.pack()

        self.rows_entry = tk.Entry(master)
        self.rows_entry.pack()

        self.cols_label = tk.Label(master, text="Columns:")
        self.cols_label.pack()

        self.cols_entry = tk.Entry(master)
        self.cols_entry.pack()

        self.create_buttons()
        self.create_matrix_entries()
        self.create_result_labels()

    def create_buttons(self):
        """Creates the buttons for the matrix operations"""
        self.create_button = tk.Button(self.master, text='Create Matrix', command=self.create_matrix)
        self.create_button.pack()

        # Create a dropdown menu for selecting matrix operations
        self.operation_var = tk.StringVar()
        self.operation_var.set("Select an operation")
        self.operation_menu = tk.OptionMenu(self.master, self.operation_var,
                                            "Operation 1: Add", "Operation 2: Multiply",
                                            "Operation 3: Determinant", "Operation 4: Transpose",
                                            "Operation 5: REF", "Operation 6: RREF")
        self.operation_menu.pack()

        evaluate_button = tk.Button(self.master, text="Evaluate Matrix", command=self.evaluate_matrix)
        evaluate_button.pack()
    
    def create_matrix_entries(self):
        """Creates the entries for the matrix that the user puts in"""
        self.matrix_entries = []
    
        rows_value = self.rows_entry.get()
        cols_value = self.cols_entry.get()

        if rows_value and cols_value:
            rows = int(rows_value)
            cols = int(cols_value)

            for i in range(rows):
                row_entries = []
                for j in range(cols):
                    entry = tk.Entry(self.master)
                    entry.pack()
                    row_entries.append(entry)
                self.matrix_entries.append(row_entries)
        else:
            messagebox.showerror("Invalid Input", "Please enter valid integer values for rows and columns.")
            
    
    def create_result_labels(self):
            self.result_label = tk.Label(self.master, text="", font=("Helvetica", 12))
            self.result_label.pack()

    def create_matrix(self):
        try:
            rows = int(self.rows_entry.get())
            cols = int(self.cols_entry.get())

            self.create_matrix_entries()
            matrix_values = []

            for _ in range(rows):
                row_input = input(f"Enter values for row {_ + 1} separated by spaces: ")
                row_values = [int(value) for value in row_input.split()]
                matrix_values.append(row_values)

            self.matrix = MatriX(rows, cols, matrix_values)
            self.result_label.config(text="Matrix created successfully!")

            # Create matrix entries after the matrix has been successfully created
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter valid integer values.")


    def evaluate_matrix(self):
        # create a list to store matrix values entered by the user
        matrix_values = []

        for entry_row in self.matrix_entries:
            row_values = []
            # Iterate through each entry in the row
            for entry in entry_row:
                value = entry.get()
                # Convert empty or whitespace values to 0
                if value.strip() == "":
                    value = 0
                # Convert the value to a floating-point number and add to the row
                row_values.append(float(value))
            # Add the row of values to the matrix_values list
            matrix_values.append(row_values)

        # Print matrix_values dimensions for debugging
        print("Matrix Values Dimensions:", len(matrix_values), len(matrix_values[0]))

        operation = self.operation_var.get()

        try:
            matrix = MatriX(len(matrix_values), len(matrix_values[0]), matrix_values)
        except Exception as e:
            print("Error creating matrix:", e)
            return

        if operation == "Operation 1: Add":
            result_matrix = matrix.add_matrix()
        elif operation == "Operation 2: Multiply":
            result_matrix = matrix.matrix_multiply()
        elif operation == "Operation 3: Determinant":
            result_matrix = matrix.det()
        elif operation == "Operation 4: Transpose":
            result_matrix = matrix.transpose()
        elif operation == "Operation 5: REF":
            result_matrix = matrix.row_echelon_form()
        elif operation == "Operation 6: RREF":
            result_matrix = matrix.reduced_row_echelon_form()

        self.display_result(result_matrix)

    '''def evaluate_matrix(self):
    # create a list to store matrix values entered by the user
        matrix_values = []

        for entry_row in self.matrix_entries:
            row_values = []
            # Iterate through each entry in the row
            for entry in entry_row:
                value = entry.get()
                # Convert empty or whitespace values to 0
                if value.strip() == "":
                    value = 0
                # Convert the value to a floating-point number and add to the row
                row_values.append(float(value))
            # Add the row of values to the matrix_values list
            matrix_values.append(row_values)

        print("Matrix Values:", matrix_values)  # Add this line for debugging

        operation = self.operation_var.get()

        if operation == "Operation 1: Add":
            result_matrix = matrix.add_matrix()
        elif operation == "Operation 2: Multiply":
            result_matrix = matrix.matrix_multiply()
        elif operation == "Operation 3: Determinant":
            result_matrix = matrix.det()
        elif operation == "Operation 4: Transpose":
            result_matrix = matrix.transpose()
        elif operation == "Operation 5: REF":
            result_matrix = matrix.row_echelon_form()
        elif operation == "Operation 6: RREF":
            result_matrix = matrix.reduced_row_echelon_form()
        
        self.display_result(result_matrix)
        # Print matrix_values dimensions for debugging
        print("Matrix Values Dimensions:", len(matrix_values), len(matrix_values[0]))

        try:
            matrix = MatriX(len(matrix_values), len(matrix_values[0]), matrix_values)
        except Exception as e:
            print("Error creating matrix:", e)
            return
        matrix_label = tk.Label(self.master, text="Matrix:")
        matrix_label.pack()

        matrix_text = "\n".join([" ".join(map(str, row)) for row in matrix_values])
        matrix_text_widget = tk.Label(self.master, text=matrix_text)
        matrix_text_widget.pack()'''


    def display_result(self, result_matrix):
        """displays the result matrix in a label

        Args:
            result_matrix (list): the list of list of matricies
        """
        formatted_matrix = "\n".join([" ".join(map(str, row)) for row in result_matrix])
        self.result_label.config(text=f'Result:\n{formatted_matrix}')

