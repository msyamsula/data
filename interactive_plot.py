#!/usr/bin/env python
# coding: utf-8

# In[11]:


import chart_studio.plotly as py #for plot
import pandas as pd #pandas
import numpy as np #numpy
import cufflinks as cf #cufflink to connect panda and python


# In[21]:


# use plotly offline
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
#make matplotlib immediately show result
get_ipython().run_line_magic('matplotlib', 'inline')


# In[22]:


init_notebook_mode(connected=True) # connect notebook to interactive js


# In[23]:


cf.go_offline() # offline mode cufflink


# In[24]:


df = pd.DataFrame(np.random.randn(100,4), columns='A B C D'.split(' '))
df


# In[25]:


data = {'Category':['A','B','C'],
       'Values':[11,23,45]}
df2 = pd.DataFrame(data)
df2


# In[28]:


df.iplot()


# In[33]:


df.iplot(kind='scatter', x='A', y='B', mode='markers') #scatter plot


# In[37]:


df2.iplot(kind="bar", x='Category', y='Values')


# In[49]:


df.count().iplot(kind='bar') # bar plot


# In[51]:


df.iplot(kind='box')


# In[60]:


data = {'x':[1,2,3,4,5], 'y': [10,20,30,20,10], 'z':[5,4,3,2,1]}
data
df3 = pd.DataFrame(data)
df3


# In[62]:


df3.iplot(kind='surface', colorscale='rdylbu')


# In[66]:


df['A'].iplot(kind='hist') #histogram for certain coloum
df.iplot(kind='hist') #histogram for all coloum


# In[67]:


df[['A','B']].iplot(kind='spread')


# In[70]:


df.iplot(kind='bubble', x='A', y='B', size='C') # bubble plot (scatter with size from another data)


# In[72]:


df.scatter_matrix() # only for all number data, can't have dataframe that is include non-numeric


# In[ ]:




