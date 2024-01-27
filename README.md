# Phishing Defender🛡️
Phishing Defender is a Python-based project that aims to protect users from phishing attacks🚫 by analyzing links on a webpage. The project utilizes web scraping techniques with Beautiful Soup to extract links from a given webpage. These extracted links are then sent to a new page, where a machine learning model🧠 predicts whether each link is phishing or legitimate based on various parameters.


## Features
- Web scraping using Beautiful Soup to extract links from a webpage.  
- Integration with a machine learning model to predict the phishing or legitimate status of each link.  
- Output display of links along with their corresponding status on a separate window.

## Requirements
Make sure you have the following dependencies installed:

- Python 
- Beautiful Soup
- Flask (for the web application)
- Machine learning model dependencies (ensure you follow the model setup instructions)
- Any Code Editor (VS Code, Pycharm)


## Installation
1. Clone the repository:
``` bash
git clone https://github.com/varunpareek690/phishing-defender.git
cd phishing-defender
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Follow the instructions in the model/README.md to train or set up the machine learning model.


__Visit http://localhost:5000 in your web browser to use Phishing Defender.__

## Usage
1. Visit any website or the demo website created in the "HACK2.0" folder.
2. Go to your browser settings, navigate to "Extensions," turn on developer options, and load the unpacked extension from the extension directory, __Phishing defencer__ in the project
3. Run this command in the terminal
  ```python
python popup.py
```
4. The flask server will go live on http://localhost:5000
5. Click the extension icon and then click the "Scrape Links" button.

## Demo

https://github.com/varunpareek690/PhishingDefender/assets/114807315/cf70176e-306c-4f3e-95e8-57a18b254738  
  
  
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
