#!/usr/bin/env python
# coding: utf-8

# # Getting to know Pandas 
# 
# Pandas can be as simple or as complex as you need it to be. As an analysis toolkit, it's designed to be flexible and provide a wide range of functionality so that the same tool can be used for a variety of tasks. Because of this, it can be a little overwhelming at first. In this notebook we will introduce some of the essential pandas functionality and list a few best practices that will make learning pandas easier as you go.
# 
# By now, you should be comfortable with:
# 
# * Reading in a CSV file
# * Inspecting the first five rows of your data
# * Selecting columns / filtering rows
# * Creating new columns from existing columns
# 
# If not, please review [AFU PDA 2 - Pandas basics](./AFU PDA 2 - Pandas basics.ipynb)
# 
# ## What's covered here
# 
# In this notebook you will learn:
# 
# * Basic indexing and working with dates
# * Reading data from multiple sources
# * Merging data (joins/vlookup)
# * Groupby, pivot_table, transform, melt
# 
# Along the way, you will also learn pandas best practices in how to write your code. For further reading on mastering pandas syntax, [Minimally sufficient Pandas](https://medium.com/dunder-data/minimally-sufficient-pandas-a8e67f2a2428) is an excellent resource.

# # Tutorial Overview
# This tutorial is divided into 4 parts:
# 
# * Test your knowledge
# * Basic indexing
# * Slicing, merging, and grouping data
# * Exercises: Your turn!

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.expand_frame_repr", False)
pd.set_option("display.width", 160)

get_ipython().run_line_magic('matplotlib', 'inline')


# # Test your knowledge
# Before starting, try to complete the excercise below. This tests your knowledge on topics covered in [AFU PDA 2 - Pandas basics](./AFU PDA 2 - Pandas basics.ipynb)
# 
# Step 1: Choose a file to load

# In[2]:


# we want to load the sales_fake.csv in the Support_Files directory
directory = 'data/'
## START YOUR CODE HERE
file_name = 'sales_fake.csv'
## END YOUR CODE HERE
path = directory + file_name

# check to make sure you have the right path
print(path)


# Step 2: Read your file into a pandas data frame and view the top 5 rows

# In[3]:


# remember, pandas has built-in methods for reading data. 
# If you can't remember which one to use, try pd.read<TAB> to view the available methods

## START YOUR CODE HERE
# read the csv
df = 
# view the top 5 rows
# remember, each dataframe also has built-in methods for working with the data.
# if you can't remember which one to use, try df.<TAB> to view the available methods
df
## END YOUR CODE HERE


# # Basic Indexing
# 
# Pandas dataframes are a collection of rows and columns, organized by an index. The index is analogous to row numbers in excel or primary keys in SQL. Understanding and working with indexes allows us to easily filter, group, and manipulate our data. Additionally, pandas understands different types of indexes. Most notably, pandas has a DatetimeIndex which makes working dates very easy.
# 
# To begin, we will read in some data, inspect the index and set a new index. After that, we will explore the functionality with our new index

# In[ ]:


# use the same file from before
df = pd.read_csv(path)


# In[ ]:


print("What type of index?")
print("-> ", df.index, "\n")

print("Inspect some values:")
print("-> ", df.index.values, "\n")

# show the first 5 rows
df.head()


# If I know the index, I can pull rows by their index

# In[ ]:


print(df.loc[3])


# Or I can pull a whole range using `START:END` notation. This is known as "Slicing". For `[1:3]`, this means start index 1 and go up to 3 but don't include 3.

# In[ ]:


print(df.loc[1:3])


# An integer index alone isn't particularly useful, so lets set a datetime index. Before we do that, we need to first understand data types in Python.
# 
# Basic data types are `float`, `integer`, `string`. A more advanced data type that python understands is `datetimes`. This is similar to programs like excel which will automatically try to detect a date column and treat it differently than a string or an integer.
# 
# Lets look at the data types in our current dataframe:

# In[ ]:


df.dtypes


# An object in python generally refers to a string or anything else that python wasn't able to automatically detect. As you can see, order_day and order_week are objects but we would like them to be dates.

# In[ ]:


# make a list of columns you want to change
columns_to_change = ['order_day', 'order_week']

# go through each column and update its dtype using pandas built-in function
for column in columns_to_change:
    df[column] = pd.to_datetime(df[column])

# check the output
df.dtypes


# In[ ]:


# this gets me a whole new set of methods related to dates
new_dt_column = df['order_day']
new_dt_column.dt.weekday_name[:5]


# Now we have a column that pandas understands is a date. If you notice, our date column also matches our index, so instead of using the row index, let's index our data frame by date

