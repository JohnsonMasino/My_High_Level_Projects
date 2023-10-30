"""
A Python code to replace a character in a string with '^'

Code developed by masino

STEP 1:
Define the function and create another list to store the result
"""
def Replace(string: str) -> str:
    new_string = ''
    """
    STEP 2:
    Now from initial string, add all items to the string replacing
    all spaces with '^'
    """
    for item in string:
        if item == " ":
            new_string += "^"
        else:
            new_string += item
    """
    STEP 3:
    Now return the new string and thats it !
    """
    return new_string
if __name__ == "__main__":
    print(Replace("My mom is a hardworking woman"))
print("\nCode developed by masino")