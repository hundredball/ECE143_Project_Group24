#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 08:33:49 2020

@author: hundredball
"""


import pandas as pd
import numpy as np
import geopandas as gpd
import geoplot as gpt
import matplotlib.pyplot as plt
import dataloader

def plot_fire_station(san_diego, years):
    '''
    Plot fire stations with number of incidents over years

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
    
    # the information of the location of fire stations
    fire_df = pd.read_csv('./data/fire_station_position.csv')
    gdf = gpd.GeoDataFrame(fire_df, geometry=gpd.points_from_xy(fire_df.longitude, fire_df.latitude))
    
    # incidents over years
    years_df = dataloader.load(years)
    years_df['address_zip'] = years_df['address_zip'].fillna(0.0).astype(int).astype(str)
    years_incidents = pd.pivot_table(years_df, values='incident_number', index=['address_zip'], columns=[], aggfunc=np.ma.count, fill_value=0)
    years_san_diego = san_diego.merge(years_incidents, on = 'address_zip', how = 'inner')
    years_san_diego['incident_number'] = years_san_diego['incident_number'].fillna(0.0).astype(int)
    
    title = 'Incidents over %d-%d'%(years[0],years[-1])
    # plot san diego map with incidents
    ax = years_san_diego.plot(column = 'incident_number', scheme = 'quantiles', legend=True, cmap = 'OrRd', figsize=(12,20))
    # combine with fire station
    gdf.plot(ax = ax, color = 'blue')
    plt.title(title)
    
    plt.show()
    

if __name__=='__main__':
    with open('./data/SanDiego_zipcode.txt', 'r') as f:
        zips = f.readline().strip().replace(',', '').split()
    county = gpd.read_file('./data/san_diego_zip_codes.geojson')
    san_diego = county[county['zip'].isin(zips)]
    san_diego = san_diego.reset_index()
    san_diego.rename(columns = {'zip':'address_zip'}, inplace = True)
    
    years = range(2008,2010)
    plot_fire_station(san_diego, years)
    
    