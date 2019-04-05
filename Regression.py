#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import math
import numpy as np
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# In[2]:


df = pd.read_csv("WIKI-PRICES.csv")
df = df[['adj_open','adj_high','adj_low','adj_close','adj_volume']]
df['HL_PCT'] = (df['adj_high']-df['adj_close']) / df['adj_close'] * 100.0
df['PCT_change'] = (df['adj_close']-df['adj_open']) / df['adj_open'] * 100.0

df = df [['adj_close','HL_PCT','PCT_change','adj_volume']]


# In[19]:


forecast_col = 'adj_close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.001*len(df)))
print(forecast_out)
df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
print(df.head())


# In[24]:


X = np.array(df.drop(['label'],1))
y = np.array(df['label'])
X = preprocessing.scale(X)
y = np.array(df['label'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

clf = LinearRegression(n_jobs=10)
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)

print(accuracy)


# In[ ]:




