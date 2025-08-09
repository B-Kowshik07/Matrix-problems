rows, cols = map(int, input("Enter rows and cols: ").split())

matrix = []
num = 1

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(num)
        num += 1

    if i % 2 == 1:
        row.reverse()

    matrix.append(row)

for r in matrix:
    print(*r)
