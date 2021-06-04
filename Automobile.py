"""
Perform the following task :
    1. Handle the missing values for Price column
    2. Get the values from Price column into a numpy.ndarray
    3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
    4. Make a pie chart for all car makers
 """
import pandas as pd

auto = pd.read_csv('Automobile.csv')   
auto.head()
auto.shape #(205, 26)
auto.columns.tolist()

# 1. Handle the missing values for Price column
auto['price'].isnull().any(axis=0) #True
auto['price'].mean() # mean = 13207.12
auto['price'] = auto['price'].fillna(auto['price'].mean())

# 2. Get the values from Price column into a numpy.ndarray
import numpy as np
data = auto['price']
data1 = np.array(data)
type(data1)

# 3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
minprice = auto['price'].min()
print("Min price is :" , minprice )
maxprice = auto['price'].max()
print("Max price is :" , maxprice )
meanprice = auto['price'].mean()
print("Mean price is :" , meanprice )
std_dev_price = auto['price'].std()
print("Std. dev price is :" , std_dev_price )

#4. Make a pie chart for all car makers
auto['make'].value_counts()[0:15].plot(kind="pie",autopct = '%1.1f%%')