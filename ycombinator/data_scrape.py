# scrape data and create dataset 
# ycombinator/data_scrape 

# imports
import re
import numpy as np 
import pandas as pd
from bs4 import BeautifulSoup
import requests
from lxml import html 

page = requests.get('https://www.seed-db.com/accelerators/viewall?acceleratorid=1011')

soup = BeautifulSoup(page.text, 'html.parser')

companies = soup.find('table', {'id': 'seedcos'})
tbody = companies.find('tbody')

#lists to append to
list0 = []
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []

# for elements in the tbody
for tr in tbody.find_all('tr'):
  status = tr.find_all('td')[0].text.strip()
  list0.append(status)
  names = tr.find_all('td')[1].text.strip()
  list1.append(names)
  websites = tr.find_all('td')[2].text.strip()
  list2.append(websites)
  cohort_dates = tr.find_all('td')[3].text.strip()
  list3.append(cohort_dates)
  exit_values = tr.find_all('td')[4].text.strip()
  list4.append(exit_values)
  total_funding = tr.find_all('td')[6].text.strip()
  list5.append(total_funding)

# create df into tidy data format
df = pd.DataFrame(data=[list3, list0, list1, list2, list4, list5])
yc = df.T

#rename columns
yc = yc.rename(columns={0:'cohort_date', 1:'status', 2:'company', 3:'website', 4:'exit_value', 5:'total_funding'})

yc['yc_cohort'] = yc['cohort_date'].replace(
    {'6/2005': 'YC S05',
     '1/2006': 'YC W06',
     '6/2006': 'YC S06',
     '1/2007': 'YC W07',
     '6/2007': 'YC S07',
     '1/2008': 'YC W08',
     '6/2008': 'YC S08',
     '1/2009': 'YC W09',
     '6/2009': 'YC S09',
     '1/2010': 'YC W10',
     '6/2010': 'YC S10',
     '1/2011': 'YC W11',
     '6/2011': 'YC S11',
     '1/2012': 'YC W12',
     '6/2012': 'YC S12',
     '1/2013': 'YC W13',
     '6/2013': 'YC S13',
     '1/2014': 'YC W14',
     '6/2014': 'YC S14',
     '1/2015': 'YC W15',
     '6/2015': 'YC S15',
     '1/2016': 'YC W16',
     '6/2016': 'YC S16',
     '1/2017': 'YC W17',
     '6/2017': 'YC S17',
     '1/2018': 'YC W18',
     '6/2018': 'YC S18',  
     })

# sort by cohort data
yc = yc.sort_values(by="cohort_date")

# uncomment below and run py file to create new csv

# yc.to_csv('yc.csv',index=False)

