print("\t \t \t Name: Jay Surya \n\t \t \t USN:1AY24AI048 \n\t \t \t Sec:M")
import random as m
n=int(input("Guess a number from 1 to 10 :"))
r=m.randint(1,3)
k=10
for i in range(1,10): 
  print("Random Number = ",r)
  if(n==r):
    print("You have guessed the number correctly")
    bool=input("Do you want to continue?[Enter yes or no]")
    if(bool=="yes"):
      n=int(input("Guess a number from 1 to 10 :"))
      r=m.randint(1,3)
    
    else:
      break
  else:
      print("Guessed the wrong number!! :( ")
      k-=1
      print("Try again {You have",k,"chances left!!}")
      bool=input("Do you want to continue?[Enter yes or no]")
      if(bool=="yes"):
        n=int(input("Guess a number from 1 to 10 :"))
        r=m.randint(1,3)
      else:
        break
