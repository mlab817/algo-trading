#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 14:05:59 2021

@author: lester
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
from datetime import datetime

def get_daily_summary(symbol):
    url = 'https://frames.pse.com.ph/security/{}'.format(symbol)
    
    html = requests.get(url)
    
    soup = BeautifulSoup(html.text, 'html.parser')
    
    tables = soup.find_all('table')
    
    daily_stock_info = {}
    
    trs = tables[0].find_all('tr')
    
    for tr in trs[1:]:
        tds = tr.find_all('td')
        daily_stock_info[tds[0].text] = tds[1].text
        daily_stock_info[tds[2].text] = tds[3].text
        daily_stock_info[tds[4].text] = tds[5].text
    
    daily_stock_info = {re.sub(r'[^\w]', '', k).lower(): v.replace(',','') for k, v in daily_stock_info.items() if v}
    daily_stock_info.update({
        'symbol': symbol.upper()
    })
    return daily_stock_info

# all_stocks = pd.read_csv('all stocks.csv')
#
# summaries = []
#
# for index, row in all_stocks.iterrows():
#     summaries.append(get_daily_summary(row.symbol.lower()))
#
# print(summaries)
#
# df = pd.DataFrame(summaries)
# df.head()
#
# def convert_type(data):
#     data.replace(',','')
#     return data
#
# df.value = df.value.apply(convert_type)
# df.high = df.high.apply(convert_type)
# df['52wklow'] = df['52wklow'].apply(convert_type)
# df.volume = df.volume.apply(convert_type)
# df.low = df.low.apply(convert_type)
# df['52wkhigh'] = df['52wkhigh'].apply(convert_type)
# df.peratio = df.peratio.apply(convert_type)
# df.aveprice = df.aveprice.apply(convert_type)
#
# df.convert_dtypes()
# df.dtypes
#
# df.to_csv('{}.csv'.format(datetime.today().strftime('%m-%d-%Y')), index=False)
