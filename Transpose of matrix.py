def transpose(matrix):
    m=len(matrix)
    n=len(matrix[0])

    transpose=[]

    for col in range(n):
        new_row=[]
        for rows in range(m):
            new_row.append(matrix[rows][col])
        transpose.append(new_row)

    return transpose

m, n = map(int, input("Enter rows and cols: ").split())
matrix = [list(map(int, input().split())) for _ in range(m)]

transposed = transpose(matrix)

print("Transpose:")
for row in transposed:
    print(*row)