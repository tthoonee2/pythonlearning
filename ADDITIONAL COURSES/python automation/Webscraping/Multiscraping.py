#we will now scrape from,ultiple
from bs4 import BeautifulSoup
import requests
url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(url)
soup = BeautifulSoup(response.text , 'lxml')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
count = 1
for i in items:
    itemname = i.find('h4',class_= 'card-title').text.strip('\n') #we strip it of the new line
    itemprice = i.find('h5').text
    print('%s ) Price: %s, Item Name: %s' % (count, itemprice, itemname))
    count += 1

    #we have retrieved all the items from the shop
from bs4 import BeautifulSoup
import requests
url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(url)
#navigate through pages
pages = soup.find('ul',class_='pagination')
urls = []
links = pages.find_all('a', class_ = 'page-link')
for link in links:
    pagenum = int(link.text) if link.text.isdigit() else None
    if pagenum != None:
        x = link.get('href')
        urls.append(x)
print(urls)
count = 1
for i in urls:
    newurl = url + i
    response = requests.get(newurl)
    soup = BeautifulSoup(response.text , 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for i in items:
        itemname = i.find('h4',class_= 'card-title').text.strip('\n') #we strip it of the new line
        itemprice = i.find('h5').text
        print('%s ) Price: %s, Item Name: %s' % (count, itemprice, itemname))
        count += 1


