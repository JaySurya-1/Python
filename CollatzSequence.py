print("\t \t \t Name: Jay Surya \n\t \t \t USN: 1AY24AI048 \n\t \t \t Sec: M")

n = int(input("Enter a number: "))
while n != 1:
    print(n, end=' -> ')
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
print(1)
