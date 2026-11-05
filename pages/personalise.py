import streamlit as st

st.title("✨ Personalise your Mausam")

st.write("Tell us what matters to you:")

air_quality = st.checkbox("🌫️ Air Quality")
uv = st.checkbox("☀️ UV")
rain = st.checkbox("🌧️ Rain")
temperature = st.checkbox("🌡️ Temperature")
outdoor = st.checkbox("🏏 Outdoor Activities")

if st.button("Save Preferences"):

    st.session_state["preferences"] = {
        "air_quality": air_quality,
        "uv": uv,
        "rain": rain,
        "temperature": temperature,
        "outdoor": outdoor
    }

    st.success("Preferences saved!")