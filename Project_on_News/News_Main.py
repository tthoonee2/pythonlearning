import requests
import urllib.request
import re

paragraph_vector = []

#da sistemare a mo di funzione
link = 'https://www.milanotoday.it/attualita/coronavirus/vaccini-covid-domicilio-medici-famiglia-base.html'
link_management = urllib.request.urlopen(link)
html_page = link_management.read()
#print(html_page) #restituzione in tipo Byte
html_page = html_page.decode("utf-8") #convertito in formato stringa da cui poi cercare
print(html_page)

#prima scrematura - ricavo i paragrafi:

paragraphs_vector = html_page.split('<p>')
paragraphs_vector = paragraphs_vector.strip()
print("this is a new string", paragraphs_vector, "\n \n \n")



#we need:
#error handling
#title retrieving
#html retrieving
#<p> retrieving 




