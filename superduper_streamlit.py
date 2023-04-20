# simple_streamlit_app.py
"""
A streamlit app to provide dupe skincare products - 
i.e. users choose an expensive product and the SuperDuper
offers another that is both similar and cheaper.

"""
import pandas as pd
import streamlit as st
import pickle
from sklearn.neighbors import NearestNeighbors
import time

# Load the data
df_ing = pd.read_csv("data/products_data.csv")
df_ing = df_ing.sort_values(['brand', 'product_names'], ascending=(True, True))

# Load the pickle file containing the features
with open("features.pkl", "rb") as f:
    features = pickle.load(f)

# Fit the KNN model
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
        price_diff = product_price - price
        if name == product_name:
            pass
        elif price_diff > 10:
            product_list.append(f"{name} from {brand}, ${price:.2f} with ${price_diff:.2f} savings")
        
    return product_list

st.title('SuperDuper')
st.write("A duping app for your favorite overpriced skincare product! 🧴")
st.markdown("![Alt Text](https://assets.vogue.com/photos/5be9f45a6bcde32d294138f6/master/w_1600,c_limit/00-story-beauty-gifts.gif)")

# Create the dropdown menus
brands = df_ing.brand.unique()
selected_brand = st.selectbox("Choose a brand", brands)

brand_products = df_ing[df_ing.brand == selected_brand].product_names.unique()
selected_product = st.selectbox("Now pick a product", brand_products)
progress_text = "Finding dupes."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text=progress_text)

# Call the SuperDuper function with the selected product and display the results
results = SuperDuper(selected_product)
if len(results) == 0:
    st.write("You already found the cheapest product! Well done, you.")
else:
    st.write("DUUUUUUUUUUUUPE:")
    for product in results:
        st.write(product)
