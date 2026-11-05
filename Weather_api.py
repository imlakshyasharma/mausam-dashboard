import requests
import streamlit as st

@st.cache_data(ttl=600)
def get_weather(city):
    ...

API_key = "8d063d789128c54c67be8900ecc80023"   # apni key yahan (ya .env wala tareeka, jo bhi tum use kar rahe ho)

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    return {
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "wind_speed": round(data["wind"]["speed"] * 3.6, 1),
        "condition": data["weather"][0]["main"],
    }

