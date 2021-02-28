class Demo:
    value=11
    def __init__(self, i, j):
        self.no1=i
        self.no2=j

    def Fun(self):
        print("From Fun No1", self.no1)
        print("From Fun No2", self.no2)
    
    def Gun(self):
        print("From Gun No1", self.no1)
        print("From Gun No2", self.no2)


def main():
    print("Enter First NUmber")
    no1=int(input())

    print("Enter Second NUmber")
    no2=int(input())

    obj1= Demo(no1,no2)
    obj2= Demo(no1,no2)

    obj1.Fun()
    obj1.Gun()
    obj2.Fun()
    obj2.Gun()

if __name__=="__main__":
    main()
