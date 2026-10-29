# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

#Subsetting the DataFrame for the type "Movie"
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

#Filtering to keep only movies that are released in the 1990's and before 2000
movies_in_the_1990s = netflix_subset[(netflix_subset["release_year"] >= 1990) & (netflix_subset["release_year"] < 2000)]

#Frequent movie duration in the 1990s is 100
plt.hist(movies_in_the_1990s["duration"])
plt.title('Distribution of movie durations in the 1990s')
plt.xlabel('Duration [in minutes]')
plt.ylabel('Number of Movies')
plt.show()

duration = 100

#I have to filter short action movies that were released in the 1990s
short_action_movies_1990s = movies_in_the_1990s[movies_in_the_1990s["genre"] == "Action"]

short_movie_count = 0

for label, row in short_action_movies_1990s.iterrows() :
    if row["duration"] < 90 :
        short_movie_count = short_movie_count + 1
    else:
        short_movie_count = short_movie_count

print(short_movie_count)
