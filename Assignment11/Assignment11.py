import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    data  = pd.read_csv("WinePredictor.csv")
    print("Length of data", len(data))

    # print(data)
    
    Labels= data.Class
    Features=data.loc[:,data.columns!="Class"]

    # print("Features",Features)

    data_train, data_test, target_train, target_test=train_test_split(Features, Labels, test_size=0.7)

    kobj = KNeighborsClassifier(n_neighbors=3)
    kobj.fit(data_train, target_train)

    output= kobj.predict(data_test)
    Accuracy = accuracy_score(target_test, output)
    
    print("Accuracy of wine prediction result is: ", Accuracy*100,"%")



if __name__=="__main__":
    main()