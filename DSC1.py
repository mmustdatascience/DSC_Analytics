#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd# For data processing e.g loading csv file
import matplotlib.pyplot as plt# for data visualization
import seaborn as sns# for data visualization 


# In[3]:


df=pd.read_csv('vgsales.csv')
df


# In[4]:


df.info()


# In[6]:


table_sales=pd.pivot_table(df,values=['Global_Sales'],index=['Year'],columns=['Genre'],aggfunc='max',margins=False)#arranging years 

plt.figure(figsize=(19,16))
sns.heatmap(table_sales['Global_Sales'],linewidths=.5,annot=True, vmin=0.01 ,cmap='PuBu')
plt.title('Max Global Sales of games')
plt.show()


# In[9]:


def top(vgs ,n=1,columns='Global_Sales'):#creating a function top 
    return vgs.sort_values(by=columns)[-n:]#sorting values
df.groupby(['Year'], group_keys=False).apply(top)[['Year','Name','Global_Sales','Genre','Platform','Publisher']]
     #to group columns at the top starting with year   


# In[10]:


df.groupby(['Name'])['Global_Sales'].sum().sort_values(ascending=False)[:40]


# In[11]:


df.head()


# In[22]:


df.drop('NA_Sales', axis=1,inplace=True)#to drop a column


# In[23]:


df.head()


# In[24]:


#Size of the dataframe
len(df)


# In[25]:


#to explore data
df.describe()


# In[26]:


#how to replace or change the value of a string of a column to an int
df['Platform']=df['Platform'].map({'Wii':1,'NES':0})
df.head()


# In[29]:


plt.hist(df['Platform'])#Drawing a histogram
plt.title('Platform(Wii=1,NES=0)')
plt.show()


# In[30]:


df=pd.read_csv('vgsales.csv')
df


# In[ ]:




