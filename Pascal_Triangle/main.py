"""Python code that returns the list os lists of integers
representing the pascal triangles of a number.

STEP 1
define the function and assume it is always integer
"""

def pascal_triangle(number: int):
    """STEP 2
    make sure that 'number is always greater than ero unless
    return an empty list'"""
    if number <= 0:
        done = []
        print(done)
        return []
    if type(number) != int:
        text = "Error due to data type"
        print(text)
        return text
    
    """STEP 3
    Define the list variable and state the condition to always
    add 1 to the beginning of the list"""
    number_list = []
    for i in range(number + 1):
        row = [1]
        """STEP 4
        if i is greater than ero then let's generate the rest of the code
        """
        if i > 0:
            for j in range(1, i):
                row.append(number_list[i -1][j - 1] + number_list[i - 1][j])
            row.append(1)
        number_list.append(row)
    done = number_list[number]
    print(done)
    return done
if __name__ == "__main__":
    pascal_triangle(9)