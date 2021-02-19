def pattern(value):
    icnt=1
    count=1
    for icnt in range(value):
        for count in range(value):
            print("*", end=" ")
        print("")

def main():
    value=int(input("Enter pattern number"))
    pattern(value)

if __name__=="__main__":
    main()
