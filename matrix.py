class Matrix:
    """This is the matrix class for all the linear algebra"""
    def __init__(self, rows, cols):
        #want the user to be able to specify the number of rows and colums
        self.rows = int(input('Enter the number of rows: '))
        self.cols = int(input('Enter the number of columns: '))
        self.matrix =[[0 for i in range(self.cols)] for j in range(self.rows)]

    def input_matrix(self):
        """Have the user be able to input values for the matrix
        """
        for i in range(self.rows):
            row_input = input(f"Enter the values for row {i + 1} separated by spaces: ")
            self.matrix[i] = list(map(float, row_input.split()))

    def display_matrx(self):
        for row in self.matrix:
            print(' '.join(map(str, row)))
