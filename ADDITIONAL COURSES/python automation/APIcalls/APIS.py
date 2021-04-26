#to start practicing apis we will be using the tool upcitemdb
#upcitemdb.com
import requests
import json
baseurl = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': '073366118238'}
response = requests.get(baseurl, 
                        params=parameters)
print(response.url)
#Now we have to parse throught the Json
### this was the first API reuqest i have ever made
content = response.content
info = json.loads(content)
#check the data types
print(type(info))
print(info)
#we now try to isolate some of the info of the dictionary
item = info['items']
iteminfo = item[0]
brand = iteminfo['brand']
title  = iteminfo['title']
print(title)
print(brand)



####good example of accessing JSON info: '''A JSON output packet contains a dictionary element called store and a key called product. How would you correctly access the data stored inside the key?'''
info = json.loads(content)
stores = info['store']
storeInfo = stores[0]
product = storeInfo['product']


#linking api-s
#RapidAPI.com






