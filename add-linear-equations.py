# author: snehashish laskar
# date: 10/6/21
# email:snehashish.laskar@gmail.com

# importing the neccessary modules
import math
from string import ascii_letters as letters

# Each equation will be represented by the clas below
class equation:

	# While initalizing the equation class the equation must be
	# formated in the format like "x + y = 12 " where each 
	# term in the equation will be seperated ny a space
	def __init__(self, equation):
		# splitig the equation
		split_equa = equation.split()
		self.split = split_equa
		# Getting the rhs and lhs of the equation
		self.lhs = split_equa[:split_equa.index("=")] 
		self.rhs = split_equa[split_equa.index("=")+1:] 

	# Function to return all the variables in the equation
	def returnVariables(self):
		variables = []
		for letter in letters:
			for r in  self.rhs:
				if letter in r:
					variables.append(r)
			for l in self.lhs:
				if letter in l:
					variables.append(l)

		return variables
	
	def getConst(self):
		consts = []

		for i in self.rhs:
			try:
				i = int(i)
				consts.append(i)
			except:
				pass
		for i in self.lhs:
			try:
				i = int(i)
				consts.append(i)
			except:
				pass
		return consts

class term:

	def __init__(self, val):
		val_cop = val
		if "-" in val:
			self.sign = "-"
		else:
			self.sign = "+"

		self.const = []
		self.var = []
		for letter in letters:
			if letter in val_cop:
				self.var.append(letter)
				val_cop = val_cop.replace(letter,"")

				self.const.append(val_cop)

	def getConst(self):

		if self.const != []:
			return self.const[0]
		else:
			return "No constants"

	def getVar(self):

		if self.var != []:
			return self.var[0]
		else:
			return "No Variables"











				





		

















# def ishanEqua(equation:str):
# 	split_equa = equation.split()

# 	lhs = split_equa[:split_equa.index("=")] 
# 	rhs = split_equa[split_equa.index("=")+1:] 

# 	var_on_left = True

# 	for i in rhs:
# 		for letter in letters:
# 			if letter in i:
# 				var_on_left = False
# 				if "-" in i:
# 					if lhs[-2] == "+":
# 						lhs[-2]= "-"
# 						del rhs[rhs.index(i)]
# 						try:
# 							lhs[2] = int(lhs[2])
# 							rhs.append("-"+lhs[2])
# 						except:
# 							pass
# 						del lhs[2]
# 						lhs.append(i.replace("-",""))
# 					else:
# 						lhs[-2] = "+"
# 						rhs.append(lhs[2])
# 						del lhs[2]
# 						del rhs[rhs.index(i)]
# 						lhs.append(i.replace("-",""))


# 	print(lhs, "=",rhs)

# ishanEqua("34x - 7x = 1x + 8")