from merge_data import full_data
import pandas as pd

movie_avg_ratings = full_data.pivot_table(index='Title', values='Rating', aggfunc='mean')
print("Average Rating per Movie:\n", movie_avg_ratings)

genre_avg_ratings = full_data.pivot_table(index='Genre', values='Rating', aggfunc='mean')
print("Average Rating per Genre:\n", genre_avg_ratings)

user_avg_ratings = full_data.pivot_table(index='Name', values='Rating', aggfunc='mean')
print("Average Rating per User:\n", user_avg_ratings)

movie_rating_count = full_data.pivot_table(index='Title', values='Rating', aggfunc='count')
print("Count of Ratings per Movie:\n", movie_rating_count)
