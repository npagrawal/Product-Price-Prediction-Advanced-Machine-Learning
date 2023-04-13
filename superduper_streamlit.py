# simple_streamlit_app.py
"""
A streamlit app to provide dupe skincare products - 
i.e. users choose an expensive product and the SuperDuper
offers another that is both similar and cheaper.

"""

import streamlit as st
import pandas as pd

products_data = pd.read_csv("data/products_data.csv")
features = pd.read_csv("data/features.csv")

model = NearestNeighbors(n_neighbors=2, algorithm='ball_tree')
model.fit(features)
dist, idlist = model.kneighbors(features)

def SuperDuper(product_name):
    product_list = []
    product_id = df_ing[df_ing["product_names"] == product_name].index
    product_id = product_id[0]
    product_price = df_ing["price"].iloc[product_id] 
    for newid in idlist[product_id]:
        name = df_ing.loc[newid].product_names
        brand = df_ing.loc[newid].brand
        price = df_ing.loc[newid].price
        if name == product_name:
            pass
        elif price < product_price:
            product_list.append(f"{name} from {brand}, ${price: .2f}")
        
    return product_list 

brand_list = products_data["brand"].values
selected_brand = st.selectbox( "Choose a brand from the dropdown menu", brand_list )
product_list = products_data["product_names"].values
selected_product = st.selectbox( "Choose a brand from the dropdown menu", product_list )

if st.button('Dupe!'):
      recommended_products = SuperDuper(selected_product)
      recommended_products
