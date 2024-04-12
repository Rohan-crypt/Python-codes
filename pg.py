#Use a class to calculate area and perimeter of a square
class Area:
    side=10
    def area(self):
        print(pow(self.side,2))
    def perimeter(self):
        print(4*self.side)
Ar=Area()
Ar.area()
Ar.perimeter()