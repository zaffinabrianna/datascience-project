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

    temp = pd.read_csv('women-in-ECS.csv')
    print(temp.to_string())

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

    #Now using with seaborn:
    colors = ["#F99DBC", "#B795D7"]
    sns.set_palette(colors)

    #For the barplot:
    #Year
    line_plots = sns.barplot(
        x="Year",
        y="Female_Graduation_Rate",
        hue = "ECS_Fields",
        data=df[df["ECS_Fields"].isin(["Computer Science", "Engineering"])],
        ci=None
    )
    
    #Country
    #line_plots = sns.barplot(
    #    x="Country",
    #    y="Female_Graduation_Rate",
    #    hue = "ECS_Fields",
    #    data=df[df["ECS_Fields"].isin(["Computer Science", "Engineering"])],
    #    ci=None
    #)
    
    #For the line plots:
    #line_plots = sns.lineplot(
    #    x="Year",
    #    y="Female_Graduation_Rate",
    #    hue = "ECS_Fields",
    #    data=df[df["ECS_Fields"].isin(["Computer Science", "Engineering"])],
    #    ci=None
    #)

    plt.show()


if __name__ == "__main__":
    main()