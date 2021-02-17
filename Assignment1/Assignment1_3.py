def Add(no1,no2):
    return no1+no2
def main():
    no1=int(input("Enter 1st Number"))
    no2=int(input("Enter 2nd Number"))
    aret = Add(no1,no2)
    print("Addition of {} and {} is {}".format(no1,no2,aret))

if __name__=="__main__":
    main()   

    