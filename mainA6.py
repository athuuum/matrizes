# 6. Faça um algoritmo em que o usuário define o tamanho da matriz e a 
# preenche por completo com dados. A partir dessa matriz o algoritmo deve 
# criar uma matriz do “tipo oposta”. A matriz oposta é obtida invertendo 
# o sinal de todos os elementos da matriz original.


from Objects.matrix import matrix

l = int(input("Quantidade de linhas: "))
c = int(input("Quantidade de colunas: "))

matrix1 = matrix(l,c)

print("Matriz: ")
for i in range(l):
   print(matrix1[i])


matrix2 = []
print("Matriz oposta: ")
for i in range(l):
    line = []
    for j in range(c):
        line.append(matrix1[i][j]*-1)
    matrix2.append(line)

for i in range(l):
   print(matrix2[i])
