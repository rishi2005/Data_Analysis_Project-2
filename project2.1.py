#E-Commerce sales Data Analysis With python

#Order_ID, Date, Customer_ID, Product, Category,Price,Quantity
#Payment Mode,City & State


#Import the imp lib.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#importing the dataset
df = pd.read_csv('Ecommerce_Sales.csv')
print(df.head())


#Data Overview

#Dataset shape and info. (for number and col in the dataset)
print(df.head())
#Attributes name (and datatype of your data type) also finds missing values
print(df.info())


#Statistics Summary (Staticstical summary: mean max avg %)
print(df.describe())

#check for missing values : Finds null value attributes
print(df.isnull().sum())

#Data Cleaning

#Convert 'Date' Column to datetime format
df['Date'] = pd.to_datetime(df['Date'])
#df['Date'] = pd.to_datetime(df['Date']), errors ='coerce') --> use if you are doing it in google collab to avoid errors
#df = df.dropna(subset=['Date']) --> use if you are doing it iin google collab
#Remove any rows with missing data
df.dropna(inplace=True)

#Create a new col "Total_amount" Price and Quality account
df['Total_Amount'] = df['Price'] * df['Quantity']

#Explore Data : Find Top 5 cities with Highest Sales
top_cities = df.groupby('City')['Total_Amount'].sum().sort_values(ascending=False).head(5)
print("Top 5 cities with highest sales:")
print(top_cities)

#Find the monthly sales
monthly_sales = df.resample('M', on='Date')['Total_Amount'].sum()
print("Monthly Sales:")
print(monthly_sales)

#Analyze Sales Scale evolve with time
sales_by_time = df.groupby(df['Date'].dt.to_period('M'))['Total_Amount'].sum()
print("Sales by time:")
print(sales_by_time)

monthly_sales.plot(kind='line', marker='o', title='Monthly Sales Trend', figsize=(10, 5))
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()