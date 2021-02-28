class Circle:
    PI=3.14
    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0
    
    def Accept(self, RadiusValue):
        self.Radius=RadiusValue

    def CalculateArea(self):
        self.Area= Circle.PI*self.Radius*self.Radius

    def CalculateCircumference(self):
        self.Circumference= 2*Circle.PI*self.Radius
    
    def Display(self):
        print("Radius of Circle is ", self.Radius)
        print("Area of Circle is ", self.Area)
        print("Circumference of Circle is ", self.Circumference)

def main():
    print("Enter radius")
    RadiusValue=int(input())
    Obj1 = Circle()
    Obj1.Accept(RadiusValue)
    Obj1.CalculateArea()
    Obj1.CalculateCircumference()
    Obj1.Display()

    print("Enter radius")
    RadiusValue=int(input())
    Obj2= Circle()
    Obj2.Accept(RadiusValue)
    Obj2.CalculateArea()
    Obj2.CalculateCircumference()
    Obj2.Display()

if __name__=="__main__":
    main()


