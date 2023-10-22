#!/usr/bin/env python
# coding: utf-8

# # Variables in Python
# - Variables acts as a container to store data in memory space.
# - Variables are pointer towards object in python
# - Variables can start with letters or underscore.
# - You cannot include special characters while creating a variable.
# 
# **Important points to remeber while creating a variable**
# 1. Python is case sensitive
# 2. If variable name involves more than 2 words, join those words with underscore.
# 3. Give meaningful name to variables

# In[1]:


#variable
10


# In[2]:


a = 10
a


# In[3]:


id(a)


# In[4]:


2name = 'Python'


# In[5]:


name2 = 'Python'
name2


# In[6]:


@name = 20


# In[7]:


#Single line comment


# In[8]:


age = 60 #age variable contains 60 value.
age


# In[9]:


#This is first session
#This is second session


# In[10]:


#Multi-line comment
'''This is first line  This is second line 
This is third line
This is fourth line'''


# # Data types in python
# 1. Integer
# 2. Float
# 3. String
# 4. Boolean

# In[11]:


#Integer
pin_code = 455156 
pin_code


# In[12]:


type(pin_code)


# In[13]:


temp = 25.2
type(temp)


# In[14]:


logical = True
type(logical)


# In[15]:


#String creation


# In[16]:


a = 50
a = 100
a


# In[17]:


s = 'We are learning python'
s1 = "We are learning python"
s2 = '''We are learning python'''


# In[18]:


s==s1


# In[19]:


s==s2


# In[20]:


st = 'It's a laptop'


# In[21]:


st = "It's a laptop"
st


# In[22]:


st1 = 'It"s a laptop'
st1


# # Typecasting
# 
# - Typecasting is used to change the data types.

# In[23]:


age
type(age)


# In[24]:


x = str(age)
type(x)


# In[25]:


int(x)


# In[26]:


float(age)


# In[27]:


age


# In[28]:


bool(-5)


# In[29]:


zero = 0

bool(zero)


# In[30]:


#We can convert any type of values to bool type, and the output for all values will be True , 
#Except 0, which is False


# # String methods

# In[31]:


#Create a string
s


# In[32]:


#Capitalize function


# In[33]:


s1 = 'we are learning python'
s1.capitalize()


# In[34]:


s.capitalize()


# In[35]:


#Count


# In[36]:


s.count('a')


# In[37]:


s.count(' ')


# In[38]:


# Starts with and endswith function


# In[39]:


s


# In[40]:


s.startswith('we')


# In[41]:


s.endswith('n')


# In[42]:


s.endswith('N')


# In[43]:


#Find


# In[44]:


s


# In[45]:


s.find('learning')


# In[46]:


s.find('We')


# In[47]:


#Replace 


# In[48]:


s


# In[49]:


s.replace('We','They')


# In[50]:


s


# In[51]:


s = s.replace('We','They')


# In[52]:


s


# In[53]:


#Basic functions 


# In[54]:


s.upper()


# In[55]:


s.lower()


# In[56]:


s


# # Data Structures
# 1. Lists
# 2. Tuple
# 3. Dictionary
# 4. Sets

# **Lists**
# 
# - Lists are the built in data structures in python.
# - Lists are heterogenous data structure.
# - Lists are mutable.

# In[57]:


#Creating lists


# In[58]:


lst = []
type(lst)


# In[59]:


lst = [10,10.2,True,'Python']
lst


# In[60]:


#append


# In[61]:


lst.append(False)


# In[62]:


lst


# In[63]:


lst.append('R')


# In[64]:


lst


# In[65]:


#Count 


# In[66]:


lst.count('R')


# In[67]:


#Index
lst.index('Python')


# In[68]:


lst.index('R')


# In[69]:


#Insert


# In[70]:


lst


# In[71]:


lst.insert(0,1000)


# In[72]:


lst


# In[73]:


lst.insert(3,'Analyst')


# In[74]:


lst


# In[75]:


#pop


# In[76]:


lst.pop()


# In[77]:


lst


# In[78]:


#remove


# In[79]:


lst.remove(10.2)


# In[80]:


lst


# **Tuple**
# 
# - Tuples are ordered and heterogenous data structure.
# - Tuples are immutable.

# In[81]:


#Create a tuple


# In[82]:


t = ()
type(t)


# In[83]:


t = (10,5.5,True,'python')
t


# In[84]:


t.count(5.5)


# In[85]:


t.index(True)


# In[86]:


#Accessing elements from tuple


# In[87]:


t


# In[88]:


t[1]


# In[89]:


t[3]


# **Dictionary**
# 
# - Python dictionaries are ordered collection of items.
# - Dictionary is mutable data structure.
# - It has key and value pair.

# In[90]:


#Creating an empty dictionary


# In[91]:


dictionary = {}
type(dictionary)


# In[92]:


#Adding elements in a dictionary


# In[93]:


dictionary = {
    'Name':'ABC',
    'Age' : 25,
    'Location' :'Pune',
    'Course': 'DS'
}


# In[94]:


dictionary


# In[95]:


#get


# In[96]:


dictionary.get('Name')


# In[97]:


dictionary.get('Course')


# In[98]:


#items


# In[99]:


dictionary.items()


# In[100]:


#keys


# In[101]:


dictionary.keys()


# In[102]:


#Adding values in dictionary(update)
dictionary.update({'Date':2023})


# In[103]:


dictionary


# In[104]:


dictionary.update({'Subject' : 'ML','Month':'July'})


# In[105]:


dictionary


# In[106]:


dictionary['Name']


# In[107]:


dictionary['Name'] = 'XYZ'


# In[108]:


dictionary


# In[109]:


dictionary['Month'] = 'Aug'


# In[110]:


dictionary


# In[111]:


dictionary.pop('Subject')


# In[112]:


dictionary


# In[113]:


dictionary.pop('Date')


# **Set**
# 
# - Set is a collection which is unordered,unindexed.
# - Set is immutable.
# - Sets are unordered, so you cannot be sure in which order the items will appear.
# - Sets do not allow duplicate values.
# - Once a set is created, you cannot change its items, but you can remove items and add new items.
# - As sets are unordered, they do not support indexing and slicing operations.

# In[114]:


lst = [10,10,10,10,12,15]
lst


# In[115]:


#Does not allow duplicate items
s1 = {10,10,10,20,30,40,50}


# In[116]:


s1


# In[117]:


#Does not support indexing


# In[118]:


s1[4]


# In[ ]:


#Add
s1.add(60)


# In[119]:


s1


# In[120]:


#pop


# In[121]:


s1.pop()


# In[122]:


s1

