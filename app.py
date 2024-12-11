import pickle
import streamlit as st
import requests

# Use the Dune 2020 poster as a placeholder when no poster is found
PLACEHOLDER_IMAGE_URL = "https://www.hdwallpapers.in/download/poster_of_dune_2020_4k_hd_movies-HD.jpg"

def fetch_poster(movie_id):
    # TMDB API URL to get movie details
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url)
    data = data.json()

    # Check if the 'poster_path' is available
    if 'poster_path' in data:
        poster_path = data['poster_path']
        # Construct the full URL for the poster image
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    else:
        # Return the Dune 2020 poster image URL if no poster is found
        return PLACEHOLDER_IMAGE_URL

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        # Get poster or placeholder image
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    
    return recommended_movie_names, recommended_movie_posters

# Streamlit UI
st.header('Sistem Expert pentru recomandarea filmelor')

# Load the movie data and similarity matrix
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Alegeti filmul/tv dorit",
    movie_list
)

if st.button('Recomandati'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
