#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    #testing the modules
    #arr = np.array([1, 2, 3, 4, 5])
    #print(arr)
    #print(type(arr))

    # Read and print CSV
    temp = pd.read_csv('women-in-ECS.csv')
    print(temp.to_string())

    # Read csv columns and print
    df = pd.read_csv('women-in-ECS.csv')
    print(df.columns.tolist())
    #Disregard this, this was orginally using pandas:
    #x = df['Country']
    #y = df['Year']
    #y = df['ECS_Fields']

    #plt.bar(x, y)
    #Tick seperation
    #plt.yticks(np.arange(0, 65, step=2))
    #plt.xlabel('X-Axis')  
    #plt.ylabel('Y-Axis')
    #plt.title('Graph')

    #plt.show()
    us_data = df[
        (df['Country'] == 'USA') &
        (df['ECS_Fields'] == 'Computer Science')]
    #Now using with seaborn:
    colors = ["#F99DBC", "#B795D7"]
    sns.set_palette(colors)

    #For the barplot:
    #Country
    line_plots = sns.barplot(
        x="Year", # x var. = country
        y="Female_Graduation_Rate", # y var. = female graduation rate
        hue = "ECS_Fields", # different bars for comp sci and engineering
        data= us_data,
        errorbar=None
    )
    
    #For the line plots:
    #line_plots = sns.lineplot(
    #    x="Year",
    #    y="Female_Graduation_Rate",
    #    hue = "ECS_Fields",
    #    data=df[df["ECS_Fields"].isin(["Computer Science", "Engineering"])],
    #    ci=None
    #)

    # Show the graph
    plt.show()


if __name__ == "__main__":
    main()