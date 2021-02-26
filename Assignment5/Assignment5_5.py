def Facto(no):
    if no==0:
        return 1
    return no *  Facto(no-1)

def main():
    no=int(input("Enter Number"))
    result = Facto(no)
    print("Factorial of Number {} is {}".format(no, result))


if __name__=="__main__":
    main()
