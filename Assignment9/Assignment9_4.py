import sys

def main():
    fileName1=sys.argv[1]
    fileName2=sys.argv[2]
    print("Entered file names are",fileName1, fileName2)

    fobj1= open(fileName1, 'r')
    contents1 = fobj1.read()

    fobj2= open(fileName2, 'r')
    contents2 = fobj2.read()

    if contents1== contents2:
        print("Success: Both the files content is same ")
    else:
        print("Failure: Both the files content is different ")

if __name__=="__main__":
    main()