Project 2: Data Classification Using AI
=========================================

Goal:
Build a basic classification model using a small dataset.

Description:
Is project mein "orders_data.csv" dataset use kiya gaya hai jo online
orders ki details rakhta hai (Product, Quantity, UnitPrice, PaymentMethod,
OrderStatus, wagera).

Model ka kaam ye hai ke Order ki details dekh kar predict kare ke uska
status kya hoga: Shipped, Cancelled, Returned, Delivered, ya Pending.

Steps (app.py mein):
1. Dataset load karna
2. Zaroori columns select karna (Product, Quantity, UnitPrice, PaymentMethod)
3. Text data ko numbers mein convert karna (Label Encoding)
4. Data ko training aur testing sets mein split karna (80% - 20%)
5. Decision Tree Classifier model train karna
6. Model ki accuracy check karna
7. Ek naye order ka status predict karna (example)

Key Skills Used:
- Data handling (pandas)
- Supervised learning basics
- Model training aur testing (scikit-learn)

How to Run:
1. requirements.txt se libraries install karein:
   pip install -r requirements.txt

2. Terminal mein ye command run karein:
   python app.py

Files:
- app.py            -> Main code
- orders_data.csv   -> Dataset
- requirements.txt  -> Required libraries
- .gitignore        -> Files jo GitHub par upload nahi karni
- readme.txt        -> Project ki tafseel (ye file)
