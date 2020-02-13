#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 10:14:25 2020

@author: hundredball
"""
import dataloader
import pandas as pd
import matplotlib.pyplot as plt

def plot_incident_time(data, unit_time):
    '''
    plot counts of incidents over month or year

    Parameters
    ----------
    data : dataframe
        records of every year
    
    unit_time : string
        month or year

    Returns
    -------
    None.

    '''

    
    assert isinstance(data, pd.DataFrame)
    assert unit_time == 'month' or unit_time == 'year'
    
    if unit_time == 'year':
        range_time = range(2007, 2021)
    elif unit_time == 'month':
        range_time = range(1, 13)
    
    type_response = unit_time + '_response'
    events_count = [len(data[data[type_response]==time]) for time in range_time]
    
    name_title = 'Counts of incidents over ' + unit_time
    plt.figure()
    plt.plot(range_time, events_count)
    plt.title(name_title)
    plt.show()
    
if __name__ == '__main__':
    data = dataloader.load(range(2007, 2020))
    plot_incident_time(data, 'month')

'''
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
'''