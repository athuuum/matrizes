# 9. Faça um algoritmo em que o usuário define o tamanho de duas matrizes e as 
# preenche por completo com dados. A partir disso faça a transposição da matriz 
# para outra matriz. A transposição de uma matriz é feita trocando suas linhas 
# por colunas. Ou seja, se a matriz é (m x n) passa a ser (n x m).

from Objects.matrix import Matrix

l1 = int(input("Quantidade de linhas (MATRIZ 1): "))
c1 = int(input("Quantidade de colunas (MATRIZ 1): "))

matrix1 = Matrix(l1,c1)

for i in range(l1):
    line = []
    for j in range(c1):
        number = int(input(f"Número ({i},{j}): "))
        matrix1.set_value(number, i, j)

l2 = int(input("Quantidade de linhas (MATRIZ 2): "))
c2 = int(input("Quantidade de colunas (MATRIZ 2): "))

matrix2 = Matrix(l2,c2)
for i in range(l2):
    line = []
    for j in range(c2):
        number = int(input(f"Número ({i},{j}): "))
        matrix2.set_value(number, i, j)

print("\nMATRIZ 1")
for i in matrix1.get():
   print(i)

print("\nMATRIZ 1 [transposta]")
for i in matrix1.get_transposed():
   print(i)

print("\nMATRIZ 2")
for i in matrix2.get():
   print(i)


print("\nMATRIZ [transposta]")
for i in matrix2.get_transposed():
   print(i)