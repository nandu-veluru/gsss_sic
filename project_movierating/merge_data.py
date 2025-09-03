from clean_data import movies, ratings, users
import pandas as pd

ratings_movies = pd.merge(ratings, movies, on="MovieID", how="left")
full_data = pd.merge(ratings_movies, users, on="UserID", how="left")

print("Merge Dataframes: ")
print(full_data.head())

