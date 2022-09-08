import streamlit as st
import pickle


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

    #return top 10 movies
    return movie_list_df['title_x'].iloc[movie_indices]
    
#fecting movies poster and discription
'''
a. fetch the poster and display
b. fetch the movie discription
addition details 
In which platform is it available
'''



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
     st.write(get_recommendations(selected_movie))


