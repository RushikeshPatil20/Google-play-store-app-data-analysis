#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import re
import plotly.express as px


# In[2]:


data = pd.read_csv('googleplaystore.csv')


# In[3]:


data.head(1)


# In[4]:


df=data.groupby('Category')


# In[5]:


df.describe()


# In[6]:


# Creating a function to convert the all size to kilobyte units
def convert_to_kilobytes(size):
#   Size colunm contains string like 'Varies with device' so lets assign 'nan' values to it
    if size == "Varies with device":
        return np.nan
#   If the data contains M it removes M convert it to float and convert it to kilobyte
    elif "M" in size:
        size = size.replace("M","")
        size = float(size)
        return round(float(size) * 1000, 2)
#   If the data contains K it removes k convert it to float 
    elif "k" in size:
        size = size.replace("k","")
        return round(float(size),2)
# Checking size conversion    
convert_to_kilobytes('456.6656545465M')


# In[7]:


data.Size=data.Size.apply(convert_to_kilobytes)


# In[8]:


data.head()


# In[9]:


df.describe()['Size']


# In[10]:


data.drop(10472,inplace=True)
data.shape


# In[11]:


df = data.groupby('Category')


# In[12]:


df.describe().transpose()


# In[13]:


data.isnull().sum()


# In[14]:


data.shape[0]


# In[15]:


data.loc[data["Size"].isnull()]


# In[16]:


# Storing the mean values of all the category
category_mean=data.groupby("Category").mean().sort_values("Size",ascending=False)["Size"]
# Printing the categories with there over all average
category_mean


# In[17]:


data.loc[data["Size"].isnull(),["Size"]] = data.loc[data["Size"].isnull()].apply(lambda X:round(category_mean[X["Category"]],2),axis=1)


# In[18]:


data.isnull().sum()


# In[19]:


data[data["App"].duplicated()]


# In[20]:


data.loc[data["Rating"].isnull()]


# In[42]:


def assign_random_values(feature):
    sample_length= data[feature].isnull().sum()
    sample_rating_value=data[~data[feature].isna()][feature].sample(sample_length)
    return (assign_random_values("Rating"))


# In[43]:


data.isnull().sum()


# In[23]:


data.loc[123]


# In[24]:


data.loc[124]


# In[25]:


category_mean=data.groupby("Category").median().sort_values("Rating",ascending=False)["Rating"]
round(category_mean,1)


# In[26]:


pattern=r'[+,]'
data.Installs=data.Installs.apply(lambda x: re.sub(pattern,'',x) )


# In[27]:


data.Installs=data.Installs.astype("int64")
data.Installs.dtype


# In[28]:


category_mean=data.groupby("Installs").mean().sort_values("Rating",ascending=False)["Rating"]
category_mean


# In[41]:


data.loc[data['Rating'].isnull()]['Rating']


# In[30]:


sample_length= data['Rating'].isnull().sum()
sample_length


# In[31]:


rating_nonull_index = data[~data['Rating'].isnull()]['Rating'].sample(sample_length)
rating_nonull_index


# In[32]:


actual_null_list=data[data['Rating'].isnull()]
actual_null_list


# In[37]:


rating_nonull_index.index=actual_null_list.index


# In[40]:


data.loc[data['Rating'].isnull()]['Rating']


# In[49]:


data.loc[113]


# In[ ]:




