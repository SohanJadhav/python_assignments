   # Task

    # CAlculte R2

    # Then increase m value by .1 in loop and check R qure value

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# MarvellousHeadBrain.csv 
def HeadBrain(name):
    dataset = pd.read_csv(name)
    # print("Size of our data is :", dataset.shape)

    X= dataset["Head Size(cm^3)"].values
    Y=dataset["Brain Weight(grams)"].values

    X=X.reshape((-1,1))

    obj=LinearRegression()
    obj.fit(X,Y)

    output= obj.predict(X)
    print("Expected result is ", output)

    dataset= pd.read_csv("Test.csv")
    X_New=dataset["Head Size(cm^3)"].values
    X_New=X_New.reshape((-1,1))
    output= obj.predict(X_New)
    print("Expected result is with New file ", output)

    rsquare= obj.score(X,Y)

    print("Value of R Square is ", rsquare)

def main():
    HeadBrain("MarvellousHeadBrain.csv")


if __name__=="__main__":
    main()

 