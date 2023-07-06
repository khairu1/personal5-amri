#!/usr/bin/env python
# coding: utf-8

# In[1]:


#   Created by Elshad Karimov on 26/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved

# Dictionary Interview Questions


# Q-1. What will be the output of the following code snippet?

a = {(1,2):1,(2,3):2}
print(a[1,2])


# In[5]:


# Q-2. What will be the output of the following code snippet?

a = {'a':1,'b':2,'c':3}
print (a['a','b'])


# In[6]:


# Q-3. What will be the output of the following code block?

fruit = {}

def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1
        
addone('Apple')
addone('Banana')
addone('apple')
print (len(fruit))


# In[7]:


# Q-4. What will be the output of the following code block?

arr = {}
arr[1] = 1
arr['1'] = 2
arr[1] += 1

sum = 0
for k in arr:
    sum += arr[k]

print(sum)


# In[8]:


# Q-5. What will be the output of the following code snippet?

my_dict = {}
my_dict[1] = 1
my_dict['1'] = 2
my_dict[1.0] = 4

sum = 0
for k in my_dict:
    sum += my_dict[k]
    
print (sum)


# In[9]:


# Q-6. What will be the output of the following code snippet?

my_dict = {}
my_dict[(1,2,4)] = 8
my_dict[(4,2,1)] = 10
my_dict[(1,2)] = 12

sum = 0
for k in my_dict:
    sum += my_dict[k]

print (sum)
print(my_dict)


# In[10]:


# Q-7. What will be the output of the following code snippet?

box = {}
jars = {}
crates = {}
box['biscuit'] = 1
box['cake'] = 3
jars['jam'] = 4
crates['box'] = box
crates['jars'] = jars
print(len(crates[box]))


# In[11]:


# Q-8. What will be the output of the following code block?

dict = {'c': 97, 'a': 96, 'b': 98}

for _ in sorted(dict):
    print (dict[_])


# In[12]:


# Q-9. What will be the output of the following code snippet?

rec = {"Name" : "Python", "Age":"20"}
r = rec.copy()
print(id(r) == id(rec))


# In[13]:


# Q-10. What will be the output of the following code snippet?

rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id1 = id(rec)
del rec
rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id2 = id(rec)
print(id1 == id2)


# In[ ]:




