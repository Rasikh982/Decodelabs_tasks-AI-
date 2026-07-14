Project 2: Data Classification Using AI
=========================================

Goal:
Build a basic classification model using a small dataset.

Description:
This project uses the "orders_data.csv" dataset, which contains details
of online orders (Product, Quantity, UnitPrice, PaymentMethod,
OrderStatus, etc.).

The model's task is to look at an order's details and predict its
status: Shipped, Cancelled, Returned, Delivered, or Pending.

Steps (in app.py):
1. Load the dataset
2. Select the required columns (Product, Quantity, UnitPrice, PaymentMethod)
3. Convert text data into numbers (Label Encoding)
4. Split the data into training and testing sets (80% - 20%)
5. Train a Decision Tree Classifier model
6. Check the model's accuracy
7. Predict the status of a new order (example)

Key Skills Used:
- Data handling (pandas)
- Supervised learning basics
- Model training and testing (scikit-learn)

How to Run:
1. Install the required libraries from requirements.txt:
   pip install -r requirements.txt

2. Run the following command in the terminal:
   python app.py

Files:
- app.py            -> Main code
- orders_data.csv   -> Dataset
- requirements.txt  -> Required libraries
- .gitignore        -> Files excluded from GitHub
- readme.txt        -> Project description (this file)
