class balancer:

	def balance(Equation):
	@staticmethod
		balanced = ""
		sides = equation.split('-->')

		LeftHandSide=sides[0].split('+')
		RightHandSide=sides[1].split('+')

		print("LHS"+ str(LeftHandSide))
		print("RHS"+ str(RightHandSide))

		LeftHandCompounds=[]
		LeftHandCompounds=[]
		for compound in LeftHandSide:
			LeftHandCompounds.append(Compound(compound))

		for compound in RightHandSide:
			RightHandCompounds.append(Compound(compound))
		

		return balanced