from Objects.matrix import Matrix

l = 5
c = 5

matrix1 = Matrix(l,c)
#matrix1.set_matrix([[1,2],[3,4]])s
#matrix1.set([[3,1,0,1],[0,-1,3,4],[1,1,0,2],[0,1,1,-1]])
matriz = [
    [1, 2, 3, 4, 5],
    [0, 1, 4, 3, 2],
    [0, 0, 1, 6, 7],
    [0, 0, 0, 1, 8],
    [0, 0, 0, 0, 1]
]
#matrix1.set([[1,-4],[5,1]])
#matrix1.set([[1,-4,0],[5,1,8],[6,3,4]])
matrix1.set(matriz)
for i in matrix1.matrix:
    print(i)

print(matrix1.get_determinant())


#print(matrix1.transposed_matrix)