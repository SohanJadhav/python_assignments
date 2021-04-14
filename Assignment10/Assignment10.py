#use matplot lib to draw data sets and check or clean data


import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Wether
# 'Overcast' 'Rainy' 'Sunny'
# 0           1       2

# Temprature
# 'Cool' 'Hot' 'Mild'
# 0          1       2

# Play
# 'No' 'Yes'
# 0       1

def CheckAccuracy(Features, Labels):
    data_train, data_test, target_train, target_test = train_test_split(Features, Labels, test_size=.5) 

    dobj= KNeighborsClassifier(n_neighbors=5)

    dobj.fit(data_train, target_train)

    output= dobj.predict(data_test)

    Accuracy = accuracy_score(target_test, output)
    return Accuracy

def main():
    data = pd.read_csv('MarvellousInfosystems_PlayPredictor.csv')

    le = preprocessing.LabelEncoder()

    original_wether_data = data.iloc[:,1]
    original_temperature_data = data.iloc[:,2]
    original_play_data = data.iloc[:,3]

    print("_"*100)
    print("Weather Data")
    le.fit(original_wether_data)
    encoded_wether_data = le.transform(original_wether_data)
    print("Weather Types: ",le.classes_)
    print("Encoded Weather data: ", encoded_wether_data)
    
    print("_"*100)
    print("Temperature Data")
    le.fit(original_temperature_data)
    encoded_temperature_data = le.transform(original_temperature_data)
    print("Temperature Types: ",le.classes_)
    print("Encoded Temperature data: ", encoded_temperature_data)

    print("_"*100)
    print("Play Data")
    le.fit(original_play_data)
    Labels = le.transform(original_play_data)
    print("Play Types: ",le.classes_)
    print("Encoded Play data: ", Labels)

    Features= []

    # try use zip to merge two columns
    for i in range(len(data)):
        Features.append([encoded_wether_data[i],encoded_temperature_data[i]])
    print("_"*100)
    print("Features Data after Merge")
    print(Features)

    dobj= KNeighborsClassifier(n_neighbors=3)
    dobj.fit(Features, Labels)

    output= dobj.predict([[2, 1], [2, 1], [0, 1], [1, 2], [1, 0], [1, 0], [0, 0], [2, 2], [2, 0], [1, 2], [2, 2], [0, 2], [0, 1], [1, 2], [1, 2], [1, 0], [1, 0], [0, 0], [2, 2], [2, 0], [1, 2], [2, 2], [2, 1], [2, 1], [0, 1], [1, 2], [1, 0], [0, 0], [2, 2], [2, 0], [2, 1], [0, 1], [1, 2], [1, 0], [1, 0], [0, 0], [2, 2], [2, 0], [1, 2], [1, 0]])
    Accuracy = accuracy_score(Labels, output)
    print("_"*100)
    print("Accuracy of play prediction result is:(K=3) ", Accuracy*100,"%")

    Accuracy = CheckAccuracy(Features, Labels)
    print("_"*100)
    print("Accuracy of play prediction result is:(K=5) ", Accuracy*100,"%")
    
if __name__=="__main__":
    main()