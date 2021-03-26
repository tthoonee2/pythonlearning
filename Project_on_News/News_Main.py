
from os import read
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


#prima scrematura - ricavo i paragrafi:

regex = r"<p>.+</p>"
test_str = html_page

matches = re.finditer(regex, test_str, re.MULTILINE)
matches = re.finditer(regex, test_str)
 #   if stringcheck.isupper(char_pos + len('via' or 'corso' or 'piazza' or 'viale')
  #  file_list.pop(i).split 

for matchNum, match in enumerate(matches, start=1):  #ITS REGEX TIMEEEE!
    
    file.write("Match {matchNum} was found at {start}-{end}: {match} \n ".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        file.write("Group {groupNum} found at {start}-{end}: {group} \n".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))


def P_extract_list():
    file = open("extracted_paragraphs.txt", "a")
    file = str(file)
    type(file)
    ii= 0
    file_list = []
    for ii in range(file.count('Match')):
        file_list.append(file.split('Match'))
    ii = 0
    for ii in file_list:
        print(file_list[ii]) #just for a test

    return file_list

#list should now contain the strings separately.
#for each string of the list evaluate if there is the word via/corso/piazza/viale, if there is return the index of the value
#from that index extract the words having a capital letter following via

def parcella_finder(string):
    if string.find('via ') != -1:
        parcella = 'via '
        return parcella
    elif string.find('viale') != -1:
        parcella = ('viale ')
        return parcella
    elif string.find('corso ') != -1:
        parcella = ('corso ')
        return parcella
    elif string.find('piazza ') != -1:
        parcella = ' piazza '
        return parcella
    else:
        pass



file_list = P_extract_list()
i = 0
for i in file_list:
    string = file_list[i]
    parcella = parcella_finder(string)
    if ('via' or 'corso' or 'piazza' or 'viale') is string:
        da_via_in_poi = string.split('via' or 'corso' or 'piazza' or 'viale')
        da_via_in_poi = da_via_in_poi[-1]
        via = ''
        for io in range(len(da_via_in_poi)):
            if da_via_in_poi[io].isspace() and da_via_in_poi[io+1].isupper():
                via = via + da_via_in_poi[io]
            elif da_via_in_poi[io].isupper():
                via = via + da_via_in_poi[io]
            elif da_via_in_poi[io].isspace():
                break
            elif da_via_in_poi[io] == '.':
                break
            elif da_via_in_poi[i].islower():
                via = via + da_via_in_poi[io]

            via = via
    else:
        pass

    totale = parcella + via
    print(totale)
    



 #   if stringcheck.isupper(char_pos + len('via' or 'corso' or 'piazza' or 'viale')
  #  file_list.pop(i).split 



    #zona --> CAP
#second part: retrieving: via, piazza, corso, viale, zona
#<p> retrieving - done --> written on file, shall i convert this to writing it on a string and that's it? or a json?
#html retrieving - done
#title retrieving - not done
#error handling - not done
#we need:

#consider only the following two 

string = ' lorem ipsum via Palmiro Togliatti ciccio pasticcio'
da_via_in_poi = string.split('via' or 'corso' or 'piazza' or 'viale')
da_via_in_poi = da_via_in_poi[-1]
via = ''

for i in range(len(da_via_in_poi)):
    if da_via_in_poi[i].isspace() and da_via_in_poi[i+1].isupper():
        via = via + da_via_in_poi[i]
    elif da_via_in_poi[i].isupper():
        via = via + da_via_in_poi[i]
    elif da_via_in_poi[i].isspace():
        break
    elif da_via_in_poi[i] == '.':
        break
    elif da_via_in_poi[i].islower():
        via = via + da_via_in_poi[i]
    

print(via)



#it strips away every world into a new string up until it reaches a dot



for i in range(file_list):
    string = file_list[i]
    
    
    
