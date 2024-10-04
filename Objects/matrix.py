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
        transposed_matrix = []
        for i in range(len(self.matrix[0])):
            line = []
            for j in range(len(self.matrix)):
                line.append(self.matrix[j][i]) 
            transposed_matrix.append(line)
        return transposed_matrix

    def get_inverted(self):
        matrix_id = self.get_id().get()
        determinant = self.get_determinant()
        if  determinant != 0:
            inverted = Matrix(self.lines, self.colunes)
            equations = []
            for i in range(self.lines):
                eq = []
                for j in range(self.colunes):
                    for k in range(self.colunes):
                        eq += f"{self.matrix[i][k]}"

                equations.append(eq)
                
            for i in equations:
                print(i)



    def get_determinant(self):
        if self.lines != self.colunes:
            raise ValueError("Determinante só pode ser calculado para matrizes quadradas.")
        elif self.lines == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        elif self.lines == 3 :
            return (self.matrix[0][0] * (self.matrix[1][1] * self.matrix[2][2] - self.matrix[1][2] * self.matrix[2][1]) -
                    self.matrix[0][1] * (self.matrix[1][0] * self.matrix[2][2] - self.matrix[1][2] * self.matrix[2][0]) +
                    self.matrix[0][2] * (self.matrix[1][0] * self.matrix[2][1] - self.matrix[1][1] * self.matrix[2][0]))
        else:
            matrix_line = self.matrix[0]
            cofactors = []
            for k in range(self.lines):
                sub_matrix = Matrix(self.lines - 1, self.colunes - 1)
                matrix = []
                for i in range(self.lines):
                    
                    lines = []
                    for j in range(self.colunes):
                        if i != 0 and j != k:
                            number = self.matrix[i][j]
                            lines.append(number)
                    if lines != []:
                        matrix.append(lines)
                if matrix != []:
                    sub_matrix.set(matrix)

                sub_determinant = sub_matrix.get_determinant()
                for i in sub_matrix.get():
                    print(i)
                print("SubD: ", sub_determinant)

                cofactor = ((-1)**(0 + k)) * sub_determinant
                cofactors.append(cofactor)

            result = 0
            for i in range(self.lines):
                result += matrix_line[i] * cofactors[i]

            return result
            
            

    
 