#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('bmi.csv')
df.head()


# In[3]:


df.describe()


# In[4]:


df.info()


# In[5]:


df.tail()


# In[6]:


df.isnull().sum()


# In[7]:


sns.displot(df['Age'],kde=True)


# In[12]:


df['Height'].mean()


# In[13]:


df['Height'].mode()


# In[17]:


print('{} is unique height in the dataset'.format(df['BmiClass'].unique()))


# In[18]:


df['Height'].value_counts().head(10).plot(kind='bar')


# In[21]:


df['BmiClass'].value_counts().plot(kind='pie')


# In[25]:


df['BmiClass'].value_counts()


# In[26]:


df['BmiClass'].value_counts().plot(kind='bar')


# In[ ]:




