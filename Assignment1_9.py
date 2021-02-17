def EvenNumber():
    icnt=1
    ecount=1
    while ecount<=10:
        if icnt%2==0:
            print(icnt)
            ecount= ecount+1
        icnt=icnt+1

def main():
    EvenNumber()

if __name__=="__main__":
    main()
