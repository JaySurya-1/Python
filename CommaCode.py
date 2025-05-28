print("\t \t \t Name: Jay Surya \n\t \t \t USN: 1AY24AI048 \n\t \t \t Sec: M")

list = []
n = int(input("Enter how many list elements: "))
print("Enter the elements:")
for i in range(n):
    inp = input()
    list += [inp]

print("Before inserting comma:\n", list)

new_string = ""
for k in list:
    new_string = new_string + k
    if list.index(k) == (len(list) - 2):
        new_string = new_string + ", and "
    elif list.index(k) == (len(list) - 1):
        new_string = new_string
    else:
        new_string = new_string + ", "

print(new_string)
