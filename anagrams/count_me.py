def count(item: chr):
    available_list = ['a', 'b', 'c']
    available_list1 = 'johnsonmasino'
    if item in available_list:
        num1 = available_list.count(item)
        print(f"From List: {num1}")
    else:
        print(f"From List: 0")

    if item in available_list1:
        num2 = available_list1.count(item)
        print(f"From string: {num2}")
    else:
        print(f"From string: 0")

if __name__ == "__main__":
    count('o')
print("\nCode developed by Masino")