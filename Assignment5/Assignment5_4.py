total=0
def AdditionDigits(no):
    global total
    if(no>0):
        total=total+no%10
        no=no//10
        AdditionDigits(no)

def main():
    global total
    no=int(input("Enter Number"))
    AdditionDigits(no)
    print("Digits Addition of Number {} is {}".format(no, total))


if __name__=="__main__":
    main()
