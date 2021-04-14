import pandas as pd
from sklearn.linear_model import LinearRegression

def main():
    data = pd.read_csv("Advertising.csv")

    # print(data)

    TV= data.TV
    Radio= data.radio
    Newspaper= data.newspaper

    # TV = TV.reshape((-1,1))
    # Radio = Radio.reshape((-1,1))
    # Newspaper = Newspaper.reshape((-1,1))

    Features = list(zip(TV,Radio,Newspaper))
    Lables =data.sales

    obj= LinearRegression()
    obj.fit(Features,Lables)

    output = obj.predict([[193.4,44.7,51.9], [237.4,5.1,23.5], [67.8,36.6,114], [193.4,44.7,51.9]])
    print("Expected result is ", output)

    Rsquare= obj.score(Features,Lables)

    print("Value of R Square is ", Rsquare)

if __name__=="__main__":
    main()