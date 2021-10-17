#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 11:36:46 2021

@author: lester
"""

import requests
from bs4 import BeautifulSoup

def extract(string, start='(', stop=')'):
    return string[string.index(start)+1:string.index(stop)]
    
def get_page_data(page=1):
    companies = []
    company_list_url = 'https://edge.pse.com.ph/companyDirectory/search.ax'
    
    resp = requests.post(company_list_url, data={
        'pageNo': page,
    })
    
    page = BeautifulSoup(resp.text,'html.parser')
    
    table = page.find('table', {'class':'list'})
    # get all rows
    trs = table.find_all('tr')
    # iterate over rows but exclude first because this is the thead
    for tr in trs[1:]:
        tds = tr.find_all('td')
        # name, symbol, sector, subsector, listing date
        a = tds[0].find('a')['onclick']
        cmpy_id, security_id = extract(a).replace('\'','').split(',')
        
        companies.append({
            'cmpy_id': int(cmpy_id, 10),
            'security_id': int(security_id, 10),
            'name': tds[0].text,
            'symbol': tds[1].text,
            'sector': tds[2].text,
            'subsector': tds[3].text,
            'listing_date':tds[4].text
            })
    
    return companies

def get_all_stocks():
    all_companies = []
    for i in range(1,7):    
        all_companies += get_page_data(page=i)
        
    return all_companies

print(get_all_stocks())
