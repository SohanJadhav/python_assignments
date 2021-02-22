def Addition(list):
    sum=0
    for i in range(len(list)):
        sum=sum+list[i]
    return sum

def main():
    arr=[]
    print("Enter Number of Elements")
    no=int(input())

    for i in range(no):
        print("Enter input number")
        no1=int(input())
        arr.append(no1)
    print("Entered array is", arr)
    total = Addition(arr)
    print("Addition of all elements is",total)

if __name__=="__main__":
    main()