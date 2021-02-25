
import functools

filterList = lambda no : no%2==0

mapList = lambda no : no*no

reduceList = lambda sum,no : sum+no

def main():
    print("Enter Number of elements")
    value =int(input())
    arr=[]
    for i in range(0,value):
        print("Enter Number")
        no = int(input())
        arr.append(no)
    print("Entered numbers are ", arr)

    filteredList = list(filter(filterList,arr))
    print("After Filter List is",filteredList)

    squareList = list(map(mapList,filteredList))
    print("After Map List is",squareList)

    sum = functools.reduce(reduceList,squareList)
    print("After Reduce result is",sum)


if __name__=="__main__":
    main()