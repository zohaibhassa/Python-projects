import random
choices=random.randint(1,100)
attemps=0
while True:
 
 guess=int(input("enter your number from 1 to 200   "))
 attemps+=1
 if guess<choices:
    print("too low")
 elif guess>choices:
    print("too high")
 elif guess==choices:
    print("you got it!!!!!")
    print(f"you got it in {attemps} attempts")
    break