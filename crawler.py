#!/usr/bin/env python
# coding=utf-8

import urllib2
import urllib
import os
import games
from bs4 import BeautifulSoup

def getFootballData(url):
    
    # 获取url地址的网页,并使用BeautifulSoup进行解析
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)

    count = 0;
        
    for item in soup('tr'):

    	count = count + 1

    	print count

    	if item.attrs == {}:
    		continue
    	print item.attrs

    	game_is_on = item.find('strong')
    	print game_is_on

    	# one_result = FootballData()

    	ref_tags = item.find_all('a')

    	for each_tag in ref_tags:
    		# print each_tag
    		print each_tag.contents[0].string

    	# one_result.team_home = ref_tags[1].contents[0]
    	


		# print item['class'] == 'matchTr'

    	# if item['class'] == 'matchTr':

    	# 	one_result = FootballData()

    		# game_on = item.find('strong');

    		# if game_on.contents[0] == "完":
    		# 	one_result. = item.find('a').contents[0]
    		# team_
    		# print item.attrs



football_link = "http://live.zgzcw.com/bd/"
football_data = []

if __name__=="__main__":
	getFootballData(football_link)

