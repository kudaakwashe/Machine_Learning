#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import math

df = pd.read_csv("WIKI-PRICES.csv")
print(df.head())


# In[13]:


df = df[['adj_open','adj_high','adj_low','adj_close','adj_volume']]
df['HL_PCT'] = (df['adj_high']-df['adj_close']) / df['adj_close'] * 100.0
df['PCT_change'] = (df['adj_close']-df['adj_open']) / df['adj_open'] * 100.0

df = df [['adj_close','HL_PCT','PCT_change','adj_volume']]

print(df.head())


# In[19]:


forecast_col = 'adj_close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
print(df.head())


# In[ ]:





# In[ ]:




