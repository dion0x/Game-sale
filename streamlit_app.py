import streamlit as st
import pandas as pd

# Load the CSV file from the current directory
file_path = 'vgchartz-2024 (1).csv'  # Use the correct relative path
game_sales_data = pd.read_csv(file_path, on_bad_lines='skip')  # Skip bad lines

# Page Title
st.title("Video Game Sales Dashboard")

# Display Dataset
st.subheader("Dataset Overview")
st.write(game_sales_data.head())

# Filter games by console, genre, or publisher
console_options = game_sales_data['console'].unique().tolist()
genre_options = game_sales_data['genre'].unique().tolist()
publisher_options = game_sales_data['publisher'].unique().tolist()

# Set default values to an empty list for no selections
console_filter = st.multiselect("Select Console", console_options, default=[])
genre_filter = st.multiselect("Select Genre", genre_options, default=[])
publisher_filter = st.multiselect("Select Publisher", publisher_options, default=[])

# Apply filters to the dataset
filtered_data = game_sales_data[
    (game_sales_data['console'].isin(console_filter) | (len(console_filter) == 0)) &
    (game_sales_data['genre'].isin(genre_filter) | (len(genre_filter) == 0)) &
    (game_sales_data['publisher'].isin(publisher_filter) | (len(publisher_filter) == 0))
]

# Display filtered data
st.subheader("Filtered Games")
st.write(filtered_data)

# Sales distribution across regions
st.subheader("Sales Distribution(In Million)")
region_sales = filtered_data[['North American sales', 'Japan sales', 'North American sales', 'other_sales']].sum()

# Streamlit's built-in bar chart
st.bar_chart(region_sales)

# Display top 10 games by total sales
st.subheader("Top 10 Games by Total Sales")
top_games = filtered_data.nlargest(10, 'total_sales')
st.write(top_games[['title', 'total_sales']])
