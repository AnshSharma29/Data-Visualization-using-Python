#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
#%matplotlib inline sets the backend of matplotlib to the 'inline' backend


# In[2]:


#Q1

# Load the dataset
df = pd.read_csv(r'C:\Users\ADMIN\Downloads\Employee data.csv')

# Extract the 'salary' column
salaries = df['salary']

# Create a histogram
plt.hist(salaries, bins=20, color='green', edgecolor='black')

# Add title and labels
plt.title('Distribution of Salaries Among Employees')
plt.xlabel('Salary')
plt.ylabel('Frequency')

# Display the plot
plt.show()


# In[3]:


#Q2

# Group the data by gender and calculate the average salary
average_salary_by_gender = df.groupby('gender')['salary'].mean()

# Create a bar plot
average_salary_by_gender.plot(kind='bar', color=['blue', 'pink'])

# Add title and labels
plt.title('Average Salary Comparison by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Salary')

# Show the plot
plt.show()


# In[4]:

#Q3
# Extract the relevant columns
prevexp = df['prevexp']
salary = df['salary']

# Create a scatter plot
plt.scatter(prevexp, salary, color='orange', alpha=0.5)

# Add title and labels
plt.title('Relationship Between Previous Work Experience and Current Salary')
plt.xlabel('Previous Work Experience')
plt.ylabel('Current Salary')

# Show the plot
plt.show()


# In[5]:

#Q4
# Count the occurrences of each education level
education_counts = df['educ'].value_counts()

# Create a pie chart
plt.pie(education_counts, labels=education_counts.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen', 'lightcoral', 'orange'])

# Add title
plt.title('Distribution of Educational Backgrounds Among Employees')

# Show the plot
plt.show()


# In[6]:

#Q5
import sweetviz as sv

# Create a data comparison report
report = sv.analyze(df)

# Save the report to an HTML file
report.show_html('sweetviz_report.html')

#Run the above generated file in a web browser to see the generated report


# In[ ]:




