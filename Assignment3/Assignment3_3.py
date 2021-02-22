def findMinFromList(list):
    minNumber=list[0]
    for i in range(len(list)):
        if list[i]<minNumber:
            minNumber=list[i]
    return minNumber

def main():
    arr=[]
    print("Enter number of elements")
    no=int(input())

    for i in range(no):
        print("Enter input number")
        no1=int(input())
        arr.append(no1)
    print("Entered numbers are", arr)

    minNumber = findMinFromList(arr)
    print("Minimum number from list is", minNumber)

if __name__=="__main__":
    main()