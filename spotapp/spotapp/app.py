from flask import Flask, render_template, request
from os import getenv
import requests
import json


def create_app():
    
    app = Flask(__name__)
    
    # Home Route
    @app.route("/", methods=['POST', 'GET'])
    @app.route("/index.html", methods=['POST', 'GET'])
    def root():
        return render_template('index.html', title='tst title')
    
    # Route to the information form
    @app.route("/prediction.html", methods=['POST', 'GET'])
    def prediction():
        return render_template('prediction.html', title='prediction')
    

    # If any of this fails, it prompts the user with an error.
    @app.route('/data', methods = ['POST', 'GET'])
    def data():
        # If method is a GET request, throw error.
        if request.method == 'GET':
            return f"The URL /data is accessed directly. Try going to '/prediction.html' to submit form"
        # If method is POST request, attempt to make prediction and add data.
        if request.method == 'POST':
            try:
                form_data = request.form
                x = requests.post(url='https://lstp-ds34-spotback.herokuapp.com/', data=form_data, timeout=120)
                prediction = dict(json.loads(x.text))
                return render_template('data.html', prediction=prediction)
            except:
                return f'Please be sure you are correctly formatting your inputs.'

    return app