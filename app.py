import streamlit as st
import pickle
import requests
from PIL import Image

def fetch_info(movie_id):
     response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ca81ad677ec863a95b58ce30413e5641'.format(movie_id))
     data=response.json()
     images="https://image.tmdb.org/t/p/w500"+data['poster_path']
     desc=data['overview']
     name=data['original_title']
     
     return images,desc,name

cosine_sim=pickle.load(open('pickle\cosine.pkl','rb'))
#recommendation function 
def get_recommendations(title,cosine_sim=cosine_sim):

    #index of the movie
    idx=indices[title]
    #pairwise similarity scores of all movies with the movie
    sim_scores=list(enumerate(cosine_sim[idx]))

    #sort the sim_scores and taking the top 10 movies
    sim_scores=sorted(sim_scores,key=lambda x:x[1],reverse=True) #sorted on the basis of the element on index 1
    
    sim_scores=sim_scores[1:11]

    movie_indices=[i[0] for i in sim_scores]    
    movie_name=movie_list_df['title_x'].iloc[movie_indices]
    movie_id=movie_list_df['id'].iloc[movie_indices]
    #return top 10 movies
    movie_poster=[fetch_info(id) for id in movie_id]
    return movie_poster
    
#fecting movies poster and discription




#importing movie details
movie_list_df= pickle.load(open('pickle\movie_name.pkl','rb'))
movie_list=movie_list_df['title_x'].values
#index of the movie
indices=pickle.load(open('pickle\indices.pkl','rb'))

#streamlit UI
st.title('Movie Recommender System')


selected_movie = st.selectbox(
     'Type movie/select movie name',
     movie_list)


if st.button('Recommend me !'):
     list_of_rec=get_recommendations(selected_movie)
    
     for i in list_of_rec:
          
          
          col1,col2=st.columns(2)
          with col1:
               st.image(i[0],width=100)
               st.write(i[2])
          with col2:
               st.write(i[1])
               #st.write(desc[i])

              
