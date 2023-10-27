"""Python File to append items to list"""
def add_to():
    first_list = input("Enter items to add in a list.\nSparate with a comma: ")
    #sorted_first_list = first_list.split(",")
    initial_list = ['Food:']
    initial_list.append(first_list.split(","))
    print(initial_list)

if __name__ == "__main__":
    add_to()
print("Code developed by Masino")