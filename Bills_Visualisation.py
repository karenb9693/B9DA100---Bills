#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 19:36:45 2019

@author: karenbyrne
"""
import pandas as pd
#import matplotlib.pyplot as plt
from itertools import cycle, islice
import seaborn as sns

bills = pd.read_csv('bills1.csv', names=["Company", "Account Name", "Year", "Month", "Day", "Value", "Type"])
bills["Value"] = pd.to_numeric(bills["Value"])
bills["Year"] = pd.to_numeric(bills["Year"])
bills["Type"] = pd.to_str(bills["Type"])

sns.countplot(bills['Year'])
#df = bills[(bills['Year']>=95) & (bills['Value']<1000)]
sns.boxplot(bills['Year'], bills['Value']).set_title("Value of bills per year")

my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k','m','c']), None, len(bills['Value'])))

bills.groupby("Company").Value.mean().sort_values(ascending=False)[:5].plot.bar(color=my_colors).set_title("mean value of bills for each company")
bills['Company'].value_counts().plot.barh(color=my_colors).set_title("Count of bills per Company")

bills.groupby(["Company","Type"]).Value.sum().sort_values(ascending=False)[:6].plot.bar(color=my_colors).set_title("sum value of bills for each company/type")
sns.scatterplot(x='Account Name', y='Value', data=bills).set_title('Bills - Value against Customer')

sns.distplot(bills['Value'], bins=10)
bills[bills['Type'] == "credit"]
sns.countplot(bills['Value']).set_title("Count of each value of bill")
sns.countplot(x="Account Name", hue="Company", data=bills).set_title('Count of bills per customer and company')











