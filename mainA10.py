# 10. Faça um algoritmo em que o usuário define o tamanho da matriz e a 
# preenche por completo com dados. A partir disso gere uma matriz inversa. 
# Para isso ela precisa ser quadrada e seu determinante tem que ser diferente 
# de zero, caso contrário não haverá inversão.

from Objects.matrix import matrix

l = int(input("Tamanho da matrix quadrada: "))

matrix1 = matrix(l,l)

print("\nMATRIZ")
for i in range(l):
   print(matrix1[i])

print("\nMATRIZ INVERSA")

inverse_matrix = []
for i in range(l):
    line = []
    for j in range(l):
        result = 0
        for k in range(l):
               if (i == j):
                  if(matrix1[i][k]!=0):
                     result = f"1/{matrix1[i][k]}"
                  print(result)
               else:
                  result += 0
                  2
           
      
        line.append(result)
    inverse_matrix.append(line)

for i in range(l):
   print(inverse_matrix[i])