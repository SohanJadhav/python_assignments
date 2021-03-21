def checkFrequency(fileName, strValue):
    fobj=open(fileName, 'r')
    count=0
    for line in fobj:
        if strValue in line:
            count=count+1
    return count

def main():
    print("Enter file name")
    fName= input()

    print("Enter string to search in file")
    strValue=input()

    frequency = checkFrequency(fName,strValue)
    print("Frequency of string {} in file {} is {}".format(strValue,fName, frequency))


if __name__=="__main__":
    main()
