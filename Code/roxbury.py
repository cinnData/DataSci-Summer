## [DS-05] Example - West Roxbury data ##

# Importing the data #
import pandas as pd
path = 'https://raw.githubusercontent.com/cinnData/DataSci-Summer/main/Data/'
filename = path + 'roxbury.csv'
df = pd.read_csv(filename)

# Exploring the data #
df.shape
df.index
df.columns
df.head()
df.tail()
df.info()
df.describe()

# Q1. Distribution of the home assessed value #
df['value'].plot.hist(figsize=(7,5), title='Figure 1. Distribution of the home assessed value',
    color='gray', edgecolor='white', xlabel='Home value (thousand USD)');

# Q2. Association between value and size measures #
df.plot.scatter(x='living_area', y='value', figsize=(5,5), 
    title='Figure 2. Home value vs living area', color='gray', s=2,
    xlabel='Living area (sq ft)', ylabel='Home value (thousand USD)');
df[['value', 'lot_sqft', 'gross_area', 'living_area']].corr()
df[['value', 'lot_sqft', 'gross_area', 'living_area']].corr().round(2)

# Q3. Trimming the data #
df1.plot.scatter(x='living_area', y='value', figsize=(5,5), 
    title='Figure 3. Home value vs living area (trimmed data)', color='gray', s=2,
    xlabel='Living area (sq ft)', ylabel='Home value (thousand USD)');
df1 = df[df['living_area'].between(1000,2000)]
df1[['value', 'lot_sqft', 'gross_area', 'living_area']].corr().round(2)
