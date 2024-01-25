#!/usr/bin/env python
# coding: utf-8

# In[101]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load the dataset
dataset = pd.read_csv('phishing_dataset_newww.csv')

# Assuming 'status' is your target variable (1 for phishing, 0 for legitimate)
X = dataset.drop('status', axis=1)
y = dataset['status']

# Convert URL column to integer using hash function
X['url'] = X['url'].apply(hash)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# Initialize the RandomForestClassifier (you can choose another algorithm if needed)
model = RandomForestClassifier()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
# a=pd.read_csv('Test.csv')
# a=pd.DataFrame(a)
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Display classification report for more detailed performance metrics
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Save the trained model for later use
joblib.dump(model, 'phishing_detection_modelfinal.pkl')


# In[95]:


# import joblib
# import pandas as pd

# # Load the trained model
# model = joblib.load('phishing_detection_model.pkl')

# # Take user input for the URL
# user_input_url = input("Enter the URL to check: ")

# # Preprocess the user input URL
# user_input = pd.DataFrame([user_input_url], columns=['url'])
# user_input['url'] = user_input['url'].apply(hash)

# # Make prediction using the trained model
# prediction = model.predict(user_input)

# # Interpret the prediction
# if prediction[0] == 1:
#     print("The URL is classified as phishing.")
# else:
#     print("The URL is classified as legitimate.")


# In[104]:


import joblib
import pandas as pd
from urllib.parse import urlparse

# Load the trained model
model = joblib.load('phishing_detection_modelfinal.pkl')

# Take user input for various features
user_input_url = input("Enter the URL to check: ")
user_input_length_url = len(user_input_url)  # You can add more features as needed
url_components = urlparse(user_input_url)
length_hostname = len(url_components.netloc)

# Count additional features
nb_dots = user_input_url.count('.')
nb_hyphens = user_input_url.count('-')
nb_at = user_input_url.count('@')
nb_qm = user_input_url.count('?')
nb_percent = user_input_url.count('%')
nb_slash = user_input_url.count('/')
nb_and = user_input_url.count('&')
nb_or = user_input_url.count('|')
nb_eq = user_input_url.count('=')
nb_star = user_input_url.count('*')
nb_colon = user_input_url.count(':')
nb_comma = user_input_url.count(',')
nb_semicolon = user_input_url.count(';')
nb_dollar = user_input_url.count('$')
nb_underscore = user_input_url.count('_')
nb_tilde = user_input_url.count('~')
nb_space = user_input_url.count(' ')
nb_www = user_input_url.lower().count('www')
nb_com = user_input_url.lower().count('com')

# Check if "https" is present in the URL
http_in_path = "http" in url_components.path.lower()
https_token = "https" in user_input_url.lower()

# Calculate additional features
ratio_digits_url = sum(c.isdigit() for c in user_input_url) / len(user_input_url)
ratio_digits_host = sum(c.isdigit() for c in url_components.netloc) / len(url_components.netloc)

# Include the new parameters
punycode = url_components.netloc.encode('idna').decode('utf-8') != url_components.netloc
port = bool(url_components.port)
tld_in_path = url_components.path.endswith(('.com', '.net', '.org', '.edu'))  # Adjust TLDs as needed
tld_in_subdomain = any(subdomain.endswith(('.com', '.net', '.org', '.edu')) for subdomain in url_components.netloc.split('.'))

# Additional features
abnormal_subdomain = False  # Placeholder, you can modify this based on your criteria
nb_subdomains = len(url_components.netloc.split('.'))
prefix_suffix = user_input_url.startswith('http://') or user_input_url.startswith('https://')
random_domain = False  # Placeholder, you can modify this based on your criteria
shortening_service = False  # Placeholder, you can modify this based on your criteria
path_extension = '.' in url_components.path
nb_redirection = user_input_url.count('//')
nb_external_redirection = False  # Placeholder, you can modify this based on your criteria
length_words_raw = len(user_input_url.split())
char_repeat = any(user_input_url.count(char * 4) for char in set(user_input_url))

