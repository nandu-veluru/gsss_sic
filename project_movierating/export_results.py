from pivot_analysis import movie_avg_ratings, genre_avg_ratings, user_avg_ratings
from merge_data import full_data

# Export pivot tables
movie_avg_ratings.to_csv("movie_avg_ratings.csv")
genre_avg_ratings.to_csv("genre_avg_ratings.csv")
user_avg_ratings.to_csv("user_avg_ratings.csv")

# Export cleaned & merged dataset
full_data.to_csv("cleaned_movie_ratings.csv", index=False)

print("All files exported successfully!")
