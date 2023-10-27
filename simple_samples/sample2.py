"""
Python Code to check how split function
works in identifying a space to split
"""
"""
STEP 1
Create a function and define the list of
the emails
"""
def cutting():
    outcome = ['a@gmail.com', 'b@gmail.com', 'www.c.com']
    """
    STEP 2
    Create a variable that will hold the splitted items
    """
    done = []
    """
    STEP 3
    Write a condition to split the items and save them in
    the variable above
    """
    for item in outcome:
        all = item.split(".")[1]
        done.append(all)
    print(done)

    """
    STEP 4
    Print the contents of the variable
    """
    """
    print(outcome)
if __name__ == "__main__":
    cutting()
    This is wrong. I should print it inside the loop
    """
if __name__ == "__main__":
     cutting()
print("\nCode developed by Masino")