# simple_streamlit_app.py
"""
A streamlit app to provide dupe skincare products - 
i.e. users choose an expensive product and the SuperDuper
offers another that is both similar and cheaper.

"""

import streamlit as st
from streamlit import session_state as session
%run notebook_4.ipynb
from notebook_4 import SuperDuper


dataframe = None

@st.cache(persist=True, show_spinner=False, suppress_st_warning=True)
def load_data():
    """
    load and cache data
    :return: products data
    """
    features = pd.read_csv("data/features.csv", index_col=0)
    return features


features = load_data()

with open("data/products_data.pickle", "rb") as f:
    products = pickle.load(f)


st.title('SuperDuper')
st.text('Dupe your favorite skincare product!')

st.text("")
st.text("")
st.text("")
st.text("")

session.options = st.multiselect(label="Choose a brand from the dropdown menu", options=products["brand"])

st.text("")
st.text("")

session.options = st.multiselect(label="Now choose a product", options=products["product_names"])

st.text("")
st.text("")

is_clicked = col1.button(label="Recommend")

if is_clicked:
    dataframe = SuperDuper(session.options, product_name=products["product_names"])

st.text("")
st.text("")
st.text("")
st.text("")

if dataframe is not None:
    st.table(dataframe)
