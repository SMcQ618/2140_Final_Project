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

    def create_buttons(self):
        self.create_button = tk.Button(self.master, text="Create Matrix", command=self.create_matrix)
        self.create_button.pack()

        # Create a dropdown menu for selecting matrix operations
        self.operation_var = tk.StringVar()
        self.operation_var.set("Select an operation")
        self.operation_menu = tk.OptionMenu(self.master, self.operation_var,
                                            "Operation 1: Add", "Operation 2: Multiply",
                                            "Operation 3: Determinant", "Operation 4: Transpose",
                                            "Operation 5: REF", "Operation 6: RREF")
        self.operation_menu.pack()

        # Create an "Evaluate Matrix" button
        evaluate_button = tk.Button(self.master, text="Evaluate Matrix", command=self.evaluate_matrix)
        evaluate_button.pack()

    def create_matrix_entries(self):
        self.matrix_entries = []

    def create_result_labels(self):
        self.result_label = tk.Label(self.master, text="", font=("Helvetica", 12))
        self.result_label.pack()

    def create_matrix(self):
        rows = int(self.rows_entry.get())
        cols = int(self.cols_entry.get())

        for entry_row in self.matrix_entries:
            for entry in entry_row:
                entry.destroy()
        self.matrix_entries = []

        # Create the entry for the matrix values
        self.matrix_entries = [
            [tk.Entry(self.master) for _ in range(cols)]
            for _ in range(rows)
        ]
        for i, entry_row in enumerate(self.matrix_entries):
            for j, entry in enumerate(entry_row):
                entry.grid(row=i + 4, column=j)

    def evaluate_matrix(self):
        matrix_values = []
        for entry_row in self.matrix_entries:
            row_values = []
            for entry in entry_row:
                value = entry.get()
                if value.strip() == "":
                    value = 0
                row_values.append(float(value))
            matrix_values.append(row_values)
    
        #create a instance
        matrix = MatriX(len(matrix_values), len(matrix_values[0]), matrix_values)
        
        operation = self.operation_var.get()
        #gets the selected option
        #perform the operations from the file
        if operation == "Operation 1: Add":
            result_matrix = matrix.add_matrix()
            messagebox.showinfo('Sums:', f'{result_matrix}')
        elif operation == "Operation 2: Mult":
            result_matrix = matrix.matrix_multiply()
            messagebox.showinfo('Products:', f'{result_matrix}')
        elif operation == "Operation 3: Det":
            result_matrix = matrix.det()
            messagebox.showinfo('Determinant:', f'{result_matrix}')
        elif operation == "Operation 4:transpose":
            result_matrix = matrix.transpose()
            messagebox.showinfo('Transposed:', f'{result_matrix}')
        elif operation == "Operation 5: REF":
            result_matrix = matrix.row_echelon_form()
            messagebox.showinfo('REF:', f'{result_matrix}')   
        elif operation == "Operation 6: RREF":
            result_matrix = matrix.reduced_row_echelon_form()
            messagebox.showinfo('RREF:', f'{result_matrix}') 

        self.display_result(result_matrix)

    def display_result(self, result_matrix):
        """displays the result matrix in a label

        Args:
            result_matrix (list): the list of list of matricies
        """
        formatted_matrix = "\n".join([" ".join(map(str, row)) for row in result_matrix])
        self.result_label.config(text=f'Result:\n{formatted_matrix}')

