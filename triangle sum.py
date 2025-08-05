def triangle_sums(N, matrix):
    upper_sum = 0
    lower_sum = 0

    for i in range(N):
        for j in range(N):
            if i + j <= N - 1:
                upper_sum += matrix[i][j]
            if i + j >= N - 1:
                lower_sum += matrix[i][j]
    return upper_sum, lower_sum


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

upper_sum, lower_sum = triangle_sums(N, matrix)
print(upper_sum)
print(lower_sum)