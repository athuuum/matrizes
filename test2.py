from Objects.matrix import Matrix

l = 4
c = 4

matrix1 = Matrix(l,c)
#matrix1.set_matrix([[1,2],[3,4]])
matrix1.set([[0,-4,0,0],[0,1,3,0],[3,2,1,-1],[0,2,1,1]])

'''for i in range(l):
    line = []
    for j in range(c):
        number = int(input(f"Número ({i},{j}): "))
        matrix1.set_value(number, i, j)'''


for i in matrix1.matrix:
    print(i)

print(matrix1.get_determinant())


#print(matrix1.transposed_matrix)