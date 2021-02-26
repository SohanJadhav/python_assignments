def pattern(no):
    i=no
    if i>0:
        print(i)
        i=i-1
        pattern(i)

def main():
    print("Enter Number")
    no=int(input())
    pattern(no)


if __name__=="__main__":
    main()