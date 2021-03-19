import threading

def SmallCharCount(str):
    print("Running Thread Name is ", threading.current_thread().getName())
    print("Running Thread Id is ", threading.get_ident())
    arr = list(str)
    count=0

    for i in range(len(arr)):
        if arr[i].islower() == True:
            count=count+1
    print("Small Character count in given string {} is {}".format(str, count))

def CapitalCharCount(str):
    print("Running Thread Name is ", threading.current_thread().getName())
    print("Running Thread Id is ", threading.get_ident())
    arr=list(str)
    count=0

    for i in range(len(arr)):
        if arr[i].isupper() == True:
            count=count+1
    print("Capital Character count in given string {} is {}".format(str, count))

def DigitCount(str):
    print("Running Thread Name is ", threading.current_thread().getName())
    print("Running Thread Id is ", threading.get_ident())
    arr=list(str)
    count=0
    for i in range(len(arr)):
        if arr[i].isdigit() == True:
            count=count+1
    print("Digits count in given string {} is {}".format(str, count))

def main():
    print("please Enter String")
    str =input()

    small= threading.Thread(name='small',target=SmallCharCount, args=(str,))
    capital= threading.Thread(name='capital',target=CapitalCharCount, args=(str,))
    digits = threading.Thread(name='digits',target=DigitCount, args=(str,))

    small.start()
    capital.start()
    digits.start()

    small.join()
    capital.join()
    digits.join()

    print()

    print("Main Exit")

if __name__=="__main__":
    main()