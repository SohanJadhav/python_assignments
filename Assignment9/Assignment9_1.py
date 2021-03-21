import os

def checkFileExists(name):
    return os.path.isfile(name)

def main():
    print("Enter File name")
    fileName=input()

    if checkFileExists(fileName) ==  True:
        print("File {} is exists".format(fileName))
    else:
        print("File {} doesn't exists".format(fileName))

if __name__=="__main__":
    main()