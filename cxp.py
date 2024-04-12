def div(m,n):
    try:
        return m/n
    except:
        print("Division by zero not possible")
a=int(input("Enter a number"))
b=int(input("Enter 2nd no"))
div(a,b)