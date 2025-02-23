import pickle
import uvicorn
import pandas as pd
import re
from urllib.parse import urlparse
from fastapi import FastAPI
from pydantic import BaseModel

# Load the trained model
with open("phishing_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Initialize FastAPI
app = FastAPI()


# Define the request model
class URLRequest(BaseModel):
    url: str


# Function to extract features from a URL
def extract_features(url):
    parsed_url = urlparse(str(url))

    url_length = len(url)
    hostname_length = len(parsed_url.netloc)
    path_length = len(parsed_url.path)

    special_chars = ['.', '/', '@', '-', '_', '?', '=', '&']
    special_counts = [url.count(char) for char in special_chars]

    https_present = 1 if parsed_url.scheme == 'https' else 0

    suspicious_words = ['login', 'bank', 'secure', 'verify', 'account', 'update']
    suspicious_count = sum(1 for word in suspicious_words if word in url.lower())

    subdomains = parsed_url.netloc.split('.')
    num_subdomains = max(len(subdomains) - 2, 0)

    ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'
    contains_ip = 1 if re.search(ip_pattern, parsed_url.netloc) else 0

    return [url_length, hostname_length, path_length, *special_counts,
            https_present, suspicious_count, num_subdomains, contains_ip]


# Define the API route
@app.post("/predict")
def predict_url(data: URLRequest):
    url = data.url

    # Extract features
    features = extract_features(url)

    # Convert to DataFrame
    feature_columns = [
        'url_length', 'hostname_length', 'path_length', '.', '/', '@', '-', '_', '?', '=', '&',
        'https_present', 'suspicious_count', 'num_subdomains', 'contains_ip'
    ]
    df = pd.DataFrame([features], columns=feature_columns)
    print(f"Model Type: {type(model)}")  # Debugging line

    # Make prediction
    prediction = model.predict(df)[0]

    # Return result
    return {"url": url, "is_phishing": bool(prediction)}


# Run the API server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
