import sys
import string
import re
import os

def insertLineDict(line):
	print "not yet implemented"

def stripPunc(line):
	#print 'stripPunc---'
	noNewLIne = line.strip('\n')
	out = re.split('\W+', noNewLIne)
	#for word in out:
		#print word
	#print '==============='
	return out
 

def scramDict(filename):
	#print '\n\nscramDict-------\n'
	library = {}
	for line in filename:
		arrayLine = stripPunc(line)
		for word in arrayLine:
			if word not in library and word != '':
				#print word
				library[word] = 1
	#print '\n================\n'
	return library

#find all questions in the text file
def findQuests(filename):
	file = open(filename, 'r')
	text = file.read()
	stripped = sneakPeek(text)
	quests = re.split("(\n\ [0-9]\.)|(\n[0-9][0-9]\.)",text)

	for i in range(len(quests)):
		quests[i] = sneakPeek

	return quests
	print "not yet implemented"

#strip everything from the question according to the sneak peak script
def sneakPeek(question):
	lowCase = question.lower()
	sub = re.sub(r'/W+', '\n', lowCase)
	words = re.split('\s+', sub)
	dict = {}
	for i, abc in words:
		dict[words[i]] = 0
	print dict
	return dict

#make a dictionary for the question
def questDict(words):
	print "not yet implemented"

def makeBank(directory):
	bank = {}
	for filename in os.listdir(os.getcwd()+'/'+directory):
		print filename
		if filename.endswith('.mack'):
			bank[filename] = scramDict(filename)
	return bank


#main function
def main():
	# file = open (str(sys.argv[1]), 'r')
	# file.close()
	#print findQuests(str(sys.argv[1]))
	sneakPeek('abcdefg   !@#$%^&*(  word test \n new things')



#if main defines runs main  
if __name__== "__main__":
  main()