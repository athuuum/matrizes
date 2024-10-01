# 5. Faça um algoritmo em que o usuário define o tamanho da matriz e a 
# preenche por completo com dados. A partir dessa matriz o algoritmo deve 
# criar uma matriz do “tipo  igualdade”. A matriz igualdade é obtida quando 
# possui a mesma quantidade de linhas/colunas e os mesmos valores ou elementos. 
# Ou seja, uma réplica da matriz original.

l = int(input("Quantidade de linhas: "))
c = int(input("Quantidade de colunas: "))

line = [0] * c
matrix = [line] * l

for i in range(l):
   print(matrix[i])  

for i in range(l):
   line = []
   for j in range(c):
       number = int(input(f"Número ({i},{j}): "))
       line.append(number)
   matrix[i] = line

print("Matriz: ")
for i in range(l):
   print(matrix[i])

matrix2 = matrix

#for i in matrix:
#   copied_line = i[:]
#   matrix2.append(copied_line)

print("Matriz igualdade: ")
for i in range(l):
   print(matrix2[i])
