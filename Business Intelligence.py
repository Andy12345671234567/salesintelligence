#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting

file_name = "train.csv"
df = pd.read_csv(file_name)

df.head()


# In[7]:


import plotly.express as px
import pandas as pd

example = df[['State', 'Sales']]
example_sales = df[['State', 'Sales']].groupby('State').sum()

fig = px.bar(example_sales, title="Long-Form Input")
fig.show()


# In[113]:


#Deleting the rows that are not useful 
#Row ID can be deleted / Country is unique, only united states / dont need product ID 
#Adjust headers 
#Ideas to get through
#1. How much sales are generated according to states?
#2  Which Region sells the most? 
#3. Which categories are being sold the most? 
#4. Which items are sold the most ? 
#5. Create a data frame for several shipment dates , howl ong it took to order and ship

#Potential buttons to put
#Time, from 2017 or something
#Region 
#Category 
#Segment

#Check for duplicates 
#There are duplicates 
df2 = df.pivot_table(index = ["Order ID"], aggfunc = 'size')

#Drop rows that are not useful
df = df.drop(['Row ID' , 'Country'], axis =1)
df


# In[114]:


#Getting Unique Values 

#Time, from 2017 or something [Widget bars]

#Region 
unique_regions = df['Region'].unique()
unique_regions

#Category 
unique_category = df['Category'].unique()
unique_category

#Segment
unique_segment = df['Segment'].unique()
unique_segment

#Sub-Category
unique_sub_category = df['Sub-Category'].unique()
unique_sub_category


# In[115]:


#1. How much sales are generated according to states? 

import matplotlib.pyplot as plt
df_sales = df.groupby('State').sum()
df_sales = df_sales.drop(['Postal Code'], axis = 1)

fig , ax = plt.subplots(figsize=(16,9))
df_sales = df[['State', 'Sales']].groupby('State').sum()
df_sales.plot(kind='bar', ax = ax)

plt.ylabel("Dollars")
plt.xlabel("American States")


# In[120]:


#2  Which Region sells the most? 

df_region = df.groupby('Region').sum()
df_region = df_region.drop(['Postal Code'], axis = 1)

fig , ax1 = plt.subplots(figsize=(16,9))
df_region = df[['Region', 'Sales']].groupby('Region').sum()
df_region.plot(kind='barh', ax = ax1)

plt.ylabel("Region")
plt.xlabel("Dollars")


# In[125]:


#3. Which categories are being sold the most? 

df_categories = df.groupby('Category').sum()
df_categories = df_categories.drop(['Postal Code'], axis = 1)

df_categories

fig , ax = plt.subplots(figsize=(16,9))
df_categproes = df[['Category', 'Sales']].groupby('Category').sum()
df_categories.plot(kind='barh', ax = ax)

plt.ylabel("Region")
plt.xlabel("Dollars")


# In[156]:


#4. Which items are sold the most, top 10 ?

df_product = df.pivot_table(index = ["Product Name"], aggfunc = 'size').sort_values(ascending=False)

fig, ax = plt.subplots(figsize = (16,9))
df_product.head(10).plot(kind='barh', ax = ax )


# In[160]:


#Getting top 10 list of items sold

server = app.server
product_names = df_product.index.tolist()
product_names[:10]

#Then getting to know how much each of them are sold for 


# In[ ]:




