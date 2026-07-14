Project 3: AI Recommendation Logic
=========================================

Goal:
Create a simple recommendation system based on user preferences.

Description:
This project uses the "orders_data.csv" dataset, which contains details
of online orders (Product, CustomerID, etc.).

The user enters a product they like. The system finds customers who
bought that product, then looks at what else those customers bought.
Based on that, it recommends the top 3 products ("customers who bought
this also bought" logic).

Steps (in app.py):
1. Load the dataset
2. Take user input (which product they like)
3. Find customers who bought that product
4. Look at the other orders from those customers
5. Count the most frequently bought products
6. Display the top 3 recommendations

Key Skills Used:
- Logic building
- Pattern matching
- Recommendation concepts

How to Run:
1. Install the required libraries from requirements.txt:
   pip install -r requirements.txt

2. Run the following command in the terminal:
   python app.py

3. When prompted, type your preferred product (Laptop/Phone/Tablet/
   Monitor/Printer/Desk/Chair)

Files:
- app.py            -> Main code
- orders_data.csv   -> Dataset
- requirements.txt  -> Required libraries
- .gitignore        -> Files excluded from GitHub
- readme.txt        -> Project description (this file)
