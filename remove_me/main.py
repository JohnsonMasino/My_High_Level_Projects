"""
A Python Code to remove dupicate character in a string
Code devloped by Masino

STEP 1:
Define the function and convert the string to a list
"""
def removal(expression):
    """
    No need to convert to a list
    Create an empty string to store the result
    """
    done = ''
    """
    Put an item into new strin gif it is not yet there"""
    for item in expression:
        if item not in done:
            done += item
    print(f"Main string is: {expression}")
    print("Without any duplicate:")
    return done
"""
We are done !!!
"""
if __name__ == "__main__":
    print(removal("Johnson"))
print("\n Code developed by Masino")
