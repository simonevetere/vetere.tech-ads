from flask import Flask, request,render_template
from flask_cors import CORS
import requests

app = Flask(__name__)

CORS(app)

@app.route('/')
def load_index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080,debug=True)

