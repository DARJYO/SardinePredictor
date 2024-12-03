import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Sample Data - Replace this with your actual dataset
data = {
    'temperature': [20, 21, 19, 18, 22, 23, 21, 20, 19, 18],
    'salinity': [35, 34, 36, 37, 35, 34, 36, 37, 35, 34],
    'sardine_presence': [1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
}

df = pd.DataFrame(data)

# Features and Labels
X = df[['temperature', 'salinity']]
y = df['sardine_presence']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'sardine_predictor_model.pkl')

print("Model trained and saved successfully.")

