#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_csv("googlestore_review.csv")
data


# In[3]:


data.describe()


# In[4]:


data.info()


# In[6]:


data.isna().sum()


# In[8]:


data['Rating'].unique()


# In[9]:


data['Content Rating'].unique()


# In[12]:


x=data.drop(['Price','Rating'],axis=1)
y=data['Rating']
x


# In[13]:


y


# In[14]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=0)


# In[15]:


x_train


# In[16]:


y_train


# In[17]:


x_test


# In[18]:


y_test


# In[ ]:




