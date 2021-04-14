   # Task

    # CAlculte R2

    # Then increase m value by .1 in loop and check R qure value



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def MeanData(arr):
    size=len(arr)
    sum=0
    for i in range(size):
        sum=sum+arr[i]
    return (sum/size)

# MarvellousHeadBrain.csv 
def HeadBrain(name):
    dataset = pd.read_csv(name)
    print("Size of our data is :", dataset.shape)

    X= dataset["Head Size(cm^3)"].values
    Y=dataset["Brain Weight(grams)"].values

    print("Length of X is :", len(X))
    print("Length of Y is :", len(Y))

    Mean_X= MeanData(X)
    Mean_Y= MeanData(Y)
    print("Mean of Independent Variable X is ", Mean_X)
    print("Mean of Independent Variable Y is ", Mean_Y)

    # m=(SUm(x-xb)*(y-yb))/sum(x-xb)^2

    numerator=0
    denominator=0

    for i in range(len(X)):
        numerator=numerator+((X[i]-Mean_X)*(Y[i]-Mean_Y))
        denominator=denominator+(X[i]-Mean_X)**2
    
    m= numerator/denominator

    print("Value of Slop is ", m)

    # Y=mX+c
    # c=Y-mX
    c = Mean_Y-(m*Mean_X)
    print("Value of Y intercepts is ", c)

    X_Start= np.min(X)-200
    X_End= np.max(X)+200

    x=np.linspace(X_Start,X_End)
    y=m*x+c

    plt.plot(x,y,color="r", label="Line of Regression")
    plt.scatter(X,Y, color="b",label="Data Plots")

    plt.xlabel("Head Size")
    plt.ylabel("Brain Weight")

    plt.legend()
    plt.show()

    ss_t=0
    ss_r=0
    for i in range(len(X)):
        y_pred=c+m*X[i]
        ss_t+=(Y[i]-Mean_Y)**2
        ss_r+=(Y[i]-y_pred)**2
    
    r2= 1-(ss_r/ss_t)

    print("Goodness of fit using R2 method is ", r2)

    print("Check R2 value by increasing slop(m) up to 1")
    
    temp_m=m
    while temp_m<1:
        ss_t=0
        ss_r=0
        for i in range(len(X)):
            y_pred=c+temp_m*X[i]
            ss_t+=(Y[i]-Mean_Y)**2
            ss_r+=(Y[i]-y_pred)**2
        r2= 1-(ss_r/ss_t)
        temp_m = temp_m +0.1
        print("Goodness of fit for m {} using R2 method is {}".format(temp_m,r2))




def main():
    print("Enter file name of dataset")
    name=input()
    HeadBrain("MarvellousHeadBrain.csv")


if __name__=="__main__":
    main()

 