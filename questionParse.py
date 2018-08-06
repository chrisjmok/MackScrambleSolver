import string
import re
import sys

class Question():
	#contains data pertaining to a specific
	#test question

	def display(self):
		print "QUESTION NUMBER " , self.number
		print "Matches ", self.numMatches, '\n'
		#print(self.words)

	def check(self, scramble):
		for key in self.words:
			if {key}.issubset(scramble.set):
				self.words[key] += 1
				self.numMatches += 1

	def sneakPeek(self, question):
		lowCase = question.lower()
		regex = re.compile('[^a-zA-Z0-9]')
		noPunc = regex.sub('\n', lowCase)
		words = re.split('\s+', noPunc)
		dict = {}
		for word in words:
			dict[word] = 0	
		return dict

	def __init__(self, rawQ = "", number = -1):
		if rawQ == "":
			sys.exit("ERROR: empty question string")
		else:
			self.number = number
			self.words = self.sneakPeek(rawQ)
			#print(self.words)
			self.numMatches = 0