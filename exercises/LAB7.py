

#exercise 1
import random

destinations = ['Milan','New York','London','Paris','Singapore','Buenos Aires','Madrid','Moscow','Tokio','San Antonio','Seattle','Amsterdam','Boston','Athens','Berlin','Dublin','Florence','Rome','Prague','Dubai','Cape Town','Bruges','Sao Paulo','Toronto','Beijing']


def top_cities(passinglist, numCities = 5):
    top = {}
    for i in range(numCities):
        rnd = random.randint(0,len(passinglist)-1)
        top[i+1] = passinglist[rnd]
    return top

top_cities(destinations,numCities=8)

        
#exercise 2:
import random

destinations = ['Milan','New York','London','Paris','Singapore','Buenos Aires','Madrid','Moscow','Tokio','San Antonio','Seattle','Amsterdam','Boston','Athens','Berlin','Dublin','Florence','Rome','Prague','Dubai','Cape Town','Bruges','Sao Paulo','Toronto','Beijing']


def top_cities2(passlist, numcities = 5):
    top2 = {}
    for i in range(numcities):
        rnd2 = random.randint(0,len(passlist)-1)
        if passlist[rnd2] not in  top2.values():  #pay attention to the differnce between not in and is not
            top2[i+1] = passlist[rnd2]
    return top2

top_cities2(destinations,numcities=8)

            
        
    