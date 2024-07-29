import streamlit as st
import pandas as pd
st.set_page_config(page_title='jagadeepnew')
st.header('PYTHON')
st.subheader('DEF FUNCTION IN PYTHON')
st.markdown('Def in python which is used to define the value')
data=pd.read_csv('tshirt_buyers_sample_data.csv')
submit=st.checkbox('submit')
if submit:
    st.dataframe(data)
    st.radio('chose one:',('a','b','c','d'))


   