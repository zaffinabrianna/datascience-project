import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    #colors = ["#F99DBC", "#B795D7"]
    # Read dataset
    df = pd.read_csv('women-in-ECS.csv')
    # Add Features for the clustering plot: Using female enrollment rate and female graduation rate 
    features = ['Female_Enrollment', 'Female_Graduation_Rate']
    # Give features to variable X
    X = df[features]

    # Create a scaler to scale features X | Learns mean and SD for Mean and applies a scale for it to prevent bias
    scaler = StandardScaler()
    X_scaler = scaler.fit_transform(X)

    # Machine Learning Section: Finds pattern within data and groups them based on their distance  
    kmeans = KMeans(n_clusters=3, random_state=42) # Creates 3 cluster groups
    df['Cluster'] = kmeans.fit_predict(X_scaler) # Fit Kmodel to scaled features

    # Create the scatter plot: x = female enrollemnt rate y = female graduation rate based on var Clusters which is scaled kmeans
    plt.scatter(df['Female_Enrollment'], df['Female_Graduation_Rate'], c=df['Cluster'], cmap='cool') #cmap = color scheme
    plt.xlabel('Female Enrollment Percentage') # x label
    plt.ylabel('Female Graduation Rate') # y label
    plt.title('K-Means Clustering Based on Female Enrollment % and Female Graduation Rate') # graph title
    plt.show() # Output the graph

if __name__ == "__main__":
    main()

