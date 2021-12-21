# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 19:49:45 2021

@author: PC
"""
#1-Read the dataset, convert it to DataFrame and display some from it.

import pandas as pd
import matplotlib.pyplot as plt
dataset=pd.read_csv("Wuzzuf_Jobs.csv")
x=dataset.iloc[:,[0]].values
y=dataset.iloc[:,1].values

#3-Clean the data (null, duplications).
dataset=dataset.dropna()
dataset=dataset.drop_duplicates(keep="first" , inplace= True)

#4-Count the jobs for each company and display that in order (What are the most demanding companies for jobs?).
print (dataset['Company'].values_counts())

#5-Show step4 in a pie chart.
plt.pie(dataset['Company'].values_counts)
plt.show() 
#6-Find out what are the most popular job titles.
t=dataset['Title'].values_counts()
print("most popular job"+t.index[0])
#7-Show step 6 in bar chart.
a=list(t.index)
b=list(t)

plt.bar(a , b , color='black', width= 0.5)
plt.xlabel("job")
plt.ylabel("no of occurance")
plt.title("most popular job titles.")
plt.show()

#8-Find out the most popular areas
d=dataset['Location'].values_counts()
print("most popular area is "+d.index[0])

#9-Show step 8 in bar chart.

aa=list(d.index)
bb=list(d)

plt.bar(aa , bb , color='black', width= 0.5)
plt.xlabel("location")
plt.ylabel("no of occurance")
plt.title("most popular areas.")
plt.show()
#10-Print skills one by one , their count, and order the output to find out the most important skills required.
s=dataset['Skills']
m=s.values_count()
print(m)
print( "most important skills required"+m.index[0] )
