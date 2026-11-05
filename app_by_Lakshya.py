# app_by_Lakshya.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_key = os.getenv("API_KEY")

import streamlit as st

home = st.Page("pages/Home.py", title="Home", default=True)
personalise = st.Page("pages/Personalise.py", title="Personalise")

pg = st.navigation([home, personalise], position="top")
pg.run()