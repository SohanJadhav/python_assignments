def ChkNum(value):
    if value%2 == 0:
        return True
    else:
        return False

def main():
    no1=int(input("Enter Number"))
    bret = ChkNum(no1)
    if bret == True:
        print("Even Number")
    else:
        print("Odd Number")

if __name__=="__main__":
    main()    

