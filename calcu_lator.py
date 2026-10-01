number1=int(input("enter your first number "))
number2=int(input("enter your second number "))
print(" 1   +")
print("2    -")
print("3    *")
print("4    /")
print("5   //")
w=int(input("enter the number before operations you want to perform "))
if w==1:
    print(number1+number2)
elif w==2:
    print(number1-number2)
elif w==3:
    print(number1*number2)
elif w==4:
    print(number1/number2)
elif w==5:
    print(number1//number2)
else:
    print("bye")
    
