def latin_matrix(matrix):
    n=len(matrix)

    for row in matrix:
        if set(row)!=set(range(1,n+1)):
            return False

    for col_index in range(n):
        col=[matrix[col_index][row_index] for row_index in range(n)]
        if set(col)!=set(range(1,n+1)):
            return False

    return True

n = int(input("Enter size of matrix (n): "))
matrix = [list(map(int, input().split())) for _ in range(n)]

if latin_matrix(matrix):
    print("It is a Latin square.")
else:
    print("Not a Latin square.")
