# Phishing Defender🛡️
Phishing Defender is a Python-based project that aims to protect users from phishing attacks🚫 by analyzing links on a webpage. The project utilizes web scraping techniques with Beautiful Soup to extract links from a given webpage. These extracted links are then sent to a new page, where a machine learning model🧠 predicts whether each link is phishing or legitimate based on various parameters.


## Features
Web scraping using Beautiful Soup to extract links from a webpage.
Integration with a machine learning model to predict the phishing or legitimate status of each link.
Output display of links along with their corresponding status on a separate page.

## Requirements
Make sure you have the following dependencies installed:

- Python 3.x
- Beautiful Soup
- Flask (for the web application)
- Machine learning model dependencies (ensure you follow the model setup instructions)


## Installation
Clone the repository:
bash
Copy code
git clone https://github.com/varunpareek690/phishing-defender.git
cd phishing-defender
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Set up the machine learning model:

Follow the instructions in the model/README.md to train or set up the machine learning model.
Run the application:

bash
Copy code
python app.py
Visit http://localhost:5000 in your web browser to use Phishing Defender.

## Usage
Enter the URL of the webpage you want to analyze on the main page.
Click on the "Submit" button.
The links extracted from the webpage and their status (phishing or legitimate) will be displayed on a new page.
Model Training
If you want to train your own machine learning model or update the existing one, refer to the instructions in the model/README.md file.

## Collaborators 
Paras Goyal  
Shivam Sharma  
Varun Pareek


## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Special thanks to __Random Forest Classifier__ for providing the pre-trained model.
Inspired by the need for better phishing protection in the digital world.
Feel free to contribute, report issues, or suggest improvements!