# Additional features
shortest_words_raw = min(user_input_url.split(), key=len)
shortest_word_host = min(url_components.netloc.split('.'), key=len)
shortest_word_path = min(url_components.path.split('/'), key=len)
longest_words_raw = max(user_input_url.split(), key=len)
longest_word_host = max(url_components.netloc.split('.'), key=len)
longest_word_path = max(url_components.path.split('/'), key=len)
avg_words_raw = sum(len(word) for word in user_input_url.split()) / len(user_input_url.split())
avg_word_host = sum(len(word) for word in url_components.netloc.split('.')) / len(url_components.netloc.split('.'))
avg_word_path = sum(len(word) for word in url_components.path.split('/')) / len(url_components.path.split('/'))
phish_hints = False  # Placeholder, you can modify this based on your criteria
domain_in_brand = False  # Placeholder, you can modify this based on your criteria
brand_in_subdomain = False  # Placeholder, you can modify this based on your criteria
brand_in_path = False  # Placeholder, you can modify this based on your criteria
suspecious_tld = False  # Placeholder, you can modify this based on your criteria
statistical_report = False  # Placeholder, you can modify this based on your criteria

# Additional features
nb_hyperlinks = 0  # Placeholder, you can modify this based on your criteria
ratio_intHyperlinks = 0.0  # Placeholder, you can modify this based on your criteria
ratio_extHyperlinks = 0.0  # Placeholder, you can modify this based on your criteria
ratio_nullHyperlinks = 0.0  # Placeholder, you can modify this based on your criteria
nb_extCSS = 0  # Placeholder, you can modify this based on your criteria
ratio_intRedirection = 0.0  # Placeholder, you can modify this based on your criteria
ratio_extRedirection = 0.0  # Placeholder, you can modify this based on your criteria
ratio_intErrors = 0.0  # Placeholder, you can modify this based on your criteria
ratio_extErrors = 0.0  # Placeholder, you can modify this based on your criteria
login_form = False  # Placeholder, you can modify this based on your criteria
external_favicon = False  # Placeholder, you can modify this based on your criteria
links_in_tags = 0  # Placeholder, you can modify this based on your criteria
submit_email = False  # Placeholder, you can modify this based on your criteria
ratio_intMedia = 0.0  # Placeholder, you can modify this based on your criteria
ratio_extMedia = 0.0  # Placeholder, you can modify this based on your criteria
sfh = False  # Placeholder, you can modify this based on your criteria
iframe = False  # Placeholder, you can modify this based on your criteria
popup_window = False  # Placeholder, you can modify this based on your criteria
safe_anchor = False  # Placeholder, you can modify this based on your criteria
onmouseover = False  # Placeholder, you can modify this based on your criteria
right_clic = False  # Placeholder, you can modify this based on your criteria
empty_title = False  # Placeholder, you can modify this based on your criteria
domain_in_title = False  # Placeholder, you can modify this based on your criteria
domain_with_copyright = False  # Placeholder, you can modify this based on your criteria
whois_registered_domain = False  # Placeholder, you can modify this based on your criteria
domain_registration_length = 0  # Placeholder, you can modify this based on your criteria
domain_age = 0  # Placeholder, you can modify this based on your criteria
web_traffic = 0  # Placeholder, you can modify this based on your criteria
dns_record = 0  # Placeholder, you can modify this based on your criteria
google_index = 0  # Placeholder, you can modify this based on your criteria
page_rank = 0  # Placeholder, you can modify this based on your criteria

