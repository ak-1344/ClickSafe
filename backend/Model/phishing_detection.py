import pandas as pd
import re
from urllib.parse import urlparse
import os
from tqdm import tqdm  # For progress bar

# Check if the file exists
if not os.path.exists("final_cleaned_phishing_dataset.csv"):
    raise FileNotFoundError("❌ ERROR: 'final_cleaned_phishing_dataset.csv' file not found!")

print("Loading dataset...")
df = pd.read_csv("final_cleaned_phishing_dataset.csv")  # Ensure correct file path
print("Dataset loaded successfully!")

# Test on a smaller subset
df = df.sample(n=100000)  # Comment this line to process the full dataset

# Ensure 'URL' column exists
if "URL" not in df.columns:
    raise KeyError("❌ ERROR: 'URL' column not found in dataset!")

# Drop rows where 'URL' is missing
print("Dropping rows with missing URLs...")
df = df.dropna(subset=["URL"])
print(f"Rows after dropping NaN: {len(df)}")

# Function to extract features from URLs
def extract_features(url):
    try:
        parsed_url = urlparse(str(url))  # Convert to string to prevent errors

        # Basic features
        url_length = len(url)
        hostname_length = len(parsed_url.netloc)
        path_length = len(parsed_url.path)

        # Count special characters
        special_chars = ['.', '/', '@', '-', '_', '?', '=', '&']
        special_counts = [url.count(char) for char in special_chars]

        # Presence of HTTPS
        https_present = 1 if parsed_url.scheme == 'https' else 0

        # Suspicious words in URL
        suspicious_words = ['login', 'bank', 'secure', 'verify', 'account', 'update']
        suspicious_count = sum(1 for word in suspicious_words if word in url.lower())

        # Number of subdomains
        subdomains = parsed_url.netloc.split('.')
        num_subdomains = max(len(subdomains) - 2, 0)  # Avoid negative values

        # Check if IP address is used instead of a domain
        ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'  # Regex for IPv4 address
        contains_ip = 1 if re.search(ip_pattern, parsed_url.netloc) else 0

        return [
            url_length, hostname_length, path_length, *special_counts,
            https_present, suspicious_count, num_subdomains, contains_ip
        ]
    except Exception as e:
        print(f"⚠️ Skipping URL due to error: {url} → {str(e)}")
        return [0] * 14  # Return default values for problematic URLs

# Define feature names
feature_columns = [
    'url_length', 'hostname_length', 'path_length', '.', '/', '@', '-', '_', '?', '=', '&',
    'https_present', 'suspicious_count', 'num_subdomains', 'contains_ip'
]

# Apply feature extraction with progress bar
print("Extracting features...")
tqdm.pandas()  # Enable progress_apply for pandas
features_df = df['URL'].progress_apply(lambda x: pd.Series(extract_features(x)))
print("Features extracted successfully!")

# Assign the extracted features properly
print("Assigning features to DataFrame...")
df[feature_columns] = features_df.values

# Save new dataset with extracted features
print("Saving dataset with extracted features...")
df.to_csv("phishing_dataset_with_features.csv", index=False)
print("\n✅ Feature extraction completed! Dataset saved.")

import pandas as pd

# Load the processed dataset
print("\n📂 Loading processed dataset...")
df = pd.read_csv("phishing_dataset_with_features.csv")

# Display basic information
print("\n🔹 Dataset Info:")
print(df.info())

# Check for missing values
print("\n🔍 Checking for missing values...")
missing_values = df.isnull().sum()
print(missing_values)

# Fill missing values with 0 (if any)
if missing_values.sum() > 0:
    df = df.fillna(0)
    print("✅ Missing values filled with 0.")

# Define Features (X) and Target (y)
print("\n📌 Selecting features and target variable...")
feature_columns = [
    'url_length', 'hostname_length', 'path_length', '.', '/', '@', '-', '_', '?', '=', '&',
    'https_present', 'suspicious_count', 'num_subdomains', 'contains_ip'
]

# Check if target column exists
target_column = "label"  # Change this based on your dataset (e.g., 'label' or 'phishing')

if target_column not in df.columns:
    raise KeyError(f"❌ ERROR: Target column '{target_column}' not found in dataset!")

X = df[feature_columns]  # Features
y = df[target_column]  # Target (0 = Legit, 1 = Phishing)

print(f"\n✅ Data ready for training! Features: {X.shape}, Target: {y.shape}")

# Display extracted features sample
print("\n🔹 Extracted Features Sample:")
print(df.head())

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Split data into training and testing sets (80% train, 20% test)
print("\n📊 Splitting dataset into training and testing sets...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print(f"Training set: {X_train.shape}, Testing set: {X_test.shape}")

# Train a RandomForest model
print("\n🚀 Training the model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
print("\n🔍 Evaluating the model...")
y_pred = model.predict(X_test)

# Model accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\n🎯 Model Accuracy: {accuracy:.4f}")

# Detailed classification report
print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred))

# Save the trained model
import joblib
joblib.dump(model, "phishing_model.pkl")
print("\n✅ Model saved as 'phishing_model.pkl'!")

test_url = "http://www.phishtank.com/phish_detail.php?phish_id=8969628"

# Extract features for the test URL
test_features = extract_features(test_url)

# Convert to DataFrame for compatibility
test_df = pd.DataFrame([test_features], columns=[
    'url_length', 'hostname_length', 'path_length', '.', '/', '@', '-', '_', '?', '=', '&',
    'https_present', 'suspicious_count', 'num_subdomains', 'contains_ip'
])

# Predict using the trained model
prediction = model.predict(test_df)[0]

# Print the result
result = "Phishing" if prediction == 1 else "Legitimate"
print(f"\n🔍 Prediction for '{test_url}': {result}")