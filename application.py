#!flask/bin/python
import pandas as pd
import numpy as np
import reverse_geocoder as rg
import us
from flask import Flask, jsonify, make_response, request, json
from sklearn.externals import joblib
from datetime import datetime
from models import *

app = Flask(__name__)
app.config.from_object('config')



@app.route('/')
def index():
		return "Woot!"

# @app.errorhandler(404)
def not_found(error):
		return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/get_ratings', methods=['POST'])
def get_ratings():
		input_data = request.get_json()
		data_for_ml = gather_data_for_ml(input_data)
		rating = predict_rating(input_data)
		return jsonify({'rating':rating})

@app.route('/get_reviews', methods=['POST'])
def get_reviews():
	input_data = request.get_json()
	lat = input_data['latitude']
	lon = input_data['longitude']
	return 'get_reviews'

@app.route('/get_nearby', methods=['POST'])
def get_nearby():
	input_data = request.get_json()
	lat = input_data['latitude']
	lon = input_data['longitude']
	result = calculate_closest_places(lat, lon)
	return jsonify({'nearby' : result})

if __name__ == '__main__':
		app.run(debug=True)

#############################################################################
############################## helper functions #############################
#############################################################################

def gather_data_for_ml(input_data):
	model_ordered_list = []
	city, state = get_city_and_state(input_data['latitude'], input_data['longitude'])
	hours = get_hours(input_data)
	model_ordered_list.extend([city, state]) # city, state
	model_ordered_list.extend(hours)
	model_ordered_list.append(input['accepts_credit_card'])
	model_ordered_list.append(input['host_large_group'])
	model_ordered_list.append(input['price_range'])
	model_ordered_list.append(input['alcohol'])
	model_ordered_list.append(input['noise_level'])
	model_ordered_list.append(input['waiter_service'])
	model_ordered_list.append(input['wifi'])
	model_ordered_list.append(get_late_night_bool(input_data))
	model_ordered_list.append(input['has_tv'])
	model_ordered_list.append(get_24_hr_bool(hours))
	model_ordered_list.append(input['drive_thru'])
	model_ordered_list.extend(get_food_category_list(input_data))
	model_ordered_list.append(calculate_closest_places(input_data['longitude'], input_data['latitude']))
	print model_ordered_list
	return model_ordered_list

def predict_rating(dataArray):
		clf = joblib.load(app.config['TRAINING_MODEL_FILEPATH'])
		result = clf.predict(dataArray)
		return result

def get_city_and_state(lat, lon):
		cityNum, stateNum = -1, -1
		result = rg.search((lat, lon))[0]
		if 'name' in result:
			city = result['name']
			if city in cityMap:
				cityNum = cityMap[city]
		if 'admin1' in result:
			state = result['admin1']
			if state in stateMap:
				stateNum = stateMap[stateToAbbr[state]]
		return cityNum, stateNum


def get_time_dff(ot, ct):
	opening =  int(ot[:-2])
	closing = int(ct[:-2])
	opening_r = ct[-2:].upper()
	closing_r = ot[-2:].upper()
	if closing == opening and  opening_r == closing_r:
		return 24
	if 'PM' in ot.upper():
		opening += 12
	if 'AM' in ct.upper():
		closing = closing + 24 if 'AM' == closing_r else closing + 12
	return (closing - opening) % 24


def get_hours(input_data):
	time_list = []
	mon =  get_time_dff(input_data['monday_close'],input_data['monday_open'])
	tue =  get_time_dff(input_data['tuesday_close'],input_data['tuesday_open'])
	wed =  get_time_dff(input_data['wednesday_close'],input_data['wednesday_open'])
	thu =  get_time_dff(input_data['thurday_close'],input_data['thurday_open'])
	fri =  get_time_dff(input_data['friday_close'],input_data['friday_open'])
	sat =  get_time_dff(input_data['saturday_close'],input_data['saturday_open'])
	sun =  get_time_dff(input_data['sunday_close'],input_data['sunday_open'])
	time_list = [thu, tue, fri, wed, mon, sun, sat]
	return time_list

def get_late_night_bool(input_data):
	def is_late(t):
		if 'AM' in t:
			return True
		elif 'PM' in t and int(t[:-2]) >= 10:
			return True
		return False
	days = []
	days.append(input_data['monday_close'])
	days.append(input_data['tuesday_close'])
	days.append(input_data['wednesday_close'])
	days.append(input_data['thurday_close'])
	days.append(input_data['friday_close'])
	days.append(input_data['saturday_close'])
	days.append(input_data['sunday_close'])
	return any([is_late(d.upper()) for d in days])
	

def get_24_hr_bool(hours):
	return any([i for i in hours if i == 24])	


def get_food_category_list(input_data):
		results = []
		for item in food_categories:
			if item in input_data['category']:
				results.append(1)
			else:
				results.append(0)
		print results
		return results

def calculate_closest_places(lon, lat, dist=1):
		df = pd.read_csv("dataset/dist.csv")
		df = df[["longitude", "latitude"]]
		df["longitude"] = (df["longitude"] - lon)**2
		df["latitude"] = (df["latitude"] - lat)**2
		result = np.sqrt(df["longitude"]+df["latitude"])
		result *= 69 # miles
		less_than_one_mile = result[result < dist]
		return len(less_than_one_mile)

def generate_tips(inputs):
		pass


## test datasets
# dataArray = [63, 6, 15.0, 15.0, 24.0, 15.0, 15.0, 24.0, 24.0, True, True, 1.0, 2,
# 						1, True, 1, False, True, False, False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
# 						0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
# 						0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
# 						0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15]

## test input
# input = {
# 	'latitude': 34.23, 			
# 	'longitude': -112.23,  			
# 	'category' : ['Turkish', 'Taiwanese', 'Ethnic Food'],
# 	'monday_open': '8AM',
# 	'monday_close': '12AM',
# 	'tuesday_open': '8AM',
# 	'tuesday_close': '12AM',
# 	'wednesday_open': '8AM',
# 	'wednesday_close': '12AM',
# 	'thurday_open': '8AM',
# 	'thurday_close':'12AM',
# 	'friday_open': '8AM',
# 	'friday_close':'12AM',
# 	'saturday_open': '8AM',
# 	'saturday_close':'12AM',
# 	'sunday_open' : '9AM',
# 	'sunday_close' : '11PM',
# 	'noise_level' : 1, 	
# 	'wifi': 2,			
# 	'alcohol': 2,	
# 	'price_range' : 2, 	
# 	'late_night': True,
# 	'has_tv' : True,
# 	'accepts_credit_card': True,
# 	'drive_thru': True,
# 	'waiter_service' : True,
# 	'host_large_group' : True,
# }