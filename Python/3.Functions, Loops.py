#!/usr/bin/env python
# coding: utf-8

# # Functions
# - In python, there are two types of function.
#     - Built-in funtions
#     - User defined function
# - We can create our own customized functions in python for code reusability.

# In[1]:


#Basic Function


# In[2]:


def simple_function():
    print('This is user defined function')   


# In[3]:


simple_function()


# In[4]:


#Docstring


# In[5]:


def function1():
    '''This function will print 2 sentences.'''
    print('This is first sentence')
    print('This is second sentence')


# In[6]:


function1()


# In[7]:


function1()


# In[8]:


#Write a python function which will return me the maximum number
def max_number(num1,num2):
    '''This function returns max number between given two number'''
    return max(num1,num2)


# In[9]:


def max_number(a,b):
    if a>b:
        return a
    else:
        return b


# In[10]:


max_number(5,5)


# In[11]:


max_number(10,15,20)


# In[12]:


def max_num1(*numbers):
    return max(numbers)


# In[13]:


max_num1(10,5,20,50,46,85,94,52,31,1000)


# In[14]:


def combine(text1,text2):
    print(text1+' '+text2)


# In[15]:


combine('Python','Language')


# In[16]:


combine('R','Python','Langauge')


# In[17]:


s = 'Python'
s[::-1]


# In[18]:


def reverse(text):
    return text[::-1]


# In[19]:


reverse('Sayali')


# - Create a python function which will take 4 arguments(Id,name, age and department) of employee and it should print the below sentence:
#     - Employee ID is 'Id'.The name of employee is 'name'.He is 'age' years old and he is from 'department' department.
#  

# In[20]:


def info(Id,name,age,department):
    print(f"Employee ID is {Id}.Name of the employee is {name}.He is {age} years old and he is from {department} department")


# In[21]:


info(101,'ABC',25,'HR')


# In[22]:


def info(Id,name,age,department):
    print(f"Employee ID is {Id}\nName of the employee is {name}\nHe is {age} years old\nHe is from {department} department")


# In[23]:


info(101,'ABC',25,'HR')


# # Loops
# 
# 1. While Loop 
# 2. For loop

# In[24]:


#While loops


# In[25]:


python = 10

while python > 0:
    print('Learning python',python)
    python = python - 1
print('Python completed')


# In[26]:


age = 0

while age < 18:
    print('Not eligible')
    age = age + 1
    
print('Eligible')


# In[27]:


#range function
list(range(1,20))


# In[28]:


list(range(1,21,2))


# In[29]:


list(range(0,21,2))


# In[30]:


#For loop


# In[31]:


lst = [1,2,3,4,5]


# In[32]:


for i in range(1,100):
    print(i)


# In[33]:


lst1 = [10,20,30,40]
lst1


# In[34]:


lst1.append(50)


# In[35]:


lst1


# In[36]:


lst = []

for i in range(1,100,2):
    lst.append(i)


# In[37]:


for x in range(1,10):
    print(x**2)


# In[38]:


#Company list
company = ['flipkart','amazon','excelr']
company


# In[39]:


for i in company:
    print(i)


# In[40]:


for i in company:
    print('www.'+i+'.com')


# # In-Class Activity:
# 
# 1. Write a program to store all names which starts with 'A' in a list.
# 2. Take a list of numbers and add 5 to each number.
# 3. Create a list of marks and print only marks > 75.

# In[41]:


names = ['Aisha','Ameya','Nikita','Arya','Pooja']
names


# In[42]:


for i in names:
    if i.startswith('A'):
        print(i)


# In[43]:


for i in range(1,10):
    print(i+5)


# In[44]:


marks = [41,54,85,98,75,85,65]

for i in marks:
    if i >= 75:
        print(i)

