from flask import Flask, request, jsonify
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import pickle

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('phishing_dataset.csv')

# Feature engineering (simplified example)
X = df[['length_url']]
y = df['status']

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X, y)

# Save the trained model as a pickle file
with open('phishing_model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Convert the pickle file to a joblib file
with open('phishing_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)
    joblib.dump(loaded_model, 'phishing_model.joblib')

@app.route('/scrape', methods=['POST'])
def scrape():
    current_url = request.form['currentUrl']

    # Load the trained model using joblib
    model = joblib.load('phishing_model.joblib')

    # Feature extraction (simplified example)
    length_url = len(current_url)
    X_new = pd.DataFrame({'length_url': [length_url]})

    # Make predictions
    prediction = model.predict(X_new)[0]

    return jsonify({'url': current_url, 'status': prediction})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)
