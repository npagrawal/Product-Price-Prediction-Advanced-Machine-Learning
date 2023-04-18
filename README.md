# Predicting Prices Using Neural Networks for Regression Analysis

The cosmetics industry brought in an estimated $262.21 billion in 2022 and is due to continue growing this year. Skincare in particular has seen an increased interest as the culture has shifted away from the glam beauty standards of the recession-era 2000s to embrace a more "natural" beauty.

My stakeholder, Inner Glow Inc., wants to make their mark on the skincare industry by coming out with their own line of products that are competetive with what's available. To do this, they first need to understand the current market and determine where they can undercut more expensive alternatives. Rampant upcharge in the skincare industry is obvious when products can range from $7-400. How can Inner Glow Inc. offer mid-line products that capture both a high-end and low-end market?

Using neural networks and XGBoost, I look at data from NoxMoon's "Inside Beauty" project, scraped from Beautypedia and Paula’s choice websites, and data I scraped myself from the Dermstore. The two datasets include product names, brands, prices, ingredients, size, and product type. There are over 7000 products at the end of cleaning. Features include one-hot encoded "special" ingredients (i.e. not ones that appear in every single product but do in a good amount of them), peptide, oil, and extract counts, and number of active and inactive ingredients, among others.

After tuning a series of neural networks, using XGBoost, and using grid search to tune XGBoost, I find in the end that the untuned XGBoost does the best with the data, scoring an MAE on the test around $17. Given the spread of product prices, this doesn't seem way off base. Features engineering determines certain ingredients, like Isopropyl Misorate, have a marginal level of importance when it comes to price. The most often overpriced brands are iS Clinical, Clarins, and SK-II, while the most underpriced ones are Neutrogena, Clinique, and L'Oreal Paris. Therefore, Inner Beauty Inc. should try to dupe the overpriced brands' products with prices that are on average higher than the underpriced ones.

I put all these findings together into the Streamlit app SuperDuper which offers users the chance to dupe their favorite high-end products and find cheaper alternatives that are at the ingredient-level similar.



[Find the app here:](https://npagrawal-product-price-prediction--superduper-streamlit-ftfs2j.streamlit.app/)
