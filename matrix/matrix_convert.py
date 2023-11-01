"""
A Python code to convert all the columns and rows of a number to 0 in a
matrix if that number is a 0
"""
def Convert():
    row1 = [1,2,3] #col1 = [1,4,7]
    row2 = [4,0,6] #col2 = [2,0,8]
    row3 = [7,8,9] #col3 = [3,6,9]
    all_mat = [row1,row2,row3]
    print(f"The entered matrix is:\n{row1}\n{row2}\n{row3}")
    row1col1 = [row1[0],row1[1],row1[2],row2[0],row3[0]]
    row1col2 = [row1[0],row1[1],row1[2],row2[1],row3[1]]
    row1col3 = [row1[0],row1[1],row1[2],row2[2],row3[2]]
    row2col1 = [row2[0],row2[1],row2[2],row1[0],row3[0]]
    row2col2 = [row2[0],row2[1],row2[2],row1[1],row3[1]]
    row2col3 = [row2[0],row2[1],row2[2],row1[2],row3[2]]
    row3col1 = [row3[0],row3[1],row3[2],row1[0],row2[0]]
    row3col2 = [row3[0],row3[1],row3[2],row1[1],row2[1]]
    row3col3 = [row3[0],row3[1],row3[2],row1[2],row2[2]]
    for item in row1col1:
        if item == 0:
            row1[0] = '#'
            row1[1] = '#'
            row1[2] = '#'
            row2[0] = '#'
            row3[0] = '#'
    for item in row1col2:
        if item == 0:
            row1[0] = '#'
            row1[1] = '#'
            row1[2] = '#'
            row2[1] = '#'
            row3[1] = '#'
    for item in row1col3:
        if item == 0:
            row1[0] = '#'
            row1[1] = '#'
            row1[2] = '#'
            row2[2] = '#'
            row3[2] = '#'
    for item in row2col1:
        if item == 0:
            row2[0] = '#'
            row2[1] = '#'
            row2[2] = '#'
            row1[0] = '#'
            row3[0] = '#'
    for item in row2col2:
        if item == 0:
            row2[0] = '#'
            row2[1] = '#'
            row2[2] = '#'
            row1[1] = '#'
            row3[1] = '#'
    for item in row2col3:
        if item == 0:
            row2[0] = '#'
            row2[1] = '#'
            row2[2] = '#'
            row1[2] = '#'
            row3[2] = '#'
    for item in row3col1:
        if item == 0:
            row3[0] = '#'
            row3[1] = '#'
            row3[2] = '#'
            row1[0] = '#'
            row2[0] = '#'
    for item in row3col2:
        if item == 0:
            row3[0] = '#'
            row3[1] = '#'
            row3[2] = '#'
            row1[1] = '#'
            row2[1] = '#'
    for item in row3col3:
        if item == 0:
            row3[0] = '#'
            row3[1] = '#'
            row3[2] = '#'
            row1[2] = '#'
            row2[2] = '#'
    for i in range(len(all_mat)):
        for j in range(len(row1)):
            if all_mat[i] == 0 or row1[j] == 0:
                all_mat[i][j]= 0
    print(f"The converted matrix is:\n{all_mat}")
if __name__ == "__main__":
    Convert()
print("\nCode developed by Masino")
"""FAILED CODE !!!"""