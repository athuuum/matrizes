# 6. Faça um algoritmo em que o usuário define o tamanho da matriz e a 
# preenche por completo com dados. A partir dessa matriz o algoritmo deve 
# criar uma matriz do “tipo oposta”. A matriz oposta é obtida invertendo 
# o sinal de todos os elementos da matriz original.


from Objects.matrix import Matrix

l = int(input("Quantidade de linhas: "))
c = int(input("Quantidade de colunas: "))

matrix1 = Matrix(l,c)
for i in range(l):
    line = []
    for j in range(c):
        number = int(input(f"Número ({i},{j}): "))
        matrix1.set_value(number, i, j)

print("Matriz: ")
for i in matrix1.get():
   print(i)

matrix2 = Matrix(l,c)
print("Matriz oposta: ")
for i in range(l):
    line = []
    for j in range(c):
        result = matrix1.get_value(i,j) * -1
        matrix2.set_value(result, i, j)

for i in matrix2.get():
   print(i)

