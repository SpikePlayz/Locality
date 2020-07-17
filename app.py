from flask import Flask, request, render_template, redirect, session, make_response, url_for, flash, jsonify
import requests
import dropbox
import json
from datetime import datetime, timedelta
import time
from flask_simple_geoip import SimpleGeoIP

app = Flask(__name__)
app.config['SECRET_KEY'] = "thisisasecret"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/", methods = ["get"])
def index():
    locationJSON = requests.get("http://ip-api.com/json/" + request.headers['X-Forwarded-For']).json()
    lat = str(locationJSON['lat'])
    lng = str(locationJSON['lon'])

    yelp = "https://api.yelp.com/v3/businesses/search?latitude=" + lat + "&longitude=" + lng + "&categories=localservices,All&limit=50"

    headers = {
        "Authorization": "Bearer OuzpIYU03EajimgwSE7bOGjgdqRsjyI8zGunpx6DR1d-LgNjk8K-ioSLjf2_g57n5xcMD4meWXFsUf5rGJo63q5yqFUMWxIYoVwRJTDFxRGQNhd3zjWI72Sh0xsRX3Yx"
      }

    businessJSON = requests.get(yelp, headers=headers).json()

    return render_template('index.html', businesses=businessJSON['businesses'])

@app.route("/test")
def test():
    return jsonify({'ip': request.headers['X-Forwarded-For']}), 200

@app.route('/gofundme')
def gofundme():
    return render_template('gofundme.html')

if(__name__ == "__main__"):
    app.run(debug=True)
