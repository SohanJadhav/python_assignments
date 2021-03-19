import threading


def checkEven(number):
    if number%2==0:
        return True
    else:
        return False

def checkOdd(number):
    if number%2 !=0:
        return True
    else:
        return False

def EvenFactorsAdditon(no1):
    addition=0
    for i in range(1, no1):
        if no1%i==0:
            if checkEven(i) == True:
                addition=addition+i
    print("Even Factor's Addtion of number {} is {}".format(no1, addition))

def OddFactorsAddition(no1):
    addition=0
    for i in range(1, no1):
        if no1%i==0:
            if checkOdd(i) == True:
                addition=addition+i
    print("Odd Factor's Addtion of number {} is {}".format(no1, addition))


def main():
    print("Enter Number")
    value = int(input())

    t1=threading.Thread(target=EvenFactorsAdditon, args=(value,))
    t1.start()
    t1.join()

    t2=threading.Thread(target=OddFactorsAddition, args=(value,))
    t2.start()
    t2.join()


if __name__=="__main__":
    main()