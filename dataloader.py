#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:20:43 2020

@author: hundredball
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load(years = range(2007,2021)):
    '''
    

    Parameters
    ----------
    years : iterable
        Fire incidents of these years will be imported. The default is range(2007,2021).

    Returns
    -------
    data : pandas.dataframe
        Fire incident of years

    '''
    
    assert hasattr(years, '__iter__')
    assert all(2007<=i<=2020 and isinstance(i, int) for i in years)
    
    data = []
    path = './data/all_fd_incidents.csv'
    try:
        data = pd.read_csv(path)
    except OSError as e:
        print(e)
        return None
    data = data[[(year_one_data in years) for year_one_data in data['year_response']]]
    
    return data

def clean_concat_data():
    '''
    Concat data from 2003 to 2020, and unify type of address_zip 
    Take over an hour

    '''
    years = list(range(2007,2021))
    data = []
    path = './data/fd_incidents_year_datasd_v1.csv'
    for year in years:
        data_year = pd.read_csv(path.replace('year',str(year)))
        data.append(data_year)
        
    data = pd.concat(data)
    data.reset_index(drop=True, inplace=True)
    
    # eliminate incidents lacking information (1749273 -> 1724049)
    data.dropna(inplace=True)
    
    # load zipcodes
    f = open('./data/SanDiego_zipcode.txt', 'r')
    str_zip_codes = f.readline()
    f.close()
    str_zip_codes = str_zip_codes.split(', ')
    zip_codes = set([int(zip_code) for zip_code in str_zip_codes])    
    
    # unify the type of address zip () (1724049 -> 1724027)
    # check if it's correct zip code in San Diego (1724027 -> 1713001)
    i = 0
    for index, row in data.iterrows():
        try:
            i += 1
            print(i)
            int_zip = int(row['address_zip'])
            if int_zip in zip_codes:
                data.at[index, 'address_zip'] = int_zip
            else:
                data.drop(index, inplace=True)
        except:
            data.drop(index, inplace=True)
            
    data.to_csv(r'./data/all_fd_incidents.csv')
    

if __name__ == '__main__':
    
    # check if types of properties of every years are unified
    data = load()
    years = list(range(2007, 2021))
    type_properties = []
    
    for prop in data.columns:
        elements = data[prop].unique()
        same_type_unique_prop = all(type(unique_prop)==type(elements[0]) \
                                     for unique_prop in elements)
        type_properties.append(same_type_unique_prop)



