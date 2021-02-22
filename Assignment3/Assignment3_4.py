def CheckNumberFrequency(list,no):
    count=0
    for i in range(len(list)):
        if list[i]==no:
            count=count+1
    return count

def main():
    arr=[]
    print("Enter Number of Elements")
    no=int(input())

    for i in range(no):
        print("Enter input number")
        no1=int(input())
        arr.append(no1)
    print("Entered elements are", arr)
    
    print("Enter element to search")
    value =int(input())
    numberFrequency=CheckNumberFrequency(arr,value)
    print("Frequency of number {} in list is {}".format(value,numberFrequency))

    


if __name__=="__main__":
    main()