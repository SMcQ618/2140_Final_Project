import sympy
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

    def add_matrx(self, other_matrix):
        """Be able to take one matrix and add it with another"""
        if self.rows != other_matrix.rows or self.cols != other_matrix.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows): #have to iterate over all the rows and cols
            for j in range(self.cols):
                result.matrix[i][j] = self.matrix[i][j] + other_matrix.matrix[i][j]
        return result
    
    def transpose(self):
        """Be able to take a row and column and switch them"""
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[j][i] = self.matrix[i][j]
        return result

    def swap_rows(self, row1, row2):
            self.matrix[row1], self.matrix[row2] = self.matrix[row2], self.matrix[row1]

    def scale_row(self, row, scalar):
        self.matrix[row] = [element * scalar for element in self.matrix[row]]

    def add_scaled_row(self, source_row, target_row, scalar):
        for i in range(self.cols):
            self.matrix[target_row][i] += scalar * self.matrix[source_row][i]
     
    #RREF use sympy
    def row_echelon_form(self):
        """Where the first nonzero in each row (leading entry) is a 1 

        Returns:
            list: where a new matrix with ones in a consecutive order
        """
        ref_matrix = Matrix(self.rows, self.cols)
        ref_matrix.matrix = [row[:] for row in self.matrix]
        #the line above creates a copy of the original matrix

        lead = 0 #the index of the leading colum in the matrix
        for r in range(ref_matrix.rows):
            if lead >= ref_matrix.cols:
                return ref_matrix

            i = r
            while ref_matrix.matrix[i][lead] == 0:
                i += 1
                if i == ref_matrix.rows:
                    i = r #iterating ov each row
                    lead += 1
                    if ref_matrix.cols == lead:
                        return ref_matrix
                    
            ref_matrix.swap_rows(i, r)
            lv = ref_matrix.matrix[i][lead] 
            #lv is the value of the leading coefficient, the nonzero entry in the leading column

            ref_matrix.add_scaled_row(r, 1.0 / lv)
            
            for i in range(ref_matrix.rows):
                if i != r:
                    lv = ref_matrix.matrix[i][lead]
                    ref_matrix.add_scaled_row(r, i, -lv)
            lead += 1
        return ref_matrix
    
    #RREF
    def reduced_row_echelon_form(self):
        """Where the leading 1 is the only nonzero in its column. 

        Returns:
            list: a matrix where there is ones in a consecutive order
        """
        rref_matrix = self.row_echelon_form()

        for r in range(rref_matrix.rows -1, -1, -1):
            lead = -1
            for c in range(rref_matrix.cols):
                if rref_matrix.matrix[r][c] != 0:
                    lead = c
                    break

            if lead != -1:
                rref_matrix.scale_row(r, 1 / rref_matrix.matrix[r][lead])
                for i in range(r):
                    rref_matrix.add_scaled_row(r, i, -rref_matrix.matrix[i][lead])
        return rref_matrix
