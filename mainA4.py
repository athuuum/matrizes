# 4. Faça um algoritmo em que o usuário define o tamanho da matriz e o algoritmo gera uma matriz do “tipo identidade”. É uma matriz quadrada onde todos os elementos da diagonal
# principal são iguais a 1 e todos os elementos fora dessa diagonal são iguais a 0.
# Obrigatório: Utilizar o formato da matriz feita em sala de aula (aula05-exercícios). Não utilizar bibliotecas e funções do python.

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
