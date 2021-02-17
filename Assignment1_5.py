def displyUsingWhile():
    print("Output Using While Loop")
    icnt=10
    while icnt>0:
        print(icnt)
        icnt = icnt-1

def displyUsingForLoop():
    print("Output Using For Loop")
    icnt=10
    for icnt in range(10,0,-1):
        print(icnt)

def main():
    displyUsingWhile()
    displyUsingForLoop()

if __name__=="__main__":
    main()