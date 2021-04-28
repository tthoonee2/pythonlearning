#first open the inspection instrument for the website
#we create a get query to save the html of the website
import requests
from bs4 import BeautifulSoup
url = 'http://quotes.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml') #with this command we tell that we are looking to get it as text and we use
# the lxml parser
print(soup)
#it works

#we want to zone in the specific data we have captured
#we know that our code is contained in <span> class
# to grab any text from the website we will have to take the class with the parser.
quotes = soup.find_all('span',class_='text')
print(quotes)
#we know want to retrieve the authors
authors = soup.find_all('small', class_='author')
#we want to retrieve the tags of each quote , yet we cannot use the normal find_all function with the <a> tag, we will
#go one step further.
#we select the tag for each <div> and later we select the tags for each quote withi the for loop
tags = soup.find_all('div',class_='tags')


#now we create a loop for each quote
for i in range(0,len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quotetags = tags[i].find_all('a',class_='tag')
    for quotetag in quotetags:
        print(quotetag.text)        #the .text is needed and is part of the library of soup, without the .text
        #the print funciton will print starting from <a> up to </a>


