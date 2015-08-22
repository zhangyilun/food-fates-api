#!flask/bin/python
from flask import Flask, jsonify
from sklearn.externals import joblib

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/')
def index():
    return "Woot!"

@app.route('/classify', methods=['GET'])
def classify():
    return jsonify({'tasks': tasks})

def predict_rating(trained_model, inputs):
    pass

def generate_tips(inputcluster):
    pass

if __name__ == '__main__':
    app.run(debug=True)