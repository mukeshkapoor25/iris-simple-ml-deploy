from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Create model directory if it doesn't exist
os.makedirs("model", exist_ok=True)

# Save model
joblib.dump(model, "model/iris_model.pkl")

print("✅ Model trained and saved to model/iris_model.pkl")