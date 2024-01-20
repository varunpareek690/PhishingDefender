from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests
import sys
import pandas as pd
import subprocess

app = Flask(__name__)

def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])


def scrape():
    current_url = request.form['currentUrl']
    page = requests.get(current_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    links_list = soup.find_all('a')
    
    scraped_data = []
    
    for link in links_list:
        if 'href' in link.attrs:
            web_link = str(link.attrs['href'])
            df = pd.read_csv('FetchLink\phishing_dataset.csv')
            if web_link in df['url'].unique():
                status = df.loc[df['url'] == web_link]['status'].values[0]
            else:
                status = 'Not in phishing dataset'

            scraped_data.append({'url': web_link, 'status': status})

    return jsonify(scraped_data) 
            
            

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
