import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

st.header('🛍️ Dahshboard Brasilia E-Commerce Dataset')

st.title("Distribution of Customers in Brazil")
# Sample DataFrame with 'geolocation_lat', 'geolocation_lng', and 'customer_id' columns
data = pd.read_csv('https://raw.githubusercontent.com/shafirafh/E-Commerce-Public-Dataset/main/customer_geolocation.csv',index_col=0)
customer_data = pd.DataFrame(data)
order_reviews_dataset = pd.read_csv('https://raw.githubusercontent.com/shafirafh/E-Commerce-Public-Dataset/main/order_reviews_dataset.csv',index_col=0)

# Brazil bounding box
BBox = (-72.66670555, -8.577855018, -36.60537441, 42.18400274)

# Load the Brazil map image
brazil = plt.imread("brazil.png")

# Create a figure and axis
fig, ax = plt.subplots(figsize=(15, 15))
ax.scatter(customer_data.geolocation_lng, customer_data.geolocation_lat, zorder=1, alpha=0.9, c='r', s=20)
ax.set_title('Plotting Spatial Data on Brasil Map')
ax.set_xlim(-72.66670555, -8.577855018)
ax.set_ylim(-36.60537441, 42.18400274)
ax.imshow(brazil, zorder=0, extent=BBox, aspect='equal')

# Display the Brazil map using st.image
#st.image(brazil, caption='Brazil Map', use_column_width=True)

# Display the scatter plot using st.pyplot
st.pyplot(fig)

# Optionally, you can add additional streamlit elements, like a table or text
#st.dataframe(customer_data)

#==========================================================================================
def single_countplot(data, x, palette=None):
    sns.set(style="whitegrid")
    ax = sns.countplot(data=data, x=x, palette=palette)

    # Adding percentages
    total = len(data[x])
    for p in ax.patches:
        height = p.get_height()
        ax.text(p.get_x() + p.get_width() / 2., height + 0.1,
                '{:.2%}'.format(height / total),
                ha="center")

# Streamlit app
st.title("Review Score Count Plot with Percentages")

# Sidebar for palette selection
palette_option = st.sidebar.selectbox("Select Color Palette", ['YlGnBu', 'Blues', 'Reds', 'Greens'])

# Display the count plot
fig, ax = plt.subplots(figsize=(10, 5))
single_countplot(data=order_reviews_dataset, x='review_score', palette=palette_option)
st.pyplot(fig)
#==========================================================================================
# Sidebar
st.sidebar.header("Choose your color")
#sidebar_input = st.sidebar.text_input("Enter something in the sidebar", "Type here...")

# Main content
#st.title("Streamlit App with Sidebar")
#st.write(f"You entered: {sidebar_input}")
st.write("Dashboard by shaf_faira")
# Add more content as needed
