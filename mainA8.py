# 8. Faça um algoritmo em que o usuário define o tamanho de duas matrizes e as 
# preenche por completo com dados. A partir disso faça a multiplicação entre as 
# matrizes e armazene em uma terceira matriz. Lembrando que para que seja possível 
# fazer a multiplicação de matrizes é necessário que o número de linhas da primeira 
# matriz seja igual ao número de colunas da segunda, trate essa exceção no algoritmo. 
# Outro ponto importante na multiplicação é que deve-se multiplicar os elementos da 
# linha da primeira matriz pelos elementos da coluna da segunda matriz e somar esses 
# produtos. Se as matrizes forem 3x2 e 2x3, multiplicar o 1° elemento da linha 1 da 
# primeira matriz pelo 1° elemento da coluna 1 da segunda matriz, somamos ao produto 
# do 2° elemento da linha 1 da primeira matriz pelo 2° elemento da coluna 1 da segunda 
# matriz e assim por diante.

from Objects.matrix import Matrix

l1 = int(input("Quantidade de linhas (MATRIZ 1): "))
c1 = int(input("Quantidade de colunas (MATRIZ 1): "))

matrix1 = Matrix(l1,c1)

for i in range(l1):
    line = []
    for j in range(c1):
        number = int(input(f"Número ({i},{j}): "))
        matrix1.set_value(number, i, j)

l2 = c1
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
print("\nMATRIZ 2")
for i in matrix2.get():
   print(i)


print("\nMATRIZ 1 X MATRIZ 2 =")


l3 = l1
c3 = c2

matrix3 = Matrix(l3,c3)

for i in range(l3):
    line = []
    for j in range(c3):
        result = 0
        for k in range(c1):
            result += matrix1.get_value(i,k)* matrix2.get_value(k,j)
        matrix3.set_value(result, i, j)
for i in matrix3.get():
   print(i)

