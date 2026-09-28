import os
import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://rijeka.anton008.com",
    "Referer": "https://rijeka.anton008.com/"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/vehicles')
def get_vehicles():
    # Primarni i alternativni izvori podataka
    urls = [
        "https://api.autotrolej.hr/api/open/v1/voznired/autobusi",
        "http://busri.alwaysdata.net/getBuses"
    ]
    
    for url in urls:
        try:
            r = requests.get(url, headers=HEADERS, timeout=5)
            if r.status_code == 200:
                return jsonify(r.json())
        except Exception as e:
            continue
            
    return jsonify([]), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
