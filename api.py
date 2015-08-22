#!flask/bin/python
from flask import Flask, jsonify, make_response, request, json
from sklearn.externals import joblib

app = Flask(__name__)
app.config.from_object('config')

dataArray = [15.0, 15.0, 24.0, 15.0, 15.0, 24.0, 24.0, True, True, 1.0, 2, 1,
       True, 1, False, True, False, False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16]

@app.route('/')
def index():
    return "Woot!"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/get_ratings', methods=['GET'])
def get_ratings():
    return str(predict_rating())
    # input_data = request.get_json()
    # rating = predict_rating(input_data)
    # return jsonify({'rating':rating})

class resources:
    def __init__(inputs):
        self.inputs = inputs

def predict_rating():
    clf = joblib.load(app.config['TRAINING_MODEL_FILEPATH'])
    result = clf.predict(dataArray) 
    return result

def generate_tips(inputs):
    pass

if __name__ == '__main__':
    app.run(debug=True)