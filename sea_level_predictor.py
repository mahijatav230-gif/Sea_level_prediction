import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Import data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    # First line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    years = pd.Series(range(1880, 2051))

    ax.plot(
        years,
        slope * years + intercept,
        color='red'
    )

    # Second line of best fit using data from 2000 onwards
    recent_df = df[df['Year'] >= 2000]

    slope, intercept, r_value, p_value, std_err = linregress(
        recent_df['Year'],
        recent_df['CSIRO Adjusted Sea Level']
    )

    years_recent = pd.Series(range(2000, 2051))

    ax.plot(
        years_recent,
        slope * years_recent + intercept,
        color='green'
    )

    # Labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save and return plot
    fig.savefig('sea_level_plot.png')

    return fig