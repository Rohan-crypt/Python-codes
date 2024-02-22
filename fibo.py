def checkFibo(num,a,b):
    if(num!=0):
        c=a+b
        print(c)
        checkFibo(num-1,b,c)
num=int(input("Enter the number of terms to be printed"))
print("0\n1")
checkFibo(num,0,1)