from flask import Flask, request
from bs4 import BeautifulSoup
import requests
import sys
import pandas as pd
import subprocess

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape():
    current_url = request.form['currentUrl']
    page = requests.get(current_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    links_list = soup.find_all('a')
    
    for link in links_list:
        if 'href' in link.attrs:
            web_links = str(link.attrs['href'])
            df = pd.read_csv('phishing_dataset.csv')
            status1 = df.loc[df['url'] == web_links]['status']
            print(web_links)
            if web_links in df['url'].unique():
                print("yes")
                z=df.loc[df['url'] == web_links]
                d=z['status']
                print(d)
                with open("output.txt","w")as f:
                    sys.stdout = f 
                    print(web_links,d,file=f)
                    sys.stdout = sys.__stdout__
            else:
                print("no")
                z=df.loc[df['url'] == web_links]
                d=z['status']
                print(d)
                with open("output.txt","w")as f:
                    sys.stdout = f 
                    print(web_links,d,file=f)
                    sys.stdout = sys.__stdout__
            
            



    return 'Scraped links printed to console'
    
if __name__ == '__main__':
    app.run()
