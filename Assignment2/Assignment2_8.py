def DisplayPattern(no):
    for i in range(1, no+1,1):
        for f in range(1,i+1):
            print(f,  end=" ")
        print("") 

def main():
    no=int(input("Enter Number"))
    DisplayPattern(no)

if __name__=="__main__":
    main()