import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD
from scipy.sparse import csr_matrix
import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter
from itertools import chain

# Load the data in chunks to handle large datasets
def load_data_in_chunks(file_path, chunksize=100000):
    chunks = []
    for chunk in pd.read_csv(file_path, chunksize=chunksize):
        chunks.append(chunk)
    return pd.concat(chunks, axis=0)

# Load movies and ratings data
movies = pd.read_csv('ml-32m/movies.csv')
ratings = load_data_in_chunks('ml-32m/ratings.csv')

# Merge movies and ratings on movieId
movie_ratings = pd.merge(ratings, movies, on='movieId')

# Drop duplicates if any
movie_ratings.drop_duplicates(inplace=True)

# Extract useful features
movie_ratings = movie_ratings[['userId', 'movieId', 'rating', 'title', 'genres']]

# Create a pivot table (user-movie matrix)
user_movie_matrix = movie_ratings.pivot_table(index='userId', columns='title', values='rating')

# Fill NaN values with 0s for similarity calculation and convert to sparse matrix
user_movie_matrix_sparse = csr_matrix(user_movie_matrix.fillna(0).values)

# Apply Truncated SVD for dimensionality reduction
svd = TruncatedSVD(n_components=50)
user_movie_matrix_reduced = svd.fit_transform(user_movie_matrix_sparse)

# Calculate cosine similarity on the reduced matrix
movie_similarity = cosine_similarity(user_movie_matrix_reduced.T)

# Convert similarity matrix to a DataFrame
movie_similarity_df = pd.DataFrame(movie_similarity, index=user_movie_matrix.columns, columns=user_movie_matrix.columns)

# Function to recommend movies based on a given movie title
def recommend_movies(movie_title, num_recommendations=5):
    if movie_title in movie_similarity_df:
        similar_movies = movie_similarity_df[movie_title].sort_values(ascending=False)[1:num_recommendations+1]
        return similar_movies
    else:
        return None

# Streamlit UI
st.title('Movie Recommendation System')

# Exploratory Data Analysis (EDA) - Rating Distribution
if st.checkbox('Show Rating Distribution'):
    plt.figure(figsize=(8, 6))
    movie_ratings['rating'].hist(bins=30)
    plt.title('Distribution of Movie Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Count')
    st.pyplot(plt)

# Exploratory Data Analysis (EDA) - Genre Popularity
if st.checkbox('Show Genre Popularity'):
    genres_split = movie_ratings['genres'].str.split('|')
    genre_count = Counter(chain.from_iterable(genres_split))
    plt.figure(figsize=(10, 6))
    plt.bar(genre_count.keys(), genre_count.values())
    plt.title('Genre Popularity')
    plt.xlabel('Genre')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    st.pyplot(plt)

# Select a movie from the list
selected_movie = st.selectbox('Choose a movie:', user_movie_matrix.columns)

# Number of recommendations
num_recommendations = st.slider('Number of Recommendations:', 1, 10, 5)

# Display recommendations
if st.button('Recommend'):
    recommendations = recommend_movies(selected_movie, num_recommendations)
    if recommendations is not None:
        st.write('Recommended Movies:')
        for movie, similarity in recommendations.items():
            st.write(f'{movie} - Similarity: {similarity:.2f}')
    else:
        st.write('No recommendations found. Please try another movie.')
