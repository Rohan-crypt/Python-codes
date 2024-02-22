def square(n):
    return n**2
def sum(a,b):
    square(a)
    return (a+b)
result=square
num=int(input("Enter a number"))
a=result(num)
print(a)
s=sum(num,a)
print(s)