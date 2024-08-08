from flask import Flask
from flask_cors import CORS
from flask import request

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Hello, world!'

@app.route('/api/data', methods=['GET'])
def get_data():
    data = request.get_json()
    # Process the received JSON data
    # ...   
    return 'Received JSON data successfully'

if __name__ == '__main__':      
    app.run()