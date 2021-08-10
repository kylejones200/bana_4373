#!/usr/bin/env python
# coding: utf-8

# # Summary
# 
# Getting started is the hardest part of learning Python. This is the first lesson in a series of tutorials designed to introduce Python as a programming language and how it can be used for business analysis. 
# 
# After completing this tutorial, you will know:
# * The overall structure of Python as a programming language
# * How to do basic operations like addition and subtraction
# * The various data types available in Python
# * How to use loops and conditional statements
# 
# ## When to use Python
# 
# Some use cases for Python:
# * Automating repetative tasks
#  * Combining PDFs
#  * Searching for text in files
#  * Downloading information from the internet
#  * Merging/updating spreadsheets
#  * Sending emails
#  * Aggregating multiple data sources
# * Data Analysis
#  * Creating reproducible analyses and reports
#  * Making visualizations and graphics
#  * Interacting with databases and using SQL
#  * Statistical analysis
#  * Transforming data (e.g. pivot/filter/summarize)
# * More advanced use cases
#  * Creating web pages
#  * Machine learning / AI
#  * Manipulating images / sound
# 
# Let’s get started.

# # Tutorial Overview
# This tutorial is divided into 5 parts:
# 1. Introduction to Python
# 2. Basic Operations
# 3. Data Types
# 4. Flow Control
# 5. Exercises: Your turn!

# # Introduction to Python
# 
# Python is a free open source scripting language. It is used for a wide range of tasks including website development and data analysis.
# 
# Python is an "object oriented" language which means that the basic unit of everything in Python is an object. We manipulate objects with methods or functions. An object could be a sentence, a list of numbers, an image, a spreadsheet, or something else. 
# 
# Python is a multi-purpose programming language. It has been called the "second-best language for everything." For example, R is better than Python for many statistics-focused tasks and JavaScript is better for web development than Python. However, if you only learn one language - Python is the best option. 

# ## How to use Python
# 
# Python is free and open source, but most people work with Python through an Integrated Development Environment (IDE). This project is built in a Jupyter Notebook. This is just an interface for writing Python code. Some people prefer other interfaces such as PyCharm, Visual Basic Studio, or Spyder. 
# 
# Amazon SageMaker uses Jupyter Notebooks. 

# ## Comments in code
# 
# The hash sign is used for comments in Python. Anything following a hash sign will not be executed. 
# 
# You can also create a block of comments using triple quotation marks. In Python, you can use one quote mark or the double quote mark - so long as you are consistent.

# In[1]:


# https://github.com/rajathkmp/Python-Lectures


# In[2]:


# jupyter notebooks are an interface for writing python code
# it is NOT a website
'''
here is comment 
another comment 
'''


# # Basic Operations 

# In[3]:


print('Hello World')


# ### Assign values to variables

# A single equal sign is used to assign a value to an object.
# 
# Two equal signs in a row is used to test equality. 

# In[4]:


x = 2
y = 5

x+y


# ### Test if two variables are equal

# In[5]:


x==y


# # Data Types

# ## Numbers
# Integers and floating point numbers can be used interchangeably (in general)

# In[6]:


val_int = 5
val_float = 5.0

print('The type of {0} is {1}'.format(val_int, type(val_int)))
print('The type of {0} is {1}'.format(val_float, type(val_float)))


# ## Strings
# A sting is a list of characters. It can be a random list of characters or words and sentences. There are special methods we can apply to strings such as manipulating the case or finding a letter. 

# In[7]:


a = 'Hello World'


# In[8]:


a.upper()


# In[9]:


# This will return the position of the letter 'W'. In Python (and most computer languages) counting begins with 0

a.find('W')


# ## Lists
# An object that stores any type of object in order. This is the storage structure to use most often. The list doesn't have to be the same kind of object. You can mix intergers, floats, and strings. However, lists are often used for computation in which case you want all the objects in a list to be the same. 

# In[10]:


mylist = [3,6,1,6,3,7,3,7,3,99,3,'alpha']
mylist


# In[11]:


# select 10th item (note 0-indexed)
mylist[9]


# In[12]:


# slicing list 
mylist[3:8]


# In[13]:


list(range(10))


# In[14]:


sum(list(range(10)))


# In[15]:


# this will throw an error.  Why doesn't it work?
sum(mylist)


# ### Exercise: 
# - Create a list of names of a few people on your team
# 
# - Print the value of the first and third names in the list
# 
# - Test if those two values are equal to each other (they are probably not)

# In[ ]:


### CODE FOR ABOVE EXERCISE ###




# ## Dictionaries
# Dictionaries are key-value storage. Each item has a key (before the colon) and a value (after the colon). It can be used to store alias names, related objects, or even functions. Python uses dictionaries extensively but at the beginning these can be tough to use. 

# In[16]:


currency_map = {
    'Canada': 'CAD', 
    'US': 'USD', 
    'United Kingdom': 'GBP', 
}

currency_map


# In[17]:


currency_map['Canada']


# In[18]:


currency_map['China'] = 'CN'


# In[19]:


