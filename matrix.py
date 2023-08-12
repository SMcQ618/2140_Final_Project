import numpy as np

#need to wrtie a method that uses
class Matrix:
    """This is the matrix class for all the linear algebra"""
    def __init__(self, rows, cols, matrix):
        """Initializing the MatrixOperations

        Args:
            rows (int): Number of rows
            cols (int): Number of columns
            matrix (list of lists): the inputted matrix
        """
        #want the user to be able to specify the number of rows and colums
        self.rows = rows
        self.cols = cols
        self.matrix = np.array(matrix)

    def input_matrix(self):
        """Have the user be able to input values for the matrix
        """
        for i in range(self.rows):
            row_input = input(f"Enter the values for row {i + 1} separated by spaces: ")
            self.matrix[i] = list(map(float, row_input.split()))

    def display_matrx(self):
        """The display function of the matrix"""
        print('Matrix')
        print(self.matrix)

    def add_matrx(self, other_matrix):
        """Add one matrix to another

        Args:
            other_matrix (Matrix): The matrix being added

        Raises:
            ValueError: if the size don't match, error

        Returns:
            Matrix: The reslt of the addition
        """
        if self.rows != other_matrix.rows or self.cols != other_matrix.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")

        #before made it that I had to iterate.
        result_matrix = self.matrix + other_matrix.matrix
        return Matrix(result_matrix)
    
    def matrix_multiply(self, other_matrix):
        """Multiply a matrix by anotehr one

        Args:
            other_matrix (Matrix): Another matrix being multiplied

        Returns:
            Matrix: The result of matrix multiplicaition
        """
        if self.col != other_matrix.rows:
            raise ValueError('Number of columns in first does not match second rows')
        
        result_matrix = np.dot(self.matrix, other_matrix.matrix)
        return Matrix(result_matrix)

    def transpose(self):
        """Be able to take a row and column and switch them"""
        self.matrix = self.matrix.T

    def swap_rows(self, row1, row2):
        """Swaps two rows in the matrix

        Args:
            row1 (int): Index of the first row to be swapped
            row2 (int): INdex of the second row
        """
        self.matrix[[row1, row2]] = self.matrix[[row2, row1]]

    def scale_row(self, row, scalar):
        """Scales a row in the matrix by a scalar value

        Args:
            row (int): Index of teh row
            scalar (float): The scalar value which to scale the row
        """
        self.matrix[row] *= scalar

    def add_scaled_row(self, source_row, target_row, scalar):
        """Adds a scaled row to another row in the matrix.

        Args:
            source_row (int): Index of the row to be scaled and added.
            target_row (int): Index of the row to which the scaled row will be added.
            scalar (float): The scalar value by which to scale the source row before adding.
        """
        self.matrix[target_row] += scalar * self.matrix[source_row]
     
    #RREF use sympy
    def row_echelon_form(self):
        """Where the first nonzero in each row (leading entry) is a 1 

        Returns:
            list: where a new matrix with ones in a consecutive order
        """
        for i in range(self.rows):
            pivot = self.matrix[i, i]
            if pivot == 0:
                for j in range(i + 1, self.rows):
                    if self.matrix[j, i] != 0:
                        self.swap_rows(i,j)
                        break
            pivot = self.matrix[i, i]
            if pivot != 0:
                self.matrix[i] /= pivot
                for k in range(i + 1, self.rows):
                    self.matrix[k] -= self.matrix[k, i] * self.matrix[i] 
    
    #RREF
    def reduced_row_echelon_form(self):
        """Where the leading 1 is the only nonzero in its column. 

        Returns:
            list: a matrix where there is ones in a consecutive order
        """
        self.row_echelon_form()
        for i in reversed(range(self.rows)):
            pivot_col = np.argmax(self.matrix[i] != 0)
            if pivot_col < self.cols:
                for j in reversed(range(i)):
                    self.matrix[j] -= self.matrix[j, pivot_col] * self.matrix[i]
    
