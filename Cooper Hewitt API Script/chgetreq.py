from requests import get
from math import ceil
import json


base_url = 'http://www.brooklynmuseum.org/opencollection/api/?method=collection.search&version=1&api_key=uQS0IVg5Oh&keyword=Textile&format=json'
# base_url = 'https://api.collection.cooperhewitt.org/rest?method=cooperhewitt.search.objects&access_token=9451d218aa09886a5b8aa815e81c25f7&department_id=35347501&per_page=500'

page_size = 20
total_items = 1027
num_pages = (total_items / page_size) + 1

print 'page_size: [%d]' % num_pages

results = []
for i in xrange(0, num_pages):
	full_url = base_url + '&results_limit=%d&start_index=%d' % (page_size, i * page_size)
	print 'fetching page [%d]: %s' % (i, full_url)
	results += get(full_url, verify=False).json()['response']['resultset']['items']

json_result = json.dumps(results, sort_keys=True, indent=4, separators=(',', ': '))

f = open('brooklyn_museum_textiles.json', 'w')
f.write(json_result)
f.close()
