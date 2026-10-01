import random
choices= ["rock","paper","scissor"]
computer=random.choice(choices)
user=input("selct rock,paper,scissor   ")
print("computer chose ",computer)
if user==computer:
    print("tie")
elif user=="rock"and computer=="scissor":
    print("you win!!!!!!!!")
elif user=="scissor"and computer=="paper":
    print("you win!!!!!!!")
elif user=="paper" and computer=="rock":
    print("youwin!!!!!")
elif user in choices:
    print("computer wins")
else:
    print("wrong input")