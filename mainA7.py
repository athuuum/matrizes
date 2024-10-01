# 7. Faça um algoritmo em que o usuário define o tamanho da matriz e a 
# preenche por completo com dados. A partir dessa matriz o algoritmo deve 
# criar uma matriz do “tipo transposta”. A matriz transposta é obtida a partir 
# da troca ordenada de linhas por colunas (e vice-versa), ou seja, todos os 
# elementos de uma linha passam a ser elementos de uma coluna, e todos os 
# elementos de uma coluna passam a ser elementos de uma linha. Seja M a 
# matriz original, a transposta é denotada por Mt.

from Objects.matrix import *

l = int(input("Quantidade de linhas: "))
c = int(input("Quantidade de colunas: "))

matrix1 = matrix(l,c)

print("\nMATRIZ: ")
for i in range(l):
   print(matrix1[i])

print("\nMATRIZ TRANSPOSTA: ")

matrix1_t = transpose(matrix1)

for i in matrix1_t:
   print(i)

"""matrix2 = []
for i in range(l):
    line = []
    for j in range(c):
        line.append(matrix1[j][i])
    matrix2.append(line)

for i in range(l):
   print(matrix2[i])"""