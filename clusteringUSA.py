import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    #colors = ["#F99DBC", "#B795D7"]
    # Read dataset
    df = pd.read_csv('fullerton_cs.csv')
    #Hot code the datasets for country and ECS_Fields:
    df_encoded = pd.get_dummies(df, columns=['Year'])

    # Add Features for the clustering plot: Using female enrollment rate and female graduation rate 
    features = ['Female_Num_Graduation', 'Male_Num_Graduation', 'Female_Num_Enrolled', 'Male_Num_Enrolled'] + \
    [col for col in df_encoded.columns if col.startswith('Year_')]
    # Give features to variable X
    X = df_encoded[features]

    # Create a scaler to scale features X | Learns mean a nd SD for Mean and applies a scale for it to prevent bias
    scaler = StandardScaler()
    X_scaler = scaler.fit_transform(X)

    # Machine Learning Section: Finds pattern within data and groups them based on their distance  
    kmeans = KMeans(n_clusters=3, random_state=42) # Creates 3 cluster groups
    df_encoded['Cluster'] = kmeans.fit_predict(X_scaler) # Fit Kmodel to scaled features

    #Create seaborn scatterplot first:
    sns.scatterplot(
        x= 'Female_Num_Enrolled', # x variable as female_enrollment
        y= 'Female_Num_Graduation', # y variable as female graduation rate
        hue = 'Cluster',
        palette='cool',
        data = df_encoded, # use the data set that has comp sci and USA
        legend='full'
    )

    centers = scaler.inverse_transform(kmeans.cluster_centers_)

    # Create the scatter plot: x = female enrollemnt rate y = female graduation rate based on var Clusters which is scaled kmeans
    plt.scatter(
        centers[:, 0],
        centers[:, 1],
        c='red', # Color for the centroids
        s=200,
        alpha=0.6,
        marker='x', # Mark the centroids for the clusters
        label='Centroids' 
        ) #cmap = color scheme
    
    plt.xlabel('Number of Females who Enrolled') # x label
    plt.ylabel('Number of Females who Graduated') # y label
    plt.title('K-Means Clustering Based on Female Enrollment % and Female Graduation Rate for USA Comp Sci') # graph title
    plt.show() # Output the graph

if __name__ == "__main__":
    main()

