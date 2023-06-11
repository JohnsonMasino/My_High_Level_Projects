#!/usr/bin/python3

def Valueerror():
    """defines the function of this file"""
    num = input("Enter two numbers separated by a space to get the summation: ")
    num = num.split(" ")
    try:
        print(int(num[0]) + int(num[1]))
    except ValueError:
        print("Oops!\nEnter numbers only")
    except Exception as e:
        print(e)
    finally:
        print("Code executed successfully")

if __name__ == "__main__":
    Valueerror()
print("\nCode developed by Masino")
