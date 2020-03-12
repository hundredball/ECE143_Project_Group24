#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 16:03:50 2020

@author: hundredball
"""



import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
import matplotlib
# import os
# import glob
import seaborn as sns
# import functools
# from datetime import datetime
# from sorted_months_weekdays import *

# from sort_dataframeby_monthorweek import *


def yearly_trends(df, pop_df):
    '''Plot the monthly and yearly trends of the incidents
    input: df - Pandas Dataframe'''
    assert isinstance(df, pd.DataFrame)
    assert isinstance(pop_df, pd.DataFrame)
    df.drop(df.loc[df['year_response']== 2020].index, inplace=True)   ## Remove year 2020 data
    
    ##yearly trends
    year_count  = df['year_response'].value_counts()
    fig, ax = plt.subplots(figsize=(20,10))
    ax = sns.lineplot(x = year_count.index, y = year_count.values, color = 'r', marker = 'o')
    ax.yaxis.set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    plt.title('Year-to-Year Trend')
    ax.set_ylabel('Number of incidents', color = 'red')
    ax2 = ax.twinx()
    ax2 = sns.lineplot(x = pop_df['Year'], y = pop_df['Population'], marker = 'o')
    ax2.yaxis.set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    plt.title('Year-to-Year Trend')
    ax.set_ylabel('Number of incidents', color = 'red')
    ax.set_xlabel('Year')
    ax2.set_ylabel('Population', color = 'blue')
    #plt.savefig('yearlyincidents.jpg')
    plt.show()
    

def monthly_trends(df):
    ## month to month trends
    assert isinstance(df, pd.DataFrame)
    df.drop(df.loc[df['year_response']== 2020].index, inplace=True)   ## Remove year 2020 data
    month_count  = df['month_response'].value_counts()
    fig, ax = plt.subplots(figsize=(20,10))
    ax = sns.lineplot(month_count.index, month_count.values, color = 'orangered', marker = 'o')
    ax.yaxis.set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    plt.title('Month-to-Month Trend')
    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12], ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct',' Nov', 'Dec'])
    plt.ylabel('Number of incidents')
    plt.xlabel('Month')
    #plt.savefig('month2month.jpg')
    plt.show()