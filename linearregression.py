import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def main():
    # Read the CSV file
    df = pd.read_csv("women-in-ECS.csv")
    x = df[['Year']] # x var = Year (independant)
    y = df['Female_Graduation_Rate'] # y var = Female Grad Rate (dependant)

    # x, y training variables help train the model and x, y test variables test it
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    model = LinearRegression() # Model is set to Linear regression
    model.fit(x_train, y_train) # train the model by minimizing MSE between predicted and actual values

    # Use trained model to predict graudation rates for x test
    y_pred = model.predict(x_test)
    # Calculate MSE for predicted and actual 
    mse = mean_squared_error(y_test, y_pred)

    # Create scatter plot for x and y
    plt.scatter(x, y)
    #plt.yticks([1, 5, 101])
    # Create regression line for prediction for variable x
    plt.plot(x, model.predict(x), color =  'red', linewidth = 2)
    # Set up the plot labels
    plt.xlabel('Year')
    plt.ylabel('Female Graduation Rate')
    plt.title('Linear Regression')
    # Show the plot
    plt.show()
if __name__ == "__main__":
    main()