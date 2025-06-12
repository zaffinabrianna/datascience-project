import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def main():
    df = pd.read_csv("women-in-ECS.csv")
    x = df[['Year']]
    y = df['Female_Graduation_Rate']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    mse = mean_squared_error(y_test, y_pred)

    plt.scatter(x, y)
    #plt.yticks([1, 5, 101])
    plt.plot(x, model.predict(x), color =  'red', linewidth = 2)
    plt.xlabel('Actual Values')
    plt.ylabel('Dependant Values')
    plt.title('Linear Regression')
    plt.show()
if __name__ == "__main__":
    main()