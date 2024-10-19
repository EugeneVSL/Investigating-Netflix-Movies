# Importing pandas and matplotlib
import pandas as pd

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# filter movies with release year in the 90s 
nineties_movies = netflix_df[(netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] <= 1999) & (netflix_df['type'] == 'Movie')]

durations = {}

for index, row in nineties_movies.iterrows():
    
    if row['duration'] not in durations:
        durations[row['duration']] = 1
    else:
        durations[row['duration']] += 1

duration = max(durations, key=durations.get)

# filter movies with release year in the 90s 
short_movies = netflix_df[(netflix_df['duration'] < 90) & (netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] <= 1999) & (netflix_df['type'] == 'Movie') & (netflix_df['genre'] == 'Action')]

short_movie_count = len(short_movies)