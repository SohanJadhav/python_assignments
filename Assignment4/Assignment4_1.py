# def CalculatePowerTwo(no):
#     n=1
#     n = pow(no,2)
#     return n

CalculatePowerTwo = lambda no : pow(no,2)

def main():
    print("Enter Number")
    no=int(input())
    ret = CalculatePowerTwo(no)
    print("Power 2 of number {} is {}".format(no,ret))


if __name__=="__main__":
    main()