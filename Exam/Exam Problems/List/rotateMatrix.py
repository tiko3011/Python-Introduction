def transposeMatrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    for i in range(rows):
        for j in range(i + 1, columns):
            matrix[i][j] += matrix[j][i]
            matrix[j][i] = matrix[i][j] - matrix[j][i]
            matrix[i][j] -= matrix[j][i]

    print(matrix)
    return matrix


def flipVerticalAxis(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    for i in range(rows):
        for j in range(columns // 2):
            mirror_j = columns - j - 1
            matrix[i][j] += matrix[i][mirror_j]
            matrix[i][mirror_j] = matrix[i][j] - matrix[i][mirror_j]
            matrix[i][j] -= matrix[i][mirror_j]

    print(matrix)
    return matrix


def rotateMatrix(matrix):
    transposeMatrix(matrix)
    flipVerticalAxis(matrix)


matrix1 = [[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 0, 1, 2],
[3, 4, 5, 6]]

rotateMatrix(matrix1)


