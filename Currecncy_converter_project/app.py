from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# API keys and URLs
EXCHANGE_RATE_API = f'https://v6.exchangerate-api.com/v6/7a4f285f93cd659f6d72a76e/latest/USD'
NEWS_API = 'https://newsapi.org/v2/everything?q=currency&apiKey=7bc5819029f640ca8b6ba28158a090c1'

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to get exchange rates
@app.route('/get_rates')
def get_rates():
    response = requests.get(EXCHANGE_RATE_API)
    return jsonify(response.json())

# Route to get currency news
@app.route('/get_news')
def get_news():
    response = requests.get(NEWS_API)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
