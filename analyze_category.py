#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:44:10 2020

@author: hundredball
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import dataloader

def plot_category_over_years(fire_df, years):
    '''
    

    Parameters
    ----------
    fire_df : pd.DataFrame
        all features of fire incidents over years
    years : iterable
        years 

    Returns
    -------
    None.

    '''
    assert isinstance(fire_df, pd.DataFrame)
    assert hasattr(years, '__iter__')
    assert all(2007<=i<=2020 and isinstance(i, int) for i in years)  
    
    category = fire_df['call_category'].value_counts()
    category.rename({'Emergency Medical Response':'EMR', 'Urgent Medical Response':'UMR', 'Non-Emergency Medical Response':'NEMR'}, inplace=True)
    category = category.sort_values(ascending=True)
    
    if len(years) == 1:
        title = 'Call Category in %d'%(years[0]);
    else:
        title = 'Call Category over %d-%d'%(years[0], years[-1])
    
    fig, ax = plt.subplots(figsize=(30,30))
    ax.barh(category.index, category.values, color='orangered')
    ax.xaxis.set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    matplotlib.rc('xtick', labelsize=30) 
    matplotlib.rc('ytick', labelsize=30) 
    plt.title(title)
    plt.savefig('call_category_%d-%d'%(years[0],years[-1]))
    plt.show()

if __name__ == '__main__':
    
    years = range(2010, 2011)
    fire_df = dataloader.load(years)
    
    plot_category_over_years(fire_df, years)
    