def FactorsAddition(value):
    addition=0
    for i in range(1,value):
        if value%i==0:
            addition=addition+i
    return addition

def main():
    value = int(input("Enter number"))
    aret = FactorsAddition(value)
    print("Factors Addition of {} is {}".format(value, aret))

if __name__=="__main__":
    main()


