"""
A Python code to roll a matrix clockwise to 90 degrees.
Code developed by Masino
"""
def Rotate():
    mat1 = [11,12,13,14]
    mat2 = [25,26,27,28]
    mat3 = [31,32,33,34]
    mat4 = [45,46,47,48]
    all_mat = f"{mat1}\n{mat2}\n{mat3}\n{mat4}"
    new_mat1 = [mat4[0],mat3[0],mat2[0],mat1[0]]
    new_mat2 = [mat4[1],mat3[1],mat2[1],mat1[1]]
    new_mat3 = [mat4[2],mat3[2],mat2[2],mat1[2]]
    new_mat4 = [mat4[3],mat3[3],mat2[3],mat1[3]]
    all_new_mat = f"{new_mat1}\n{new_mat2}\n{new_mat3}\n{new_mat4}"
    print(f"The matrix to be rolled clockwise to 90 degree is:\n{all_mat}\n")
    print(f"The rolled matrix to 90 degrees is:\n{all_new_mat}")

if __name__ == "__main__":
    Rotate()
print("\nCode developed by Masino")
