def are_same(ana1, ana2):
    if len(ana1) != len(ana2):
        return False
    if sorted(ana1) == sorted(ana2):
        return True
if __name__ == "__main__":
    print(are_same("salesmen", "nameless"))
print("\nCode developed by Masino")