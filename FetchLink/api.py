from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_webpage():
    url = request.json['url']
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.title.string
    response = {
        'title': title
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
