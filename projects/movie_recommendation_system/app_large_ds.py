import pandas as pd
import numpy as np
from scipy.sparse import coo_matrix, csr_matrix
import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter
from itertools import chain

# Function to reduce memory usage
def reduce_memory_usage(df):
    start_mem = df.memory_usage().sum() / 1024**2
    for col in df.columns:
        col_type = df[col].dtype
        if col_type != object:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                df[col] = pd.to_numeric(df[col], downcast='integer')
            else:
                df[col] = pd.to_numeric(df[col], downcast='float')
    end_mem = df.memory_usage().sum() / 1024**2
    return df

# Load data
movies = pd.read_csv('ml-32m/movies.csv')
movies = reduce_memory_usage(movies)

ratings = pd.read_csv('ml-32m/ratings.csv')
ratings = reduce_memory_usage(ratings)

# Merge and preprocess
movie_ratings = pd.merge(ratings, movies, on='movieId')
del ratings, movies  # Free memory
movie_ratings.drop_duplicates(inplace=True)

# Directly create sparse matrix
user_ids = movie_ratings['userId'].astype('category').cat.codes
movie_ids = movie_ratings['title'].astype('category').cat.codes
ratings = movie_ratings['rating'].values

user_movie_matrix_sparse = coo_matrix((ratings, (user_ids, movie_ids))).tocsr()

user_map = movie_ratings['userId'].astype('category').cat.categories
movie_map = movie_ratings['title'].astype('category').cat.categories

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
selected_movie = st.selectbox('Choose a movie:', movie_map)

# Number of recommendations
num_recommendations = st.slider('Number of Recommendations:', 1, 10, 5)

# Display recommendations
if st.button('Recommend'):
    movie_id = np.where(movie_map == selected_movie)[0][0]
    similar_movie_ids = user_movie_matrix_sparse.T.dot(user_movie_matrix_sparse[:, movie_id].T).toarray().ravel()
    similar_movies = [(movie_map[i], similar_movie_ids[i]) for i in np.argsort(similar_movie_ids)[::-1][:num_recommendations]]
    for movie, score in similar_movies:
        st.write(f'{movie} - Similarity Score: {score:.2f}')
