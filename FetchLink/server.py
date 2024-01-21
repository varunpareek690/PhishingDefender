from flask import Flask, request, jsonify
import joblib
import pandas as pd
from urllib.parse import urlparse

app = Flask(__name__)

# Load the trained model
model = joblib.load('phishing_detection_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Take user input for various features
        user_input_url = request.form['url']
        user_input_length_url = len(user_input_url)  # You can add more features as needed
        url_components = urlparse(user_input_url)
        length_hostname = len(url_components.netloc)

        # Count additional features
        # ... (you can add more feature extraction logic here)

        # Create a DataFrame with the user input
        user_input_data = pd.DataFrame({
            'url': [hash(user_input_url)],
            'length_url': [user_input_length_url],
            'length_hostname': [length_hostname],
            # ... (add more features)
        })

        # Make prediction using the trained model
        prediction = model.predict(user_input_data)

        # Interpret the prediction
        if prediction[0] == 1:
            result = "The URL is classified as phishing."
        else:
            result = "The URL is classified as legitimate."

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)  # Change the port to your desired port number
