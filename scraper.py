import requests
import os
import time
import json

def timestamp():
	return time.strftime('%Y-%m-%d_%H-%M-%S')

def log(message):
	now = timestamp()
	with open(CONFIG['log_file'], 'a') as f:
		f.write(now + ' => ' + message + '\n')

try:
	with open('scraper.json', 'r') as f:
		CONFIG = json.load(f)
	log('START, Loaded config from scraper.json')

	to_get = CONFIG['url'] + '?last_id=' + str(CONFIG['last_id'])

	log('Making get request to %s' % to_get)
	resp = requests.get(to_get)
	data = resp.json()

	new_id = data['max_id']
	items = data['items']
	output = CONFIG['output'] + '/' + timestamp() + '.json'

	log('Checking if output directory exists (%s)' % CONFIG['output'])
	path = os.path.dirname(CONFIG['output'])
	if not os.path.exists(path):
		log('Output does not exist, attempting to create')
		os.makedirs(path)
	else:
		log('Output directory exists')

	log('Writing %s pulled items to %s' % (len(items), output))
	with open(output, 'w+') as f:
		json.dump(items, f)

	log('Updating scraper.json with last_id as %s' % new_id)
	with open('scraper.json', 'w') as f:
		CONFIG['last_id'] = new_id
		string = json.dumps(CONFIG)
		string = string.replace(',', ',\n\t')
		f.write(string)
except Exception as error:
	log('Failed with exception: %s' % error)