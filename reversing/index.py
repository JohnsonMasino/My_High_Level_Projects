def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    # Concatenate s1 with itself
    s1_s1 = s1 + s1

    # Check if s2 is a substring of s1_s1
    if s2 in s1_s1:
        return True
    else:
        return False

if __name__ == "__main__":
    s1 = "waterbottle"
    s2 = "erbottlewat"
    result = is_rotation(s1, s2)
    print(f"'{s2}' is a rotation of '{s1}': {result}")
print("\nCode developed by Masino")