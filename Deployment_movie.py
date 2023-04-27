import streamlit as st
import pandas as pd
import pickle
import requests
import certifi

def movie_poster(movieid):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=83766519875d54927b6ec415849dc30b&language=en-US'.format(movieid))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
def recommend(movie):
    movieindex=movies[movies['title']==movie].index[0]
    distance=similarity[movieindex]
    movieslist=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    movie_posters=[]
    for i in movieslist:
        movie_id=movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        movie_posters.append(movie_poster(movie_id))
    return recommended_movies,movie_posters
movies_list=pickle.load(open('C:/Users/HITESH KRISHNA/Desktop/Projects/ML Projects/movies.pkl','rb'))
movies=pd.DataFrame(movies_list)
similarity=pickle.load(open('C:/Users/HITESH KRISHNA/Desktop/Projects/ML Projects/similarity.pkl','rb'))

st.title(":blue[Movie Recommendation System]")
option=st.selectbox(":red[Select the movie you want to watch!!]",movies['title'].values)
if st.button('Recommend'):
    names,posters=recommend(option)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
 



