def Convert():
    r1 = [1, 2, 3]  # col1 = [1, 2, 3]
    r2 = [4, 0, 6]  # col2 = [4, 0, 6]
    r3 = [7, 8, 9]  # col3 = [7, 8, 9]

    row1 = [int(item) for item in r1]
    row2 = [int(item) for item in r2]
    row3 = [int(item) for item in r3]

    print(f"The entered matrix is:\n{row1}\n{row2}\n{row3}")

    for i in range(len(row1)):
        for j in range(len(row1)):
            if row1[i] == 0 or row2[i] == 0 or row3[i] == 0:
                row1[i] = 0
                row2[i] = 0
                row3[i] = 0

    print(f"The converted matrix is:\n{row1}\n{row2}\n{row3}")

if __name__ == "__main__":
    Convert()

print("\nCode developed by Masino")
