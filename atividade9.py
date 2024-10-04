# Definir o tamanho da primeira matriz
n = int(input("Quantidade de Linhas da primeira matriz: "))
m = int(input("Quantidade de Colunas da primeira matriz: "))

# Montar e incluir a primeira matriz
matriz = []
for l in range(n):
    linha = []
    for c in range(m):
        numero = int(input("Numero da Matriz 1 ({},{}): ".format(l, c)))
        linha.append(numero)
    matriz.append(linha)

# Definir o tamanho da segunda matriz
o = int(input("Quantidade de Linhas da segunda matriz: "))
p = int(input("Quantidade de Colunas da segunda matriz: "))

# Verificar se as matrizes tem tamanhos iguais
if n != o or m != p:
    print("Erro: As matrizes devem ter o mesmo tamanho para continuar.")
else:

    # Montar e incluir a segunda matriz
    matriz2 = []
    for l in range(o):
        linha2 = []
        for c in range(p):
            numero = int(input("Numero da Matriz 2 ({},{}): ".format(l, c)))
            linha2.append(numero)
        matriz2.append(linha2)

    # Transpor a primeira matriz
    matriz_transposta = [[0 for _ in range(n)] for _ in range(m)]

    for l in range(n):
        for c in range(m):
            matriz_transposta[c][l] = matriz[l][c]

    # Transpor a segunda matriz
    matriz_transposta2 = [[0 for _ in range(p)] for _ in range(o)]

    for l in range(p):
        for c in range(o):
            matriz_transposta2[c][l] = matriz2[l][c]

    # Exibir a primeira matriz
    print("\nMatriz 1: ")
    for linha in matriz:
        print(linha)

    # Exibir a segunda matriz
    print("\nMatriz 2: ")
    for linha2 in matriz2:
        print(linha2)

    # Exibir a transposta da primeira matriz
    print("\nTransposição da Matriz 1: ")
    for linha_transposta in matriz_transposta:
        print(linha_transposta)

    # Exibir a transposta da primeira matriz
    print("\nTransposição da Matriz 2: ")
    for linha_transposta2 in matriz_transposta2:
        print(linha_transposta2)
