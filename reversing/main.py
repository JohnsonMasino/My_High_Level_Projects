"""
This is a python code that reverses a string exactly character by character.
This code developed by Masino

STEP 1:
Define the funtion and convert the string to a list
"""
def Re_Verse():
    names = input("Enter the string here: ")
    name_list = list(names)
    """
    STEP 2:
    Now that the string is converted to a list, reverse it.
    """
    reversed_list = reversed(name_list)
    """
    STEP 3:
    Now convert the reversed list back to a string
    """
    new_string = ''.join(reversed_list)
    """
    STEP 4:
    Now you can return the new string variable
    """
    print(f"Reversing {names}, we have:")
    return new_string
"""
WE ARE DONE!
THAT WAS SIMPLE INNIT ?
"""
if __name__ == "__main__":
    print(Re_Verse())
print("\nCode developed by Masino")