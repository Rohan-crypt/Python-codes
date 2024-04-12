class Employee:
    Name="Ram"
    Dept="HR"
    def __init__(self,N,D):
        self.N=N
        self.D=D
        print(self.N, self.D)
    def address(self,city):
        print(city)
E1=Employee("Divya","EIED")
E2=Employee("Divyansh", "CSE")