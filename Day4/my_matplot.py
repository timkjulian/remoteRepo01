#!/usr/bin/env python3
"""
Author : hvalle <me@wsu.com>
Date   : 8/12/2021
Purpose: Test matplotlib, numpy, and pandas
"""

from matplotlib import pyplot as plt
import pandas as pd


def first_matplotlib():
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.xlabel('This is the x label')
    plt.ylabel('This is the y label')
    plt.title('My first plot')
    plt.show()


def first_pandas():
    data = {'year': [2008, 2012, 2016],
            'attendees': [112, 321, 729],
            'average age': [24, 43, 31]}
    df = pd.DataFrame(data)
    print(df)
    # Get one col
    print(df['year'])
    print(type(df['year']))
    # earlier_than_2013 = df['year'] < 2013
    plt.plot(df['year'], df['attendees'])
    plt.plot(df['year'], df['average age'])
    plt.legend(['attendees', 'average age'])
    plt.show()


def import_data_pandas(data):
    # Load data from csv files
    print(data.head())
    print(f'Total of {len(set(data.country))} unique countries')
    # Plot data from one country
    afghanistan = data[data.country == 'Afghanistan']
    plt.plot(afghanistan.year, afghanistan.gdpPerCapita)
    plt.title("Afghanistan's GDP Per Capita")
    plt.show()


def continent_data(data):
    # Compare Asia and Europe's GDP per capita
    # Get the list of continents
    continents = set(data.continent)
    print(continents)
    data_2007 = data[data.year == 2007]
    asia_2007 = data_2007[data_2007.continent == 'Asia']
    europe_2007 = data_2007[data_2007.continent == 'Europe']
    # Print number of countries per continent
    print(f'Asia countries: {len(set(asia_2007.country))}')
    print(f'Europe countries: {len(set(europe_2007.country))}')


# --------------------------------------------------
def main():
    """Make your noise here"""
    # first_pandas()
    data = pd.read_csv('countries.csv')
    # import_data_pandas(data)
    continent_data(data)


# --------------------------------------------------
if __name__ == '__main__':
    main()
