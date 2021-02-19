def AdditionDigits(no):
    total=0
    while no>0:
        digit=no%10
        total=total+digit
        no=no//10
    return total

def main():
    no=int(input("Enter Number"))
    total = AdditionDigits(no)
    print("Digits Addition of Number {} is {}".format(no, total))


if __name__=="__main__":
    main()