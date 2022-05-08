import numpy as np

class Matrix :
    def __init__(self ,rows: int, columns: int) :
        self.rows = rows
        self.columns = columns
        self.data = np.zeros((rows, columns))
        self.name = "Unkown"
    
    def update_row(self, lst: list[int], index: int):
        index -= 1
        if(self.columns != len(lst) or index > self.rows) :
            return False
        
        
        for i in range(self.columns):
            self.data[index][i] = lst[i]
        return True

    def update_column(self, lst: list[int], index: int):
        index -= 1
        if(self.rows != len(lst) or self.columns < index):
            return False

        for i in range(self.rows):
            self.data[i][index] = lst[i]
        return True

    def scale_row(self,row: int, scaler: int):
        for i in range(self.columns):
            self.data[row][i] *= scaler

    def swap_row(self, row1: int, row2: int):
        for i in range(self.columns):
            temp = self.data[row1][i]
            self.data[row1][i] = self.data[row2][i]
            self.data[row2][i] = temp
    
    def sum_row(self, row: int, scaler: int, scaled: int):
        for i in range(self.columns):
            self.data[row][i] += self.data[scaled][i] * scaler

    def matrix_copy(self):
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j]
        
        return result
    
    def sub_matrix(self, row: int, column: int):
        row -= 1
        column -= 1
        
        if (self.rows <= 1 or self.columns <= 1) :
            return  False
        
        result = Matrix(self.rows - 1, self.columns - 1)
        i_index = 0
        

        for i in range(self.rows):
            j_index = 0
            if (i != row):
                for j in range(self.columns):
                    if (j != column):
                        result.data[i_index][j_index] = self.data[i][j]
                        j_index += 1
                        
                        
                i_index += 1

        return result

    def determinant(self):
        if (self.rows != self.columns) :
            return  False
        
        if(self.rows == 1):
            return self.data[0][0]
        if(self.rows == 2):
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]

        total = 0
        for i in range(self.rows):
            total += ((-1) ** i) * (self.data[0][i]) * (self.sub_matrix(1,i + 1)).determinant()        
        return total
    
    def inverse(self, i_index: int, j_index: int):
        
        if (self.row != self.columns or self.row <= 1) :
            return  False

def matrix_sum(m1: Matrix, m2: Matrix):
    if (m1.rows != m2.rows or m1.columns != m2.columns):
        return False
    
    result = Matrix(m1.rows, m1.columns)
    for i in range(m1.row):
        for j in range(m1.columns):
            result.data[i][j] = m1.data[i][j] + m2.data[i][j]
    return result

def matrix_scale(m1: Matrix, scaler: int):
    for i in range(m1.row):
        for j in range(m1.columns):
            m1.data[i][j] *= scaler
    
    return True

def matrix_multiplication(m1: Matrix, m2: Matrix):
    if (m1.columns != m2.rows):
        return False
    
    result = Matrix(m1.rows, m2.columns)

    for i in range(m1.rows):
        for j in range(m2.columns):
            total = 0
            for z in range(m1.columns):
                total += m1.data[i][z] * m2.data[z][j]
            result.data[i][j] = total
    
    return result



#the VECTOR class is a subclass of matrix
class Vector(Matrix):
    def __init__(self, rows: int, columns: int = 1):
        super().__init__(rows, columns)
        self.columns = 1
        self.data =np.zeros((rows, columns))

    def update(self, lst: list[int]) :
        if(len(self.data) != len(lst)):
            return False

        for i in range(self.rows):
            self.data[i][0] = lst[i]
        return True


def dot_product(v1: Vector, v2: Vector):
    if (v1.row != v2.row):
        return False
    sum = 0
    for i in range(v1.row):
        sum += v1.data[i][0] * v2.data[i][0]
    
    return sum

def cross_product(v1: Vector, v2: Vector):
    if (v1.rows != v2.rows or v1.rows != 3):
        return False
    
    result = Vector(v1.rows)
    result.data[0][0] = v1.data[1][0] * v2.data[2][0] - v1.data[2][0] * v2.data[1][0] 
    result.data[1][0] = v1.data[2][0] * v2.data[0][0] - v1.data[0][0] * v2.data[2][0] 
    result.data[2][0] = v1.data[0][0] * v2.data[1][0] - v1.data[1][0] * v2.data[0][0]
    return result

""""
#below this line all functions are created for calculating rref
def find_pivot_up(m1: Matrix, column: int, starting_row: int):
    while (starting_row < m1.rows and m1.data[starting_row][column] == 0):
        starting_row += 1
    
    starting_row -= 1
    if (m1.data[starting_row][column] == 0):
        return False
    else :
        return (starting_row,column)

def find_pivot_down(m1: Matrix, column: int, starting_row: int):
    while (starting_row >= 0 and m1.data[starting_row][column] == 0):
        starting_row -= 1
    
    starting_row += 1
    if (m1.data[starting_row][column] == 0):
        return False
    else :
        return (starting_row,column)

def rref(m1: Matrix):
    pivot = find_pivot_up(m1, 0,0)
    edit_column = 0
    edit_row = 0

    while(pivot == False):
        edit_column += 1
        pivot = find_pivot_up(m1, edit_column, 0)
    
    #gauss part of algorithm
    while(pivot != False and edit_column < m1.columns and edit_row < m1.rows):
        m1.swap_row(edit_row, pivot[0])
        oporate_pivot_guass(m1, (edit_row, edit_column))
        edit_column += 1
        edit_row += 1
        pivot = find_pivot_up(m1, edit_column, edit_row)
        while(pivot == False):
            edit_column += 1
            pivot = find_pivot_up(m1, edit_column, 0)
        

def oporate_pivot_guass(m1: Matrix, pivot):
    if (m1.data[pivot[0]][pivot[1]] != 1):
        m1.scale_row(pivot[0], (1 / m1.data[pivot[0]][pivot[1]]))
    
    for i in range(pivot[0] + 1, m1.rows):
        if (m1.data[i][pivot[1]] != 0):
            m1.sum_row(i, m1.data[i][pivot[1]] * -1, pivot[0])

def oporate_pivot_jordan(m1: Matrix, pivot):
    for i in range(0, pivot[0]):
        m1.sum_row   


""" 

