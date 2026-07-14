# Project 2: Data Classification Using AI
# Goal: Orders ka status predict karna (Shipped, Cancelled, Returned, Delivered, Pending)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("orders_data.csv")
print("Dataset ki shape:", data.shape)
print(data.head())
data = data[["Product", "Quantity", "UnitPrice", "PaymentMethod", "OrderStatus"]]
le_product = LabelEncoder()
data["Product"] = le_product.fit_transform(data["Product"])

le_payment = LabelEncoder()
data["PaymentMethod"] = le_payment.fit_transform(data["PaymentMethod"])

le_status = LabelEncoder()
data["OrderStatus"] = le_status.fit_transform(data["OrderStatus"])
X = data[["Product", "Quantity", "UnitPrice", "PaymentMethod"]]
y = data["OrderStatus"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("\nModel ki Accuracy:", accuracy)
new_order = pd.DataFrame({
    "Product": le_product.transform(["Laptop"]),
    "Quantity": [2],
    "UnitPrice": [500.0],
    "PaymentMethod": le_payment.transform(["Credit Card"])
})

result = model.predict(new_order)
print("Predicted Order Status:", le_status.inverse_transform(result)[0])
