# Definir o tamanho da matriz
n = int(input("Quantidade de Linhas da primeira matriz: "))
m = int(input("Quantidade de Colunas da primeira matriz: "))

linha = [0] * m
matriz = [linha] * n

# Monta a matriz e a preenche com 0
matriz = []
for l in range(n):
    linha = []
    for c in range(m):
        linha.append(0)
    matriz.append(linha)

print("\nMatriz Original: ")
for linha in matriz:
    print(linha)

# Buscar diagonal, substitui os valores da diagonal por 1
for l in range(n):
   for c in range(m):
      if l == c:
          matriz[l][c] = 1

# Exibir resultado final com diagonal
print("\nMatriz Digaonal: ")
for linha in matriz:
    print(linha)
