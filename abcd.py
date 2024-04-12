def Abc(text):
    return text.upper()
def dff(text):
    return text.lower()
print(Abc("My name is ram"))
name = Abc
print(name("My name is Sajid"))



def greet(func):
    greeting=func("Wekcome to the class")
    print(greeting)
greet(Abc)
greet(dff)