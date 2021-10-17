#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 11:36:10 2021

@author: lester
"""

import requests
from bs4 import BeautifulSoup

def get_stock_information(symbol=''):
    base_url = 'https://frames.pse.com.ph/security/'

    stock_info = {}
    stock_info['symbol'] = symbol
    
    page = requests.get(base_url + symbol.lower())
    
    soup = BeautifulSoup(page.text, 'html.parser')
    
    stock_info['logo'] = soup.find('img', {'class':'sector-blank'})['src']
    
    tables = soup.find_all('table')
    
    trs = tables[0].find_all('tr')
    
    data = {}
    
    for tr in trs:
        tds = tr.find_all('td')
        data[tds[0].text] = tds[1].text
        data[tds[2].text] = tds[3].text
        data[tds[4].text] = tds[5].text
        
    clean_data = {k: v for k, v in data.items() if v}
    stock_info.update(clean_data)
    
    t2 = tables[2]
    
    market_statistics = []
    
    trs = t2.find_all('tr')
    
    for tr2 in trs[1:]:
        tds = tr2.find_all('td')
        
        market_statistics.append({
            'year': tds[0].text,
            'volume': tds[1].text,
            'value': tds[2].text
        })
        
    stock_info['market_statistics'] = market_statistics
    
    t4 = tables[4]
    
    trs4 = t4.find_all('tr')
    trs4
    
    shares_info = {}
    
    for tr in trs4:
        tds = tr.find_all('td')
        shares_info[tds[0].text] = tds[1].text
        
    stock_info.update(shares_info)
    
    return stock_info

print(get_stock_information('AP'))