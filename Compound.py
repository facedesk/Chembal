from Element import Element
class Compound:
	
	def __init__(self,inputstring):
		self.inputstring = inputstring
		self.inputToParse = inputstring
		self.Elements=[]
		self.CoValence = 1
		self.ParseElements()


	def __str__(self):
		base = ""
		for Element in self.Elements:
			base = base + str(Element)

		if(self.CoValence ==1):
			return base
		else:
			return str(self.CoValence) + base



	def ParseElements(self):
		self.CoValence = int(self.GetCoValence())
		while(self.inputToParse!= ""):
			#print(self.inputToParse)
			self.Elements.append(Element(self.GetAndRemoveBeginningElement()))
			if((self.inputToParse != "" and self.inputToParse[0].isdigit())):
				valence = self.GetAndRemoveBeginningNumeric()
				self.Elements[-1].Valence = int(valence)
			
	def GetCoValence(self):
		self.inputToParse = self.inputToParse.strip()
		
		if(not self.inputToParse[0].isdigit()):
			return 1
		else:
			return self.GetAndRemoveBeginningNumeric()
			

	def GetAndRemoveBeginningNumeric(self):
		index = 0
		numeric = ""

		while(self.inputToParse[index].isdigit()):
			numeric += self.inputToParse[index]
			self.inputToParse = self.inputToParse[1:]
		
		return numeric
	def GetAndRemoveBeginningElement(self):
		index = 0
		alpha = ""
		
		while(
 		self.inputToParse != ""
		and	not self.inputToParse[index].isdigit() 
		and  (alpha == "" or  self.inputToParse[index].IsLower())):
			alpha += self.inputToParse[index]
			self.inputToParse = self.inputToParse[1:]
		return alpha
	
if __name__ == "__main__":
	test = " 2H2O "
	compound = Compound(test)
	print(test)
	print(compound)
	
		
