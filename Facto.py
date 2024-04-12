class Factorial:
    Num=5
    def fact(self):
        c=1
        for i in range(1,self.Num+1):
            c=c*i
        print(c)
F1=Factorial()
F1.fact()