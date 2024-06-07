import pandas as pd
import tkinter as tk
from tkinter import messagebox

# Load the movies and ratings data
movies = pd.read_csv('movies.csv', encoding='latin1')
ratings = pd.read_csv('ratings.csv', encoding='latin1')

# Merge movies with ratings
data = pd.merge(ratings, movies, on='movieId')

# Function to filter movies based on genre
def filter_movies_by_genre(data, genre):
    genre_movies = data[data['genres'].str.contains(genre, case=False)]
    return genre_movies

# Function to get top movies by genre based on average ratings
def get_top_movies_by_genre(data, genre, n=5):
    genre_movies = filter_movies_by_genre(data, genre)
    top_movies = genre_movies.groupby('title')['rating'].mean().sort_values(ascending=False).head(n)
    return top_movies

# Function to recommend top n movies for a given genre
# Function to recommend top n movies for a given genre
def recommend_top_movies(genre, n=5):
    top_movies = get_top_movies_by_genre(data, genre, n)
    return top_movies, n

# Function to handle button click
def get_recommendations():
    genre = genre_entry.get()
    if genre:
        top_movies, n = recommend_top_movies(genre)
        recommendations = "\n".join([f"{title}: {rating:.2f}" for title, rating in top_movies.items()])
        messagebox.showinfo(f"Top {n} {genre} movies", recommendations)
    else:
        messagebox.showwarning("Input Error", "Please enter a genre")

# Create the main window
root = tk.Tk()
root.title("Movie Recommendation System")

# Create and place the widgets
tk.Label(root, text="Enter Genre:").grid(row=0, column=0, padx=10, pady=10)
genre_entry = tk.Entry(root)
genre_entry.grid(row=0, column=1, padx=10, pady=10)

recommend_button = tk.Button(root, text="Get Recommendations", command=get_recommendations)
recommend_button.grid(row=1, columnspan=2, pady=10)

# Run the application
root.mainloop()
