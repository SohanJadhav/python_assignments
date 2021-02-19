import Arithmatic as AR

def main():
    no1=float(input("Enter first number"))
    no2=float(input("Enter second number"))

    aret=AR.Addition(no1,no2)
    bret=AR.Substraction(no1,no2)
    mret=AR.Multiplication(no1,no2)
    dret=AR.Divide(no1,no2)
    print("Addition of {} and {} is {}".format(no1,no2,aret))
    print("Substraction of {} and {} is {}".format(no1,no2,bret))
    print("Multiplication of {} and {} is {}".format(no1,no2,mret))
    print("Divide of {} and {} is {}".format(no1,no2,dret))

if __name__=="__main__":
    main()



