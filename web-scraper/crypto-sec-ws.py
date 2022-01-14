#!/usr/bin/env python
# coding: utf-8

# # Sena Labs: crypto.sec Web Scraping Activity
# 
# #### Goal: Extract exploit specific data from html/xml text data
# Extract vectors: ptcl_name, Date, amount_lost
# 
# The following data extracted will be an introductory method to how the Sena REKT Report dataset will use methods such as webscraping to autonmously upload and valid attack data within the DeFi ecosystem.

# In[1]:


import pandas as pd
from pandas import DataFrame

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import requests
import re

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


# In[3]:


# url = "https://cryptosec.info/defi-hacks/"
# req = Request(url , headers={'User-Agent': 'Mozilla/5.0'}
              
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

site= "https://cryptosec.info/defi-hacks/"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page)
print(soup)


# In[4]:


def getHTMLdoc(site):
        response = requests.get(site)
        return response.text


# In[5]:


html_doc = getHTMLdoc(site)


# In[6]:


soup = BeautifulSoup(html_doc, 'html.parser')


# In[7]:


print(soup.prettify())


# In[8]:


# Get the title
title = soup.title
print(title)


# In[9]:


header = soup.header()
print(header)


# In[10]:


text = soup.get_text()


# In[11]:


print(soup.get_text)


# In[12]:


soup.find_all("div")


# In[13]:


ptcl_table = soup.find_all('h3', attrs = {'class':'eae-tl-item-title'})
ptcl_table[0:5]


# In[14]:


extracted_pctl = []
# Create a master list
for item in soup.select('h3.eae-tl-item-title'):
    extracted_pctl.append(item.text)


# In[15]:


extracted_pctl[0:5]


# In[16]:


len(extracted_pctl)


# In[17]:


dates_table = soup.find_all('div', attrs = {'class':'eae-tl-item-meta-inner'})
dates_table[0:5]


# In[18]:


extracted_dates = []
# Create a master list
for item in soup.select('div.eae-tl-item-meta-inner'):
    extracted_dates.append(item.text)


# In[19]:


extracted_dates[0:5]


# In[20]:


new_extracted_dates = []
for i in extracted_dates:
    j = re.sub(' \s+', '', i)
    # j = j.translate('\t\n')
    j = j.strip('\t\n')
    new_extracted_dates.append(j)


# In[21]:


new_extracted_dates[0:5]


# In[22]:


len(new_extracted_dates)


# In[23]:


long_month_names = ['January','February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November','December']


# In[24]:


def monthToNum(shortMonth):
    return {
            'January': 1,
            'February': 2,
            'March': 3,
            'April': 4,
            'May': 5,
            'June': 6,
            'July': 7,
            'August': 8,
            'September': 9,
            'October': 10,
            'November': 11,
            'December': 12
    }[shortMonth]


# In[25]:


# Create a dummie list of all the miscellanous Strings in from the span elements
# From here we can sift out the dollar amounts, which is the data we're looking for
dummie_list = []
rows = soup.find_all('span')

for row in rows:
        r = row.get_text()
        dummie_list.append(r)


# In[26]:


dummie_list


# In[27]:


# Create a final list of dollar values that represent amount lost
amt_table = []

for i in dummie_list:
    if i == 'Amount stolen: n/a':
        i = "null" # Makes all n/a seen as null
        
    if('$' in i and 'Amount stolen: ' not in i or i == "null"):
           amt_table.append(i)


# In[28]:


amt_table.pop(0)
amt_table[0:20]


# In[29]:


len(amt_table)


# In[30]:


df = pd.DataFrame(extracted_pctl, columns = ["protocol_name"])
df.head()


# In[31]:


df1 = pd.DataFrame(new_extracted_dates, columns = ["date_of_attack"])
df1.head()


# In[32]:


df2 = pd.DataFrame(amt_table, columns = ["amount_lost"])
df2.head()


# In[33]:


df=df.join(df1)
df=df.join(df2)
df.head()


# In[35]:


# Converting dataframe data to Excel
# The data stored accounts for crypto.sec landing page data
df.to_excel('sena_cryptosec_ws.xlsx', index=False)


# In[ ]:




