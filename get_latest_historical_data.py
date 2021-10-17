#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 11:47:12 2021

@author: lester
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_latest_historical_data(symbol):
    url = 'https://frames.pse.com.ph/security/{}'.format(symbol.lower())
    
    html = requests.get(url)
    
    soup = BeautifulSoup(html.text, 'html.parser')
    
    table = soup.find('table',{'id':'data'})
    
    # get all trs
    trs = table.find_all('tr')
    
    historical_data = []
    
    # skip the header row
    for tr in trs[1:]:
        tds = tr.find_all('td')
        historical_data.append({
            'date': datetime.strftime(datetime.strptime(tds[0].text, '%b %d, %Y'), '%Y-%m-%d'),
            'open': float(tds[1].text.replace(',','')),
            'high':float(tds[2].text.replace(',','')),
            'low': float(tds[3].text.replace(',','')),
            'close': float(tds[4].text.replace(',','')),
            'average': float(tds[5].text.replace(',','')),
            'volume': int(tds[6].text.replace(',','')),
            'value': float(tds[7].text.replace(',',''))
            })
    
    return historical_data
    
get_latest_historical_data('ali')
