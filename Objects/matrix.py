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