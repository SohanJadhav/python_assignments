import threading

def Thread1Display():
    for i in range(1, 51):
        print(i, end=" ")

def Thread2Display():
    for i in range(50, 0, -1):
        print(i, end=" ")

def main():
    print("Running Thread 1")
    thread1= threading.Thread(target=Thread1Display, args=())
    thread1.start()
    thread1.join()
    print("Thread 1 Completed!")

    print("Running Thread 2")
    thread2= threading.Thread(target=Thread2Display, args=())
    thread2.start()
    thread2.join()
    print("Thread 2 Completed!")

    print("Main exit!")



if __name__=="__main__":
    main()