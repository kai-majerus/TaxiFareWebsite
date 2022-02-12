import streamlit as st
import datetime
import requests
import numpy as np

st.set_page_config(
            page_title="Taxi Fare Predictor", # => Quick reference - Streamlit
            page_icon="🚕",
            layout="centered", # wide
            initial_sidebar_state="auto") # collapsed

'''
# TaxiFareModel
'''
columns = st.columns(3)
d = columns[0].date_input('Date')
t = columns[1].time_input('Time', datetime.time())
passenger_count = columns[2].slider('Passenger count', min_value=1, max_value=10, step=1)

pickup_columns = st.columns(2)
pickup_longitude = pickup_columns[0].number_input('Pickup longitude')
pickup_latitude = pickup_columns[1].number_input('Pickup latitude')

dropoff_columns = st.columns(2)
dropoff_longitude = dropoff_columns[0].number_input('Dropoff longitude')
dropoff_latitude = dropoff_columns[1].number_input('Dropoff latitude')


st.write(f'Taxi on {d} at {t} for {passenger_count} passengers starting at {pickup_longitude}, {pickup_latitude} and ending at {dropoff_longitude}, {dropoff_latitude}')

pickup_datetime = datetime.datetime.combine(d, t)

url = 'https://taxifare.lewagon.ai/predict'
params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

response = requests.get(url, params=params)
prediction = np.round(response.json()['fare'], 2)
st.markdown("""
# Predicted Fare"""
)
st.metric("",f"${prediction}")
