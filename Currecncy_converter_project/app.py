from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'YOUR_API_KEY'
API_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    amount = float(request.form.get('amount'))
    from_currency = request.form.get('fromCurrency')
    to_currency = request.form.get('toCurrency')

    response = requests.get(f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{from_currency}/{to_currency}')
    data = response.json()

    exchange_rate = data.get('conversion_rate')
    converted_amount = amount * exchange_rate

    result = {
        'converted_amount': round(converted_amount, 2),
        'from_currency': from_currency,
        'to_currency': to_currency
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
