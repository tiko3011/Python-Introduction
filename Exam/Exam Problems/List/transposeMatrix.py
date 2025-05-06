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


matrix1 = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]

transposeMatrix(matrix1)
