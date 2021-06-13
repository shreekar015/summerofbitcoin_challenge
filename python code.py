#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pandas as pd


# In[38]:


df=pd.read_csv("mempool[1].csv")


# In[39]:


df.shape


# In[40]:


df.head()


# In[41]:


df.dtypes


# In[42]:


first_column = df. iloc[:, 0]


# In[43]:


a=list(first_column)


# In[44]:


for i in range(0,len(a)):
    print(a[i])


# In[ ]:





# In[45]:


for i in range(0,len(a)):
    file_object = open('block.txt', 'a')
    
    file_object.write(a[i])
    file_object.write("\n")
    
    file_object.close()


# In[ ]:




