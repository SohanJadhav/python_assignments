import threading

def Even():
    print("Even number up to 10")
    for i in range(10):
        if i%2==0:
            print(i)

def Odd():
    print("Odd number up to 10")
    for i in range(10):
        if i%2 != 0:
            print(i)

def main():
    print("Inside Main")
    evenThread = threading.Thread(target=Even, args=())
    oddThread = threading.Thread(target=Odd, args=())

    evenThread.start()
    oddThread.start()

    evenThread.join()
    oddThread.join()

    print("Exit from Main")

if __name__=="__main__":
    main()