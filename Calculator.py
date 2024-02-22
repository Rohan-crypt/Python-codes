a=int(input("Give the first number"))
b=int(input("Give the second number"))
c=input("Enter your operation")
if c is '+':
    print("Sum is "+str(a+b))
elif c is '-':
    print("Difference is "+str(a-b))
elif c is '*':
    print("Product is "+str(a*b))
elif c is '/':
    print("Division is "+str(a/b))
elif c is '//':
    print(str(a//b))
elif c is '%':
    print("Remainder is "+str(a%b))
    print("Equal or not "+str(a!=b))
else:
    print("Wrong Operation")