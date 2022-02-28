#!/usr/bin/env python
# coding: utf-8

# In[18]:


import requests
import bs4
from bs4 import BeautifulSoup as bs
import pandas as pd
import time


# In[19]:


switch = True
def scrape():
    dataFrame = {'Hash' : [], 'Time' : [], 'BTC-value' : [], 'USD-value' : []}
    frame = pd.DataFrame(data=dataFrame)
    
    while switch == True:
        #get the data
        link = "https://www.blockchain.com/btc/unconfirmed-transactions"
        page = requests.get(link)
        soup = bs(page.content)
    
        numbers = soup.find_all("span", {'class' : 'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC'})
        hash = soup.find_all("a", {'class' : 'sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK'})


        #Make the arrays for the values we need
        hash_value = [content.get_text() for content in hash]
        time_value = [content.get_text() for content in numbers[0::3]]
        BTC_value = [content.get_text() for content in numbers[1::3]]
        USD_value = [content.get_text() for content in numbers[2::3]]

        #Make dataframe
        dataFrame = {'Hash' : hash_value, 'Time' : time_value, 'BTC-value' : BTC_value, 'USD-value' : USD_value}
        frame = pd.DataFrame(dataFrame)
        frame_complete = frame
        
        scrape.appendedDF = frame.append(frame_complete).drop_duplicates()
        frame = scrape.appendedDF
        
scrape()


# In[20]:


print(scrape.appendedDF)

#data cleaning
scrape.appendedDF['BTC-value'] = scrape.appendedDF['BTC-value'].map(lambda x: x.rstrip(' BTC'))
scrape.appendedDF['BTC-value'] = scrape.appendedDF['BTC-value'].str.replace(r'\,', '')

scrape.appendedDF['USD-value'] = scrape.appendedDF['USD-value'].map(lambda x: x.lstrip('$'))
scrape.appendedDF['USD-value'] = scrape.appendedDF['USD-value'].str.replace(r'\,', '')

scrape.appendedDF['USD-value'] = scrape.appendedDF['USD-value'].astype('float')
scrape.appendedDF['BTC-value'] = scrape.appendedDF['BTC-value'].astype('float')

#get the biggest transaction and write it
timestamps = scrape.appendedDF['Time'].unique()

f = open("transactions.txt", "w")
for timestamp in timestamps:
    BTC = scrape.appendedDF.loc[scrape.appendedDF['Time'] == timestamp, 'BTC-value'].max()
    series = scrape.appendedDF.loc[scrape.appendedDF['BTC-value'] == BTC]
    
    f.write(f" ----------- HIGHEST TRANSACTION OF {timestamp}  -----------")
    f.write("\n")
    for names in series.columns:
        if names != "Time":
            f.write(f"{names}: {series.iloc[0][names]}")
            f.write("\n")
    
    f.write("\n")

f.close()

