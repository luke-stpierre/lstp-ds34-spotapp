from flask import Flask, request
from backapp.model import transform


def create_app():
    
    app = Flask(__name__)
    
    # Home Route
    # Only allowed method is POST
   
    @app.route("/", methods=['POST'])
    def root():
        # Request data from the POST request
        data = request.form
        # call model.transform() to format 
        # data for Tensorflow model
        pred_data = transform(data)
        
        return pred_data
    
    return app