from requests import get
#for later

def get_urls_from_listing(collection_results):
	results = []
	# for every line in the file
	for line in collection_results:
		finding = line.find('search-the-collections')
		if finding > -1 and line[:2] == "<a":
			results += ['http://metmuseum.org/'+line[9:line.find('?')]] 
	return set(results)


def page_from_file(file_name):
	return open(file_name,'r')
#for later

f = open('metmuseumurls.txt', 'w')

base_url = "http://metmuseum.org/collections/search-the-collections?where=United+States&what=Textiles&rpp=60&pg="
list_of_full_urls = [base_url + str(i) for i in range(1,26)]

i = 1
for indv_url in list_of_full_urls:
	print "i'm okay %d: %s" % (i, indv_url)
	i +=1

	listing = get(indv_url).content.split('\n')
	for item in get_urls_from_listing(listing):
		f.write(item + '\n')


f.close()




