# In[ ]:


df = df.set_index('order_day')
df.head()


# Now, instead of a row number, we have a date for our index. Let's revisit our index methods

# In[ ]:


# get data for a particular date
print(df.loc['2017-01-15'].head())
# get data for a slice
print(df.loc['2017-02-15':'2017-02-20'].head())
# get data for a month
print(df.loc['2017-07'].head())


# Now that our index knows about dates, we easily get some calendar view. For example, lets look at units by Month and Quarter:

# In[ ]:


print(df.resample('Q')['units'].sum()) 
print(df.resample('M')['units'].sum())


# # You try!
# 
# Using the same dataframe above (you can make sure it's there by running all the cells up til now), complete the following questions to test your understanding:
# 
# Step 1: create a new dataframe using the date index

# In[ ]:


# filter to data for November and December and save it to a new df called nov_to_dec
nov_to_dec = 

nov_to_dec.head()


# Step 2: Re-index your new data frame by product_family

# In[ ]:


# hint: nov_to_dec.<TAB> will show you the available methods
nov_to_dec_reindexed = 

nov_to_dec_reindexed.head()


# Step 3: Get the data only for "Consumables"

# In[ ]:


# hint: remember, df.loc lets you grab data by index label
nov_to_dec_consumables = 

nov_to_dec_consumables.head()


# Step 4: Sum units in nov_to_dec_consumables and divide it by all units in nov_to_dec. This tells you what percentage Consumables was of all product families in November and December

# In[ ]:


total_consumables_nov_to_dec = 


# In[ ]:


# hint: we still have a dataframe indexed by date, nov_to_dec. Try using that
total_units_nov_to_dec = 


# In[ ]:


# run this cell

print(
    "Consumables were {:.1%} of all units From November to December.".format(
        total_consumables_nov_to_dec / total_units_nov_to_dec
    )
)


# Normally, this isn't how you would go about getting an answer like this using pandas, but it does demonstrate how to easy it is to work with data using slices and indexes. We could have accomplished the same thing using special functions, filtering, or groupby's. Groupby is what we will cover next!

# # Groupby's and aggregations
# 
# In the last example, we used resample to sum over units to see aggregations by different calendar dimensions. This highlights one of pandas most powerful features: **GroupBy**'s and **Aggregations**.
# 
# GroupBy's provide a very flexible way to organize your data and Aggregations create summary views. GroupBy/Aggregate in pandas is much like pivot tables in excel, with lots of extras on top. Pandas also includes `pivot_table`, `melt`, and `transform` methods for shaping data. If interested, we cover those in more depth in [AFU PDA 3 - Pandas - Groupby, pivot_table, transform and melt](./AFU PDA 3 - Pandas - Groupby, pivot_table, transform and melt.ipynb)
# 
# At a high level, a GroupBy is a logical way to split your data and then apply some operation to each split before returning the results. This is known as Split-Apply-Combine:

# <img src='img/split-apply-combine.PNG'>

# To get the sum of units and OPS by each product_family, first create a groupby object (this is similar to a dataframe, except broken up into chunks as in the picture above).  Then, pick the columns you want to aggregate (units and ops in this case) and apply the .sum() method.  Pandas will automatically aggregate each product family "chunk" and combine them into a single dataframe.
# 
# GroupBy is one of panda's most versatile features. Be sure to checkout panda's documentation on [Split-Apply-Combine](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html)

# In[ ]:


sales_by_product_family = df.groupby('product_family')[['units', 'ops']].sum()
print(sales_by_product_family)


# In SQL, this is equivalent to:
# 
# `SELECT
#     product_family
#     ,SUM(units) AS units
#     ,SUM(ops) AS ops
# FROM
#     df
# GROUP BY
#     product_family
# ;`

# The above example involves using the .sum() method on a groupby object, but there is a more general approach that we recommend, using .aggregate().  In Python, and especially Pandas, there are many different ways to perform the same operation, and .aggregate() is a versatile method that can help narrow down your options.

# In[ ]:


sales_by_product_family = df.groupby('product_family')[['units', 'ops']].aggregate('sum')
print(sales_by_product_family)


# This is particularly helpful if you want to use different aggregate functions for different columns, which you'll see in the next couple of examples.

# Next, let's look at gl units by quarter, using the .resample() method:

# In[ ]:


gl_by_qtr = df.groupby(['gl'])[['units','ops']].resample('Q').sum().head(n=12)
gl_by_qtr


# Let's look at a more general case without using resample:

# In[ ]:


column_list = ['product_family']
aggregations = {'units':['sum','mean'],'ops':['min','max']}

