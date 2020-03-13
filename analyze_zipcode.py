#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:20:29 2020

@author: hundredball
"""


import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import dataloader

def fireIncidentPerZipcode(fireDataFrame):
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

    zip_count  = fireDataFrame['address_zip'].value_counts()
    zip_count = zip_count[0:30]
    plt.figure(figsize=(12,14))
    ax = sns.barplot(y = zip_count.index, x= zip_count.values, alpha=0.8, color = 'orangered',orient = 'h', order=zip_count.index)
    ax.xaxis.set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    plt.title('Number of fires by zipcode', fontsize=20)
    plt.ylabel('ZIP Code(top 30)', fontsize=18)
    plt.xlabel('Number of fire incidents', fontsize=18)
    ax.text(123600,1.3,'Max at 92101(Downtown)',fontsize=20)
    plt.savefig('pic_zip-num.png')

    plt.show()

if __name__ == '__main__':
    
    fireDataFrame = dataloader.load(range(2007,2020))
    fireIncidentPerZipcode(fireDataFrame)
