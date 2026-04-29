import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    # the index of that given movie
    movie_index = movies[movies['title'] == movie].index[0]
    # the distance/similarity of that movie with other
    distance = similarity[movie_index]
    # that 5 recommendation of similar movies
    movie_list = sorted(list(enumerate(similarity[0])), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    for i in movie_list:
        # title of that recommended index of movies
        recommended_movies.append(movies.loc[i[0]].title)

    return recommended_movies
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommendation System')

select_movie_name=st.selectbox('How would like to be contacted?',movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(select_movie_name)
    for i in recommendations:
        st.write(i)
    