import numpy as np

#need to wrtie a method that uses
class MatriX:
    """This is the matrix class for all the linear algebra"""
    def __init__(self, rows, cols, matrix=None):
        """Initializing the MatrixOperations

        Args:
            rows (int): Number of rows
            cols (int): Number of columns
            matrix (list of lists): the inputted matrix
        """
        #want the user to be able to specify the number of rows and colums
        self.rows = rows
        self.cols = cols
        if matrix is None:
            self.matrix = np.zeros((rows, cols))
        else:
            self.matrix = np.array(matrix)

    def select_mode(self, mode):
        self.mode = mode
        print('Select a mode:\n')
        print('1. Input Matrix')
        print('2. Add Matrix')
        print('3. Multiply Matrix')
        print('4. Transpose Matrix')
        print('5. Switch Matrix')
        print('6. Scale Row')
        print('7. Add Scaled Column')
        print('8. REF')
        print('9. RREF')
        choice = input('Enter your choice: ')
        if choice == '1':
            self.input_matrix(self)
            self.display_matrx()
        elif choice == '2':
            self.input_matrix(self)
            other_matrix = MatriX.input_matrix()
            self.add_matrx(self, other_matrix)
            self.display_matrx()
        elif choice == '3':
            self.input_matrix(self)
            other_matrix = self.input_matrix()
            self.matrix_multiply(self, other_matrix)
            self.display_matrx()
        elif choice == '4':
            self.input_matrix(self)
            self.transpose(self)
            self.display_
        elif choice == '5':
            self.input_matrix(self)
            self.switch(self)
            self.display_matrx()
        elif choice == '6':
            self.input_matrix(self)
            self.scale_row(self)
            self.display_matrx()
        elif choice == '7':
            self.input_matrix(self)
            self.add_scaled_column(self)
            self.display_matrx()
        elif choice == '8':
            self.input_matrix(self)
            self.ref(self)
            self.display_matrx()
        elif choice == '9':
            self.input_matrix(self)
            self.rref(self)
            self.display_matrx()
        else:
            print('Invalid input')

    def input_matrix(self):
        """Have the user be able to input values for the matrix
        """
        for i in range(self.rows):
            row_input = input(f"Enter the values for row {i + 1} separated by spaces: ")
            self.matrix[i] = list(map(float, row_input.split()))

    def display_matrx(self):
        """The display function of the matrix"""
        print('Matrix:')
        print(self.matrix)

    def add_matrix(self, other_matrix):
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
        #create a new matrix instance with the result matrix
        return MatriX(self.rows, self.cols, result_matrix)
    
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
        return MatriX(self.rows, other_matrix, result_matrix)

    def det(self):
        """Determine the determinant of the matrix'''
        """
        return np.linalg.det(self.matrix)

    def transpose_numpy(self):
        """Be able to take a row and column and switch them"""
        transposed_matrix = []
        for j in range(self.cols):
            transposed_row = [self.matrix[i][j] for i in range(self.rows)]
            transposed_matrix.append(transposed_row)
        return transposed_matrix

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
        if not (0 <= row < self.rows):
            raise ValueError("Invalid row index")
        self.matrix[row] *= scalar

    def add_scaled_row(self, source_row, target_row, scalar):
        """Adds a scaled row to another row in the matrix.

        Args:
            source_row (int): Index of the row to be scaled and added.
            target_row (int): Index of the row to which the scaled row will be added.
            scalar (float): The scalar value by which to scale the source row before adding.
        """
        if not (0 <= source_row < self.rows and 0 <= target_row < self.rows):
            raise ValueError("Invalid row indices")
        self.matrix[target_row] += scalar * self.matrix[source_row]
     
    #RREF use sympy
    def row_echelon_form(self):
        """Where the first nonzero in each row (leading entry) is a 1 

        Returns:
            list: where a new matrix with ones in a consecutive order
        """
        new_matrix = self.matrix.copy() 
        #create a copy of the matrix
        for i in range(self.rows):
            pivot = new_matrix[i, i]
            if pivot == 0:
                for j in range(i + 1, self.rows):
                    if new_matrix[j, i] != 0:
                        new_matrix[[i, j]] = new_matrix[[j, i]]
                        #essentially swapping the rows
                        break
            pivot = new_matrix[i, i]
            if pivot != 0:
                new_matrix[i] /= pivot #divide the first entry by all the values
                for k in range(i + 1, self.rows):
                    new_matrix[k] -= new_matrix[k, i] * new_matrix[i]
        #create a new martix instance with the modified inside
        return MatriX(self.rows, self.cols, new_matrix)
    
    
    #RREF
    def reduced_row_echelon_form(self):
        """Where the leading 1 is the only nonzero in its column. 

        Returns:
            list: a matrix where there is ones in a consecutive order
        """
        new_matrix = self.row_echelon_form().matrix.copy()  # Get the matrix in row echelon form and make a copy
        for i in reversed(range(self.rows)):
            pivot_col = np.argmax(new_matrix[i] != 0)
            if pivot_col < self.cols:
                for j in reversed(range(i)):
                    new_matrix[j] -= new_matrix[j, pivot_col] * new_matrix[i]
        # Create a new MatriX instance with the modified matrix and return it
        return MatriX(self.rows, self.cols, new_matrix)
    
