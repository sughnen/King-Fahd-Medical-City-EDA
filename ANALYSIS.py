#!/usr/bin/env python
# coding: utf-8

# In[175]:


#Importing liberies
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix
from dython.nominal import identify_nominal_columns


# In[176]:


#First converted the file into UTF-8 format and then into CSV
#Read CSV file
df = pd.read_csv('Original.csv')


# In[177]:


#Looking at the first ten roles of the data
df.head()


# In[178]:


#Data has 521 roles and 32 coumns with missing values
df.shape


# In[179]:


#Creat a wrangle function and prepare your data
def wrangle(filepath):
    # Read CSV file
    df = pd.read_csv(filepath)

    #For the sake of simplicity, we fill in the NaN with the value that is most common in the 
    #colimns USING (value_counts and fillna()).
    df = df.fillna({"US": "V"})
    df = df.fillna({"MARKERS":"ER+PR+H-"})
    df = df.fillna({"GRADE":"II"})
    df = df.fillna({"Size US (List)":"More Than  20 & Less  OR Equal 50 MM"})
    df = df.fillna({"SIZE SURGRY":"15MM"})
    df = df.fillna({"LN":"0l1"})
    df = df.fillna({"L.CTOMY":"LP"})
    df = df.fillna({"M.TOMY":"MRM"})
    df = df.fillna({"STAGE":"T1N0M0"})
    df = df.fillna({"Stages (list)":"0"})
    df = df.fillna({"BIRADS":"0"})
    #Drop low-high cardinallity feature variables
    df.drop(columns=['ID','KFMC','NAME','SLNB','LND','yc XCT','XCT','XRT','XHT','F UP','CTABD','CTCHEST','MRI BREAST','BONE SCSN','OTHERS','MEATASTASES'], inplace=True)
    return df


# In[180]:


df = wrangle('Original.csv')


# In[181]:


df.head()


# In[182]:


df.dtypes


# In[183]:


df["C.TYPE"].value_counts()


# In[184]:


#Downloading clean data to my local machine
df.to_csv('C:\\Users\\Elitebook 820\\Desktop\\PLOTLY EXPRESS\\Original.csv');


# In[213]:


# Count the number of occurrences of each category
counts = df['BIRADS'].value_counts()

# Set the figure size
plt.figure(figsize=(8,8))

# Plot the pie chart
counts.plot.pie(title='Percentage Distribution of BIRADS', autopct='%1.1f%%')

# Show the plot
plt.show()


# In[186]:


df['GRADE'].unique()


# In[212]:


# Count the number of occurrences of each category
counts = df['BREAST DENSITY'].value_counts()

# Set the figure size
plt.figure(figsize=(8, 8))

# Plot the pie chart
counts.plot.pie(title='Percentage Distribution of BREAST DENSITY', autopct='%1.1f%%')

# Show the plot
plt.show()


# In[211]:


# Count the number of occurrences of each category
counts = df['L.CTOMY'].value_counts()

# Set the figure size
plt.figure(figsize=(8, 8))

# Plot the pie chart
counts.plot.pie(title='Percentage Distribution of L.CTOMY', autopct='%1.1f%%')

# Show the plot
plt.show()


# In[221]:


fig = plt.figure(figsize=(10, 6))
# Create a box plot showing the relationship between AGE and C.TYPE
ax = sns.boxplot(x='C.TYPE', y='AGE', data=df)

# Add a title to the plot
ax.set_title("Relationship between AGE and C.TYPE")
# Rotate the x-axis labels by 90 degrees
plt.xticks(rotation=90);


# In[208]:


fig = plt.figure(figsize=(10, 6))

# Create a bar plot showing the mean values for each category
ax=sns.barplot(x='M.TOMY', y='AGE', data=df)

# Add a title to the plot
ax.set_title("M.TOMY vs AGE")
# Rotate the x-axis labels by 90 degrees
plt.xticks(rotation=90)
plt.show();


# In[192]:


# Create a bar plot showing the mean values for each category
ax = sns.barplot(x='L.CTOMY', y='AGE', data=df)

# Add a title to the plot
ax.set_title("L.CTOMY vs AGE")
# Rotate the x-axis labels by 90 degrees
plt.xticks(rotation=90);


# In[207]:


fig = plt.figure(figsize=(10, 6))

# Create a box plot showing the relationship between AGE and GRADE
ax = sns.boxplot(x='GRADE', y='AGE', data=df)

# Add a title to the plot
ax.set_title("Relationship between AGE and GRADE")

# Set the figure size
plt.show()


# In[218]:


fig = plt.figure(figsize=(10, 6))

# Create a box plot showing the relationship between AGE and GRADE
ax = sns.boxplot(x='US', y='AGE', data=df)

# Add a title to the plot
ax.set_title("Relationship between AGE and US")

# Set the figure size
plt.show()


# In[232]:


fig = plt.figure(figsize=(10, 6))

# Create a bar plot using Matplotlib
plt.bar(df['Stages (list)'].unique(), df['Stages (list)'].value_counts())
#Stages (list) frequency

# Label the title, x-axis, and y-axis
#plt.title('Frequency of Stages (list) Values')
plt.xlabel('Stages (list)')
plt.ylabel('Frequency')
plt.show();


# In[234]:


#using Chi-squared test of independence to determines whether there is a significant
#association between two categorical variables.

from scipy.stats import chi2_contingency

# Select the columns to use in the test
column_1 = df['Stages (list)']
column_2 = df['AGE']

# Calculate the chi-squared statistic and p-value
chi2, p, dof, expected = chi2_contingency(pd.crosstab(column_1, column_2))

# Interpret the result
if p < 0.05:
    print('There is a significant association between the two categorical variables.')
else:
    print('There is no significant association between the two categorical variables.')


# In[236]:


#using Chi-squared test of independence to determines whether there is a significant
#association between ('C.TYPE' and 'AGE').

from scipy.stats import chi2_contingency

# Select the columns to use in the test
column_1 = df['C.TYPE']
column_2 = df['AGE']

# Calculate the chi-squared statistic and p-value
chi2, p, dof, expected = chi2_contingency(pd.crosstab(column_1, column_2))

# Interpret the result
if p < 0.05:
    print('There is a significant association between the two categorical variables.')
else:
    print('There is no significant association between the two categorical variables.')


# In[238]:


fig = plt.figure(figsize=(10, 6))
# Create a bar plot showing the mean values for each category
ax = sns.barplot(x='C.TYPE', y='AGE', data=df)

# Add a title to the plot
ax.set_title("Relationship between AGE and C.TYPE")
# Rotate the x-axis labels by 90 degrees
plt.xticks(rotation=90)
plt.show();


# In[239]:


# Count the number of occurrences of each category
counts = df['C.TYPE'].value_counts()

# Set the figure size
plt.figure(figsize=(8,8))

# Plot the pie chart
counts.plot.pie(title='Percentage Distribution of C.TYPE', autopct='%1.1f%%')

# Show the plot
plt.show()


# In[ ]:




