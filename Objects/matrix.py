class Matrix():

    def __init__(self, lines, colunes, is_square=False):
        self.lines = lines
        self.colunes = colunes
        if self.colunes == self.lines:
            self.is_square = True
        else:
            self.is_square = False
        self.matrix = [[0 for _ in range(colunes)] for _ in range(lines)]

    def get(self):
        return self.matrix
    
    def get_value(self,l, c):
        return self.matrix[l][c]

    def set_value(self, value, l, c):
        self.matrix[l][c] = value

    def set(self, mat):
        self.matrix = mat

    def get_id(self):
        if self.is_square == False:
            raise ValueError("Matriz identidade só pode ser calculada para matrizes quadradas.")
        else:
            id = Matrix(self.lines,self.colunes)
            for i in range(self.lines):
                lines = []
                for j in range(self.colunes):
                    number = 0
                    if i == j:
                        number = 1
                    id.set_value(number,i,j)

            return id
                    
    def get_transposed(self):
        transposed_matrix = Matrix(self.colunes, self.lines)
        for i in range(self.colunes):
            for j in range(self.lines):
                transposed_matrix.set_value(self.matrix[j][i], i, j) 
        return transposed_matrix

    def get_inverted(self):
        determinant = self.get_determinant()
        if  determinant != 0:
            inverted_matrix = Matrix(self.lines, self.colunes)
            #A matriz adjunta de A é a transposta da matriz de cofactores.
            adjunt_matrix = self.get_cofactor_matrix().get_transposed().get()
            for i in range(self.lines):
                for j in range(self.colunes):
                    number = adjunt_matrix[i][j] / self.get_determinant()
                    inverted_matrix.set_value(number,i,j)
            return inverted_matrix
        
    def get_cofactor_matrix(self):
        cofactor_matrix = Matrix(self.lines,self.colunes)
        for i in range(self.lines):
            for j in range(self.colunes):
                number = self.get_cofactor(i,j)
                cofactor_matrix.set_value(number, i, j)
        return cofactor_matrix


    def get_cofactor(self, line, colune):
        sub_matrix = Matrix(self.lines - 1, self.colunes - 1)
        matrix = []
        for i in range(self.lines):
            lines = []
            for j in range(self.colunes):
                if i != line and j != colune:
                    number = self.matrix[i][j]
                    lines.append(number)
            if lines != []:
                matrix.append(lines)
        if matrix != []:
            sub_matrix.set(matrix)

        sub_determinant = sub_matrix.get_determinant()
        cofactor = ((-1)**(line + colune)) * sub_determinant

        return cofactor

            
    def get_determinant(self):
        if self.lines != self.colunes:
            raise ValueError("Determinante só pode ser calculado para matrizes quadradas.")
        elif self.lines == 1:
            return self.matrix[0][0]
        elif self.lines == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        elif self.lines == 3 :
            dig_sec = (self.matrix[0][2] * self.matrix[1][1] * self.matrix[2][0]) + (self.matrix[0][0] * self.matrix[1][2] * self.matrix[2][1]) + (self.matrix[0][1] * self.matrix[1][0] * self.matrix[2][2])
            dig_pri = (self.matrix[0][0] * self.matrix[1][1] * self.matrix[2][2]) + (self.matrix[0][1] * self.matrix[1][2] * self.matrix[2][0]) + (self.matrix[0][2] * self.matrix[1][0] * self.matrix[2][1])
            return dig_pri - dig_sec
        else:
            matrix_line = self.matrix[0]
            cofactors = []

            for i in range(self.lines):
                cofactor = self.get_cofactor(0, i)
                cofactors.append(cofactor)
            result = 0

            for i in range(self.lines):
                result += matrix_line[i] * cofactors[i]

            return result 
            
            

    
 