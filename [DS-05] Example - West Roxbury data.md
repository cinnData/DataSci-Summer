# [DS-05] Example - West Roxbury data

## Introduction

In the US, assessed valuation determines the value of a residence for tax purposes. The **assessed value** is the price placed on a home by the corresponding government municipality, in order to calculate property taxes. A model predicting the current assessed value from available, objective data could be useful for **automatic assessment** and for spotting assessment errors. Although, in general, the assessed value tends to be lower than the appraised fair market value of property, the data on assessed values could also provide rough estimates for the mortgage industry.

The objective of this example is to explore the relationship between the assessed value and some home features, based on a data set obtained in the West Roxbury neighborhood, in southwest Boston (Massachussets). The data include information on 5,801 single family owner-occupied homes.

## The data set

The data set (file `roxbury.csv`) contains 12 home features plus the total assessed value of the property. The variables included are:

* `value`, the total assessed value for property, in thousands of USD.

* `lot_sqft`, the total lot size of parcel in square feet.

* `yr_built`, the year the property was built.

* `gross_area`, the gross floor area in square feet.

* `living_area`, the total living area in square feet.

* `floors`, the number of floors.

* `rooms`, the number of rooms.

* `bedrooms`, the number of bedrooms.

* `full_bath`, the number of full baths.

* `half_bath`, the number of half baths.

* `kitchen`, the number of kitchens.

* `fireplace`, the number of fireplaces.

* `remodel`, a dummy for remodeled houses.

Source: G Shmueli, PC Bruce, I Yahav, NR Patel & KC Lichtendahl (2018), *Data Mining for Business Analytics*, Wiley (slightly edited).

## Questions

Q1. How is the distribution of the home assessed value in West Roxbury?

Q2. Popular wisdom suggests that there is a positive association between the size of a house and its value. How can we evaluate that?

Q3. Statistical measures of association are frequently affected by extreme values. Can this happen in this case? Explore this by trimming the data, retaining only those homes for which the most influential size measure falls between two threshold values that make sense for you.

## Importing the data

We use the Pandas function `read_csv()` to import the data. First, we import the package:

```
In [1]: import pandas as pd
```

The source file is stored in a GitHub repository, so we can use a remote path to get access. The path is:

```
In [2]: path = 'https://github.com/cinnData/DataSci-Summer/blob/main/Data/'
```

Pasting the path and the file name, we get a complete file name:

```
In [3]: filename = path + 'roxbury.csv'
```

We can now apply `read_csv()`:

```
In [4]: df = pd.read_csv(filename)
```

## Exploring the data


To explore the data set, we use the standard Pandas methods. First, the shape is the expected one, 13 columns and 5,801 row.

```
In [5]: df.shape
Out[5]: (5801, 13)
```

Since we didn't specify an index, a range index has been created.

```
In [6]: df.index
Out[6]: RangeIndex(start=0, stop=5801, step=1)
```

The names of the columns can also be listed.

```
In [7]: df.columns
Out[7]: 
Index(['value', 'lot_sqft', 'yr_built', 'gross_area', 'living_area', 'floors',
       'rooms', 'bedrooms', 'full_bath', 'half_bath', 'kitchen', 'fireplace',
       'remodel'],
      dtype='object')
```

The methods `.head()` and `.tail()` extract the first and the last rows. The default number is 5.

```
In [8]: df.head()
Out[8]: 
   value  lot_sqft  yr_built  gross_area  living_area  floors  rooms   
0  344.2      9965      1880        2436         1352     2.0      6  \
1  412.6      6590      1945        3108         1976     2.0     10   
2  330.1      7500      1890        2294         1371     2.0      8   
3  498.6     13773      1957        5032         2608     1.0      9   
4  331.5      5000      1910        2370         1438     2.0      7   

   bedrooms  full_bath  half_bath  kitchen  fireplace  remodel  
0         3          1          1        1          0        0  
1         4          2          1        1          0        1  
2         4          1          1        1          0        0  
3         5          1          1        1          1        0  
4         3          2          0        1          0        0  
```

```
In [9]: df.tail()
Out[9]: 
      value  lot_sqft  yr_built  gross_area  living_area  floors  rooms   
5796  404.8      6762      1938        2594         1714     2.0      9  \
5797  407.9      9408      1950        2414         1333     2.0      6   
5798  406.5      7198      1987        2480         1674     2.0      7   
5799  308.7      6890      1946        2000         1000     1.0      5   
5800  447.6      7406      1950        2510         1600     2.0      7   

      bedrooms  full_bath  half_bath  kitchen  fireplace  remodel  
5796         3          2          1        1          1        1  
5797         3          1          1        1          1        0  
5798         3          1          1        1          1        0  
5799         2          1          0        1          0        0  
5800         3          1          1        1          1        0  
```

The method .info() prints a report of the data frame content. There are no missing values. The distinction between int and float columns is not relevant for a statistical description, so don't pay attention.

