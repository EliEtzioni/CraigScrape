#!/usr/bin/env python3
# Code to scrape San Diego's Craigslist for surfboard pictures, prices, and info 
# Ulitmately, the goal would be to turn this into a webapp where users can choose which city to grab data from
import requests
from bs4 import BeautifulSoup

item = input("What are you looking for?") # Get what user is looking for
item.replace(" ","+") # Replace all spaces with + so that it can be added to URL

url = "https://sandiego.craigslist.org/search/sss?sort=date&query=" + item #create customer URL
response = requests.get(url) # Get a requests object to work more with later
data = response.text # Get the website source code out of the requests object

soup = BeautifulSoup(data,'lxml') # Convert the source code into a BeautifulSoup object
tags = soup.find_all('a', {"class": "result-title hdrlnk"}) # finds all links to individual postings

links = []
for tag in tags: 
	links.append(tag.get('href')) # Get the links to each individual posting

# print(links)  # ---- Can use this to make sure you're capturing all links from the page

post_titles = []
post_prices = []
post_images = []
bunches = []
#post_links = [] --- but you already have these, just don't forget to incorporate them as the contact/go to post button

#test_url = links[0] -- for testing purposes only 
for url in links:
	response = requests.get(url) # Get a  requests object to work more with later
	data = response.text # Get the source code for the individual webpage for each item for sale
	soup = BeautifulSoup(data,'lxml') # Convert into a BeautifulSoup object

	title = soup.find('span', {"id": "titletextonly"}).get_text()
	
	price = soup.find('span', {"class": "price"})
	if price == None: # if the post has no price
		price = "No price"
	else:
		price = price.get_text()

	image = soup.find('img')
	if image == None: # if the post has no images
		image = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg" # "No image available"
	else:
		image = image['src']

	post_titles.append(title)
	post_prices.append(price)
	post_images.append(image) 
	bunches.append([title,price,image,url])

print(post_titles)
print(post_prices)
print(post_images)
print(bunches)