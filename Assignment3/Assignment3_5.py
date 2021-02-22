import MarvellousNum

def Addition(list):
    sum=0
    for i in range(len(list)):
        sum=sum+list[i]
    return sum

def ListPrime(list):
    arrList=[]
    for i in range(len(list)):
        if(MarvellousNum.CheckPrime(list[i]) == 0):
            arrList.append(list[i])
    return arrList

def main():
    arr=[]
    print("Enter Number of Elements")
    no=int(input())

    for i in range(no):
        print("Enter input number")
        no1=int(input())
        arr.append(no1)
    print("Entered elements are", arr)
    primeList = ListPrime(arr)
    print("Filtered Prime List", primeList)
    total = Addition(primeList)
    print("Addition of all Prime Numbers: ", total)


if __name__=="__main__":
    main()