def pattern(value):
    icnt=1

    for icnt in range(1,value+1):
        for i in range(1,value+1):
            print(i, end=" ")
        print(" ")

def main():
    value=int(input("Enter pattern number"))
    pattern(value)

if __name__=="__main__":
    main()
