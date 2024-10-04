def get_cofactor(self, line):
    cofactors = []
    for k in range(self.lines):
        sub_matrix = Matrix(self.lines - 1, self.colunes - 1)
        matrix = []
        for i in range(self.lines):
            
            lines = []
            for j in range(self.colunes):
                if i != line and j != k:
                    number = self.matrix[i][j]
                    lines.append(number)
            if lines != []:
                matrix.append(lines)
        if matrix != []:
            sub_matrix.set(matrix)

        sub_determinant = sub_matrix.get_determinant()
        cofactor = ((-1)**(0 + k)) * sub_determinant
        cofactors.append(cofactor)
    return cofactors