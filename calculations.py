#!/usr/bin/env python3
import csv
import pandas as pd

def main():
    df = pd.read_csv('women-in-ECS.csv')
    FGR_median = df['Female_Graduation_Rate'].median()
    FGR_average = df['Female_Graduation_Rate'].mean()
    FGR_Q1 = df['Female_Graduation_Rate'].quantile(.25)
    FGR_Q3 = df['Female_Graduation_Rate'].quantile(.75)
    FGR_max = df['Female_Graduation_Rate'].max()
    FGR_min = df['Female_Graduation_Rate'].min()
    FGR_range = FGR_max - FGR_min

    print('Average:', FGR_average)
    print('Quarter 1: ', FGR_Q1)
    print('Median: ', FGR_median)
    print('Quarter 3: ', FGR_Q3)
    print('Max: ', FGR_max)
    print('Min: ', FGR_min)
    print('Range: ', FGR_range)

if __name__ == "__main__":
    main()     