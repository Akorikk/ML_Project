from flask import Flask
from ML.logger import logging 
from ML.exception import CustomException
import os, sys

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():

    try:
        raise Exception('Testing file')
    except Exception as e:
        PO = CustomException(e, sys)
        logging.info(PO.error_massage)

        logging.info("testing")

        return "Running Good"

if __name__ == "__main__":
    app.run(debug= True)