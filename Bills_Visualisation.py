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

bills = pd.read_csv('bills.csv', names=["Company", "Account Name", "Year", "Month", "Day", "Value", "Type"])
bills["Value"] = pd.to_numeric(bills["Value"])
bills["Year"] = pd.to_numeric(bills["Year"])
#bills["Type"] = pd.to_str(bills["Type"])

sns.countplot(bills['Year']).set_title("Count of Bills per year") #9
#df = bills[(bills['Year']>=95) & (bills['Value']<1000)]
fig = sns.boxplot(bills['Type'], bills['Value']).set_title("Value of bills per Type")


my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k','m','c']), None, len(bills['Value'])))

p1 = bills.groupby("Company").Value.mean().sort_values(ascending=False)[:5].plot.bar(color=my_colors).set_title("mean value of bills for top 5 companies")
p1.set_axis_labels('Mean', 'Company')

p2 = bills['Company'].value_counts().plot.barh(color=my_colors).set_title("Count of bills per Company")

p3 = bills.groupby(["Company","Type"]).Value.sum().sort_values(ascending=False)[:50].plot.bar(color=my_colors).set_title("sum value of bills for each company/type")
#p4 = sns.scatterplot(x='Account Name', y='Value', data=bills).set_title('Bills - Value against Customer')

sns.distplot(bills['Value'], bins=10).set_title("Distribution of Bills Values")
sns.countplot(bills['Month']).set_title("Count of Bills per Month")
#sns.countplot(x="Account Name", hue="Company", data=bills).set_title('Count of bills per customer and company')

g = sns.catplot(x="Month", hue="Year", col="Type",
                 data=bills[bills['Month'] == 11], kind="count",
                 height=4, aspect=.7).set_title("Conparison of Cred Vs Deb in Nov by year");

                
ax = sns.countplot(x="Company", data=bills,
                    facecolor=(0, 0, 0, 0),
                    linewidth=5,
                    edgecolor=sns.color_palette("dark", 10))
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

chart = sns.countplot(
    data=bills,
    x="Company",
    palette='Set1'
)
chart.set_xticklabels(chart.get_xticklabels(), rotation=45, horizontalalignment='right')



ax = sns.countplot(y="Year", hue="Type", data=bills)
