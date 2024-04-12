class Employee:
    Name="Bhavya"
    Dept="CSE"
    def info(self,city):
        print(self.Name, self.Dept, city)
E1=Employee()
E2=Employee()
city="Dehradun"
E1.info(city)
E2.info()