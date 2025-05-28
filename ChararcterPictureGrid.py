print("\t \t \t Name: Jay Surya \n\t \t \t USN: 1AY24AI048 \n\t \t \t Sec: M")

rows = int(input("Enter odd number of rows: "))
mid = rows // 2

print("\nDiamond Pattern:\n")
for i in range(rows):
    spaces = abs(mid - i)
    chars = rows - 2 * spaces
    print(" " * spaces + "@ " * chars)
