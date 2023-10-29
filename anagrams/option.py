"""This is a python code to show if two inputs are anagrams or not.
Code developed by Masino

STEP 1:
Check if you can convert the input into a list."""
def count(name1, name2):
    listed = []
    listed1 = []
    for item in name1:
        listed.append(item)
    for item in name2:
        listed1.append(item)
    #return all_listed
    """STEP 2:
    It Appears we can split the items so now we to identify if any item
    in one name is not in the other.
    But first, we need to make sure the lenght of both names are equal."""

    if len(listed) != len(listed1):
        return False
    
    """STEP 3:
    Now lets check if an item in the first name is not in the other name"""
    for item in listed:
        if item not in listed1:
            return False
    """This is the correction from STEP 5"""
    for item in listed:
        num1 = listed.count(item)
        num2 = listed1.count(item)
        if num1 != num2:
            print("From the number block")
            return False
    """STEP 4:
    Now we will return the possible answer"""
    return True
"""STEP 5:
We have just one more issue we missed that we have to go and fix and that is
the number of occurence of each letter> They should be equal in both names.
"""
if __name__ == "__main__":
    print(count("listen", "silent"))
print("\nCode developed by masino")
