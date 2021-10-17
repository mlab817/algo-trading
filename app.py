from flask import Flask, request
from get_daily_summary import get_daily_summary
from get_historical_data import get_historical_data

import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET' and request.args['stock']:
        return get_daily_summary(request.args['stock'])
    return 'Select stock'

@app.route('/get_historical_data', methods=['GET'])
def historical_data():
    if request.args['stock']:
        return get_historical_data(
            request.args['stock'],
            13,
            234
        ).to_json(orient='records')
    return 'Select stock'