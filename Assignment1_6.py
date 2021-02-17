def CheckNumber(value):
    if  value > 0:
       print("Positive Number")
    elif value == 0:
        print("Zero")
    else:
       print("Negative Number")

def main():
    no1=int(input("Enter Number"))
    CheckNumber(no1)
        

if __name__=="__main__":
    main()