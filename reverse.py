def reverse(str):
    rev=""
    for i in str:
        rev=rev+i
    return rev
str=input("Enter a String")
print("Reverse of the string", reverse(str))