"""
A simple code to check how to add item into a list
"""
def Addin(name: str) -> str:
    print(name)
    name = list(name)
    new_list = ''
    for item in name:
        if item not in new_list:
            new_list += item
    return new_list
if __name__ == "__main__":
    print(Addin('Masino'))