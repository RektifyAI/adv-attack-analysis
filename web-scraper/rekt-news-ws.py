#!/usr/bin/env python
# coding: utf-8

# # Sena Labs: rekt.news Web Scraping Activity
# 
# ##### Goal: Extract attack/exploit specific data from html/xml text data
# Extract vectors: protocol_name, date, amount_lost
# 
# The following data extracted will be an introductory method to how the Sena REKT Report dataset will use methods such as Python webscraping to autonomously upload and valid attack data within the DeFi ecosystem. The following webscrapin method is more efficient than initial manual data entry that will be needed later in validation and data cleaning.

# In[1]:


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


# In[15]:


# Testing for any more null elements 
exp_list.remove('')


# In[16]:


# Remove the rekt extension that is attached to protocol name
ext = '-rekt'
exp_list = [elem.replace(ext, '') for elem in exp_list]
exp_list = [elem.replace('-', '') for elem in exp_list]
exp_list = [elem.replace('leaderboard', '') for elem in exp_list]


print(exp_list)


# In[17]:


exp_list[:5]


# In[18]:


exp_list.remove('')


# In[19]:


# Final test
exp_list.remove('')


# In[20]:


len(exp_list)


# ### Search for Dates and amount_lost within list elements
# After using the website inspector shortcut we were able to sift throught the HTML file for rekt.news and find that all dates and amounts were concatenated together within list elements. 

# In[21]:


from datetime import datetime
from dateutil import parser
import dateutil.parser as dparser


# In[22]:


# li is the html tag for list elements within a table 
list_elements = soup.find_all("li")

list_elements


# In[23]:


table = soup.find_all('div', attrs = {'class':'leaderboard-row-details'})
table


# In[24]:


print(len(table))


# In[25]:


main = []
# Create a master list of conglomerated amounts and dates
for item in soup.select('div.leaderboard-row-details'):
    main.append(item.text)


# In[26]:


main[0:5]


# In[27]:


dates = []
for item in main:
    dates = [elem.replace('000,000 | ', '') for elem in dates]
    s1 = slice(8,27,1)
    dates.append(item[s1])


# In[28]:


dates[:5]


# In[29]:


clean_dates = []
for item in dates:
    regex = " (\\d{2}/\\d{2}/\\d{4})";
    i = item.lstrip(',000,000 | ')
    
    clean_dates.append(i)


# In[30]:


# A list of all of the cleaned dates
clean_dates[0:5]


# In[31]:


len(clean_dates)


# In[32]:


main[0:5]


# In[33]:


amt = []
for item in main:
    amt = [elem.replace(' | ', '') for elem in amt]
    s2 = slice(0,13,1)
    amt.append(item[s2])


# In[34]:


amt[0:5]


# In[35]:


clean_amt = []
for x in amt:
    i = x.rstrip('| ')           
    clean_amt.append(i)


# In[36]:


# The last 6 elements will have to be manually cleaned which is not a grueling burden
clean_amt[0:5]


# In[37]:


print(len(clean_amt))


# In[38]:


# Testing if the length of each list are equal so the DataFrame
# is built with the proper dimensions
if (len(clean_amt) == len(exp_list)) and (len(exp_list) == len(clean_dates)):
    print(True)
else:
    print(False)


# In[39]:


exp_list[0:5]


# In[40]:


df = pd.DataFrame(exp_list, columns= ["protocol_name"])
df.head()


# In[41]:


df1 = pd.DataFrame(clean_dates, columns= ["date_of_attack"])
df1.head()


# In[42]:


df2 = pd.DataFrame(clean_amt, columns= ["amount_lost"])
df2.head()


# In[43]:


df=df.join(df1)
df.head()


# In[44]:


# Final DataFrame with all columns appended
# Special thanks to BeautifulSoup
df=df.join(df2)
df.head()


# In[45]:


# Converting dataframe data to Excel
# The data stored accounts for the rekt 2020-2021 leaderboard
df.to_excel('sena_rektnews_ws.xlsx', index=False)


# In[ ]:





# In[ ]:




