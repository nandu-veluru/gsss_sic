from load_data import movies, ratings, users

print(movies.isna().sum()) #Checks for missing values
print(ratings.isna().sum())
print(users.isna().sum())

ratings['Rating'] = ratings['Rating'].fillna(0)
 #Fill zero if thers is no vlaue

movies.drop_duplicates(inplace=True)
ratings.drop_duplicates(inplace=True)
users.drop_duplicates(inplace=True)

print("Cleaned DataFrames ready!")