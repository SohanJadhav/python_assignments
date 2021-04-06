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

def main():
    data = pd.read_csv('MarvellousInfosystems_PlayPredictor.csv')

    le = preprocessing.LabelEncoder()

    original_wether_data = data.iloc[:,1]
    original_temperature_data = data.iloc[:,2]
    original_play_data = data.iloc[:,3]

    le.fit(original_wether_data)
    encoded_wether_data = le.transform(original_wether_data)

    le.fit(original_temperature_data)
    encoded_temperature_data = le.transform(original_temperature_data)

    le.fit(original_play_data)
    Labels = le.transform(original_play_data)

    Features= []
    for i in range(len(data)):
        Features.append([encoded_wether_data[i],encoded_temperature_data[i]])

    data_train, data_test, target_train, target_test = train_test_split(Features, Labels, test_size=.5) 

    dobj= KNeighborsClassifier(n_neighbors=3)
    dobj.fit(data_train, target_train)

    output= dobj.predict(data_test)
    Accuracy = accuracy_score(target_test, output)
    
    print("Accuracy of play prediction result is: ", Accuracy*100,"%")
    

if __name__=="__main__":
    main()