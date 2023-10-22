#!/usr/bin/env python
# coding: utf-8

# # User Input

# In[1]:


name = input()


# In[2]:


name


# In[3]:


Age = input('Enter your age: ')


# In[4]:


Age


# In[5]:


type(Age)


# In[10]:


num1 = int(input('First number: '))
num2 = int(input('Second Number: '))


# In[11]:


num1+num2


# # Conditional Statements
# - if
# - else
# - elif

# In[12]:


userid = 'abc123'

if userid == 'abc123':
    print('Log in successful')   


# In[14]:


userid = 'abc1'

if userid == 'abc123':
    print('Log in successful')  
else:
    print('Try again')


# In[18]:


#Check whether the player is Virat kolhi
player_name = input('Enter players name: ')

if player_name == 'Virat':
    print('Yes')
else:
    print('No')


# In[21]:


#Check whether the number is positive/negative/Zero

number = int(input('Enter any number: '))

if number > 0:
    print('Positive')
elif number < 0:
    print('Negative')
else:
    print('Zero')


# In[4]:


name = "Sayali"


# In[7]:


print('Hi! How are you sayali?')
print('Hi How are you',name,'?')


# In[8]:


#Format

print(f"Hi ,how are you {name}?")


# - Take input from user, name, age, location,designation
# - Write this sentence: My name is 'name'. I am 'age' years old. I live in 'location'. I work as 'designation'

# In[12]:


name = input('Enter your name: ')
age = int(input('Enter your age: '))
location = input('Enter your location: ')
designation = input('Enter your designation: ')

#print('My name is',name,'I am ',age,'years old')
print(f"My name is {name}. I am {age} years old. I live in {location}.I work as {designation}")


# In[15]:


#Write python program which tell whether the person is eligible to do vote.
age = int(input('Enter your age: '))

if age >= 18:
    print('You are eligible')
else:
#     print('You are not eligible.You need to wait for',18-age,'years.')
    print(f"You are not eligible. You need to wait for more {18-age} years." )


# In[5]:


# Give grades based on percentages
#A : marks >85
#B : marks < 85 and >70
#C : marks <70 and > 60
#D 


# In[19]:


marks = int(input('Enter your marks: '))

if marks >= 85:
    print('A')
elif (marks < 85 and marks >= 70):
    print('B')
elif (marks < 70 and marks >= 60):
    print('C')
else:
    print('D')


# # In-Class Exercise:
# 
# 1. Write a program which will print Century if the player has made more than 100 runs else it shold write how many more runs he needs to have to complete the century.
# 2. Write a program to check the number is one digited, two digited and three digited.
# 3. Write a program to check whether the user has entered number 99 or not.

# In[21]:


runs = int(input('Enter runs: '))

if runs >= 100:
    print('Century')
else:
    print(f"You need to make more {100-runs} runs.")


# In[26]:


num = int(input('Enter any number: '))

if num < 10:
    print('One digited')
elif (num >= 10 and num <100 ):
    print('Two digited')
elif (num >=100 and num < 1000):
    print('Three digited')
else:
    print('Invalid')


# In[28]:


number = int(input('Enter number: '))

if number == 99:
    print('Yes')
else:
    print('No')

