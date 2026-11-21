

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Create a folder for the charts.
Path("charts").mkdir(exist_ok=True)

movies = pd.read_csv("movies.csv")
users = pd.read_csv("users.csv")
watch_history = pd.read_csv("watchhistory.csv")

print("Movies:", len(movies))
print("Users:", len(users))
print("Viewing records:", len(watch_history))

print("MOVIES")
print(movies.head())
print("\nWATCH HISTORY")
print(watch_history.head())
print("\nMISSING VALUES IN WATCH HISTORY")
print(watch_history.isna().sum())

# Clean the three tables.
movies = movies.drop_duplicates(subset="movie_id").dropna(subset=["movie_id", "title", "genres"])
users = users.drop_duplicates(subset="user_id").dropna(subset=["user_id", "name"])
watch_history["rating"] = pd.to_numeric(watch_history["rating"], errors="coerce")
watch_history = watch_history.dropna(subset=["user_id", "movie_id", "rating"])
watch_history = watch_history[watch_history["rating"].between(1, 5)]

# Combine viewing events with movie titles and user names.
viewing_data = watch_history.merge(movies, on="movie_id", how="inner")
viewing_data = viewing_data.merge(users, on="user_id", how="inner")

print("Valid viewing records after cleaning:", len(watch_history))
print("Matched viewing records after merging:", len(viewing_data))
print("Unmatched records excluded:", len(watch_history) - len(viewing_data))
print(viewing_data[["name", "title", "genres", "rating"]].head())

movie_views = viewing_data["title"].value_counts()
average_ratings = viewing_data.groupby("title")["rating"].mean().sort_values(ascending=False)

# Some movies have more than one genre. Count each matching genre.
genre_views = viewing_data.assign(
    genre=viewing_data["genres"].str.split("|", regex=False)
).explode("genre")["genre"].value_counts()

print("Total views in sample:", len(viewing_data))
print("Unique viewers:", viewing_data["user_id"].nunique())
print("Average rating:", round(viewing_data["rating"].mean(), 2))
print("\nViews per movie:\n", movie_views)
print("\nView events involving each genre:\n", genre_views)

plt.figure(figsize=(9, 4))
movie_views.plot(kind="bar")
plt.title("Recorded Viewing Events by Movie")
plt.xlabel("Movie")
plt.ylabel("Number of viewing events")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("charts/01_movie_views.png", dpi=150)
plt.close()

plt.figure(figsize=(9, 4))
average_ratings.plot(kind="bar")
plt.title("Average Viewer Rating by Movie")
plt.xlabel("Movie")
plt.ylabel("Average rating (1 to 5)")
plt.ylim(0, 5.5)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("charts/02_movie_ratings.png", dpi=150)
plt.close()

plt.figure(figsize=(9, 4))
genre_views.plot(kind="bar")
plt.title("Viewing Events Associated with Each Genre")
plt.xlabel("Genre")
plt.ylabel("Events involving the genre")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("charts/03_genre_views.png", dpi=150)
plt.close()

print("Notebook finished successfully — 3 charts created in the charts folder.")

