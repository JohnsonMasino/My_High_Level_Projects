def gibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return gibo(n - 1) - gibo(n -2)
    
def fibo(n, x, y):
    if n == x:
        return x
    elif n == y:
        return y
    else:
        return gibo(n - 1) - gibo(n - 2)
if __name__ == "__main__":
    print(fibo(3, 5, 7))
print("\nCode developed by Masino")