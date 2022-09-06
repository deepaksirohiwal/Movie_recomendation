import streamlit as st
import pickle

movie_list= pickle.load(open('movie_name.pkl','rb'))
movie_list=movie_list['title_x'].values
st.title('Movie Recommender System')


selected_movie = st.selectbox(
     'Type movie/select movie name',
     movie_list)
if st.button('Recommend me !'):
     st.write(selected_movie)

