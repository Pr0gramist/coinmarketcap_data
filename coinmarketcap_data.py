'''
Live Cryptocurrency Data using CoinMarketCap API

CoinMarketCap Documentation: https://coinmarketcap.com/api

Author: Stivan Kitchoukov
'''

#Importing Libraries
import requests
import json


'''
VARIABLES
'''

#URL to pull data
ticker_url = "https://api.coinmarketcap.com/v1/ticker/"

#Get data from URL
ticker_page = requests.get(ticker_url)
ticker_data = ticker_page.json()


'''
FUNCTIONS
'''

#Function to return array of all crypto IDs
def get_all_ids():
	ids = []

	for i in ticker_data:
		ids.append(i["id"])
	
	return ids

#Function to return array of all crypto elements
def get_all_elements():
	elements = []
	
	element_url = ticker_url + "/bitcoin/"
	element_page = requests.get(element_url)
	element_data = element_page.json()
	
	for i,j in element_data[0].items():
		elements.append(i)
	
	return elements
	
#Function to get data of cryptocurrency - pass crypto ID and element
def get_crypto_data(crypto_id, element):
	crypto_url = ticker_url + "/" + crypto_id.lower() + "/"
	crypto_page = requests.get(crypto_url)
	crypto_data = crypto_page.json()

	if crypto_page.status_code != 200:
		return "URL is not Valid. Check your Crypto ID."
	else:
		return crypto_data[0][element]		
