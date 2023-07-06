#!/usr/bin/env python
# coding: utf-8

# In[1]:


#   Created by Elshad Karimov on 23/04/2020.
#   Copyright © 2020 AppMillers. All rights .

newTuple = ('a', 'b', 'c', 'd', 'e')
newTuple1 = tuple('abcde')
print(newTuple)


# In[2]:


print(newTuple1)


# In[3]:


# Access Tuple elements

print(newTuple[-5::2]) 


# In[4]:


#  Traverse through tuple

for i in newTuple:
        print(i)


# In[5]:


for index in range(len(newTuple)):
        print(newTuple[index])


# In[6]:


#  How to search for an element in Tuple?

print('a' in newTuple)


# In[10]:


def searchInTuple(pTuple, element):
        for i in pTuple:
            if i == element:
                return pTuple.index(i)
        return 'The element does not exist'

    
        print(searchInTuple(newTuple, 'a'))


# In[11]:


# Tuple Operations / Functions

myTuple = (1,4,3,2,5)
myTuple1 = (1,2,6,9,8,7)
print(myTuple + myTuple1)


# In[12]:


print(myTuple * 4)


# In[13]:


print(2 in myTuple1)


# In[14]:


myTuple1.count(2)


# In[15]:


myTuple1.index(2)


# In[16]:


x, y, z = (10,15,20,25,30,35,40)[0::3]
print(x,y,z)


# In[17]:


x, y = (y, x)[::-1]
print(x, y)


# In[ ]:




