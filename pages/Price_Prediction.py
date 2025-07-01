import streamlit as st
import pickle
import numpy as np
import pandas as pd 


st.set_page_config(page_title='hourse price prediction ')


st.sidebar.title("🏡 Price Prediction & Recommender System")

with open('./datasets/df.pkl','rb') as file:
    df=pickle.load(file)


with open('./datasets/pipeline.pkl','rb') as file:
    pipeline=pickle.load(file)

st.title("📊 Property Price Prediction")

st.write("Your price prediction UI goes here.")


property_type = st.selectbox('property type ',['flat','house'])

sector= st.selectbox('sector',sorted(df['sector'].unique().tolist()))

bedrooms= float(st.selectbox('no of bedrooms',sorted(df['bedRoom'].unique().tolist())))

bathroom= float(st.selectbox('no of bathrooms',sorted(df['bathroom'].unique().tolist())))

balcony= st.selectbox('no of balcony',sorted(df['balcony'].unique().tolist()))

property_age= st.selectbox('property age',sorted(df['agePossession'].unique().tolist()))

built_up_area=  float(st.number_input('built_up_area'))

servant_room=float(st.selectbox('servant room',[0.0,1.0]))

store_room=float(st.selectbox('store room',[0.0,1.0]))


furnishing_type=st.selectbox('furnishing type',sorted(df['furnishing_type'].unique().tolist()))

luxury_category=st.selectbox('luxury category',sorted(df['luxury_category'].unique().tolist()))

floor_category=st.selectbox('floor category',sorted(df['floor_category'].unique().tolist()))

if st.button('predict'):
    data=[[property_type,sector,bedrooms,bathroom,balcony,property_age,built_up_area,servant_room,store_room,furnishing_type,luxury_category,floor_category]]
    columns= ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
       'agePossession', 'built_up_area', 'servant room', 'store room',
       'furnishing_type', 'luxury_category', 'floor_category']
    c=pd.DataFrame(data,columns=columns)

    st.dataframe(c)
    baseprice=np.expm1(pipeline.predict(c))
    low= baseprice-0.22
    high= baseprice+0.22

    st.text("the price of the flat is between {} cr and {} cr ".format(low,high))