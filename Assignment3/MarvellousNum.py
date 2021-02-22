def CheckPrime(no):
    flag=0
    if no>1:
        for i in range(2, no):
            if no%i==0:
                flag=1
                break
    else:
        flag=1
    return flag