```
In [10]: df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5801 entries, 0 to 5800
Data columns (total 13 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   value        5801 non-null   float64
 1   lot_sqft     5801 non-null   int64  
 2   yr_built     5801 non-null   int64  
 3   gross_area   5801 non-null   int64  
 4   living_area  5801 non-null   int64  
 5   floors       5801 non-null   float64
 6   rooms        5801 non-null   int64  
 7   bedrooms     5801 non-null   int64  
 8   full_bath    5801 non-null   int64  
 9   half_bath    5801 non-null   int64  
 10  kitchen      5801 non-null   int64  
 11  fireplace    5801 non-null   int64  
 12  remodel      5801 non-null   int64  
dtypes: float64(2), int64(11)
memory usage: 589.3 KB
```
A common statistical summary can be extracted with the method `.describe()`.

```
In [11]: df.describe()
Out[11]: 
             value      lot_sqft     yr_built   gross_area  living_area   
count  5801.000000   5801.000000  5801.000000  5801.000000  5801.000000  \
mean    392.655287   6277.959317  1937.078780  2924.530598  1656.895708   
std      99.158875   2669.921281    25.468896   883.742358   540.348856   
min     105.000000    997.000000  1798.000000   821.000000   504.000000   
25%     325.100000   4772.000000  1920.000000  2347.000000  1308.000000   
50%     375.900000   5683.000000  1935.000000  2700.000000  1548.000000   
75%     438.700000   7023.000000  1955.000000  3239.000000  1873.000000   
max    1217.800000  46411.000000  2011.000000  8154.000000  5289.000000   

            floors        rooms     bedrooms    full_bath    half_bath   
count  5801.000000  5801.000000  5801.000000  5801.000000  5801.000000  \
mean      1.683675     6.994656     3.229960     1.296673     0.613860   
std       0.444903     1.437721     0.846619     0.522003     0.533861   
min       1.000000     3.000000     1.000000     1.000000     0.000000   
25%       1.000000     6.000000     3.000000     1.000000     0.000000   
50%       2.000000     7.000000     3.000000     1.000000     1.000000   
75%       2.000000     8.000000     4.000000     2.000000     1.000000   
max       3.000000    14.000000     9.000000     5.000000     3.000000   

           kitchen    fireplace      remodel  
count  5801.000000  5801.000000  5801.000000  
mean      1.015342     0.739872     0.250819  
std       0.122920     0.565147     0.433522  
min       1.000000     0.000000     0.000000  
25%       1.000000     0.000000     0.000000  
50%       1.000000     1.000000     0.000000  
75%       1.000000     1.000000     1.000000  
max       2.000000     4.000000     1.000000  
```

## Q1. Distribution of the home assessed value

```
In [12]: df['value'].plot.hist(figsize=(7,5), title='Figure 1. Distribution of the home assessed value',
    ...:     color='gray', edgecolor='white', xlabel='Home value (thousand USD)');
```

![](https://github.com/cinndata/DataSci-Summer/blob/main/Figures/05-1.png)

## Q2. Association between value and size measures

```
In [13]: df[['value', 'lot_sqft', 'gross_area', 'living_area']].corr()
Out[13]: 
                value  lot_sqft  gross_area  living_area
value        1.000000  0.546193    0.800398     0.837030
lot_sqft     0.546193  1.000000    0.448949     0.426085
gross_area   0.800398  0.448949    1.000000     0.899715
living_area  0.837030  0.426085    0.899715     1.000000
```

```
In [14]: df[['value', 'lot_sqft', 'gross_area', 'living_area']].corr().round(2)
Out[14]: 
             value  lot_sqft  gross_area  living_area
value         1.00      0.55        0.80         0.84
lot_sqft      0.55      1.00        0.45         0.43
gross_area    0.80      0.45        1.00         0.90
living_area   0.84      0.43        0.90         1.00
```

```
In [15]: df.plot.scatter(x='living_area', y='value', figsize=(5,5), 
    ...:     title='Figure 2. Home value vs living area', color='gray', s=2,
    ...:     xlabel='Living area (sq ft)', ylabel='Home value (thousand USD)');
```

![](https://github.com/cinndata/DataSci-Summer/blob/main/Figures/05-2.png)

## Q3. Trimming the data

```
In [16]: df1 = df[df['living_area'].between(1000,2000)]
```

```
In [17]: df1[['value', 'lot_sqft', 'gross_area', 'living_area']].corr().round(2)
Out[17]: 
             value  lot_sqft  gross_area  living_area
value         1.00      0.40        0.46         0.60
lot_sqft      0.40      1.00        0.21         0.17
gross_area    0.46      0.21        1.00         0.62
living_area   0.60      0.17        0.62         1.00
```

```
In [18]: df1.plot.scatter(x='living_area', y='value', figsize=(5,5), 
    ...:     title='Figure 3. Home value vs living area (trimmed data)', color='gray', s=2,
    ...:     xlabel='Living area (sq ft)', ylabel='Home value (thousand USD)');
```

![](https://github.com/cinndata/DataSci-Summer/blob/main/Figures/05-3.png)
