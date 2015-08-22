import json
import collections
import csv
from collections import OrderedDict

def flatten(json, parent_key='', sep='_'):
	items = []
	for k, v in json.items():
		new_key = parent_key + sep + str(k) if parent_key else k
		if isinstance(v, collections.MutableMapping):
			items.extend(flatten(v, new_key, sep=sep).items())
		else:
			items.append((new_key, v))
	return OrderedDict(items)

def get_unique_keys(list_of_tuple):
	keys = []
	for i in list_of_tuple:
		if i[0] not in keys:
			keys.append(i[0])
	return keys

def parse_row_and_update_global_unique_keys(json, global_unique_keys):
	list_of_tuple = []
	for k, v in json.items():
		if k not in global_unique_keys:
			global_unique_keys.append(k)
		list_of_tuple.append((k, v))
	return list_of_tuple, global_unique_keys

def map_data_to_header(list_of_tuple, global_unique_keys, myfile, wr):
	result = []
	keys = get_unique_keys(list_of_tuple)
	for i in global_unique_keys:
		if i in keys:
			for k in range(len(list_of_tuple)):
				if list_of_tuple[k][0] == i:
					result.append(list_of_tuple[k][1])
		else:
			result.append("-")
	result = [i.encode("utf-8") if (not isinstance(i, (int, long, list, float))) else i for i in result]
	wr.writerow(result)

def parse_json(fname, output_file_name):
	global_unique_keys = []
	results = []
	with open(fname, 'r') as f:
		for row in f:
			json_row = json.loads(row)
			flattened_row = flatten(json_row)
			list_of_tuple, global_unique_keys = parse_row_and_update_global_unique_keys(flattened_row, global_unique_keys)
			results.append(list_of_tuple)

	myfile = open(output_file_name, 'wb')
	wr = csv.writer(myfile)
	wr.writerow(global_unique_keys) # write header
	for item in results:
		map_data_to_header(item, global_unique_keys, myfile, wr)

parse_json('yelp_academic_dataset_tip.json', "processed_tip.csv")
parse_json('yelp_academic_dataset_checkin.json',  "processed_checkins.csv")
parse_json('yelp_academic_dataset_user.json', "processed_user.csv")
parse_json('yelp_academic_dataset_business.json', "processed_business.csv")
parse_json('yelp_academic_dataset_review.json', "processed_review.csv")