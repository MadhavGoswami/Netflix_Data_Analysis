#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_csv("file.csv")


# In[14]:


df.head()


# In[15]:


df.tail()


# In[16]:


df.shape


# In[17]:


df.size


# In[18]:


df.columns


# In[19]:


df.dtypes


# In[20]:


df.info()


# In[21]:


df.duplicated()


# In[22]:


df[df.duplicated()]


# In[23]:


df.drop_duplicates(inplace= True)


# In[24]:


df[df.duplicated()]


# In[25]:


df.shape


# In[26]:


df.isnull()


# In[27]:


df.isnull().sum()


# In[28]:


import seaborn as sns


# In[29]:


sns.heatmap(df.isnull())


# In[30]:


df[df['Title'].isin(['House of Cards'])]


# In[31]:


df[df['Title'].str.contains('House of Cards')]


# In[32]:


df['Release_Date']=pd.to_datetime(df['Release_Date'])


# In[33]:


df.head()


# In[34]:


df['Release_Date'].dt.year.value_counts()


# In[35]:


df['Release_Date'].dt.year.value_counts().plot(kind='bar')


# In[37]:


df.groupby('Category').Category.count()


# In[38]:


df['Year']=df['Release_Date'].dt.year


# In[39]:


df[(df['Category']=='Movie')& (df['Year']==2020)]


# In[40]:


df[(df['Country']=='India') & (df['Category']=='TV Show')]


# In[41]:


df[(df['Country']=='India') & (df['Category']=='TV Show')]['Title']


# In[42]:


df['Director'].value_counts().head(10)


# In[43]:


df[(df['Category']=='Movie')&(df['Type']=='Comedies') | (df['Country']=='Uniterd Kindom')]


# In[44]:


df2=df.dropna()


# In[45]:


df2


# In[46]:


df['Rating'].nunique()


# In[47]:


df['Rating'].unique()


# In[48]:


df[(df['Category']=='Movie')&(df['Rating']=='TV-14')& (df['Country']=='Canada')]


# In[49]:


df[['Minutes','Unit']]=df['Duration'].str.split(' ',expand=True)


# In[50]:


df.head(5)


# In[51]:


df.sort_values(by='Year').head(2)


# In[52]:


df.sort_values(by='Year', ascending=False).head(2)


# In[53]:


df[(df['Category']=='Movie')&(df['Type']=='Dramas')].head(2)


# In[ ]:




