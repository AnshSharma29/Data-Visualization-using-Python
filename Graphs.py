#python file for combined code

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

%matplotlib inline
#%matplotlib inline sets the backend of matplotlib to the 'inline' backend

#accessing the dataset
iris=pd.read_excel(r'path of the dataset')

#printing the head and tail columns of the dataset
print(iris.head())
print(iris.tail())

#heavy coding ----> moderate coding ----> no coding
#Scatter plot using matplotlib 
fig,ax=plt.subplots()

#scatter the sepal lenght against sepal width
ax.scatter(iris['Petal_length'],iris['Sepal_width'])

#set a title and labels
ax.set_title('Iris datasets')
ax.set_xlabel('Sepal_length')
ax.set_ylabel('Sepal_width')

#Line chart using Matplotlib
columns=iris.columns.drop(['Species_name'])

#create x data
x_data=range(0, iris.shape[0])

#create figure and axis
fig,ax=plt.subplots()

#plot each column
for column in columns:
    ax.plot(x_data, iris[column], label=column)

#set title and legend
ax.set_title('Iris Dataset')
ax.legend()

#making a scatter plot of the dataset
iris.plot.scatter(x='Sepal_length', y='Sepal_width', title='Iris Dataset')

#making timeline graph of the dataset
iris.drop(['Species_name'], axis=1).plot.line(title='Iris Dataset')

#making scatter plot using seaborn library
import seaborn as sns

sns.scatterplot(x='Sepal_length', y='Sepal_width', data=iris)

#scatter plot using seaborn with modifications
sns.scatterplot(x='Sepal_length', y='Sepal_width', hue='Species_name', data=iris)

#line chart using seaborn
sns.lineplot(data=iris.drop(['Species_name'], axis=1))

#heatmap with annotations using Matplotlib
corr = iris.corr()
fig, ax = plt.subplots()
# create heatmap
im = ax.imshow(corr.values)

# set labels
ax.set_xticks(np.arange(len(corr.columns)))
ax.set_yticks(np.arange(len(corr.columns)))
ax.set_xticklabels(corr.columns)
ax.set_yticklabels(corr.columns)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        text = ax.text(j, i, np.around(corr.iloc[i, j], decimals=2), ha="center", va="center", color="black")
      
#heatmap using seaborn
sns.heatmap(iris.corr(), annot=True)

#pairplot using seaborn
sns.pairplot(iris)

#Facetgrid using seaborn
g=sns.FacetGrid(iris,col='Species_name')
g=g.map(sns.kdeplot, 'Sepal_length')





