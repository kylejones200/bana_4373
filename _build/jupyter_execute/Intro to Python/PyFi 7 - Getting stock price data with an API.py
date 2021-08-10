#!/usr/bin/env python
# coding: utf-8

# # Summary - Web Scraping and APIs
# 
# How do we get data to analyze? One way is to use webscrapping (that is how the AirBNB dataset was created). Another way is to use APIs (application programming interfaces). These allow us to get real time data without having to store our own copy. 
# 
# # Tutorial Overview
# This tutorial is divided into 4 parts:
# 1. Example of getting financial and non-financial stock data
# 2. Example of time series with RDS-A ticker
# 3. Using Bollinger Bands as an algorithmic trading strategy
# 4. Exercises: You're turn!

# # Example: Get financial and non-financial stock data
# 
# In this example we use the website `https://financialmodelingprep.com` to get data about stocks. The site can give us real time pricing data as well as financial metrics and other information about the company. 
# 
# We will start out by getting some basic data and saving it as an excel workbook for later use.

# In[1]:


import requests # this lets us call the API to the external website
import pandas as pd

def getdata(stock: str):
    """This function gets data from the API and returns specific values
    :param stock: Official stock ticker symbol
    
    :returns share_price: Array of current share price
    :returns cash: Array of cash on hand 
    :returns debt: Array of debt
    :returns qRev: Array of quarterly revenue
    :returns ceo: Name of the CEO 
    """
    # Company Quote Group of Items
    company_quote = requests.get(f"{base}quote/{stock}?apikey={key}")
    company_quote = company_quote.json()
    share_price = float(company_quote[0]['price'])

    # Balance Sheet Group of Items
    BS = requests.get(f"{base}financials/balance-sheet-statement/{stock}?period=quarter&apikey={key}")
    BS = BS.json()

    # Total Cash
    cash = float(BS['financials'][0]['Cash and short-term investments'])
    # Total Debt
    debt = float(BS['financials'][0]['Total debt'])

    # Income Statement Group of Items
    IS = requests.get(f"{base}financials/income-statement/{stock}?period=quarter&apikey={key}")
    IS = IS.json()

    # Most Recent Quarterly Revenue
    qRev = float(IS['financials'][0]['Revenue'])

    # Company Profile Group of Items
    company_info = requests.get(f"{base}company/profile/{stock}?apikey={key}")
    company_info = company_info.json()

    # Chief Executive Officer
    ceo = company_info['profile']['ceo']

    return (share_price, cash, debt, qRev, ceo)

base = 'https://financialmodelingprep.com/api/v3/'
key = 'ac711b8ed8ca5245691b502cb9c3e105'
tickers = ('AAPL', 'MSFT', 'GOOG', 'T', 'CSCO', 'INTC', 'ORCL', 'AMZN', 'FB', 'TSLA', 'NVDA')
    
data = map(getdata, tickers)   

quarter = '1Q2020'

df = pd.DataFrame(data,
                    columns=['Share Price ($)', 'Total Cash', 'Total Debt', f'{quarter} Revenue', 'CEO'],
                    index=tickers)

writer = pd.ExcelWriter('example.xlsx')
df.to_excel(writer, 'Statistics')
writer.save()


# In[32]:


"{a}, {b}, {c}".format(a = quarter, b= "Kevin", c= 8)


# In[11]:


df.head(10)


# In[13]:


# convert to billions for easier reading

cols_to_convert = ['Total Cash','Total Debt','1Q2020 Revenue']

df[cols_to_convert] = df[cols_to_convert] / 10**9


# In[32]:


df.head(10)


# # Example of time series with RDS-A
# 
# Let's explore the RDS-A stock ticker. 

# In[6]:


# getting historical data for RDS-A. This code calls the API and transforms the result into a DataFrame.
import pandas as pd
from pandas.io.json import json_normalize 


# In[7]:


df = pd.read_json("https://financialmodelingprep.com/api/v3/quotes/nyse?apikey=0b9ecbdc251f332ac3369952d0feb2aa")


# In[8]:


df.head()


# In[25]:


key = '0b9ecbdc251f332ac3369952d0feb2aa'
ticker = "T"
target = "https://financialmodelingprep.com/api/v3/historical-price-full/{}?apikey={}".format(ticker, key)
df = pd.read_json(target)
df = json_normalize(df['historical'])
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)


# In[2]:


df.to_csv('{} data.csv'.format(ticker))


# In[14]:


df = pd.read_csv('data/RDS-A data.csv')
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
ticker = "RDS-A"

df.head()


# In[26]:


get_ipython().run_line_magic('matplotlib', 'inline')

df['adjClose'].plot()


# # Bollinger Bands
# 
# A basic method of analysis for stocks is the Bollinger band. This uses the moving average and the moving standard deviation to identify points where the trader should buy/sell. We start by defining how the Bollinger Bands are calculated and defining how we want the data to be plotted. These defined functions can be used again for analizing another stock. 

# In[27]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

def bollinger_bands(df, target_col: str = 'adjClose')->pd.DataFrame:
    """Calculates Bollinger Bands and returns an updated DataFrame. 

    :param df: DataFrame
    :param target_col: column that will be used for the calcuations
    :type target_col: str

    :return df: df with additional columns
    :rtype df: pd.DataFrame
    """
    
    df['20 Day MA'] = df[target_col].rolling(20).mean()
    df['20 Day MA_lower bound'] = df['20 Day MA'] - df[target_col].rolling(20).std()*2
    df['20 Day MA_upper bound'] = df['20 Day MA'] + df[target_col].rolling(20).std()*2
    
    return df

def bb_plot(df: pd.DataFrame = df, target_col: str = 'adjClose'):
    """Calculates time series plot with Bollinger Bands 

    :param df: DataFrame
    :param target_col: column that will be used for the calcuations
    :type target_col: str

    :return: plot
    :rtype: matplotlib.pyplot
    """
    
    x = df.index
    y= df[['adjClose', '20 Day MA', '20 Day MA_lower bound','20 Day MA_upper bound']]

    plt.fill_between(x, rds['20 Day MA_lower bound'],rds['20 Day MA_upper bound'], alpha = .5)
    plt.plot(x,y)
    plt.title("Bollinger Bands for {}".format(ticker))
    plt.xlabel('Date (Year/Month)')
    plt.ylabel('Price(USD)')
    plt.legend(y)
    plt.show()
    
    return plt


# In[28]:


rds = bollinger_bands(df.sort_values(by='date'), 'adjClose')
bb_plot(rds)


# ## Bollinger Band Strategy
# 
# The basic strategy is to buy/sell short if the actual value moves beyond the bands. The assumption is that the stock will return toward the mean. 
# 
# Let's test our returns if we follow this strategy. 

# In[29]:


import numpy as np

def bb_strategy(df: pd.DataFrame)->pd.DataFrame:
    """Calculates the returns of implementing the Bollinger Bands 

    :param df: DataFrame

    :return df: df with additional columns for Positing, Market Return, and Strategy Return
    :rtype df: pd.DataFrame
    """
    df['Position'] = None
    #Fill our newly created position column - set to sell (-1) when the price hits the upper band, and set to buy (1) when it hits the lower band
    for row in range(len(df)):
    
        if (df['adjClose'].iloc[row] > df['20 Day MA_upper bound'].iloc[row]) and (df['adjClose'].iloc[row-1] < df['20 Day MA_upper bound'].iloc[row-1]):
            df['Position'].iloc[row] = -1
        
        if (df['adjClose'].iloc[row] < df['20 Day MA_lower bound'].iloc[row]) and (df['adjClose'].iloc[row-1] > df['20 Day MA_lower bound'].iloc[row-1]):
            df['Position'].iloc[row] = 1  

    #Forward fill our position column to replace the "None" values with the correct long/short positions to represent the "holding" of our position
    #forward through time
    df['Position'].fillna(method='ffill',inplace=True)

    #Calculate the daily market return and multiply that by the position to determine strategy returns
    df['Market Return'] = np.log(df['adjClose'] / df['adjClose'].shift(1))
    df['Strategy Return'] = df['Market Return'] * df['Position']
    
    return df

rds = bb_strategy(rds)
rds['Strategy Return'].cumsum().plot() 


# ## Conclusion
# Yikes! Our returns are pretty bad just following the Bollinger Band strategy. We should do more analysis and try another strategy. 

# # Exercises: Your Turn!

# 1. What was the "Open" price of Royal Dutch Shell-A stock (RDS-A) on February 18, 2020?

# In[ ]:





# 2. What was the highest volume of RDS-A stock traded in one day?

# In[ ]:





# 3. On what day day did this occur?

# In[ ]:





# 4. What was RDS-A's biggest one day stock growth in dollar terms? in percentage terms?

# In[ ]:





# 5. Create line plot showing RDS-A stock price over time

# In[ ]:





# 6. Create line chart showing average monthly stock price of Royal Dutch Shell-A (RDS-A) since January 2019 using 'adjClose.'
# 
# hint: df['column'].dt.to_period("M") can convert a date to a month

# In[ ]:





# 7. Create same chart but normalize it so that the stock starts at 1 on January 2019

# In[ ]:





# # Extensions
# 
# This section lists some ideas for extending the tutorial that you may wish to explore.
# * Describe three examples when using APIs for data would be better than downloading data as spreadsheets.
# 
# # Further Reading
# This section provides more resources on the topic if you are looking to go deeper.
# 
# ## Books
# * Python for Finance, by Yves Hilpisch. http://shop.oreilly.com/product/0636920032441.do
#  * [Git Repo](https://github.com/yhilpisch/py4fi2nd)
# * Mastering Python for Finance,  James Ma Weiming. https://www.amazon.com/dp/1789346460/
#  * [Git Repo](https://github.com/PacktPublishing/Mastering-Python-for-Finance-Second-Edition)
# * Python Finance Cookbook, Eryk Lewinson. https://www.packtpub.com/data/python-for-finance-cookbook
#  * [Git Repo](https://github.com/erykml/Python-for-Finance-Cookbook)
# 
# ## APIs
# * [Requests library](https://requests.readthedocs.io/en/master/)
#     
# # Summary
# 
# In this tutorial, you were introduced to accessing data using APIs. Specifically, you learned:
# * How to access stock data and store it as a Pandas DataFrame
# * You did basic analysis using Bollinger Bands and even applied a basic algorithmic trading strategy
# 
# # Next
# 
# Use the easiest option to get data and then take the data and do amazing analysis.
