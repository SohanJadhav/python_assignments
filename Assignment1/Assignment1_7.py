def check(value):
    if value %5==0:
        return True
    else:
        return False

def main():
    no1=int(input("Enter Number"))
    bret = check(no1)
    print(bret)

if __name__=="__main__":
    main()