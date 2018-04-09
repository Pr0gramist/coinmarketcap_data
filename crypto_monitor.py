'''
CRYPTO MONITOR

Author: Sivan Kitchoukov
'''

#Importing libraries and files
import time
import coinmarketcap_data as crypto_data


'''
USER PROMPT
'''
#Prompt user what cryptocurrency to monitor
print('Choose one of the following to monitor (other inputs will default to 1):')
print("(1) Bitcoin")
print("(2) Ethereum")

try:
	if int(input()) == 2 :
		crypto_id = "ethereum"
	else:
		crypto_id = "bitcoin"
except ValueError:
	crypto_id = "bitcoin"


print("--------------------------------------------------")
print("--------------------------------------------------")
print("                 LIVE MONITOR")
print("--------------------------------------------------")
print("--------------------------------------------------")

'''
MAIN LOOP - KEEP MONITOR RUNNING
'''
while True:
	print(crypto_id + ": $" + crypto_data.get_crypto_data(crypto_id, "price_usd"))
	time.sleep(300)