# Create a DataFrame with the user input
user_input_data = pd.DataFrame({
    'url': [hash(user_input_url)],
    'length_url': [user_input_length_url],
    'length_hostname': [length_hostname],
    'nb_dots': [nb_dots],
    'nb_hyphens': [nb_hyphens],
    'nb_at': [nb_at],
    'nb_qm': [nb_qm],
    'nb_and': [nb_and],
    'nb_or': [nb_or],
    'nb_eq': [nb_eq],
    'nb_underscore': [nb_underscore],
    'nb_tilde': [nb_tilde],
    'nb_percent': [nb_percent],
    'nb_slash': [nb_slash],
    'nb_star': [nb_star],
    'nb_colon': [nb_colon],
    'nb_comma': [nb_comma],
    'nb_semicolumn': [nb_semicolon],
    'nb_dollar': [nb_dollar],
    'nb_space': [nb_space],
    'nb_www': [nb_www],
    'nb_com': [nb_com],
    'http_in_path': [http_in_path],
    'https_token': [https_token],
    'ratio_digits_url': [ratio_digits_url],
    'ratio_digits_host': [ratio_digits_host],
    'punycode': [punycode],
    'port': [port],
    'tld_in_path': [tld_in_path],
    'tld_in_subdomain': [tld_in_subdomain],
    'abnormal_subdomain': [abnormal_subdomain],
    'nb_subdomains': [nb_subdomains],
    'prefix_suffix': [prefix_suffix],
    'random_domain': [random_domain],
    'shortening_service': [shortening_service],
    'path_extension': [path_extension],
    'nb_redirection': [nb_redirection],
    'nb_external_redirection': [nb_external_redirection],
    'length_words_raw': [length_words_raw],
    'char_repeat': [char_repeat],
    'shortest_words_raw': [shortest_words_raw],
    'shortest_word_host': [shortest_word_host],
    'shortest_word_path': [shortest_word_path],
    'longest_words_raw': [longest_words_raw],
    'longest_word_host': [longest_word_host],
    'longest_word_path': [longest_word_path],
    'avg_words_raw': [avg_words_raw],
    'avg_word_host': [avg_word_host],
    'avg_word_path': [avg_word_path],
    'phish_hints': [phish_hints],
    'domain_in_brand': [domain_in_brand],
    'brand_in_subdomain': [brand_in_subdomain],
    'brand_in_path': [brand_in_path],
    'suspecious_tld': [suspecious_tld],
    'statistical_report': [statistical_report],
    'nb_hyperlinks': [nb_hyperlinks],
    'ratio_intHyperlinks': [ratio_intHyperlinks],
    'ratio_extHyperlinks': [ratio_extHyperlinks],
    'ratio_nullHyperlinks': [ratio_nullHyperlinks],
    'nb_extCSS': [nb_extCSS],
    'ratio_intRedirection': [ratio_intRedirection],
    'ratio_extRedirection': [ratio_extRedirection],
    'ratio_intErrors': [ratio_intErrors],
    'ratio_extErrors': [ratio_extErrors],
    'login_form': [login_form],
    'external_favicon': [external_favicon],
    'links_in_tags': [links_in_tags],
    'submit_email': [submit_email],
    'ratio_intMedia': [ratio_intMedia],
    'ratio_extMedia': [ratio_extMedia],
    'sfh': [sfh],
    'iframe': [iframe],
    'popup_window': [popup_window],
    'safe_anchor': [safe_anchor],
    'onmouseover': [onmouseover],
    'right_clic': [right_clic],
    'empty_title': [empty_title],
    'domain_in_title': [domain_in_title],
    'domain_with_copyright': [domain_with_copyright],
    'whois_registered_domain': [whois_registered_domain],
    'domain_registration_length': [domain_registration_length],
    'domain_age': [domain_age],
    'web_traffic': [web_traffic],
    'dns_record': [dns_record],
    'google_index': [google_index],
    'page_rank': [page_rank],
    # Add more features here
})

# Make prediction using the trained model
prediction = model.predict(user_input_data)

# Interpret the prediction
if prediction[0] == 1:
    print("The URL is classified as phishing.")
else:
    print("The URL is classified as legitimate.")


# In[93]:


# Assuming you have a validation dataset (X_val, y_val)
X_val_processed = X_test  # Preprocess X_val similarly to training data
y_val_pred = model.predict(X_val_processed)

accuracy_val = accuracy_score(y_test, y_val_pred)
print(f"Validation Accuracy: {accuracy_val:.2f}")


# In[92]:


import matplotlib.pyplot as plt


# In[65]:


plt.scatter(dataset.status, dataset.length_url)
plt.title('Status v/s length of hostname', fontsize=10)
plt.xlabel('Status', fontsize=10, labelpad=10)
plt.ylabel('length_hostname', fontsize=10, labelpad=10)


# In[ ]:




