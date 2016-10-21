import json

class Element:
	def __init__(self,Name):
		#do things
		#print("Element Created")
		self.Name = Name
		self.Valence = 1#not needed abs(self.FindValenceFromName(self.Name))


	def __str__(self):
		if(self.Valence ==1 ):
			return self.Name
		else:
			return self.Name + str(self.Valence)


	def GetJsonOfElements(self):
			with open('valence.json') as data_file:
				data = json.load(data_file)
			return data
	def FindValenceFromName(self,name):
		if(self.CheckIfValidElement(name)):
			return self.GetJsonOfElements()[name]
		else:
			return 1
	

	def CheckIfValidElement(self,name):
		data = self.GetJsonOfElements()
		return data.has_key(name)




if __name__ == "__main__":
	H = Element("H")
	print(H.Name + " with Valence " + str(H.Valence))