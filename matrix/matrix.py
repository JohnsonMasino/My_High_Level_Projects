"""
A Python code to locate a number in a matrix
"""
def Print_matrix():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list3 = [7, 8, 9]
    print(f'The matrix is:\n{list1}\n{list2}\n{list3}')
    position = input("Enter the Row and Column numbers respectively to hide your money.\nSeparate them with a comma: ")
    splitted_pos = position.split(",")
    splitted_pos[0] = int(splitted_pos[0])
    splitted_pos[1] = int(splitted_pos[1])
    if splitted_pos[0] == 1:
        if splitted_pos[1] == 1:
            list1[0] = 'x'
            print(f"The position you marked is:\n{list1}\n{list2}\n{list3}")
        elif splitted_pos[1] == 2:
            list1[1] = 'x'
            print(f"The position you marked is:\n{list1}\n{list2}\n{list3}")
        elif splitted_pos[1] == 3:
            list1[2] = 'x'
            print(f"The position you marked is:\n{list1}\n{list2}\n{list3}")
        else:
            print("There is no column for the number you entered")
    elif splitted_pos[0] == 2:
        if splitted_pos[1] == 1:
            list2[0] = 'x'
            print(f"The position you marked is:\n{list1}\n{list2}\n{list3}")
        elif splitted_pos[1] == 2:
            list2[1] = 'x'
            print(f"The position you marked is:\n{list1}\n{list2}\n{list3}")
        elif splitted_pos[1] == 3:
            list2[2] = 'x'
            print(f"The position you marked is:\n{list1}\n{list2}\n{list3}")
        else:
            print("There's no colum for the number you entered")
    elif splitted_pos[0] == 3:
        if splitted_pos[1] == 1:
            list3[0] = 'x'
            print(f"The position you marked is:\n{list1}\n{list2}\n{list3}")
        elif splitted_pos[1] == 2:
            list3[1] = 'x'
            print(f"The position you marked is:\n{list1}\n{list2}\n{list3}")
        elif splitted_pos[1] == 3:
            list3[2] = 'x'
            print(f"The position you marked is:\n{list1}\n{list2}\n{list3}")
        else:
            print("There's no colum for the number you entered")
    else:
        print("There's no row for the number you entered")

if __name__ == "__main__":
    Print_matrix()
print("\nCode developed by Masino")