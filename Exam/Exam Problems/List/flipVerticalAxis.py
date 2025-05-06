# [[1, 0, 0],
# [1, 0, 0]]

# [[0, 0, 1],
# [0, 0, 1]]

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


matrix1 = [
    [1, 2, 3, 0],
    [4, 5, 6, 0],
    [7, 8, 9, 0]
]

flipVerticalAxis(matrix1)
