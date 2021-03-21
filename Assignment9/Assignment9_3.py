import sys

def main():
    fobj= open('ABC.txt', 'r')
    data = fobj.read()

    fileName=sys.argv[1]
    fobj1=open(fileName,'w')
    fobj1.write(data)

if __name__=="__main__":
    main()