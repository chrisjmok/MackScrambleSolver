import sys
import re
import os
from questionParse import Question
class Test():
	#Test contains data for parsed tests

	#input filename for test
	def __init__(self, fname = ""):
		self.fname = fname
		self.questions = []

	def display(self):
		print("TEST NAME\n" + self.fname + '\n')
		for question in self.questions:
			question.display()

	def check(self, scramble):
		for question in self.questions:
			question.check(scramble)

	#input filename for opening test file
	def readTest(self, directory):
		if self.fname == "":
			sys.exit("no filename for this test object")
		else:
			os.listdir(os.getcwd()+'/'+ directory)
			file = open(directory+'/'+self.fname, 'r')
			text = file.read()
			#unparsed questions
			rawQuestions = re.split("\n\ [0-9]\.|\n[0-9][0-9]\.",text)
			number = 0
			for question in rawQuestions:
				self.questions.append(Question(question, number))
				number += 1

			# count = 0
			# for x in self.questions:
			# 	print("question", count)
			# 	print(x)
			# 	print("\n")
			# 	count+=1


