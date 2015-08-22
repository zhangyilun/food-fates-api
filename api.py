#!flask/bin/python
import subprocess
from flask import Flask, jsonify, make_response, request, json
from sklearn.externals import joblib

app = Flask(__name__)
app.config.from_object('config')

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    }
]

@app.route('/')
def index():
    return "Woot!"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/get_ratings', methods=['POST'])
def get_ratings():
    input_data = request.get_json()
    rating = predict_rating(input_data)
    return jsonify({'rating':rating})

class resources:
    def __init__(inputs):
        self.inputs = inputs

def predict_rating(dataArray):
    clf = joblib.load(TRAINING_MODEL_FILEPATH)
    result = clf.predict(dataArray) 
    return result

def generate_tips(inputs):
    pass

if __name__ == '__main__':
    app.run(debug=True)