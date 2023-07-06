#!/usr/bin/env python
# coding: utf-8

# In[1]:


#   Created by Elshad Karimov on 23/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Tuple Interview Questions



# Q-1. What will be the output of the following code block?

init_tuple = ()
print (init_tuple.__len__())


# In[2]:


# Q-2. What will be the output of the following code block?

init_tuple_a = 'a', 'b'
init_tuple_b = ('a', 'b')

print (init_tuple_a == init_tuple_b)


# In[3]:


# Q-3. What will be the output of the following code block?

init_tuple_a = '1', '2'
init_tuple_b = ('3', '4')

print (init_tuple_a + init_tuple_b)


# In[4]:


# Q-4. What will be the output of the following code block?

init_tuple_a = 1, 2
init_tuple_b = (3, 4)

[print(sum(x)) for x in [init_tuple_a + init_tuple_b]]


# In[5]:


# Q-5. What will be the output of the following code block?

init_tuple = [(0, 1), (1, 2), (2, 3)]
result = sum(n for _, n in init_tuple)

print(result)


# In[6]:


# Q-6. Which of the following statements given below is/are true?

# A. Tuples have structure, lists have an order.
# B. Tuples are homogeneous, lists are heterogeneous.
# C. Tuples are immutable, lists are mutable.
# D. All of them.


# In[7]:


# Q-7. What will be the output of the following code block?

l = [1, 2, 3]
init_tuple = ('Python',) * (l.__len__() - l[::-1][0])

print(init_tuple)


# In[8]:


# Q-8. What will be the output of the following code block?

init_tuple = ('Python') * 3

print(type(init_tuple))


# In[9]:


# Q-9. What will be the output of the following code block?

init_tuple = (1,) * 3
init_tuple[0] = 2
print(init_tuple)


# In[10]:


# Q-10. What will be the output of the following code block?

init_tuple = ((1, 2),) * 7
print(len(init_tuple[3:8]))


# In[ ]:




