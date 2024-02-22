num=int(input("Enter number to get input "))
fact=1
if num == 0:
    print("Factorial is: " + 1)
elif num < 0:
    print("Invalid number")
else:
    while num > 0:
        fact=fact*num
        num-=1
    print("Factorial is "+ str(fact))