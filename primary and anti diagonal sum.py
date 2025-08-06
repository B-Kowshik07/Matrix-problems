def diagonal_sums(matrix):
    n = len(matrix)
    primary_sum = 0
    anti_sum = 0

    for i in range(n):
        primary_sum += matrix[i][i]
        anti_sum += matrix[i][n - 1 - i]

    return primary_sum, anti_sum

# Sample matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

p_sum, a_sum = diagonal_sums(matrix)

print("Primary Diagonal Sum:", p_sum)
print("Anti-Diagonal Sum:", a_sum)