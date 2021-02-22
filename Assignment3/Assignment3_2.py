def findMaxFromList(list):
    maxNumber=list[0]
    for i in range(len(list)):
        if list[i]>maxNumber:
            maxNumber=list[i]
    return maxNumber

def main():
    arr=[]
    print("Enter number of elements")
    no=int(input())

    for i in range(no):
        print("Enter input number")
        no1=int(input())
        arr.append(no1)
    print("Entered numbers are", arr)

    maxNumber = findMaxFromList(arr)
    print("Max number from list is", maxNumber)

if __name__=="__main__":
    main()