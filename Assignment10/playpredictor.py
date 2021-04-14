import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np


def playpredictor():

    # Step 1
    data = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")
    print("Data set loaded successfully with data lenght as ", len(data))


    # Step 2
    Feature =["Wether", "Temperature"]
    print("Features",Feature)

    Wether = data.Wether
    Temperature = data.Temperature
    Play = data.Play

    # print(Wether)
    # print(Temperature)
    # print(Play)

    lboj = preprocessing.LabelEncoder()

    WetherX = lboj.fit_transform(Wether)
    TemperatureX = lboj.fit_transform(Temperature)
    Lable = lboj.fit_transform(Play)

    print("Encoded Wether is ", WetherX)
    print("Encoded Temperature is ",TemperatureX)

    features = list(zip(WetherX,TemperatureX))

    print("Encoded features is ",features)

    # Step 3
    obj = KNeighborsClassifier(n_neighbors=3)

    obj.fit(features,Lable)

    # Step 4
    output= obj.predict([[2, 1], [2, 1], [2, 1], [2, 1]])

    for value in range(len(output)):
        if value==1:
            print("You can play")
        else:
             print("Don't play")

    # if output==1:
    #     print("You can play")
    # else:
    #     print("Don't play")


def main():

    print("Welcome to Playpredictor Case study")
    playpredictor()

if __name__=="__main__":
    main()