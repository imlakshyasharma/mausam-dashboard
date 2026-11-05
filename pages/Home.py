import streamlit as st
import pandas as pd
import numpy as np

# Defines the pages
home = st.Page("app_by_Lakshya.py", title="Home", default=True)
personalise = st.Page("pages/Personalise.py", title="Personalise")

# Register navigation
pg = st.navigation([home, personalise], position="hidden")

# This is the API code
from Weather_api import get_weather

# "Delhi NCR" ko API samajhti nahi, isliye mapping
city_map = {
    "Delhi NCR": "Delhi",
    "Noida": "Noida",
    "Mumbai": "Mumbai",
    "Jaipur": "Jaipur",
}

col1, col2, col3 = st.columns([3, 3, 1])

with col1:
    st.header("Mausam 🌤️")

with col2:
    selected = st.selectbox(
        "City",
        list(city_map.keys()),
        key="city",
        label_visibility="collapsed",
    )

with col3:
    st.write("")
    if st.button("✨ Personalise", use_container_width=True):
        st.switch_page("pages/Personalise.py")

weather = get_weather(city_map[selected])
# ... rest of our dashboard ...


col4, col5 = st.columns(2)
with col4:
    st.write("Good Morning!👋🏻")
    st.markdown(f"Feels like {weather['feels_like']}°C")
    
with col5:
    st.write("WEATHER RISK")
    st.markdown(f"""
<div>
    <div style="font-size: 65px; font-weight: bold; line-height: 1;">{weather['temperature']}°C</div>
    <div style="font-size: 20px; margin-top: 5px;">Moderate</div>
</div>
""", unsafe_allow_html=True)
    st.subheader("Sunny ☀️")

st.divider()

col6, col7, col8, col9  = st.columns(4)
col6.metric("AQI", "123", "") 
col7.metric("Wind speed💨", f"{weather['wind_speed']}km/h", "")
col8.metric("Humidity 💧", f"{weather['humidity']}%", "")
st.subheader(f"{weather['condition']} ☀️")
col9.metric("☀️ UV Levels", "9") 

st.divider()

st.header("Today's highlights")
col10, col11, col12 = st.columns(3)
col10.error("🌡️ High temperature")
col11.error("☀️ High UV exposure")
col12.warning("💨 Windy weather")

import pandas as pd
import numpy as np
import streamlit as st

st.subheader("📊 24-Hour Forecast")

# Dummy data: 24 hourly points, starting from current hour
hours = pd.date_range(start="2026-09-12 00:00", periods=24, freq="h").strftime("%H:%M")

chart_data = pd.DataFrame(
    np.random.randn(24, 1) / 3 + 32,   # values wobbling around 32°C
    columns=["Temperature (°C)"],
    index=hours
)

st.line_chart(chart_data)

def set_background_image(url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background_image("https://images.unsplash.com/photo-1419833173245-f59e1b93f9ee?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
