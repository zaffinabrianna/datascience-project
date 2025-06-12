import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    #colors = ["#F99DBC", "#B795D7"]
    df = pd.read_csv('women-in-ECS.csv')
    features = ['Female_Enrollment', 'Female_Graduation_Rate']
    X = df[features]

    scaler = StandardScaler()
    X_scaler = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=3, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X_scaler)
    
    plt.figure(figsize=(10, 6))

    plt.scatter(df['Female_Enrollment'], df['Female_Graduation_Rate'], c=df['Cluster'], cmap='cool')
    plt.xlabel('Female Enrollment Percentage')
    plt.ylabel('Female Graduation Rate')
    plt.title('K-Means Clustering Based on Female Enrollment % and Female Graduation Rate')
    plt.show()

if __name__ == "__main__":
    main()

