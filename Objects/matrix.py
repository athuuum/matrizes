
class Matrix():

    def __init__(self, lines, colunes):
        self.lines = lines
        self.colunes = colunes
        self.matrix = [[0 for _ in range(colunes)] for _ in range(lines)]

    def get(self):
        return self.matrix
    
    def get_value(self,value, l, c):
        return self.matrix[l][c]

    def set_value(self, value, l, c):
        self.matrix[l][c] = value

    def transpose(self):
        result = []
        for i in range(len(self.matrix[0])):
            line = []
            for j in range(len(self.matrix)):
                line.append(self.matrix[j][i]) 
            result.append(line)
        return result

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
            pass

