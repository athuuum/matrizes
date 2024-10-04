# 10. Faça um algoritmo em que o usuário define o tamanho da matriz e a 
# preenche por completo com dados. A partir disso gere uma matriz inversa. 
# Para isso ela precisa ser quadrada e seu determinante tem que ser diferente 
# de zero, caso contrário não haverá inversão.

from Objects.matrix import Matrix

l = int(input("Tamanho da matrix quadrada: "))

matrix1 = Matrix(l,l)

for i in range(l):
    line = []
    for j in range(l):
        number = int(input(f"Número ({i},{j}): "))
        matrix1.set_value(number, i, j)
        
print("\nMATRIZ")
for i in range(l):
   print(matrix1.get()[i])

print(matrix1.get_determinant())
   
print("\nMATRIZ INVERSA")
inverted = matrix1.get_inverted()

for i in inverted.get():
    print(i)


