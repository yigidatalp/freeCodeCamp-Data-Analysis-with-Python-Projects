# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 20:12:58 2023

@author: Yigitalp
"""
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    X = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(X, y)

    # Create first line of best fit
    first_model = linregress(X, y)
    first_X_pred = pd.Series([i for i in range(1880, 2051)])
    first_y_pred = first_model.slope*first_X_pred + first_model.intercept
    plt.plot(first_X_pred, first_y_pred, 'r')

    # Create second line of best fit
    new_df = df[df['Year'] >= 2000]
    new_X = new_df['Year']
    new_y = new_df['CSIRO Adjusted Sea Level']

    second_model = linregress(new_X, new_y)
    second_X_pred = pd.Series([i for i in range(2000, 2051)])
    second_y_pred = second_model.slope*second_X_pred + second_model.intercept
    plt.plot(second_X_pred, second_y_pred, 'g')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()