currency_map['China']


# In[20]:


restaurant_rating = {
    "fast": 0,
    "Italian": 3,
    "Tex-Mex": 5
}


# In[21]:


# By convention, we use k for the dictionary key and v for the dictionary value

for k, v in restaurant_rating.items():
    print("I give {k} food a rating of {v}".format(k=k, v=v))


# ### Exercise:
# - What is the currency code for the United Kingdom? Print it.
# 
# - Add a key-value pair to the dictionary that maps Japan to its currency (JPY)
# 
# - Print the currency code for Japan.

# In[ ]:


### CODE FOR ABOVE EXERCISE ###




# # Control Flow

#  ## IF Statement
# Notice the indentations (tabs) after the "if" and "else" lines.  Tabs are important in Python as their placement often affects how code is executed.  In an if statement, the tabs determine when the if/else sections end.

# In[22]:


x = 12
if x > 10:
    # this code is executed only if the condition is True
    print("hello")
else:
    # otherwise, this code is executed
    print("world")


# ## For Loop

# In[23]:


mylist = [3,6,1,6,3,7,3,7,3,99,3,'alpha']

for e in mylist:
    # this code executes multiple times, once for each element in the list
    # on each iteration, the variable e changes to the next value
    print(e)


# ## List Comprehensions
# 
# List comprehensions are a convention in Python that allows us to avoid writing loops or conditions. 

# In[25]:


# The above condition could be written as a list comprehension this way
x = [12]
print("{word}".format(word = ["hello" if x > 10 else "world" for x in x]))

# The For Loop would be written this way
mylist = [3,6,1,6,3,7,3,7,3,99,3,'alpha']
print("{item}".format(item = mylist))


# ## Functions
# Tabs are important again here.  Functions are defined based on the lines of code that are indented below the "def" line.

# In[26]:


def firstfunc():
    print("Hello World!")
    print("This is my first function.")


# In[27]:


firstfunc()


# In[28]:


def times(x,y):  # variables inside parenthesis are the "parameters"
    z = x*y
    return z

# note that x and y are defined local to function (in its "scope")


# In[29]:


# Why does this line error?
a = times()


# In[30]:


# run the function and capture the value it returns by assigning it to the variable c
c = times(4,5)
print(c)


# # Exercises: Your Turn!
# 
# 1) Create a string variable of your name and call it "name"

# In[ ]:





# 2) Use a slice (square bracket notation [a:b]) on the string "name" to print only your first name

# In[ ]:





# 3) Create a list, named "num", of numbers between 1 and 10, inclusive

# In[ ]:





# 4) Calculate the sum of all numbers in "num" 

# In[ ]:





# 5) Create a function called "sum_numbers" that returns the sum of the numbers in a list 
#     (hint 1: parameter should be the list)
#     (hint 2: make sure you are returning the value, not just printing it)

# In[ ]:





# 6) Print only the even numbers in num 
#     (hint: calculate remainder with '%')

# In[ ]:





# 7) Create a function "product" that finds the product of all numbers in a list

# In[ ]:





# # Extensions
# 
# This section lists some ideas for extending the tutorial that you may wish to explore.
# * Think of some of your recent job tasks. Would Python have helped with those tasks?

# # Further Reading
# This section provides more resources on the topic if you are looking to go deeper.
# 
# ## Books
# * Python for Data Analysis, by William McKinney. http://shop.oreilly.com/product/0636920023784.do
# * Python Data Science Handbook, by Jake VanderPlas. https://jakevdp.github.io/PythonDataScienceHandbook/
# * Data Science from Scratch in Python, by Joel Grus. https://github.com/joelgrus/data-science-from-scratch
# * Automate the boring stuff, by Al Sweigart. https://automatetheboringstuff.com/
# 
# ## Additional Tutorials
# * Python for Finance classes (covers beginner to intermediate). http://www.financeandpython.com/default.html
# * Programming Historian (range of trainings for Python, R, and other languages). https://programminghistorian.org/en/
# * Free training is available from a number of online groups, including: 
#  * [Udacity: Intro to Data Analysis](https://www.udacity.com/course/intro-to-data-analysis--ud170)
#  * [LinkedIn Learning: Python: Data Analysis](https://www.linkedin.com/learning/python-data-analysis-2)
#  * [Codeacademy](https://www.codecademy.com/catalog/language/python)
# * Other notebooks that introduce Python and Jupyter
#  * [Python for Quantitative Economics](https://python-programming.quantecon.org/)
#  * [Python for Science](https://github.com/barbagroup/Caminos/blob/master/2--Python_for_Science.ipynb)
#  * [Core Python Programming Concepts](https://github.com/kthyng/python4geosciences/blob/master/materials/1_core.ipynb)

# # Summary
# 
# In this tutorial, you were introduced to the Python programming language. Specifically, you learned:
# * The structure of Python as a programming language
# * How to do basic operations like addition and subtraction
# * The various data types available in Python
# * How to use loops and conditional statements

# # Next
# 
# In the next section, you will Python to do basic data analysis with the Pandas Library. 
