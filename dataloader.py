#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:20:43 2020

@author: hundredball
"""

import pandas as pd
import matplotlib.pyplot as plt

def load(years = list(range(2007,2021))):
    '''
    

    Parameters
    ----------
    years : list
        Fire incidents of these years will be imported. The default is list(range(2007,2021)).

    Returns
    -------
    data : pandas.dataframe
        Fire incident of yeas

    '''
    
    assert isinstance(years, list)
    assert all(2007<=i<=2020 and isinstance(i, int) for i in years)
    
    data = []
    path = './data/fd_incidents_year_datasd_v1.csv'
    for year in years:
        data_year = pd.read_csv(path.replace('year',str(year)))
        data.append(data_year)
        
    data = pd.concat(data)
    
    return data

data = load()
years = list(range(2007,2021))

# Counts of incidents over years
events_count = [len(data[data['year_response']==year]) for year in years]
dict_count = dict(zip(years,events_count))

plt.figure()
plt.plot(years, events_count)
plt.title('Counts of incidents over years')

plt.show()

# Create a table for counts of each incident over years
call_categories = data['call_category'].unique()
problem_categories = data['problem'].unique()
dict_event = dict()

for year in years:
    event_count_year = [len(data[(data['call_category'] == event) & (data['year_response'] == year)]) for event in call_categories]
    dict_event[year] = event_count_year
    
df_event_counts = pd.DataFrame.from_dict(dict_event)
dict_categories = dict( zip(range(len(call_categories)), call_categories) )
df_event_counts.rename(index=dict_categories, inplace = True)
