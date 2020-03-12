#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 08:33:49 2020

@author: hundredball
"""


import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import dataloader

def calculate_incidents_per_station(incidents_df):
    '''
    Get number of incidents per station from years of incidents

    Parameters
    ----------
    incidents_df : pd.DataFrame
        data over years

    Returns
    -------
    incidents_per_station_df: pd.DataFrame
        number of incidents per station

    '''
    assert isinstance(incidents_df, pd.DataFrame)
    
    # information of fire station
    stations_df = pd.read_csv('./data/fire_station_position.csv')
    stations_df.rename(columns={'zip':'address_zip'}, inplace=True)
    stations_zip = stations_df['address_zip'].value_counts()
    
    # change information of fire station to dataframe
    stations_zip_df = stations_zip.to_frame()
    stations_zip_df.reset_index(inplace=True)
    stations_zip_df.rename(columns={'address_zip':'num_stations','index':'address_zip'}, inplace=True)
    
    # create a dataframe with num_incidents, num_stations, incidents_per_station based on zip
    incidents_zip = incidents_df['address_zip'].value_counts()
    incidents_zip_df = incidents_zip.to_frame()
    incidents_zip_df.reset_index(inplace=True)
    incidents_zip_df.rename(columns={'address_zip':'num_incidents','index':'address_zip'}, inplace=True)
    incidents_per_station_df = incidents_zip_df.merge(stations_zip_df, on='address_zip', how='outer')
    incidents_per_station_df['incidents_per_station'] = incidents_per_station_df['num_incidents']/incidents_per_station_df['num_stations']
    incidents_per_station_df = incidents_per_station_df.fillna(0).sort_values(by='incidents_per_station', ascending=False)
    incidents_per_station_df['address_zip'] = incidents_per_station_df['address_zip'].astype(str)
    incidents_per_station_df.reset_index(drop=True, inplace=True)
    
    return incidents_per_station_df

def plot_fire_heatmap(san_diego, years, with_fire_station=False):
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
    assert isinstance(with_fire_station, bool)
    
    # incidents over years
    years_df = dataloader.load(years)
    years_df['address_zip'] = years_df['address_zip'].fillna(0.0).astype(int).astype(str)
    years_incidents = pd.pivot_table(years_df, values='incident_number', index=['address_zip'], columns=[], aggfunc=np.ma.count, fill_value=0)
    years_san_diego = san_diego.merge(years_incidents, on = 'address_zip', how = 'inner')
    years_san_diego['incident_number'] = years_san_diego['incident_number'].fillna(0.0).astype(int)
    
    # plot san diego map with incidents
    if len(years) == 1:
        title = 'Number of incidents in %d'%(years[0])
    else:
        title = 'Incidents over %d-%d'%(years[0],years[-1])
    ax = years_san_diego.plot(column = 'incident_number', scheme = 'quantiles', legend=True, cmap = 'OrRd', figsize=(12,20))
    
    # combine with fire station
    if with_fire_station:
        fire_df = pd.read_csv('./data/fire_station_position.csv')
        gdf = gpd.GeoDataFrame(fire_df, geometry=gpd.points_from_xy(fire_df.longitude, fire_df.latitude))
        gdf.plot(ax = ax, color = 'blue')
    
    plt.title(title)
    plt.axis('off')
    #plt.savefig('Incidents_over_%d-%d'%(years[0],years[-1])+'.png')
    plt.show()    
    
def plot_incidents_per_station(san_diego, years, with_fire_station=False):
    '''
    Plot number of incidents per station over years

    Parameters
    ----------
    san_diego : TYPE
        DESCRIPTION.
    years : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    assert isinstance(san_diego, gpd.GeoDataFrame)
    assert hasattr(years, '__iter__')
    assert all(2007<=i<=2020 and isinstance(i, int) for i in years)  
    assert isinstance(with_fire_station, bool)
    
    # information of incidents over years
    incidents_df = dataloader.load(years)
    
    # get dataframe with incidents per stations
    incidents_per_station_df = calculate_incidents_per_station(incidents_df)
    
    # merge incidents_per_station with san diego map
    years_san_diego = san_diego.merge(incidents_per_station_df, on = 'address_zip', how = 'inner')
    
    # plot the heatmap
    if len(years) == 1:
        title = 'Number of incidents per station in %d'%(years[0]);
    else:
        title = 'Number of incidents per station over %d-%d'%(years[0], years[-1])
    ax = years_san_diego.plot(column = 'incidents_per_station', scheme = 'quantiles', legend=True, cmap = 'OrRd', figsize=(12,20))
    
    # combine with fire station
    if with_fire_station:
        fire_df = pd.read_csv('./data/fire_station_position.csv')
        gdf = gpd.GeoDataFrame(fire_df, geometry=gpd.points_from_xy(fire_df.longitude, fire_df.latitude))
        gdf.plot(ax = ax, color = 'blue')
        
    plt.title(title)
    #plt.savefig('incidents_per_station_%d-%d'%(years[0], years[-1])+'.png')
    plt.show()
    
def plot_std_incidents(years):
    '''
    

    Parameters
    ----------
    years : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    assert hasattr(years, '__iter__')
    assert all(2007<=i<=2020 and isinstance(i, int) for i in years)  
    
    std_list = []
    
    # information of incidents over years
    incidents_df = dataloader.load(years)
    
    # get dataframe with incidents per stations
    incidents_per_station_df = calculate_incidents_per_station(incidents_df)
    
    # remove samples with no stations
    incidents_per_station_df = incidents_per_station_df[incidents_per_station_df['incidents_per_station']!=0]
    std_list.append(incidents_per_station_df['incidents_per_station'].std())
    
    for i in range(len(incidents_per_station_df)):
        incidents_per_station_df.loc[i, 'num_stations'] += 1
        incidents_per_station_df['incidents_per_station'] = incidents_per_station_df['num_incidents']/incidents_per_station_df['num_stations']
        incidents_per_station_df.replace(np.inf, 0, inplace=True)
        std_list.append(incidents_per_station_df['incidents_per_station'].std())
        
    title = 'std of number of incidents per station %d-%d'%(years[0],years[-1])
    plt.figure()
    plt.plot(std_list)
    plt.xlabel('number of added fire stations')
    plt.ylabel('std of number of incidents per station')
    plt.title(title)
    #plt.savefig('std_incidents_per_station_%d-%d'%(years[0],years[-1]) + '.png')
    plt.show()
    

if __name__=='__main__':
    with open('./data/SanDiego_zipcode.txt', 'r') as f:
        zips = f.readline().strip().replace(',', '').split()
    county = gpd.read_file('./data/san_diego_zip_codes.geojson')
    san_diego = county[county['zip'].isin(zips)]
    san_diego = san_diego.reset_index()
    san_diego.rename(columns = {'zip':'address_zip'}, inplace = True)
    
    years = range(2010,2011)
    
    plot_fire_heatmap(san_diego, years, with_fire_station=False)
    
    #plot_incidents_per_station(san_diego, years, with_fire_station=False)
    
    #plot_std_incidents(years)
    
    