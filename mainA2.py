# Definir o tamanho da primeira matriz
n = int(input("Quantidade de Linhas da primeira matriz: "))
m = int(input("Quantidade de Colunas da primeira matriz: "))

# Montar e incluir a primeira matriz
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

# Definir o tamanho da segunda matriz
o = int(input("Quantidade de Linhas da segunda matriz: "))
p = int(input("Quantidade de Colunas da segunda matriz: "))

# Verificar se as matrizes tem tamanhos iguais
if n != o or m != p:
    print("Erro: As matrizes devem ter o mesmo tamanho para continuar.")
else:

    # Montar e incluir a segunda matriz
    linha2 = [0] * p
    matriz2 = [linha2] * o

    l = 0
    while l < o:
        linha2 = []
        c = 0
        while c < p:
            numero = int(input("Numero da Matriz 2 ({},{}): ".format(l, c)))
            linha2.append(numero)
            c += 1
        matriz2[l] = linha2
        l += 1

    # Terceira matriz para armazenar a soma
    matriz_final = [[0 for _ in range(m)] for _ in range(n)]

    # Subtrair as matrizes
    l = 0
    while l < n:
        c = 0
        while c < m:
            matriz_final[l][c] = matriz[l][c] - matriz2[l][c]
            c += 1
        l += 1

    # Exibir a primeira matriz
    print("\nMatriz 1: ")
    for linha in matriz:
        print(linha)

    # Exibir a segunda matriz
    print("\nMatriz 2: ")
    for linha2 in matriz2:
        print(linha2)

    # Exibir a matriz resultante final
    print("\nMatriz Final:")
    i = 0
    while i < n:
        print(matriz_final[i])
        i += 1
