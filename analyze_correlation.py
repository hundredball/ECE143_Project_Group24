#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:20:29 2020

@author: hundredball
"""


import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import seaborn as sns
import dataloader

def plot_correlation_month_zip(fireDataFrame):
    '''
    Plot the correlation map of incidents between month and zip code

    Parameters
    ----------
    fireDataFrame : pd.DataFrame
        data of incidents

    Returns
    -------
    None.

    '''
    
    assert isinstance(fireDataFrame, pd.DataFrame)
    
    ## HEAT MAP OF THE DISTRIBUTION OF NUMBER OF INCIDENTS ACROSS EACH ZIP CODE AND ACROSS EVERY MONTH
    monthZipPivotTable = pd.pivot_table(fireDataFrame, values='incident_number', index=['month_response'], columns=['address_zip'], aggfunc=np.ma.count, fill_value=0)
    fig, ax = plt.subplots(figsize=(20,10))
    ax = sns.heatmap(monthZipPivotTable, cmap='YlOrRd')
    ax.set_yticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'], rotation = 0)
    
    plt.show()
    
def plot_correlation_time_incidents(fireDataFrame):
    '''
    Plot the number of incidents through the time in one day

    Parameters
    ----------
    fireDataFrame : pd.DataFrame
        data of incidents

    Returns
    -------
    None.

    '''
    
    assert isinstance(fireDataFrame, pd.DataFrame)
    
    # Extract time from the date_response
    v = fireDataFrame['date_response']
    l = []
    for i in v:
        r = str(i)
        r = datetime.strptime(r, '%Y-%m-%d %H:%M:%S')
        k = r.strftime('%H')
        l.append(k)
    
    fireDataFrame['Timestamp'] = pd.Series(l , index = fireDataFrame.index)
    fireDataFrame.sort_values(by = 'Timestamp', inplace = True)
    
    # Read and plot the number of incidents recorded across the day
    hour_count  = fireDataFrame['Timestamp'].value_counts()
    fig,ax = plt.subplots(figsize=(20,10))
    ax = sns.lineplot(hour_count.index, hour_count.values, color = 'orangered', marker = 'o')
    ax.yaxis.set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    plt.title('Time and number of incidents correlation')
    plt.ylabel('Number of incidents')
    plt.xlabel('Time(hours)')
    plt.annotate('Least number of reported incidents', xy=(4,31492), xytext=(8,30000),
                arrowprops=dict(arrowstyle="->",facecolor='black'))
    plt.annotate('Most number of reported incidents', xy=(12,94723), xytext=(2,92000),
                arrowprops=dict(arrowstyle="->",facecolor='black'))
    plt.show()
    

if __name__ == '__main__':
    
    fireDataFrame = dataloader.load(range(2007,2020))
    plot_correlation_month_zip(fireDataFrame)
    plot_correlation_time_incidents(fireDataFrame)