import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_csv('../data/flight_data_clean.csv')

#list of cities to keep that line up with Airbnb dataset
cities_to_keep = [
     'Austin', 'Boston', 'Chicago', 'Columbus', 'Denver', 'Ft Lauderdale', 
        'honolulu', 'Jersey City', 'Las Vegas', 'Los Angeles', 'Nashville', 
     'New Orleans', 'New York City', 'Portland', 'Rhode Island', 
     'San Diego', 'San Francisco', 'Seattle', 'Minneapolis', 'Washington'
    ]

#filter the DataFrame to keep only the specified cities in the 'city2' column
df = df[df['city2'].isin(cities_to_keep)]

#define the recommendation function
def recommend_destinations(starting_city, min_budget, max_budget, num_recommendations=5):
#filter the DataFrame based on the budget range
    filtered_df = df[(df['fare'] >= min_budget) & (df['fare'] <= max_budget)]
    
#create a list of all unique destination city
    destination_city = list(filtered_df['city2'].unique())

#vcectorize city2 names with CountVectorizer
    cv = CountVectorizer().fit_transform(destination_city)
    vectors = cv.toarray()
    
#calculate cosine similarity between the starting city and all other cities
    city_index = destination_city.index(starting_city)
    cosine_similarities = cosine_similarity([vectors[city_index]], vectors).flatten()
#create a DataFrame with cities and their similarity scores
    similarity_df = pd.DataFrame({
        'city': destination_city,
        'similarity': cosine_similarities})
    
#merge with the filtered DataFrame to keep only relevant destinations
    result_df = pd.merge(filtered_df, similarity_df, left_on='city2', right_on='city')

#sort by similarity score and remove duplicates
    result_df = result_df.sort_values(by='similarity', ascending=False).drop_duplicates(subset='city2')
#get the recommended cities and their fares
    recommended_cities = result_df[['city2', 'fare']].values
    
#randomly select 5 cities from the recommended cities
    if len(recommended_cities) > num_recommendations:
        recommended_cities = recommended_cities[np.random.choice(len(recommended_cities), num_recommendations, replace=False)]
    
    return recommended_cities

# Title

st.title('Travel within YOUR Budget!')
st.text('Suggestions for your next vacation is just a few entries away!')
st.divider()

starting_city_list = [ 'Chicago', 'Columbus', 'Denver', 
     'Las Vegas', 'Los Angeles', 'Nashville', 
    'New Orleans', 'New York City', 'Portland', 
    'San Diego', 'San Francisco', 'Seattle', 'Washington'
    ]


city1 = st.selectbox('Select Your Starting City', starting_city_list)
st.write('You selected:', city1)

min_budget = st.number_input(label='Enter Minimum Budget for Flight', value=None, placeholder="$50-$500")

max_budget = st.number_input(label='Enter Maximum Budget for Flight', value=None, placeholder="$50-$500")


if st.button(label='Submit', key='1'):
    recommended_cities = recommend_destinations(city1, min_budget, max_budget)

    if recommended_cities is not None:
        st.write(f'Recommended cities and their fares from {city1}:')
        st.dataframe(recommended_cities)

st.divider()

st.subheader('Airbnb Recommendations')

data = pd.read_csv('../data/air_bnb_data_clean.csv')

def simple_recommend_rooms(city, min_budget, max_budget, data):
    # Filter the dataset based on the user input
    filtered_data = data[(data['city'].str.lower() == city.lower()) &
                         (data['room_price'] >= min_budget) &
                         (data['room_price'] <= max_budget)].reset_index(drop=True)
    
    # Sort by room price to get the most relevant results within the budget
    filtered_data = filtered_data.sort_values(by='room_price')
    
    # Get the top 5 rooms
    top_5_rooms = filtered_data.head(5)
    
    # Select the relevant columns to display
    result = top_5_rooms[['room_id', 'neighbourhood', 'room_price', 'city', 'state']]
    
    return result

bnb = ['Boston', 'Chicago', 'Columbus', 'Denver', 
     'Las Vegas', 'Los Angeles', 'Nashville', 
    'New Orleans', 'New York City', 'Portland', 
    'San Diego', 'San Francisco', 'Seattle', 'Washington'
    ]

bnb = st.selectbox('Airbnb', bnb)
st.write('You selected;', bnb)

min_budget = st.number_input(label='Min Budget for Airbnb', value=None, placeholder='$50-$500')

max_budget = st.number_input(label='Max Budget for Airbnb', value=None, placeholder='$50-$500')
if st.button(label='Submit', key='2'):
    result = simple_recommend_rooms(bnb, min_budget, max_budget, data)

    if result is not None:
        st.write(f'Recommended Airbnb {bnb}:')
        st.dataframe(result)
