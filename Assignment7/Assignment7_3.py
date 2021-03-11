class Numbers:
    def __init__(self, no1):
        self.Value=no1
    
    def ChkPrime(self):
        flag=True
        if self.Value>1:
            for i in range(2, self.Value):
                if self.Value%i==0:
                    flag=False
                    break
        else:
            flag=False
        return flag
    
    def ChkPerfect(self):
        sum=0
        for i in range(self.Value):
            for j in range(1, int(self.Value/2)+1):
                if(self.Value%j==0):
                    sum=sum+j
            if sum == self.Value:
                return True
            else:
                return False
        
    def SumFactors(self):
        addition=0
        for i in range(1,self.Value):
            if self.Value%i==0:
                addition=addition + i
        print("{} Addition of Factors is {}".format(self.Value, addition))

    def Factors(self):
        factors=[]
        for i in range(1,self.Value):
            if self.Value%i==0:
                factors.append(i)
        print("{} Factors are {}".format(self.Value, factors))

def main():
    print("Enter Number")
    no1=int(input())
    Obj1=Numbers(no1)
    ret = Obj1.ChkPrime()
    if ret == True:
        print("Number {} is Prime".format(no1))
    else:
        print("Number {} is Not Prime".format(no1))
    
    ret = Obj1.ChkPerfect()
    if ret == True:
        print("Number {} is Perfect".format(no1))
    else:
        print("Number {} is Not Perfect".format(no1))
    
    ret = Obj1.SumFactors()
    ret =Obj1.Factors()

    print("*****************************")

    print("Enter Number")
    no1=int(input())
    Obj2=Numbers(no1)
    ret = Obj2.ChkPrime()
    if ret == True:
        print("Number {} is Prime".format(no1))
    else:
        print("Number {} is Not Prime".format(no1))
    
    ret = Obj2.ChkPerfect()
    if ret == True:
        print("Number {} is Perfect".format(no1))
    else:
        print("Number {} is Not Perfect".format(no1))
    
    ret = Obj2.SumFactors()
    ret =Obj2.Factors()
    

if __name__=="__main__":
    main()

    