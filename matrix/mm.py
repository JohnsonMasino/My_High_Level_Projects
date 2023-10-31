def Convert(matrix):
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    # Initialize flags to track if there are any zeros in each row and column
    zero_in_row = [False] * n_rows
    zero_in_col = [False] * n_cols

    # Find the positions of zeros in the matrix and update the flags
    for i in range(n_rows):
        for j in range(n_cols):
            if matrix[i][j] == 0:
                zero_in_row[i] = True
                zero_in_col[j] = True

    # Update the matrix based on the flags
    for i in range(n_rows):
        for j in range(n_cols):
            if zero_in_row[i] or zero_in_col[j]:
                matrix[i][j] = 0

    return matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 2, 6],
        [7, 0, 9]
    ]

    print("The entered matrix is:")
    for row in matrix:
        print(row)

    converted_matrix = Convert(matrix)

    print("The converted matrix is:")
    for row in converted_matrix:
        print(row)
