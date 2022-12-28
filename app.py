import pickle
import streamlit as st
from tmdbv3api import Movie, TMDb

movie = Movie()
tmdb = TMDb()
tmdb.api_key = '034b7a8b06d378cd54055e179ab07b94'
tmdb.language = 'ko-KR'

def get_rec(title):
    idx = movies[movies['title']==title].index[0]
    sim_score = list(enumerate(cos_sim[idx]))
    sim_score = sorted(sim_score, key=lambda x: x[1], reverse=True)
    sim_score = sim_score[1:11]
    movie_indices = [i[0] for i in sim_score]
    images = []
    titles = []
    for i in movie_indices:
        id = movies['id'].iloc[i]
        details = movie.details(id)
        image_path = details['poster_path']
        if image_path:
            image_path = 'https://image.tmdb.org/t/p/w500' + image_path
        else:
            image_path = 'no_image.jpg'
        images.append('https://image.tmdb.org/t/p/w500'+details['poster_path'])
        titles.append(details['title'])
    return images, titles

movies = pickle.load(open('movies.pickle', 'rb'))
cos_sim = pickle.load(open('cos_sim2.pickle', 'rb'))

st.set_page_config(layout='wide')
st.header('my movie')

movie_list = movies['title'].values
title = st.selectbox('choose a movie', movie_list)
if st.button('recommand'):
    with st.spinner('wait..'):
        images, titles = get_rec(title)
        idx=0
        for i in range(0,2):
            cols = st.columns(5)
            for col in cols:
                col.image(images[idx])
                col.write(titles[idx])
                idx += 1