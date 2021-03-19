import threading

def EvenListAddition(inputList):
    addition =0
    for i in range(len(inputList)):
        if inputList[i]%2 ==0:
            addition=addition+inputList[i]
    print("Addition of All Even elements from list is ", addition)

def OddListAddition(inputList):
    addition =0
    for i in range(len(inputList)):
        if inputList[i]%2 !=0:
            addition=addition+inputList[i]
    print("Addition of All Odd elements from list is ", addition)

def main():
    arr=[]
    print("Enter Number of elements")
    no1= int(input())

    for i in range(no1):
        no = int(input("Enter NUmber"))
        arr.append(no)

    print("Entered array elements are ", arr)

    evenlist = threading.Thread(target=EvenListAddition, args=(arr,))
    oddlist = threading.Thread(target=OddListAddition, args=(arr,))

    evenlist.start()
    oddlist.start()

    evenlist.join()
    oddlist.join()

    print("Main Exit!")

if __name__=="__main__":
    main()