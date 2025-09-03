from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)


movies_file = "movies.csv"
ratings_file = "ratings.csv"
users_file = "users.csv"


movies = pd.read_csv(movies_file)
if not os.path.exists(ratings_file):
    pd.DataFrame(columns=["UserID", "MovieID", "Rating", "Timestamp"]).to_csv(ratings_file, index=False)
ratings = pd.read_csv(ratings_file)
users = pd.read_csv(users_file)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/view")
def view():
    global ratings
    
    avg_ratings = ratings.groupby("MovieID")["Rating"].mean().reset_index()
    avg_ratings = avg_ratings.merge(movies, on="MovieID")
    return render_template("view.html", movies=avg_ratings.to_dict(orient="records"))


@app.route("/rating", methods=["GET", "POST"])
def rating():
    global ratings
    message = ""
    if request.method == "POST":
        user = request.form["user"]
        movie = request.form["movie"]
        rating_val = float(request.form["rating"])
        timestamp = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")

        
        new_row = pd.DataFrame([[user, movie, rating_val, timestamp]],
                               columns=["UserID", "MovieID", "Rating", "Timestamp"])
        new_row.to_csv(ratings_file, mode="a", header=False, index=False)

        
        ratings = pd.read_csv(ratings_file)

        message = "✅ Rating submitted successfully!"

    return render_template("rating.html", movies=movies.to_dict(orient="records"), message=message)


@app.route("/analysis")
def analysis():
    global ratings, movies

    
    merged = ratings.merge(movies, on="MovieID", how="left")

    
    movie_avg = merged.pivot_table(values="Rating", index="Title", aggfunc="mean").reset_index()

    
    genre_avg = merged.pivot_table(values="Rating", index="Genre", aggfunc="mean").reset_index()

    
    user_avg = merged.pivot_table(values="Rating", index="UserID", aggfunc="mean").reset_index()

    
    count_ratings = merged.pivot_table(values="Rating", index="Title", aggfunc="count").reset_index()
    count_ratings.rename(columns={"Rating": "RatingCount"}, inplace=True)

    
    movie_avg.to_csv("movie_avg_ratings.csv", index=False)
    genre_avg.to_csv("genre_avg_ratings.csv", index=False)
    user_avg.to_csv("user_avg_ratings.csv", index=False)
    merged.to_csv("cleaned_movie_ratings.csv", index=False)

    return render_template(
        "analysis.html",
        movie_avg=movie_avg.to_dict(orient="records"),
        genre_avg=genre_avg.to_dict(orient="records"),
        user_avg=user_avg.to_dict(orient="records"),
        count_ratings=count_ratings.to_dict(orient="records")
    )


if __name__ == "__main__":
    app.run(debug=True)
