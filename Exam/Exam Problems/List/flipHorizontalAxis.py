# [[1, 0],
# [0, 1],
# [0, 0]]
#
# [[0, 0],
# [0, 1],
# [1, 0]]

def flipVerticalAxis(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    for i in range(rows // 2):
        for j in range(columns):
            mirror_i = rows - i - 1
            matrix[i][j] += matrix[mirror_i][j]
            matrix[mirror_i][j] = matrix[i][j] - matrix[mirror_i][j]
            matrix[i][j] -= matrix[mirror_i][j]

    print(matrix)
    return matrix


matrix1 = [
    [1, 2, 3, 0],
    [4, 5, 6, 0],
    [7, 8, 9, 0]
]

flipVerticalAxis(matrix1)
