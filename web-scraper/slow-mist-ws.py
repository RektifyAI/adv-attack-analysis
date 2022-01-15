#!/usr/bin/env python
# coding: utf-8

# # Sena Labs: slowmist.io Web Scraping Activity
# 
# #### Goal: Extract exploit specific data from html/xml text data
# Extract vectors: protocol_name, Date, amount_lost, attack_type, description_text
# 
# The following data extracted will be an introductory method to how the Sena REKT Report dataset will use methods such as webscraping to autonmously upload and valid attack data within the DeFi ecosystem. 
# 
# The description text is especially important to extract because in a future project it will be analyzed using Natural Language Processing(NLP) to attach weights to words using Python's nltk package.

# In[1]:


import pandas as pd
from pandas import DataFrame

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import requests
import re
from bs4 import BeautifulSoup

import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


from urllib.request import urlopen
from bs4 import BeautifulSoup


# In[ ]:


# Importing slowmist.io main page -- Page 1
url = "https://hacked.slowmist.io/en/"
page = requests.get(url)
html = urlopen(url)


# In[ ]:


def getHTMLdoc(url):
        response = requests.get(url)
        return response.text


# In[ ]:


html_doc = getHTMLdoc(url)


# In[ ]:


soup = BeautifulSoup(html_doc, 'html.parser')


# In[ ]:


print(soup.prettify())


# In[ ]:


# Get the title
title = soup.title
print(title)


# In[ ]:


text = soup.get_text()


# In[ ]:


print(soup.text)


# In[ ]:


# Finding all list elements. List elements contain the 
soup.find_all("li")


# In[ ]:


ptcl_table = soup.find_all('h3')
ptcl_table 


# In[ ]:


dummie_ptcl_table = []
for row in ptcl_table:
        r = row.get_text()
        dummie_ptcl_table.append(r)


# In[ ]:


dummie_ptcl_table[0:5]


# In[ ]:


cleaned_ptcl_table = []
for item in dummie_ptcl_table:
    new_item = item.replace('Hacked target: ', "")
    cleaned_ptcl_table.append(new_item)


# In[ ]:


cleaned_ptcl_table[0:5]


# In[ ]:


len(cleaned_ptcl_table)


# In[ ]:


dates_table = soup.find_all('span', attrs = {'class':'time'})
dates_table


# In[ ]:


cleaned_dates_table = []
for item in soup.select('span.time'):
    cleaned_dates_table.append(item.text)


# In[ ]:


cleaned_dates_table[0:5]


# In[ ]:


final_dates = []
for item in cleaned_dates_table:
    i = datetime.datetime.strptime(item, '%Y-%m-%d').strftime('%m/%d/%Y')
    final_dates.append(i)


# In[ ]:


final_dates[0:5]


# In[ ]:


len(final_dates)


# In[ ]:


table = soup.find_all('span')
table[0:5]


# In[ ]:


content_table = []
for i in table:
    j = i.get_text()
    content_table.append(j)
    print(j)


# In[ ]:


content_table[0:10] 
# This is a list of all the dates, amount lost, and attack methods
# Data cleaning before extraction is the best method to getting
# the rest of the data needed for the DataFrame


# In[ ]:


amt_table = []
for row in content_table:
        k = re.sub(' \s+', '', row)
        k = k.strip('\t\n')
        amt_table.append(k)


# In[ ]:


amt_table[0:10]


# In[ ]:


new_amt_table = []
for item in amt_table:
    if ('Amount of loss:' in item):
        item = item.strip('Amount of loss:')
        new_amt_table.append(item)


# In[ ]:


new_amt_table[0:10]


# In[ ]:


len(new_amt_table)


# In[ ]:


amt_table[0:10]


# In[ ]:


attack_table = []
for item in amt_table:
    if ('Attack method:' in item):
        i = item.lstrip('Attack method: ')
        attack_table.append(i)


# In[ ]:


attack_table[0:10]


# In[ ]:


len(attack_table)


# In[ ]:


table = soup.find_all('p')
table


# In[ ]:


content_table = []
for i in table:
    j = i.get_text()
    content_table.append(j)
    print(j)


# In[ ]:


content_table[0:10]


# In[ ]:


description_table = []
for item in content_table:
    if ('Description of the event:' in item):
        i = item.lstrip('Description of the event:')
        description_table.append(i)


# In[ ]:


description_table


# In[ ]:


len(description_table)


# In[ ]:


df = pd.DataFrame(cleaned_ptcl_table, columns = ["protocol_name"])
df.head()


# In[ ]:


df1 = pd.DataFrame(final_dates, columns = ["date_of_attack"])
df1.head()


# In[ ]:


df2 = pd.DataFrame(new_amt_table, columns = ["amount_lost"])
df2.head()


# In[ ]:


df3 = pd.DataFrame(attack_table, columns = ["attack_type"])
df3.head()


# In[ ]:


df4 = pd.DataFrame(description_table, columns = ["descripton_text"])
df4.head()


# In[ ]:


df=df.join(df1)
df=df.join(df2)
df=df.join(df3)
df=df.join(df4)
df.head()


# In[ ]:


# Converting dataframe data to Excel
# The data stored accounts for slowmist.io landing page data
df.to_excel('sena_slowmist_ws.xlsx', index=False)

