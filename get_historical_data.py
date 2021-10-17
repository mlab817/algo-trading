#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 11:34:39 2021

@author: lester
"""

# Get stock data

import pandas as pd
import requests
from datetime import datetime

def get_historical_data(symbol, company_id, security_id):
    historical_chart_url = 'https://edge.pse.com.ph/common/DisclosureCht.ax'
    data = requests.post(historical_chart_url, json={
        'cmpy_id': company_id,
        'endDate': datetime.today().strftime('%m-%d-%Y'),
        'security_id': security_id,
        'startDate': "01-01-2000"
        })
    
    chart_data = data.json()['chartData']
    chart_df = pd.DataFrame(chart_data)
    
    return chart_df

all_stocks = pd.read_csv('all stocks.csv')

for index, row in all_stocks.iterrows():
    stock = get_historical_data(row.symbol, row.cmpy_id, row.security_id)
    print(stock)
    break