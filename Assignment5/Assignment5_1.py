i=1
def pattern(no):
    global i
    if i<=no:
        print("*")
        no=no-1
        pattern(no)

def main():
    print("Enter Number")
    no=int(input())
    pattern(no)


if __name__=="__main__":
    main()