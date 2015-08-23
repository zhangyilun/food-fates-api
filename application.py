#!flask/bin/python
import pandas as pd
import numpy as np
import reverse_geocoder as rg
import us, urllib
from flask import Flask, Response, jsonify, make_response, request, json
from sklearn.externals import joblib
from datetime import datetime
from models import *

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index():
		return "Woot!"

@app.errorhandler(404)
def not_found(error):
		return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/get_ratings', methods=['POST'])
def get_ratings():
		input_data = str(request.data)
		r = json.loads(input_data)
		data_for_ml = gather_data_for_ml(r)
		rating = predict_rating(data_for_ml)
		return jsonify({'result' : rating})
		

@app.route('/get_reviews', methods=['POST'])
def get_reviews():
	input_data = str(request.data)
	r = json.loads(input_data)
	lat = r['latitude']
	lon = r['longitude']
	df = pd.read_csv("dataset/review_filtered.csv")
	dists = calculate_array_of_dist(lon, lat, df)
	df['dist'] = dists
	df = df.sort('dist', ascending=1)
	top20 = df['text'][:20]
	result = score_sentences(top20, 0.8)
	return jsonify(result)


@app.route('/get_nearby', methods=['POST'])
def get_nearby():
	input_data = str(request.data)
	r = json.loads(input_data)
	result = calculate_closest_places(r['longitude'], r['latitude'])
	return jsonify({'nearby' : result})


#############################################################################
############################## helper functions #############################
#############################################################################

def score_sentences(sents, thresh, is_print=False):
    output = { 'pos' : [], 'neg' : [] }
    for sent in sents:
        f = urllib.urlopen("http://text-processing.com/api/sentiment/",
                           urllib.urlencode({'text':sent}))
        result = json.loads(f.read())

        label = result['label']
        prob = result['probability'][label]
        if prob > thresh and label != 'neutral':
            if label == 'pos':
                s = "\x1b[32m[%2.f%% %s] %s\x1b[0m " % (prob*100, label, sent)
            else:
                s = "\x1b[31m[%2.f%% %s] %s\x1b[0m " % (prob*100, label, sent)
            if is_print:
                print s
        if label == 'pos':
        	output['pos'].append({'label': label,
                    						'prob': prob, 
                    						'sentence': sent})
        else:
        	output['neg'].append({'label': label,
                    						'prob': prob, 
                    						'sentence': sent})
    return output


def calculate_array_of_dist(lon, lat, df, dist=1):
		df["longitude"] = (df["longitude"] - lon)**2
		df["latitude"] = (df["latitude"] - lat)**2
		result = np.sqrt(df["longitude"]+df["latitude"])
		result *= 69 # miles
		return result

def predict_rating(dataArray):
		clf = joblib.load(app.config['TRAINING_MODEL_FILEPATH'])
		result = clf.predict(dataArray)[0]
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
		return results

def calculate_closest_places(lon, lat, dist=1, csv_file="dataset/dist.csv"):
		df = pd.read_csv(csv_file)
		df = df[["longitude", "latitude"]]
		df["longitude"] = (df["longitude"] - lon)**2
		df["latitude"] = (df["latitude"] - lat)**2
		result = np.sqrt(df["longitude"]+df["latitude"])
		result *= 69 # miles
		less_than_one_mile = result[result < dist]
		return len(less_than_one_mile)

def generate_tips(inputs):
		pass


def gather_data_for_ml(input_data):
	model_ordered_list = []
	a = input_data['latitude']
	b = input_data['longitude']
	city, state = get_city_and_state(a, b)
	hours = get_hours(input_data)
	model_ordered_list.extend([city, state]) # city, state
	model_ordered_list.extend(hours)
	model_ordered_list.append(input_data['accepts_credit_card']) #bool
	model_ordered_list.append(input_data['host_large_group']) #bool
	model_ordered_list.append(input_data['price_range'])
	model_ordered_list.append(input_data['alcohol'])
	model_ordered_list.append(input_data['noise_level'])
	model_ordered_list.append(input_data['waiter_service']) #bool
	model_ordered_list.append(input_data['wifi'])
	model_ordered_list.append(get_late_night_bool(input_data))
	model_ordered_list.append(input_data['has_tv']) #bool
	model_ordered_list.append(get_24_hr_bool(hours)) #bool
	model_ordered_list.append(input_data['drive_thru']) #bool
	model_ordered_list.extend(get_food_category_list(input_data))
	model_ordered_list.append(calculate_closest_places(input_data['longitude'], input_data['latitude']))
	return model_ordered_list

if __name__ == '__main__':
		app.run(host='0.0.0.0')