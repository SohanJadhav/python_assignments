def display(name):
    nameLength = len(name)
    return nameLength

def main():
    name = input("Enter Name")
    lret = display(name)
    print("Length of Entered Name:{} is {}".format(name,lret))


if __name__=="__main__":
    main()