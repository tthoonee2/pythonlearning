#to call an API which is firealled by a key
#take a base url
import requests
baseurl = '...' #--> base url
key = 'xxxxxxxxxxxxxxxxxxx' # --> key of the request (unique ID of the user of the API)
parameters = {'APPID': key, 'q':'Seattle,US'}
response = requests.get(baseurl, params = parameters)
print(response.content)
#we get a JSON dict from the request now