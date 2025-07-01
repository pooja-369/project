import streamlit as st
import pickle
import numpy as np
import pandas as pd 
import os 


st.title("🏡 Property Recommender")
st.sidebar.title("🏡 Price Prediction & Recommender System")

st.write("Your recommendation UI goes here.")

st.set_page_config(page_title='recommender apartment ')

base_path = os.path.dirname(__file__)
datasets_path = os.path.abspath(os.path.join(base_path, '..', 'datasets'))

with open(os.path.join(datasets_path, 'location_distance.pkl'), 'rb') as f:
    location_df = pickle.load(f)

with open(os.path.join(datasets_path, 'cosine_sim1.pkl'), 'rb') as f:
    cosine_sim1 = pickle.load(f)

with open(os.path.join(datasets_path, 'cosine_sim2.pkl'), 'rb') as f:
    cosine_sim2 = pickle.load(f)

with open(os.path.join(datasets_path, 'cosine_sim3.pkl'), 'rb') as f:
    cosine_sim3 = pickle.load(f)




def recommend_properties_with_scores(property_name, top_n=5):
    
    cosine_sim_matrix = 30*cosine_sim1 + 20*cosine_sim2 + 8*cosine_sim3
    # cosine_sim_matrix = cosine_sim3
    
    # Get the similarity scores for the property using its name as the index
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    
    # Sort properties based on the similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the indices and scores of the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n+1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n+1]]
    
    # Retrieve the names of the top properties using the indices
    top_properties = location_df.index[top_indices].tolist()
    
    # Create a dataframe with the results
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })
    
    return recommendations_df




st.title('Local conveniences!')
st.write()

selectedlocation = st.selectbox('location',sorted(location_df.columns.tolist()))

radius = st.number_input('Radius in kms')

if st.button('Search'): 
    searchList =location_df[location_df[selectedlocation]<radius*1000] [selectedlocation].sort_values()

    for key,value in searchList.items():
        st.text(str(key)+"   -   "+str(value/1000)+ "kms")


st.title('Apartments similar to your choice !')

selectedApartment=st.selectbox('select an apartment',sorted(location_df.index.to_list()))


if st.button('Recommend'):
    result=recommend_properties_with_scores(selectedApartment)
    st.dataframe(result)



   