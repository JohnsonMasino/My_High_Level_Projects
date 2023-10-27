#!/usr/bin/python3

def Num():
    """defines the numbers function"""
    while True:
        num = input("Enter a number please: ")
        if num.isdigit():
            num = int(num)
            numb = num + 10
            print(f"Number plus 10 is: {numb}")
            break
        else:
            print("Sorry!\nMust enter a number")

if __name__ == "__main__":
    Num()
print("\nCode developed by Masino")
