# WAP yhat does arithmetic operation
def operator(a,b,ch):
    if(ch=='+'):
        return (a+b)
    elif(ch=='-'):
        return (a-b)
    elif(ch=='*'):
        return (a*b)
    elif(ch=='/'):
        return (a/b)
    else:
        return 0
a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
ch=input("Enter operation")
result=operator(a,b,ch)
if(result==0):
    print("Invalid input")
else:
    print("Answer is", result)