"""
Python Code to ascertain if two strings are anagrams or not.

STEP 1:
Define the function
"""
def are_anagrams(string1: str, string2: str) -> bool:
    """STEP 2:
    Since two strings can never be anagrams if their length are
    not equal, return false  if they not.
    """
    if len(string1) != len(string2):
        return False
    """
    STEP 3:
    Count the number of occurence of each character
    
    lenght1 = 0
    length2 = 0
    for item in string1:
        if item in 
    
    That is wrong or long route
    Since for two strings to be anagrams, the sorted
    for of both should be the same
    Let's check the sorted form of both and compare

    EDITED: We have to convert strings to list first before sorting
    """
    for item in string1:
        if item not in string2:
            return False
        
    string1 = list(string1)
    string2 = list(string2)
    new_string1 = string1.sort()
    new_string2 = string2.sort()
    if new_string1 != new_string2:
        print("From sorted comapared not equal")
        return False
    else:
        print("From sorted compared equal")
        return True
    """
    STEP 3:
    Now return True"""
    # return True
"""We are done !"""
if __name__ == "__main__":
    print(are_anagrams("masino", "nasimo"))
print("\nCode developed by masino")