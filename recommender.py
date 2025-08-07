import pandas as pd
import random

# Step 1: Generate simulated experiences dataset
cities = ["barcelona", "rome", "tokyo", "paris", "bangkok", "new york", "cape town", "sydney", "dubai", "rio de janeiro"]
categories = ["Cultural", "Nature", "Food", "Adventure", "Historical"]
experience_pool = [
    "City Walking Tour", "Local Food Experience", "Museum Visit", "Hiking Trip",
    "Boat Ride", "Cooking Class", "Temple Visit", "Market Tour", "Sunset View", "Live Music Night"
]

data = []
random.seed(42)

for city in cities:
    for _ in range(5):
        data.append({
            "City": city,
            "Experience": random.choice(experience_pool),
            "Category": random.choice(categories),
            "Price": round(random.uniform(20, 200), 2),
            "Rating": round(random.uniform(3.5, 5.0), 1)
        })

experiences_df = pd.DataFrame(data)

# Step 2: Save the dataset
experiences_df.to_csv("C:\\Users\\aishwaryas1\\Downloads\\Travel_Rec_System-main\\Travel_Rec_System-main\\data\\experiences_df.csv", index=False)

# Step 3: Define user preference vector
user_vector = {
    "preferred_categories": ["Cultural", "Food"],
    "budget_range": (40, 150),
    "min_rating": 4.0,
    "weights": {
        "rating": 0.5,
        "category": 0.3,
        "budget": 0.2
    }
}


# Step 4: Define scoring logic
def category_match_score(preferred, category):
    return 1.0 if category in preferred else 0.0


def budget_fit_score(budget_range, price):
    return 1.0 if budget_range[0] <= price <= budget_range[1] else 0.0


def rating_score(rating):
    return rating / 5.0


def compute_score(exp_row, user_vector):
    w = user_vector["weights"]
    return (
        w["rating"] * rating_score(exp_row["Rating"]) +
        w["category"] * category_match_score(user_vector["preferred_categories"], exp_row["Category"]) +
        w["budget"] * budget_fit_score(user_vector["budget_range"], exp_row["Price"])
    )


# Step 5: Define main recommender
def recommend_experiences(user_vector, experiences_df, top_m=3):
    df = experiences_df.copy()
    df["City"] = df["City"].str.lower()
    df["Score"] = df.apply(lambda row: compute_score(row, user_vector), axis=1)
    top_by_city = (
        df.sort_values(by=["City", "Score"], ascending=[True, False])
          .groupby("City")
          .head(top_m)
          .reset_index(drop=True)
    )
    return top_by_city[["City", "Experience", "Category", "Price", "Rating", "Score"]]


# Step 6: Try it!
recommend_experiences(user_vector, experiences_df, top_m=3)