#!/usr/bin/env python3
import csv
import pandas as pd

def main():
    # Read CSV and put it into a variable using pandas
    df = pd.read_csv('women-in-ECS.csv')
    # Get median of the Female Graduation Rate
    FGR_median = df['Female_Graduation_Rate'].median()
    # Get mean of the Female Graduation Rate
    FGR_average = df['Female_Graduation_Rate'].mean()
    # Get the upper precentile of the Female Graduation Rate (Q1)
    FGR_Q1 = df['Female_Graduation_Rate'].quantile(.25)
    # Get the lower percentile of the Female Graduation Rate (Q3)
    FGR_Q3 = df['Female_Graduation_Rate'].quantile(.75)
    # Get the max of the Female Graduation Rate
    FGR_max = df['Female_Graduation_Rate'].max()
    # Get the min of the Female Graduation Rate
    FGR_min = df['Female_Graduation_Rate'].min()
    # Find the range of the Female Graduation Rate
    FGR_range = FGR_max - FGR_min

    # Outputting Info:
    print('Average:', FGR_average)
    print('Quarter 1: ', FGR_Q1)
    print('Median: ', FGR_median)
    print('Quarter 3: ', FGR_Q3)
    print('Max: ', FGR_max)
    print('Min: ', FGR_min)
    print('Range: ', FGR_range)

if __name__ == "__main__":
    main()     