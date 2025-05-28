print("\t \t \t Name: Jay Surya \n\t \t \t USN: 1AY24AI048 \n\t \t \t Sec: M")

r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))

for i in range(r):
    for j in range(c):
        # Zig-zag occurs at alternating row positions
        if (i + j) % (r - 1) == 0:
            print("-", end="")
        else:
            print(" ", end="")
    print()
