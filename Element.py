import json

class Element:
	def __init__(self,Name):
		#do things
		#print("Element Created")
		self.Name = Name
		self.Valence = self.FindValenceFromName(self.Name)
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