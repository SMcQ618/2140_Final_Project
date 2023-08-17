import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter.simpledialog import askinteger
from matriX import MatriX  

class Matrix_Operations:
    def __init__(self, master):
        self.master = master
        self.master.title("Matrix Operations")

        self.matrix_entries = [] #this is for the first matrix
        self.other_matrix_entries = [] #this will be for the second matrix for adding/mul
        self.create_matrix_entries()

        self.create_buttons()

    def create_matrix_entries(self):
        """create the matrix entries for user"""
        rows = askinteger("Input", "Enter the number of rows:")
        cols = askinteger("Input", "Enter the number of columns:")

        if rows is None or cols is None:
            return

        for i in range(rows):
            row_frame = tk.Frame(self.master)
            row_frame.pack()

            row_entries = []
            for j in range(cols):
                entry = tk.Entry(row_frame)
                entry.pack(side=tk.LEFT)
                row_entries.append(entry)
            self.matrix_entries.append(row_entries)

    def create_buttons(self):
        """create buttons or diff matrix operations"""
        self.transpose_button = tk.Button(self.master, text="Transpose", command=self.transpose_matrix)
        self.transpose_button.pack()

        self.determinant_button = tk.Button(self.master, text="Determinant", command=self.determinant)
        self.determinant_button.pack()

        self.ref_button = tk.Button(self.master, text="REF", command=self.calc_ref)
        self.ref_button.pack()

        self.rref_button = tk.Button(self.master, text="RREF", command=self.calc_rref)
        self.rref_button.pack()

    
    def transpose_matrix(self):
        """Tranposes the matrix and updates the entry fields with the result"""
        matrix_values = []
        for row_entries in self.matrix_entries:
            row_values = []
            for entry in row_entries:
                value = entry.get()
                row_values.append(value)
            matrix_values.append(row_values)

        transposed_matrix = [[matrix_values[j][i] for j in range(len(matrix_values))] for i in range(len(matrix_values[0]))]

        for row_entries in self.matrix_entries:
            for entry in row_entries:
                entry.delete(0, tk.END)

        for i in range(len(self.matrix_entries)):
            for j in range(len(self.matrix_entries[0])):
                entry = self.matrix_entries[i][j]
                entry.insert(0, transposed_matrix[i][j])

    def determinant(self):
        matrix_value = self.get_matrix_values()

        if matrix_value:
            matrix = MatriX(len(matrix_value), len(matrix_value[0]), matrix_value)
            determinant = matrix.det()
            #this will create a pop-up window saying what the determinant is
            determinant_popup = tk.Toplevel(self.master)
            determinant_popup.title("Determinant")
            #wanted the determinant to be its own window
            determinant_label = tk.Label(determinant_popup, text=f"The determinant is {determinant}", font=("Helvetica", 12))
            determinant_label.pack()


    def calc_ref(self):
        """Calculates the Row Echelon FOrm and displays teh results"""
        matrix_values = self.get_matrix_values()

        if matrix_values:
            matrix = MatriX(len(matrix_values), len(matrix_values[0]), matrix_values)
            ref_matrix = matrix.row_echelon_form()

            self.update_matrix_entries_with_result(ref_matrix)
    
    def calc_rref(self):
        """Calculates the reduced row echelon form and displays the result"""
        matrix_values = self.get_matrix_values()

        if matrix_values:
            matrix = MatriX(len(matrix_values), len(matrix_values[0]), matrix_values)
            rref_matrix = matrix.reduced_row_echelon_form()

            self.update_matrix_entries_with_result(rref_matrix)

    def update_matrix_entries_with_result(self, result_matrix):
            """Updates the matrix entry fiesl with the result

            Args:
                result_matrix (list): the result is lists of lists that have different values
            """
            for i, row_entries in enumerate(self.matrix_entries):
                for j, entry in enumerate(row_entries):
                    entry.delete(0, tk.END)
                    entry.insert(0, result_matrix.matrix[i, j])

    def get_matrix_values(self):
        """Retrieve matrix values from entry fields and check the input

        Returns:
            _type_: _description_
        """
        matrix_values = []
        for row_entries in self.matrix_entries:
            row_values = []
            for entry in row_entries:
                value = entry.get()
                if value.strip() == "":
                    messagebox.showerror("Invalid Input", "Please enter valid integer values for matrix entries.")
                    return None
                row_values.append(float(value))
            matrix_values.append(row_values)
        return matrix_values
    
if __name__ == "__main__":
    root = tk.Tk()
    app = Matrix_Operations(root)
    root.mainloop()
