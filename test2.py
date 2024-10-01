from Objects.matrix import Matrix

matrix1 = Matrix(3,2)
#matrix1.set_matrix([[1,2],[3,4]])


for i in matrix1.matrix:
    print(i)

matrix1.get_determinant()


#print(matrix1.transposed_matrix)