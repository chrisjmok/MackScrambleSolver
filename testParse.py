import sys
import re
import questionParse
class Test():
	#Test contains data for parsed tests

	#input filename for test
	def __init__(self, fname = ""):
		self.fname = fname
		self.questions = []

	#input filename for opening test file
	def readTest(self):
		if self.fname == "":
			sys.exit("no filename for this test object")
		else:
			file = open(self.fname, 'r')
			text = file.read()
			#unparsed questions
			rawQuestions = re.split("\n\ [0-9]\.|\n[0-9][0-9]\.",text)
			self.questions = rawQuestions 
			count = 0
			for x in self.questions:
				print("question", count)
				print(x)
				print("\n")
				count+=1


