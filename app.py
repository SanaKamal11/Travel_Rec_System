import streamlit as st
import pandas as pd
from recommender import recommend_experiences


# Load your data
experiences_df = pd.read_csv("C:\\Users\\aishwaryas1\\Downloads\\Travel_Rec_System-main\\Travel_Rec_System-main\\data\\experiences_df.csv")  # or pd.read_csv("data/experiences.csv")

# App title and intro
st.title("🌍 Personalized Travel Recommender")
st.write("Get tailored travel experiences based on your preferences!")

# Sidebar for user inputs
with st.sidebar:
    st.header("Tell us about you ✈️")
    name = st.text_input("Your Name")
    age = st.number_input("Age", min_value=0, max_value=120, value=30)
    budget_min, budget_max = st.slider("Your Budget Range (USD)", 20, 1000, (100, 300))
    season = st.selectbox("Preferred Season", ["Any", "Spring", "Summer", "Fall", "Winter"])
    interests = st.multiselect(
        "Your Interests",
        ["Cultural", "Nature", "Food", "Adventure", "Historical"]
    )
    min_rating = st.slider("Minimum Experience Rating", 3.0, 5.0, 4.0, step=0.1)


# Convert inputs to user vector
def build_user_vector(interests, budget_min, budget_max, min_rating):
    return {
        "preferred_categories": interests if interests else [],
        "budget_range": (budget_min, budget_max),
        "min_rating": min_rating,
        "weights": {
            "rating": 0.5,
            "category": 0.3,
            "budget": 0.2
        }
    }


user_vector = build_user_vector(interests, budget_min, budget_max, min_rating)

# Trigger recommendation
if st.button("Get Recommendations"):
    if not interests:
        st.warning("⚠️ Please select at least one interest.")
    else:
        st.subheader("🏙️ Top Experiences Across Cities")
        recommendations = recommend_experiences(user_vector, experiences_df, top_m=3)
        st.dataframe(recommendations)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Sana Kamal | [GitHub Repo](https://github.com/SanaKamal11/Travel_Rec_System)")
