# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 14:21:58 2021

@author: mlab8
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
import json



    
all_companies
len(all_companies)

df = pd.DataFrame(all_companies)
df.tail()

df.to_csv('all stocks.csv', index=False)        


all_stocks.head()

all_stocks.subsector.unique()
all_stocks.sector.unique()

print(get_stock_information('bpi'))

stock_profiles = []

for index, row in all_stocks.iterrows():
    try:
        stock_profiles.append(get_stock_information(row.symbol))
    except:
        continue

with open('stocks.json', 'w') as f:
    json.dump(stock_profiles, f)