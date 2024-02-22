def checkPrime(num):
    c=0
    for i in range(2,num):
        if (num%i)==0:
            c=c+1
    return c

num=int(input("Enter a number"))
result=checkPrime(num)
if result <= 1 :
    print(" Number is prime ")
else:
    if (num%2)==0:
        print(" Number is even ")
    else:
        print("Number is odd but not prime")