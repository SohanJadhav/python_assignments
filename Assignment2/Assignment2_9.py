def NumbersDigits(no):
    value = no/10
    return int(value)

def main():
    no=int(input("Enter Number"))
    temp =no
    count=0
    while no!=0:
        count=count+1
        no=NumbersDigits(no)  
    print("Number of digits in {} are {}".format(temp, count))


if __name__=="__main__":
    main()