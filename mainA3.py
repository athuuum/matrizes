# 3. Faça um algoritmo em que o usuário define o tamanho da matriz e a preenche por completo com dados. A partir dessa matriz o algoritmo deve criar uma matriz do “tipo diagonal”.
# A matriz diagonal é quadrada e todos os elementos fora da diagonal principal são iguais a 0.
# Obrigatório: Utilizar o formato da matriz feita em sala de aula (aula05-exercícios). Não utilizar bibliotecas e funções do python.

# Definir o tamanho da matriz
n = int(input("Quantidade de Linhas da primeira matriz: "))
m = int(input("Quantidade de Colunas da primeira matriz: "))

# Montar e incluir matriz
linha = [0] * m
matriz = [linha] * n

l = 0
while l < n:
    linha = []
    c = 0
    while c < m:
        numero = int(input("Numero da Matriz 1 ({},{}): ".format(l, c)))
        linha.append(numero)
        c += 1
    matriz[l] = linha
    l += 1

# Exibir a matriz original
print("\nMatriz Original: ")
for linha in matriz:
    print(linha)

# Buscar diagonal, substitui valores que não são na diagonal por 0
for l in range(n):
   for c in range(m):
      if l != c:
          matriz[l][c] = 0

# Exibir a matriz diagonal
print("\nMatriz Digaonal: ")
for linha in matriz:
    print(linha)
