import pandas as pd 

movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")
users = pd.read_csv("users.csv")

print(movies.head())
print(ratings.head())
print(users.head())

