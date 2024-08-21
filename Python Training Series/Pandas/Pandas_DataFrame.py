
# #### Create a DataFrame df from the dictionary data with index labels:
import numpy as np
import pandas as pd
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data, index=labels)


# #### Display a summary of the basic information about this DataFrame and its data
df.info()

# #### Return the first 3 rows of the DataFrame df
df.head(3)

# #### Select just the ‘animal’ and ‘age’ columns from the DataFrame df
df[['animal', 'age']]

# #### Select the data in rows [3, 4, 8] and in columns ['animal', 'age']
df.loc[df.index[[3, 4, 8]], ['animal', 'age']]

# #### Select only the rows where the number of visits is greater than 3
df[df['visits'] > 3]

# #### Select the rows where the age is missing, i.e., it is NaN
df[df['age'].isna()]

# #### Select the rows where the animal is a cat and the age is less than 3
df[(df['animal'] == 'cat') & (df['age'] < 3)]

# #### Select the rows where the age is between 2 and 4 (inclusive)
df[df['age'].between(2, 4)]

# #### Change the age in row ‘f’ to 1.5
df.at['f', 'age'] = 1.5

# #### Calculate the sum of all visits in df
df['visits'].sum()

# #### Calculate the mean age for each different animal in df
df.groupby('animal')['age'].mean()

# #### Append a new row ‘k’ to df with your choice of values for each column, then delete that row to return the original DataFrame
df.loc['k'] = ['dog', 5.5, 2, 'no']
df = df.drop('k')

# #### Count the number of each type of animal in df
df['animal'].value_counts()

# #### Sort df first by the values in the ‘age’ in descending order, then by the value in the ‘visits’ column in ascending order
df.sort_values(by=['age', 'visits'], ascending=[False, True])

# #### Replace the ‘priority’ column with boolean values (‘yes’ should be True and ‘no’ should be False)
df['priority'] = df['priority'].map({'yes': True, 'no': False})

# #### In the ‘animal’ column, change the ‘snake’ entries to ‘python’
df['animal'] = df['animal'].replace('snake', 'python')

# #### For each animal type and each number of visits, find the mean age
df.pivot_table(index='animal', columns='visits', values='age', aggfunc='mean')

# ### Data Frames Advanced
# ##### Filter out rows which contain the same integer as the row immediately above
df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
df = df.loc[df['A'].shift() != df['A']]

# #### Subtract the row mean from each element in the row
df = pd.DataFrame(np.random.random(size=(5, 3)))
df = df.sub(df.mean(axis=1), axis=0)

# #### Which column of numbers has the smallest sum? Return that column’s label
df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))
smallest_sum_column = df.sum().idxmin()

# #### Count how many unique rows a DataFrame has (ignore all rows that are duplicates)
nan = np.nan

data = [[0.04,  nan,  nan, 0.25,  nan, 0.43, 0.71, 0.51,  nan,  nan],
        [ nan,  nan,  nan, 0.04, 0.76,  nan,  nan, 0.67, 0.76, 0.16],
        [ nan,  nan, 0.5 ,  nan, 0.31, 0.4 ,  nan,  nan, 0.24, 0.01],
        [0.49,  nan,  nan, 0.62, 0.73, 0.26, 0.85,  nan,  nan,  nan],
        [ nan,  nan, 0.41,  nan, 0.05,  nan, 0.61,  nan, 0.48, 0.68]]

columns = list('abcdefghij')

df = pd.DataFrame(data, columns=columns)

third_nan_column = df.apply(lambda row: row.index[row.isna().cumsum() == 3][0], axis=1)


