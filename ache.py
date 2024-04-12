import time
for i in range(10):
    time.sleep(1)
    print(i)



try:
    def sum(a,b):
        return (a/b)
    m=int(input("Enter 1st no"))
    n=int(input("Enter 2nd number"))
    print("Sum is",sum(m,n))

except(ZeroDivisionError):
    print("Please do not give zero for second number")