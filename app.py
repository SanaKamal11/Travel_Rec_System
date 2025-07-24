import streamlit as st
import pandas as pd
from recommender import recommend_experiences
from data_loader import load_experiences_data  # or replace with pd.read_csv

# Load your data
experiences_df = load_experiences_data()  # or pd.read_csv("data/experiences.csv")

st.title("🌍 Personalized Travel Recommender")
st.write("✅ Streamlit app loaded!")

with st.sidebar:
    st.header("Tell us about you ✈️")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120)
    budget = st.slider("Budget (USD)", 100, 10000, 1500)
    season = st.selectbox("Preferred Travel Season", ["Any", "Spring", "Summer", "Fall", "Winter"])
    interests = st.multiselect(
        "Select Interests",
        ["Culture", "Adventure", "Relaxation", "Food", "Nature", "Nightlife", "History"]
    )

# Convert inputs into user_vector
def build_user_vector(age, budget, season, interests):
    return {
        "age": age,
        "budget": budget,
        "season": season,
        "interests": interests
    }

user_vector = build_user_vector(age, budget, season, interests)

# Recommendation logic trigger
# Recommendation logic trigger
if st.button("Get Recommendations"):
    if not interests:
        st.warning("⚠️ Please select at least one interest.")
    elif budget < 300:
        st.error("Your budget might be too low for international travel.")
    else:
        # --- TEST MODE: manually display first 5 rows of data ---
        st.subheader("🏙️ Sample City")
        st.write("Top 5 Recommended Experiences:")
        sample_data = experiences_df.head(5)
        st.dataframe(sample_data)


st.markdown("---")
st.markdown("Made with ❤️ by Sana Kamal | [GitHub Repo](https://github.com/SanaKamal11/Travel_Rec_System)")
