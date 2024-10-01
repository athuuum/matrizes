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
