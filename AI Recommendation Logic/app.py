# Project 3: AI Recommendation Logic
# Goal: User ki pasand (interest) ke basis par products recommend karna

import pandas as pd

data = pd.read_csv("orders_data.csv")

print("Dataset ki shape:", data.shape)
print(data.head())

user_choice = input("\nAap konsa product pasand karte hain? (Laptop/Phone/Tablet/Monitor/Printer/Desk/Chair): ")
matching_orders = data[data["Product"].str.lower() == user_choice.lower()]
customers = matching_orders["CustomerID"].unique()

print(f"\n{len(customers)} customers ne '{user_choice}' khareeda hai.")
other_orders = data[data["CustomerID"].isin(customers)]
other_orders = other_orders[other_orders["Product"].str.lower() != user_choice.lower()]
recommendations = other_orders["Product"].value_counts()

print(f"\nAgar aapko '{user_choice}' pasand hai, to aapko ye bhi pasand aa sakte hain:")

if len(recommendations) == 0:
    print("Koi recommendation nahi mili.")
else:
    top_recommendations = recommendations.head(3)
    for product, count in top_recommendations.items():
        print(f"- {product} ({count} logon ne khareeda)")
