# simple_streamlit_app.py
"""
A streamlit app to provide dupe skincare products - 
i.e. users choose an expensive product and the SuperDuper
offers another that is both similar and cheaper.

"""
!pip install sklearn
import pandas as pd
import streamlit as st
import pickle
from sklearn.neighbors import NearestNeighbors


# Load the data
df_ing = pd.read_csv("data/products_data.csv")

# Load the pickle file containing the features
with open("features.pkl", "rb") as f:
    features = pickle.load(f)

# Fit the KNN model
model = NearestNeighbors(n_neighbors=2, algorithm='ball_tree')
model.fit(features)
dist, idlist = model.kneighbors(features)    
    
def SuperDuper(product_name):
    product_list = []
    product_id = products[products["product_names"] == product_name].index
    product_id = product_id[0]
    product_price = products["price"].iloc[product_id] 
    for newid in idlist[product_id]:
        name = df_ing.loc[newid].product_names
        brand = df_ing.loc[newid].brand
        price = df_ing.loc[newid].price
        if name == product_name:
            pass
        elif price < product_price:
            product_list.append(f"{name} from {brand}, ${price: .2f}")
        
    return product_list 

st.title('SuperDuper')

# Create the dropdown menus
brands = df_ing.brand.unique()
selected_brand = st.selectbox("Choose a brand from the dropdown menu", brands)
brand_products = df_ing[df_ing.brand == selected_brand].product_names.unique()
selected_product = st.selectbox("Now pick a product", brand_products)

# Call the SuperDuper function with the selected product and display the results
results = SuperDuper(selected_product)
if len(results) == 0:
    st.write("No similar products found.")
else:
    st.write("Similar products:")
    for product in results:
        st.write(product)