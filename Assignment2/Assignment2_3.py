def CalculateFactorial(no):
    result =1
    if no<0:
        print("Factorial of negative number does not exists!")
    else:
        for i in range(1,no+1):
            result=result*i
        print("Factorial of number {} is {}".format(no, result))

def main():
    no=int(input("Enter number"))
    CalculateFactorial(no)

if __name__=="__main__":
    main()