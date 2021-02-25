import  functools

filteredList = lambda no : no >=70 and no <=90 

mapList = lambda no : no + 10

productList = lambda sum,no : sum * no

def main():
    print("Enter number of elements")
    value=int(input())
    arr=[]
    for i in range(0, value):
        print("Enter Number")
        no = int(input())
        arr.append(no)
    print("Entered number list is {}".format(arr))
    
    filterResult = list(filter(filteredList, arr))
    print("Filtered list is",filterResult)

    mapResult = list(map(mapList, filterResult))
    print("Map list is",mapResult)

    reduceResult = functools.reduce(productList, mapResult)
    print("Reduce Product of list is",reduceResult)

if __name__=="__main__":
    main()