# 4. Faça um algoritmo em que o usuário define o tamanho da matriz e o algoritmo gera uma matriz do “tipo identidade”.
# É uma matriz quadrada onde todos os elementos da diagonal
# principal são iguais a 1 e todos os elementos fora dessa diagonal são iguais a 0.

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

id_matrix = matrix1.get_id()
          
# Exibir resultado final com diagonal
print("\nMatriz Identidade: ")
for linha in id_matrix.get():
    print(linha)
