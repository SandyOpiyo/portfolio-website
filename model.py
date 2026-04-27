# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

# Step 1: Load dataset
df = pd.read_csv("data.csv")

# Step 2: Explore data
print("First 5 rows:\n", df.head())
print("\nMissing values:\n", df.isnull().sum())

# Step 3: Define features and target
X = df[['Age', 'EstimatedSalary']]
y = df['Purchased']

# Step 4: Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 5: Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Step 6: Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 7: Make predictions
predictions = model.predict(X_test)

# Step 8: Evaluate model
accuracy = accuracy_score(y_test, predictions)
cm = confusion_matrix(y_test, predictions)

print("\nModel Accuracy:", accuracy)
print("\nConfusion Matrix:\n", cm)

# Step 9: Visualization
plt.figure()
plt.scatter(df['Age'], df['EstimatedSalary'], c=df['Purchased'])
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.title("Customer Purchase Distribution")
plt.show()
# Test with new data
new_customer = [[35, 40000]]
new_customer_scaled = scaler.transform(new_customer)

prediction = model.predict(new_customer_scaled)

print("\nNew Customer Prediction (1=Will Buy, 0=Won't):", prediction[0])
