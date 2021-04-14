import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

def linearRegression():
    X=[1,2,3,4,5]
    Y=[3,4,2,4,5]
    print("Values of Independent of variables X",X)
    print("Values of Independent of variables Y",Y)

    X_Mean=np.mean(X)
    Y_Mean=np.mean(Y)
    print("Mean of Independent of variables X",X_Mean)
    print("Mean of Independent of variables Y",Y_Mean)
    
    n=len(X)

    Numerator=0
    Denominator=0

    for i in range(len(X)):
        Numerator = Numerator + ((X[i]-X_Mean)* (Y[i]-Y_Mean))
        Denominator = Denominator + ((X[i]-X_Mean)**2)    
    
    m=Numerator/Denominator
 
    # y = mx+c
    C =  Y_Mean- (m*X_Mean)
    print("Slop of Regression line is ", m)
    print("Y intercept of Regression line is ", C)

    Yp =[]
    for i in range(len(X)):
        Yp.append((m*X[i])+C)

    print("Yp is :", Yp)

    # Diplay plotting of above points
    x=np.linspace(1,6,n)
    y=C+m*x
    plt.plot(x,y,color="#58b970", label="Regression Line")
    plt.scatter(X,Y,color="#ef5423", label="Scatter Plot")
    plt.legend()
    plt.show()

    #find out goodnees of fit of R Square
    ss_t=0
    ss_r=0
    for i in range(n):
        y_pred=C+m*X[i]
        ss_t+=(Y[i]-Y_Mean)**2
        ss_r+=(Y[i]-y_pred)**2
    
    r2= 1-(ss_r/ss_t)
    print("Goodness of fit using R2 method is ", r2)



def main():
    print("Welcome to Linear Regrssion")
    linearRegression()

if __name__=="__main__":
    main()


#   Use  R square method to calculate r squre value value 

#  R square = sumation(yp-ybar)**2/summation(y-ybar)**2