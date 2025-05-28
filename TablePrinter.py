print("\t \t \t Name: Jay Surya \n\t \t \t USN: 1AY24AI048 \n\t \t \t Sec: M")

table_data = { "fruits": "apples oranges cherries banana","name": "Alice Bob Carol David", "animals": "dogs cats moose goose"}

for i, j in table_data.items():
    print(i.ljust(10), end="")    
    print(j.ljust(20), end="\n")  
