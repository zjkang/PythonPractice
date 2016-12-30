# simple web crawler programming in Python

#lesson 2
def get_page(url):
	try:
		import urllib
	 	return urllib.urlopen(url).read()
 	except:
 		return ""	

def get_next_target(page):
	start_link = page.find('<a href=')
	if start_link == -1:
		return None, 0
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote+1)
	url = page[start_quote + 1:end_quote]
	return url, end_quote

def print_all_links(page):
	while True:
		url, endpos = get_next_target(page)
		if url:
			print url
			page = page[endpos:]
		else:
			break;

#print_all_links(get_page('http://xkcd.com/353'))
#print get_page('httP://xkcd.com/353')


#lesson 3: collect all links
def get_all_links(page):
	links = []
	while True:
		url, endpos = get_next_target(page)
		if url:
			links.append(url)
			page = page[endpos:]
		else:
			break;	
	return links

def union(p,q):
	for e in q:
		if e not in p:
			p.append(e)

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
    return crawled


#lesson 4: query [keyword,[url1,url2]], build the web index
index = []

def add_to_index(index,keyword,url):
    if keyword in index:
    	index[keyword].append(url)
    else:
    	index[keyword] = [rul]

#insert index from page
def add_page_to_index(index,url,content):
    ls = content.split()
    for entry in ls:
        add_to_index(index,entry,url)

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
        	content = get_page(page)
        	add_page_to_index(index,page,content)
        	union(tocrawl, get_all_links(get_page(page)))
        	crawled.append(page)
    return index

# lesson 5: time execuation
# hash table (dictionary), improve lookup
import time

def time_execution(code):
	start = time.clock()
	result = eval(code)
	run_time = time.clock() - start
	return result, run_time

def spin_loop(n):
	i = 0
	while i < n:
		i = i + 1

def lookup(index, keyword):
	if keyword in index:
		return index[keyword]
	return None

#print ord('a') # ord(<one letter string>) -> number
#print chr(97)
#print str(3)
#print ord('udacity')

def test_hash_function(func, keys, size):
	results = [0] * size
	keys_used = []
	for w in keys:
		if w not in keys_used:
			hv = func(w,size)
			results[hv] += 1
			keys_used.append(w)
	return results

def bad_hash_string(keyword, bucket):
	return ord(keyword[0]) % bucket

def hash_string(keyword, buckets):
	h = 0
	for c in keyword:
		h = (h + ord(c)) % buckets
	return h

def make_hashtable(nbuckets):
    table = []
    for unused in range(0, nbuckets):
        table.append([])
    return table

#range(<start>,<stop>)

#def make_hashtable_NOT(nbuckets):
#	return [[]] * nbuckets

def hahstable_get_bucket(htable, key):
	return htable[hash_string(key,len(htable))]

def hashtable_add(htable, key, value):
	hahstable_get_bucket(htable,key).append([key,value])

def hashtable_looiup(htable,key):
	bucket = hahstable_get_bucket(htable,key)
	for entry in bucket:
		if entry[0] == key:
			return entry[1]
	return None

def hahstable_update(htable,key,value):
	bucket = hahstable_get_bucket(htable,key)
	for entry in bucket:
		if entry[0] == key:
			entry[1] = value
			return 
	bucket.append([key,value])

#string, list, dictionary 

# lesson 6: 



































