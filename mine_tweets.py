#! /usr/bin/env python
# encoding=utf8 

import requests, re, os, time, csv

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
#from selenium.webdriver.common.action_chains import ActionChains

from model import *

twitterservice = webdriver.chrome.service.Service(os.path.abspath("/usr/bin/chromedriver")) 
twitterservice.start()

chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')  

twitter = webdriver.Remote(twitterservice.service_url,   desired_capabilities=chrome_options.to_capabilities())
twitter.implicitly_wait(10)

# Twitter Accounts to scrap tweets. Feel free to add twitter username here @........
links = ['billionaire_key'
		,'inspowerminds'
		,'motivatinquotes'
		,'thisinspiresus'
		,'motivationalui'
		,'thesuccesstalk'
		,'motivation'
		]

def tweets(url):
	twitter.get(url)
	time.sleep(10) 

	html = twitter.page_source
	soup = BeautifulSoup(html, "html.parser")

	table = soup.findAll("li", {"id": re.compile("stream-item-tweet-")})
	for tb in table:
		tbody = tb.find("div", {"class": "js-tweet-text-container"}).text.split('#')[0].strip()

		# Check if tweet already exists, if not add to DB
		qname = session.query(Quotes.quote).filter(Quotes.quote == tbody).first()#[0]

		if not qname:
			qa = Quotes(quote=tbody)
			session.add(qa)
			session.commit()

		# Lazy way of clearing html content (but it works)
		html = ''

for link in links:
	url = f'https://twitter.com/{link}'

	SCROLL_PAUSE_TIME = 2

	# Get scroll height
	last_height = twitter.execute_script("return document.body.scrollHeight")

	while True:
		tweets(url)

		# Scroll down to bottom
		twitter.execute_script("window.scrollTo(0, document.body.scrollHeight);")

		# Wait to load page (Two seconds were good enough)
		time.sleep(SCROLL_PAUSE_TIME)

		# Calculate new scroll height and compare with last scroll height, if its equal, you've reached the bottom of the page so break otherwise set new height and continue scrapping
		new_height = twitter.execute_script("return document.body.scrollHeight")
		if new_height == last_height:
		    break
		last_height = new_height

# Quit browser then service
twitter.quit()
twitterservice.stop()