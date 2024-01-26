from flask import Flask, request, jsonify, render_template
from bs4 import BeautifulSoup
import requests
import sys
import pandas as pd
import subprocess
from model import model_RF
from testing_model import test_fnx

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
            a=test_fnx(web_link)
            scraped_data.append({'url': web_link, 'status': a})
    return jsonify(scraped_data) 
            

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)