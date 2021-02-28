
class Arithmetic:
    def __init__(self):
        self.Value1=0
        self.Value2=0

    def Accept(self, no1, no2):
        self.Value1=no1
        self.Value2=no2

    def Addition(self):
        return self.Value1 + self.Value2

    def Substraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        return self.Value1 / self.Value2

def main():
    print("Enter First Number")
    no1=int(input())
    print("Enter First Number")
    no2=int(input())
    Obj1=Arithmetic()
    Obj1.Accept(no1,no2)
    ret = Obj1.Addition()
    print("Addtion of {} and {} is {}".format(no1,no2,ret))
    ret = Obj1.Substraction()
    print("Substraction of {} and {} is {}".format(no1,no2,ret))
    ret = Obj1.Multiplication()
    print("Multiplication of {} and {} is {}".format(no1,no2,ret))
    ret = Obj1.Division()
    print("Division of {} and {} is {}".format(no1,no2,ret))


    print("Enter First Number")
    no1=int(input())
    print("Enter First Number")
    no2=int(input())
    Obj2=Arithmetic()
    Obj2.Accept(no1,no2)
    ret = Obj2.Addition()
    print("Addtion of {} and {} is {}".format(no1,no2,ret))
    ret = Obj2.Substraction()
    print("Substraction of {} and {} is {}".format(no1,no2,ret))
    ret = Obj2.Multiplication()
    print("Multiplication of {} and {} is {}".format(no1,no2,ret))
    ret = Obj2.Division()
    print("Division of {} and {} is {}".format(no1,no2,ret))


if __name__=="__main__":
    main()