def main():
    fileName=input("Enter file name to read content: ")
    try:
        fobj=open(fileName, 'r')
    except Exception as eobj:
        print("Error occures while reading file", eobj)
    else:
        print(fobj.read())

if __name__=="__main__":
    main()