
print("Enter your chemical equation in the format below")
print("ex C5 H12 + O2 --> CO2 + H2O")
'C5H12 + 8O2 ---> 5CO2 + 6H2O'
equation = "C5H12 + O2 --> CO2 + H2O"
# input(">")
sides = equation.split('-->')

LeftHandSide=sides[0].split('+')
RightHandSide=sides[1].split('+')

print("LHS"+ str(LeftHandSide))
print("RHS"+ str(RightHandSide))
 
 