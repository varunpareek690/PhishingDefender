import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from joblib import dump

# Load the dataset
dataset = pd.read_csv('Phishing_defencer/testingdatanew.csv')

# Assuming 'status' is your target variable (1 for phishing, 0 for legitimate)
X = dataset.drop('status', axis=1)
y = dataset['status']

# Convert URL column to integer using hash function
X['url'] = X['url'].apply(hash)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# Initialize the RandomForestClassifier (you can choose another algorithm if needed)
model_RF = RandomForestClassifier()

# Train the model
model_RF.fit(X_train, y_train)

# Make predictions on the test set
# a=pd.read_csv('Test.csv')
# a=pd.DataFrame(a)
y_pred = model_RF.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Display classification report for more detailed performance metrics
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Save the trained model for later use
dump(model_RF, 'model.joblib')