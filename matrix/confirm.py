def mat(matrix):
    row = len(matrix)
    col = len(matrix[0])
    new_row = [False] * row
    new_col = [False] * col
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                new_row[i] = True
                new_col[j] = True
    for i in range(row):
        for j in range(col):
            if new_row[i] or new_col[j]:
                matrix[i][j] = 0
    return matrix
if __name__ == "__main__":
    matrix1 = [
        [1,2,3],
        [4,0,9],
        [9,8,7]
    ]
    print("The main matrix is: ")
    for i in matrix1:
        print(i)
    converted_matrix = mat(matrix1)
    print("\nConverted matrix is: ")
    for i in converted_matrix:
        print(i)
print("\nCode developed by Masino")