
import urllib.request
import re


paragraph_vector = []
#creazione e apertura di un file di testo per semplificare il processo di scrittura delle stringhe dei paragrafi

file = open("extracted_paragraphs.txt", "w")
file = open("extracted_paragraphs.txt", "a")

#da sistemare a mo di funzione
link = input('inserisci il link:\n')
link_management = urllib.request.urlopen(link)
html_page = link_management.read()
#print(html_page) #restituzione in tipo Byte
html_page = html_page.decode("utf-8") #convertito in formato stringa da cui poi cercare
print(html_page)

#prima scrematura - ricavo i paragrafi:

regex = r"<p>.+</p>"

test_str = html_page

matches = re.finditer(regex, test_str, re.MULTILINE)
matches = re.finditer(regex, test_str)

for matchNum, match in enumerate(matches, start=1):  #ITS REGEX TIMEEEE!
    
    file.write("Match {matchNum} was found at {start}-{end}: {match} \n ".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        file.write("Group {groupNum} found at {start}-{end}: {group} \n".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))





#we need:
#error handling - not done
#title retrieving - not done
#html retrieving - done
#<p> retrieving - done --> written on file, shall i convert this to writing it on a string and that's it? or a json?
#second part: retrieving VIA