df.groupby(column_list).aggregate(aggregations)


# In[ ]:


def summarize_data(df, cols, aggs):
    return df.groupby(cols).aggregate(aggs)

column_list = ['product_family', df.index.quarter]
aggregations = {'units':['min','max'],'ops':['sum','mean']}

summarize_data(df, column_list, aggregations)


# # Pivot a dataframe using the .pivot_table() function

# Just as in Excel, we can pivot our data, which typically involves swapping rows with columns and applying an aggregate function:

# In[ ]:


df_pivot = pd.pivot_table(data=df, index=df.index, columns='product_family', values='units', aggfunc='sum')
df_pivot.head()


# Here, the "index" argument determines the row grouping (just like "rows" in an Excel pivot table).  The "columns" and "values" arguments are also the same as their Excel counterparts.

# Note: a dataframe's columns can have indices just like its rows can.  An unintended consequence of using .pivot_table() is that it adds an index to the new dataframe's columns, so we'll use the line below to undo this:

# In[ ]:


df_pivot.columns = list(df_pivot.columns)


# # Unpivot a dataframe using the .melt() function

# Now we'll essentially undo the pivot transformation we just applied. Reversing a pivot is difficult in Excel, but it's one line in Pandas with .melt(). This function doesn't work very well with indices, so first we'll reset the order_day index so it becomes a column again:

# In[ ]:


df_pivot = df_pivot.reset_index()
df_pivot.head()


# In[ ]:


df_unpivot = pd.melt(frame=df_pivot, id_vars=['order_day'], value_name='units', var_name='product_family')

# then set the index back to order_day
df_unpivot = df_unpivot.set_index('order_day')

df_unpivot.head()


# We have now unpivoted product_family so it is a column again.  Keep in mind we could have done this all in one line, including resetting and setting the index, but we broke it out into steps for illustration.

# # Exercises: You try!

# 1) What is the GL with the highest OPS? (_hint:_ you can use the df.groupby(cols).aggregate({} syntax)

# In[ ]:





# 2) What percentage of the Consumables OPS does Amazon Pantry have?

# In[ ]:





# 3) What date had the highest total OPS?

# In[ ]:





# 4) Create pivot table of OPS with gl as the row headers and order_day as the columns

# # Combining multiple data sets with pandas using Merge

# In[ ]:


import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')

# define variables as much as possible
# this makes your code more re-usable and readable
# remember, a variable is where a value is stored, a string is the value
# file_path: variable to tell me where to find the file
# holidays_url: url for a list of holidays on github

holidays_url = 'https://gist.githubusercontent.com/shivaas/4758439/raw/'


# In[ ]:


# show reading a file without a header
holidays = pd.read_csv(holidays_url)
holidays.head()


# In[ ]:


# passing in the file names 
holidays = pd.read_csv(holidays_url, header=None, names=['date','holiday'])

# add in holiday date types
holidays.head()
holidays.dtypes


# In[ ]:


holidays['date'] = pd.to_datetime(holidays['date'])
holidays = holidays.set_index('date')


# In[ ]:


sales_data_with_holidays = pd.merge(df, holidays, right_index=True, left_index=True, how='left')


# In[ ]:


# sales_data_with_holidays['holiday'] = sales_data_with_holidays['holiday'].fillna('No holiday')
sales_data_with_holidays.columns


# In[ ]:


sales_data_with_holidays[~sales_data_with_holidays['holiday'].isnull()].head()


# # Extensions
# 
# This section lists some ideas for extending the tutorial that you may wish to explore.
# * Describe three examples when Pandas would be better than using Excel directly.
# * Complete the next example that uses Pandas to clean a dataset. 
# 
# # Further Reading
# This section provides more resources on the topic if you are looking to go deeper.
# 
# ## Books
# * Python for Data Analysis, by William McKinney. http://shop.oreilly.com/product/0636920023784.do
# 
# ## APIs
# * Pandas. https://pandas.pydata.org/
# 
# ## Articles
# * Getting started with Pandas in 5 minutes, on Towards Data Science. https://medium.com/bhavaniravi/python-pandas-tutorial-92018da85a33
# * My Pandas Cheat Sheet, on Towards Data Science. https://towardsdatascience.com/my-python-pandas-cheat-sheet-746b11e44368
#     
# # Summary
# 
# In this tutorial, you used Pandas for more advanced data analysis. Specifically, you learned:
# * Basic indexing and working with dates
# * Reading data from multiple sources
# * Merging data (joins/vlookup)
# * Groupby, pivot_table, transform, melt
# 
# # Next
# 
# In the next section, you will use Pandas to explore a dataset. 

# In[ ]:




