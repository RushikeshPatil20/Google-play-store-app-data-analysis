#!/usr/bin/env python
# coding: utf-8

# # Google Play Store Data Analysis

# #### ![Google-Play-Store-1280.jpg](attachment:Google-Play-Store-1280.jpg)

# ### Each app (row) has values for catergory, rating, size, and more. Another dataset contains customer reviews of the android apps

# ### Dataset will involve various step such as:
# - [Importing data](https://github.com/AlmaBetter-Project-TEam/Google-Play-Store-EDA)
# - Loading first Dataset:[Playstore](https://www.kaggle.com/gauthamp10/google-playstore-apps "Click Me here to View Dataset")
#   * DataCleaning (First Dataset:Playstore)
#   * Handling Outliers (First Dataset:Playstore)
#   * Beginining of Data Visualization of First Dataset : Playstore
# - Loading (Second Dataset:User Reviews)
#   * Data Cleaning (Second Dataset:User Reviews)
#   * Beginining of Data Visualization of Second Dataset : User Reviews
#   * Merging two Datsets (Playstore & User Reviews)
#   * Begining of Data Visualization of two Datsets (Playstore & User Reviews) 

# 
# 
# ## Importing libraries

# In[5]:


# Importing  various libraries required for data analysis 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import re
import plotly.express as px


# ### Loading dataset

# In[6]:


data = pd.read_csv('Google-Playstore.csv')


# In[ ]:




