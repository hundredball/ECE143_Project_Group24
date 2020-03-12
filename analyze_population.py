#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 15:01:28 2020

@author: hundredball
"""

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

def plot_population_heatmap(san_diego, years):
    '''
    Plot population heat map over years

    Parameters
    ----------
    san_diego : gpd.GeoDataFrame
        map of san diego
    years : iterable of int
        recorded duration

    '''
    
    assert isinstance(san_diego, gpd.GeoDataFrame)
    assert hasattr(years, '__iter__')
    assert all(2007<=i<=2020 and isinstance(i, int) for i in years)  
    
    pop_df = pd.read_csv('./data/SanDiego_population.csv')
    pop_df['address_zip'] = pop_df['address_zip'].astype(str)
    
    pop_san_diego = san_diego.merge(pop_df, on = 'address_zip', how = 'outer')
    pop_san_diego.fillna({'population':0, 'density':0}, inplace=True)
    pop_san_diego.plot(column = 'population', scheme = 'quantiles', legend=True, cmap = 'Blues', figsize=(20,12))
    
    if len(years) == 1:
        title = 'San Diego Population in %d'%(years[0])
    else:
        title = 'San Diego Population over %d-%d'%(years[0],years[-1])
        
    plt.axis('off')
    plt.title(title)
    #plt.savefig('San_Diego_Population_%d-%d'%(years[0], years[-1]))
    plt.show()
    
if __name__ == '__main__':
    
    with open('./data/SanDiego_zipcode.txt', 'r') as f:
        zips = f.readline().strip().replace(',', '').split()
    county = gpd.read_file('./data/san_diego_zip_codes.geojson')
    san_diego = county[county['zip'].isin(zips)]
    san_diego = san_diego.reset_index()
    san_diego.rename(columns = {'zip':'address_zip'}, inplace = True)
    
    years = range(2010,2011)
    
    plot_population_heatmap(san_diego, years)
