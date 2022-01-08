#!/usr/bin/env python
# coding: utf-8

# # Sena Labs: rekt.news Web Scraping Activity
# 
# #### Goal: Extract exploit specific data from html/xml text data
# Extract vectors: ptcl_name, Date, amount_lost
# 
# The following data extracted will be an introductory method to how the Sena REKT Report dataset will use methods such as webscraping to autonmously upload and valid attack data within the DeFi ecosystem.

# In[45]:


import pandas as pd
from pandas import DataFrame

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import requests
import re
from bs4 import BeautifulSoup

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


from urllib.request import urlopen
from bs4 import BeautifulSoup


# In[3]:


url = "https://rekt.news/leaderboard/"
page = requests.get(url)
html = urlopen(url)


# In[4]:


def getHTMLdoc(url):
        response = requests.get(url)
        return response.text


# In[5]:


html_doc = getHTMLdoc(url)


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


print(soup.text)


# In[12]:


soup.find_all("a")


# In[13]:


# find all the anchor tags with "href" 
# attribute starting with "/"
exp_list=[]
for link in soup.find_all('a', 
                          attrs={'href': re.compile("^/")}):
    
    # display the actual urls
    content=link.get('href')
    
    clean_content=content.split('/')
    
    # Remove multiple null String elements twice
    clean_content.remove('')
    clean_content.remove('')
    
    # Remove all incapusulating list brackets from list elements
    new_list =(','.join(clean_content))
    
    exp_list.append(new_list)
    


# In[14]:


exp_list[:5]


# In[51]:


# Testing for any more null elements 
exp_list.remove('')


# In[52]:


# Remove the rekt extension that is attached to protocol name
ext = '-rekt'
exp_list = [elem.replace(ext, '') for elem in exp_list]
exp_list = [elem.replace('-', '') for elem in exp_list]
exp_list = [elem.replace('leaderboard', '') for elem in exp_list]


print(exp_list)


# In[53]:


exp_list[:5]


# In[54]:


# Final test
exp_list.remove('')


# In[55]:


len(exp_list)


# ### Search for Dates and amount_lost within list elements

# In[19]:


from datetime import datetime
from dateutil import parser
import dateutil.parser as dparser


# In[20]:


list_elements = soup.find_all("li")

list_elements


# In[21]:


table = soup.find_all('div', attrs = {'class':'leaderboard-row-details'})
table


# In[22]:


print(len(table))


# In[23]:


main = []
# Create a master list of conglomerated amounts and dates
for item in soup.select('div.leaderboard-row-details'):
    main.append(item.text)


# In[24]:


main[0:5]


# In[25]:


dates = []
for item in main:
    dates = [elem.replace('000,000 | ', '') for elem in dates]
    s1 = slice(8,27,1)
    dates.append(item[s1])


# In[26]:


dates[:5]


# In[27]:


clean_dates = []
for item in dates:
    regex = " (\\d{2}/\\d{2}/\\d{4})";
    i = item.lstrip(',000,000 | ')
    
    clean_dates.append(i)


# In[28]:


clean_dates[0:5]


# In[29]:


len(clean_dates)


# In[30]:


main[0:5]


# In[56]:


amt = []
for item in main:
    amt = [elem.replace(' | 0', '') for elem in amt]
    s2 = slice(0,13,1)
    amt.append(item[s2])


# In[57]:


amt[0:5]


# In[ ]:


clean_amt = []
for item in amt:
    i = item.rstrip(' | ')
    for item in amt:
            i = item.rstrip(' | 6')           
            for item in amt:
                i = item.rstrip(' | 5')
                for item in amt:
                    i = item.rstrip(' | 1')
                    for item in amt:
                            i = item.rstrip(' | 06')
clean_amt.append(i)


# In[ ]:


clean_amt


# In[ ]:


df = pd.Dataframe()
df['ptcl_name'] = exp_list[0::2]
df['Date'] = clean_dates[1::3]
df['amount_lost'] = clean_amt[2:4]


# In[ ]:


# Converting dataframe data to Excel
df.to_excel('sena_rekt_report.xlsx', index=False)


# In[ ]:




