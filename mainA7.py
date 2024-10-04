# 7. Faça um algoritmo em que o usuário define o tamanho da matriz e a 
# preenche por completo com dados. A partir dessa matriz o algoritmo deve 
# criar uma matriz do “tipo transposta”. A matriz transposta é obtida a partir 
# da troca ordenada de linhas por colunas (e vice-versa), ou seja, todos os 
# elementos de uma linha passam a ser elementos de uma coluna, e todos os 
# elementos de uma coluna passam a ser elementos de uma linha. Seja M a 
# matriz original, a transposta é denotada por Mt.

from Objects.matrix import Matrix

l = int(input("Quantidade de linhas: "))
c = int(input("Quantidade de colunas: "))

matrix1 = Matrix(l,c)
for i in range(l):
    line = []
    for j in range(c):
        number = int(input(f"Número ({i},{j}): "))
        matrix1.set_value(number, i, j)

print("\nMATRIZ: ")
for i in matrix1.get():
   print(i)

print("\nMATRIZ TRANSPOSTA: ")

transposed_matrix = matrix1.get_transposed()
for i in transposed_matrix:
   print(i)

