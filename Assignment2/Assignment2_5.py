def CheckPrime(no):
    flag=0
    if no>1:
        for i in range(2, no):
            if no%i==0:
                flag=1
                break
    else:
        flag=1
    return flag

def main():
    no1=int(input("Enter number to check prime or not"))
    result = CheckPrime(no1)
    if result == 1:
       print("It is not Prime Number")
    else:
        print("It is Prime Number")
    
if __name__=="__main__":
    main()

