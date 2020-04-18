#!/usr/bin/env python
from flask import Flask #, request, jsonify
#from flask.logging import create_logger
#import logging
#import pandas as pd
#from sklearn.externals import joblib
#from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

@app.route('/')
def home():
    return "Hey there!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    #app.run(debug=True)