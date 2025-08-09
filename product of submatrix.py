def product_submatrix(matrix,k):
    m=len(matrix)
    n=len(matrix[0])

    cropped_rows=matrix[k:m-k]
    crop=[row[k:n-k]for row in cropped_rows]

    product=1

    for row in crop:
        for values in row:
            product*=values

    return crop,product


m,n=map(int,input("ENter the no of rowsXcols: ").split())
matrix=[list(map(int,input().split())) for _ in range(m)]
k=int(input("Enter the number of rows&cols to crop: "))

result_matrix,product=product_submatrix(matrix,k)

for rows in result_matrix:
    print(*rows)

print("Product: ",product)

