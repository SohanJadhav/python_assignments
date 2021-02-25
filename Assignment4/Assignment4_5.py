def FilterPrimeNumber(no):
    flag=True
    if no>1:
        for i in range(2, no):
            if no%i==0:
                flag=False
                break
    else:
        flag=False
    return flag

maplist = lambda no : no*2


def FindMax(max, no):
    if max < no:
        max=no
    return max


def main():
    print("Enter Number of elements")
    value = int(input())
    arr=[]

    for i in range(0,value):
        print("Enter Number")
        no = int(input())
        arr.append(no)
    print("Entered List is ", arr)

    primeList = list(filter(FilterPrimeNumber, arr))
    print("After Filter List is ", primeList)

    resultList = list(map(maplist, primeList))
    print("After AMp List is ", resultList)

    maxNumber = reduce(FindMax, resultList)
    print("Max Number from list is ", maxNumber)

if __name__=="__main__":
    main()