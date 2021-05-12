class humanbeing():
    
	def __init__(self):
		self.gender = ''
		self.name = ''
		
	def setgender(self,value):
		self.gender = value
		
	def getgender(self):
		return self.gender
		
	def __str__(self):
		x = ''
		x = self.name + " 's gender is" self.gender
		return x
			
class Boy(humanbeing):
	
	def __init__(self,name):
    		humanbeing.__init__(self)
		self.name = name
		
	


class Girl(Boy):
	setgender('female')
	pass
	

