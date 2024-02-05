#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 13:43:14 2024

@author: andisiwematu
"""

import pandas as pd

df =pd.read_csv("movie_dataset.csv")

print(df)


print(df.info())

#pd.set_option('display.max_rows', None)



df = df.rename(columns={'Runtime (Minutes)': 'Runtime(Minutes)', 'Revenue (Millions)': 'Revenue(Millions)'})
print(df)

print(df.info())

print(df.describe())



df = df.reset_index(drop=True)

print(df)

x1 = df["Revenue(Millions)"].mean()

df["Revenue(Millions)"].fillna(x1, inplace = True) 


x2 = df["Metascore"].mean()

df["Metascore"].fillna(x2, inplace = True)


df2 = df.sort_values(by=['Rating'], ascending=False)

print(df2.head())

"""print(df2.head())
     Rank            Title  ... Revenue(Millions)  Metascore
54     55  The Dark Knight  ...            533.32  82.000000
80     81        Inception  ...            292.57  74.000000
117   118           Dangal  ...             11.15  58.985043
36     37     Interstellar  ...            187.99  74.000000
96     97    Kimi no na wa  ...              4.68  79.000000

[5 rows x 12 columns]"""


df["Revenue(Millions)"].mean()

"""82.9563761467888"""

print(df2.head())

print(df2.describe())

print(df.info())

#Average revenue of movies from 2015 to 2017

start_Year = 2015

end_Year = 2016

filtered_df = df[(df['Year'] >= start_Year) & (df['Year'] <= end_Year)]

average_value = filtered_df['Revenue(Millions)'].mean()

print(average_value)


#movies  released in the year 2016

year_2016 = df[(df['Year'] > 2015)]

year_2016

Year_2016_all = df_movies_all[df_movies_all['Year'] > 2015]

#297

#movies  directed by Christopher Nolan

Chris_Nolan = df[df['Director'] == 'Christopher Nolan']

print(Chris_Nolan)

"""   Rank                  Title  ... Revenue(Millions) Metascore
36     37           Interstellar  ...            187.99      74.0
54     55        The Dark Knight  ...            533.32      82.0
64     65           The Prestige  ...             53.08      66.0
80     81              Inception  ...            292.57      74.0
124   125  The Dark Knight Rises  ...            448.13      78.0

[5 rows x 12 columns]"""


ratings = df[df['Rating'] >= 8]
print(ratings)
#78
print(Chris_Nolan['Rating'].median())
#8.6

grouped = df.groupby('Year')
print(grouped)

#year with the highest average rating


df.groupby("Year").agg({"Rating":"mean"})


"""       Rating
Year          
2006  7.125000
2007  7.133962
2008  6.784615
2009  6.960784
2010  6.826667
2011  6.838095
2012  6.925000
2013  6.812088
2014  6.837755
2015  6.602362
2016  6.436700
"""

movies_2006 = df[df['Year'] == 2006].shape[0]
movies_2016 = df[df['Year'] == 2016].shape[0]

# Calculate the percentage increase

percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100

print(percentage_increase)
#575.0

#most common actor in all the movies

target_name = 'Mark Wahlberg'

name_frequency = df['Actors'].str.count(target_name).sum()

print(name_frequency)

#15

#unique genres are there in the dataset

genres_df = df['Genre'].str.split(',').explode().str.strip()

unique_genres_count = genres_df.nunique()

print(unique_genres_count)

#################################


import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt



correlation_matrix = df.corr()

print(correlation_matrix)Rating

correlation = df['Runtime(Minutes)'].corr(df['Rating'])

# Plot a scatter plot for visualization

sns.lineplot(x='Runtime(Minutes)', y='Rating', data=df)

plt.title(f'Correlation between Runtime and Rating: {correlation:.2f}')

plt.show()


##year vs Revenue

correlation = df['Year'].corr(df['Revenue(Millions)'])

# Plot a scatter plot for visualization

sns.lineplot(x='Year', y='Revenue(Millions)', data=df)

plt.title(f'Correlation between Year and Revenue(Millions): {correlation:.2f}')

plt.show()

####Rating vs. Revenue

correlation = df['Rating'].corr(df['Revenue(Millions)'])

# Plot a scatter plot for visualization

sns.lineplot(x='Rating', y='Revenue(Millions)', data=df)

plt.title(f'Correlation between Rating and Revenue(Millions): {correlation:.2f}')

plt.show()


##Runtime vs Revenues

correlation = df['Runtime(Minutes)'].corr(df['Revenue(Millions)'])

# Plot a scatter plot for visualization

sns.lineplot(x='Runtime(Minutes)', y='Revenue(Millions)', data=df)

plt.title(f'Correlation between Revenue(Millions) and Runtime(Minutes): {correlation:.2f}')

plt.show()

correlation = df['Rating'].corr(df['Metascore'])

# Plot a scatter plot for visualization

sns.lineplot(x='Rating', y='Metascore', data=df)

plt.title(f'Correlation between Rating and Metascore: {correlation:.2f}')

plt.show()


correlation = df['Runtime(Minutes)'].corr(df['Votes'])

# Plot a scatter plot for visualization

sns.lineplot(x='Runtime(Minutes)', y='Votes', data=df)

plt.title(f'Correlation between Votes and Runtime(Minutes): {correlation:.2f}')

plt.show()
