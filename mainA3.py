# 3. Faça um algoritmo em que o usuário define o tamanho da matriz e a preenche por completo com dados. 
# A partir dessa matriz o algoritmo deve criar uma matriz do “tipo diagonal”.
# A matriz diagonal é quadrada e todos os elementos fora da diagonal principal são iguais a 0.

from Objects.matrix import Matrix

# Definir o tamanho da matriz
n = int(input("Tamanho da matriz quadrada: "))

# Montar e incluir matriz
matrix1 = Matrix(n,n)

for i in range(n):
    line = []
    for j in range(n):
        number = int(input(f"Número ({i},{j}): "))
        matrix1.set_value(number, i, j)
# Exibir a matriz original
print("\nMatriz Original: ")
for linha in matrix1.get():
    print(linha)

# Buscar diagonal, substitui valores que não são na diagonal por 0
'''for l in range(n):
   for c in range(m):
      if l != c:
          matriz[l][c] = 0'''
diagonal_matrix = matrix1.get_diagonal_matrix()

# Exibir a matriz diagonal
print("\nMatriz Digaonal: ")
for linha in diagonal_matrix.get():
    print(linha)
