
Multiplication = lambda no1,no2 : no1*no2

def main():
    print("Enter First Number")
    no1=int(input())
    print("Enter Second Number")
    no2=int(input())

    ret = Multiplication(no1,no2)
    print("Multiplication of number {} and {} is {}".format(no1,no2,ret))
    


if __name__=="__main__":
    main()