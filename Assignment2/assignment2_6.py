def DisplayPattern(no):
    for i in range(no, 0,-1):
        for f in range(i):
            print("*",  end=" ")
        print("") 

def main():
    no=int(input("Enter Number"))
    DisplayPattern(no)

if __name__=="__main__":
    main()