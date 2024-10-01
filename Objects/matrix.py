def matrix(l, c):
    line = [0] * c
    matrix = [line] * l

    for i in range(l):
        line = []
        for j in range(c):
            number = int(input(f"Número ({i},{j}): "))
            line.append(number)
        matrix[i] = line

    return matrix


def transpose(matrix):
    result = []
    for i in range(len(matrix[0])):
        line = []
        for j in range(len(matrix)):
            line.append(matrix[j][i]) 
        result.append(line)
    return result