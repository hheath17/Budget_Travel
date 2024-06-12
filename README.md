# Budgeting Your Travel

---

## Jupyter Notebook Table of Contents
---
-  [01_fare_cleaning_EDA.ipynb](./data/01_fare_cleaning_EDA.ipynb)
-  [02_airbnb_cleaning_EDA.ipynb](./data/02_airbnb_cleaning_EDA.ipynb)
-  [03_fair_visuals.ipynb](./data/03_fair_visuals.ipynb)
-  [04_airbnb_visuals.ipynb](./data/04_airbnb_visuals.ipynb)
-  [05_airfare_cv_cs.ipynb](./data/05_fare_and_airbnb_rec.ipynb)
-  [06_fare_bnb_rec_sys.ipynb](./data/06_fare_and_airbnb_rec.ipynb)
-  [07_streamlit_app.py](./data/07_streamlit_app.py)


## Background & Introduction
---
A couple facts from others below.

According to Guardian research, American workers experienced a significant 16% decline in self-reported financial health from 2022 to 2023...over a third of employees experienced increased anxiety, depression, or other mental health needs in the past two years.2 With money tight, and stress levels high, a vacation may be exactly what you need. But vacations can be costly, so it’s essential to plan ahead and budget accordingly so you can make the most of your getaway. - guardianlife.com 

In the U.S., a one-week vacation for a solo traveler costs about \\$1,984, while a family of four can cost around \\$7,936. - gogocharters.com

As travel becomes more and more expensive I was curious to create a resource that would provide travelers help in determining some locations that fit within their budget.  



## Resources
---
-  [AFAR.com](https://www.afar.com/magazine/best-large-cities-in-the-united-states-to-live-in-and-visit)
-  [Guardianlife.com](https://www.guardianlife.com/how-to-budget-for-a-vacation)
-  [Travel Trends](https://theilha.com/shifting-travel-trends-in-the-us-financial-constraints-and-sustainability-drive-consumer-behavior/)
-  [Average Vacation Costs](https://gogocharters.com/blog/average-vacation-cost/#:~:text=Average%20Vacation%20Costs%20in%202024%3A%20Transportation%2C%20Entertainment%2C%20and%20Budgeting%20Tips&text=Quick%20Answer%3A%20In%20the%20U.S.,four%20can%20cost%20around%20%247%2C936)


## Problem Statement
---
Many individuals face financial constraints yet still desire the ability to live, explore, and travel to maintain their well-being. The challenge is to provide travelers with options for flights and accommodations that fit within a specified budget. This project aims to develop a solution using data from Airbnb and past flight fares to identify the top five cities a traveler can visit within their budget.

To address this, we will implement a recommender system that offers personalized travel recommendations. Additionally, a Streamlit App will be created, allowing users to input their starting city and budget range. The app will then return the top five destinations that meet the user's financial budget for both airfare.  From there the traveler is then able to move on in the app and select their desired city under the Airbnb portion of the app and budget contraints, in which the app will provide Airbnb data for them to research room ID's on the Airbnb app. 

Cities utilizied in this project are listed below.  These are top US cities for travel. 

-  Chicago
-  Columbus 
-  Denver   
-  Las Vegas 
-  Los Angeles
-  Nashville 
-  New Orleans
-  New York City  
-  Portland  
-  San Diego  
-  San Francisco   
-  Seattle 
-  Washington           
               

# Dataset Dictionary
---


| Feature       | Data Type | Description                                                               |
|-------------------|-----------|---------------------------------------------------------------------------|
| air_bnb_data_clean.csv           | int/str       | Cleaned Airbnb data.                                           |
| air-bnb-listings-to-use.csv     | int/str    | Airbnb dataset from Kaggle.                                |
| consumer_airfare_report_US.csv  | int/str    | Airfare dataset from data.gov.           |
| fare_result_df.csv   | int/str       | Flight fare results after CountVectorizer and Recommender System created.                                               |
| flight_data_clean.csv | int/str       |Cleaned flight data.                             |


## Dataset Sources
---
-  [Airbnb Dataset from Kaggle](https://www.kaggle.com/datasets/joyshil0599/airbnb-listing-data-for-data-science)
-  [Airfare Dataset from Data.gov](https://catalog.data.gov/dataset/consumer-airfare-report-table-1a-all-u-s-airport-pair-markets)


## Analysis 
---
Cleaning and EDA was completed on both datasets where nulls were eliminated, duplicates were looked at along with outliers. CountVectorizer was used to convert the textual data in the flight fare dataset into a matrix of tokens, I then completed cosine similarities within this dataset to provide some insight on the relationship between departure city and arrival cities that would work within the recommender system.  I also tried to do this on the Airbnb dataset but ultimately decided that travel starts with airfare so a recommender system would only be created with simple python code to narrow down Airbnb recommendations based on user input of city they decided to select from the airfare recommender.  The cosine similarities within the flight fare dataset explored the relationships between departure and arrival cities.  This provided insights into which city pairs are most similar, which helps with the recommender system.  The cosine similarity metric helped measure the similarity between flight routes similer to the travelers starting city based on patterns and popularity of the destination.

Libraries Used
-  Pandas
-  Matplotlib
-  Seaborn
-  Sklearn

## Recommendations & Conclusions
---

It is fairly easy to travel on a budget with a little research and providing specific parameters.  The cosine similarity anaylsis helped identify flight routes that align with the traveler's preference. Combining this with the user input formed the basis of teh recommender system which can guide travelers with both flight and lodging. 

Further research and data collection could improve this streamlit app.  Continuous user feedback can be used to refine and improve the recommender system over time, also keeping it relevant and precise.  Gathering more data including things like user preferences, seasonal trends and travel patterns could enhance the accuracy of the recommender system.  





