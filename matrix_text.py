def det(matrix):
    n = len(matrix)

    if n == 1:
        return matrix[0][0]
    
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    total = 0
    for j in range(n):
        minor = [row[:j] + row[j+1:] for row in matrix[1:]]
        sign = 1 if j % 2 == 0 else - 1
        total += sign * matrix[0][j] * det(minor)

    return total

matrix_list = [
    [2,1,0,3,1,0,2,1,0,1],
    [1,3,2,0,1,1,0,2,1,0],
    [0,2,4,1,0,1,1,0,2,1],
    [3,0,1,5,2,0,1,1,0,2],
    [1,1,0,2,4,1,0,1,1,0],
    [0,1,1,0,1,3,2,0,1,1],
    [2,0,1,1,0,2,4,1,0,1],
    [1,2,0,1,1,0,1,3,2,0],
    [0,1,2,0,1,1,0,2,4,1],
    [1,0,1,2,0,1,1,0,1,3]
]

result = det(matrix_list)
print(result)