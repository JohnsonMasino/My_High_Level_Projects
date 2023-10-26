"""A code to list the list of integers representing pascal
triangle of a number

STEP 1
Define the function
"""

def triangle(number):
    """
    STEP 2
    State the condition that return empty list if number is 0
    """
    if number <= 0:
        return []
    """
    STEP 3
    set a variable to contain 1 in a list that is in a list
    """
    main_list = [[1]]
    for i in range(1, number):
        prev_row = main_list[-1]
        cur_row = [1]
        for j in range(1, i):
            cur_row.append(prev_row[j - 1] + prev_row[j])
        cur_row.append(1)
        main_list.append(cur_row)
    for item in main_list:
        print(str(item))
    return main_list

if __name__ == "__main__":
    triangle(5)
print("\nCode developed by Masino")
