# 10. Faça um algoritmo em que o usuário define o tamanho da matriz e a 
# preenche por completo com dados. A partir disso gere uma matriz inversa. 
# Para isso ela precisa ser quadrada e seu determinante tem que ser diferente 
# de zero, caso contrário não haverá inversão.

from Objects.matrix import Matrix

l = 2
matrix1 = Matrix(l,l)
#matrix1.set([[3,1,0,1],[0,-1,3,4],[1,1,0,2],[0,1,1,-1]])
matrix1.set([[2,0],[4,3]])

# for i in range(l):
#     line = []
#     for j in range(l):
#         number = int(input(f"Número ({i},{j}): "))
#         matrix1.set_value(number, i, j)
        
print("\nMATRIZ")
for i in range(l):
   print(matrix1.get()[i])
   
print("\nMATRIZ INVERSA")
matrix1.get_inverted()
matrix_id = matrix1.get_id()
matrix_inv = matrix1.get_inverted()
for i in matrix_id.get():
   print(i)
